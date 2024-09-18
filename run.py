from flask import Flask, render_template, request, redirect, url_for, send_file
from docxtpl import DocxTemplate
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
import os
import json
import uuid
import google.generativeai as genai
import pypandoc
from dotenv import load_dotenv

app = Flask(__name__)

app.config['SECRET_KEY'] = '01dba1f150e40469f6cd5eaf1b54dab4'  

# Cargar variables de entorno
load_dotenv()

# Configurar el modelo Gemini
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

UPLOAD_FOLDER = 'uploads'
JSON_FOLDER = 'json'
FORM_DATA_FOLDER = 'FormData'
RENDER_FOLDER = 'render'
TMP_MD_FOLDER = 'tmp/md'
TMP_SUBDOC_FOLDER = 'tmp/subdoc'
DOCUMENTS_FOLDER = 'documents'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_FOLDER'] = JSON_FOLDER
app.config['FORM_DATA_FOLDER'] = FORM_DATA_FOLDER
app.config['RENDER_FOLDER'] = RENDER_FOLDER
app.config['TMP_MD_FOLDER'] = TMP_MD_FOLDER
app.config['TMP_SUBDOC_FOLDER'] = TMP_SUBDOC_FOLDER
app.config['DOCUMENTS_FOLDER'] = DOCUMENTS_FOLDER

def get_placeholders(docx_file):
    doc = DocxTemplate(docx_file)
    return list(doc.get_undeclared_template_variables())

def create_dynamic_form(fields):
    class DynamicForm(FlaskForm):
        pass
    
    for field in fields:
        setattr(DynamicForm, f"{field}_input", StringField(field))
        setattr(DynamicForm, f"{field}_type", SelectField(f"Tipo de {field}", choices=[('data', 'Data'), ('prompt', 'Prompt')]))
    
    setattr(DynamicForm, 'submit', SubmitField('Generar documento'))
    return DynamicForm()


@app.route('/', methods=['GET', 'POST'])
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    class FileSelectForm(FlaskForm):
        file_select = SelectField('Seleccione un archivo', choices=[('', 'Seleccione un archivo')] + [(f, f) for f in files])
        submit = SubmitField('Generar documento con IA')
    
    form = FileSelectForm()
    
    if request.method == 'POST' and form.validate():
        selected_file = form.file_select.data
        if selected_file:
            placeholders = get_placeholders(os.path.join(app.config['UPLOAD_FOLDER'], selected_file))
            json_filename = f"{uuid.uuid4()}.json"
            json_path = os.path.join(app.config['JSON_FOLDER'], json_filename)
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump({p: {"value": "", "type": "data"} for p in placeholders}, f, ensure_ascii=False)
            
            return redirect(url_for('generate_document', json_file=json_filename, template_file=selected_file))
    
    return render_template('index.html', form=form)

@app.route('/generate/<json_file>', methods=['GET', 'POST'])
def generate_document(json_file):
    json_path = os.path.join(app.config['JSON_FOLDER'], json_file)
    template_file = request.args.get('template_file')
    
    if not template_file:
        return "Error: No se especificó el archivo de plantilla", 400
    
    with open(json_path, 'r', encoding='utf-8') as f:
        placeholders = json.load(f)
    
    form = create_dynamic_form(placeholders.keys())
    
    if request.method == 'POST' and form.validate():
        form_data = {}
        for field in placeholders:
            form_data[field] = {
                "value": request.form.get(f"{field}_input"),
                "type": request.form.get(f"{field}_type")
            }
        
        # Guardar los datos del formulario
        form_data_filename = f"{uuid.uuid4()}.json"
        form_data_path = os.path.join(app.config['FORM_DATA_FOLDER'], form_data_filename)
        with open(form_data_path, 'w', encoding='utf-8') as f:
            json.dump(form_data, f, ensure_ascii=False)
        
        # Procesar los campos de tipo prompt
        render_data = {}
        for field, data in form_data.items():
            if data['type'] == 'prompt':
                # Generar contenido con el modelo Gemini
                response = model.generate_content(
                    data['value'],
                    generation_config=genai.types.GenerationConfig(
                        candidate_count=1,
                        max_output_tokens=1000,
                        temperature=1.0
                    )
                )
                
                if hasattr(response, 'text'):
                    content = response.text
                else:
                    content = "No se generó contenido."
                
                # Guardar el contenido en un archivo Markdown
                md_filename = f"{field}_{uuid.uuid4()}.md"
                md_path = os.path.join(app.config['TMP_MD_FOLDER'], md_filename)
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Convertir Markdown a DOCX
                docx_filename = f"{field}_{uuid.uuid4()}.docx"
                docx_path = os.path.join(app.config['TMP_SUBDOC_FOLDER'], docx_filename)
                pypandoc.convert_file(md_path, 'docx', outputfile=docx_path)
                
                render_data[field] = {"subdoc_file": docx_path}
            else:
                render_data[field] = data['value']
        
        # Guardar los datos de renderizado
        render_filename = f"{uuid.uuid4()}.json"
        render_path = os.path.join(app.config['RENDER_FOLDER'], render_filename)
        with open(render_path, 'w', encoding='utf-8') as f:
            json.dump(render_data, f, ensure_ascii=False)
        
        # Renderizar el documento final
        template_path = os.path.join(app.config['UPLOAD_FOLDER'], template_file)
        if not os.path.exists(template_path):
            return f"Error: El archivo de plantilla '{template_file}' no existe", 404
        doc = DocxTemplate(template_path)
        
        context = {}
        for key, value in render_data.items():
            if isinstance(value, dict) and 'subdoc_file' in value:
                subdoc = doc.new_subdoc(value['subdoc_file'])
                context[key] = subdoc
            else:
                context[key] = value
        
        doc.render(context)
        
        # Guardar el documento final
        final_doc_filename = f"{uuid.uuid4()}.docx"
        final_doc_path = os.path.join(app.config['DOCUMENTS_FOLDER'], final_doc_filename)
        doc.save(final_doc_path)
        
        return send_file(final_doc_path, as_attachment=True)
    
    return render_template('generate.html', form=form, placeholders=placeholders)

if __name__ == '__main__':
    app.run(debug=True)