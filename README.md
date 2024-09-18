```bash
virtualenv env

source env/bin/activate

pip freeze > requirements.txt

export FLASK_APP="run.py"

flask run

export FLASK_ENV="development"
```

Necesito crear usando Python y Flask un servicio que permita seleccionar archivos que son cargados en una carpeta de mi computadora los archivos cargados en esa carpeta se deben mostrar en el navegador web para que el usuario pueda seleccionar uno de ellos. La carpeta se llama uploads esta en mi proyecto.

Cuando el usuario selecciona un archivo, debe aparecer un boton Generar documento con un LLM cuando el usuario presiona el boton suceden los siguientes procesos:

Primero se obtiene los placeholders del archivo docx seleccionado usando la libreria python-docxtpl y el resultado se guarda en un archivo json con un nombre que crearas aleatoriamente que representa los placeholders de ese documento guardas el json en la carpeta json 


Luego creas un formulario dinámico usando WTForms donde todos los campos son de tipo input text el label de cada campo es el key del json y el valor del campo es el ingresado por el usuario en el campo input text. debajo del formulario creas un boton de tipo submit llamado Generar documento.

codigo de ejemplo

```bash
pip install docxtpl
pip install -U WTForms
```


```python
from docxtpl import DocxTemplate
import json
import os

def cargar_plantilla(ruta_archivo):
    """
    Carga una plantilla de Word y extrae las variables definidas.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    
    tpl = DocxTemplate(ruta_archivo)
    variables = tpl.get_undeclared_template_variables()
    return tpl, variables

def crear_json_variables(variables, ruta_salida):
    """
    Crea un archivo JSON con las variables extraídas.
    """
    datos = {var: "" for var in variables}
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def main():
    ruta_plantilla = "assets/templates/Formato_Planeador.docx"
    ruta_json = "assets/data/variables.json"

    try:
        tpl, variables = cargar_plantilla(ruta_plantilla)
        crear_json_variables(variables, ruta_json)
        print(f"Se han extraído {len(variables)} variables y se han guardado en {ruta_json}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

Estados en el Formulario Dinámico:

Campos Tipo Prompt:
Si un campo es marcado como prompt por el usuario, el modelo de lenguaje utilizará el texto de entrada para generar contenido según el prompt.
Ejemplo de acción:
El texto ingresado por el usuario es enviado al modelo LLM, que genera un archivo en formato Markdown, el cual luego es procesado.

Campos Tipo Data:
Si un campo es marcado como data por el usuario, este valor se usará para reemplazar directamente el placeholder en el documento final.
No se modificará el valor en tiempo de ejecución.


.env
```bash
GOOGLE_API_KEY="AIzaSyCePJRDNZ1l7X0xbx57_BOvb3l5m2qdOfo"
```


```python
import google.generativeai as genai
import os

API_KEY="AIzaSyCePJRDNZ1l7X0xbx57_BOvb3l5m2qdOfo"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
```

Cuando se precione el boton "Generar documento" primero se debe obtener el contenido del formulario tipo prompt 
ahora necesito configurar el modelo gemini para que tome los campos del formulario tipo prompt y genere archivos markdown 

crear un json con los valores del formulario ingresados por el usuario creo que tocara predefinir una estructura json para que permita obtener los campos de tipo prompt y de tipo data junto con su clave y valor. Los datos de los campos tipo prompt son enviados al modelo para generar las respuestas a los prompt.

Las respuestas son guardadas en archivos de formato Markdown temporales

Los archivos Markdown son convertidos a docx usando pypandoc para ser usandos como objetos subdoc en el renderizado del documento final.

La aplicación recupera las rutas de acceso y claves de los archivos temporales docx mediante las funciones GetTempPath y GetKey para crear las claves y valores del objeto subdoc.

Se guarda el json final que tiene tanto los valores tipo data (son valores de tipo string) y los valores de tipo prompt (son valores de tipo objeto subdoc) este archivo json contiene todos los valores de los placeholders para renderizarlo en el archivo docx final.

El archivo docx final es guardado en la carpeta documents 

**Se crean y modifican los siguientes archivos json en tiempo de ejecución:**

json que obtiene los placeholders y es usado para crear el formulario dinámico el cual se guarda en la carpeta json

json que obtiene los datos ingresados por el usuario en los campos del formulario, tiene el tipo (prompt o data) y los valores en el input text, este json es usado para enviar los valores de tipo prompt al modelo y mantiene todos los datos de los campos del formulario y se guarda en la carpeta FormData

json que es estructurado para ser usado para el renderizado su estructura contiene los valores de tipo data y prompt donde data su valor es un string mientras prompt su valor es la ruta de acceso de los archivos temporales docx y se guarda en la carpeta render

Ejemplo de renderizado de objetos subdoc

```python
import json
from docxtpl import DocxTemplate

# Cargar la plantilla principal
doc = DocxTemplate('templates/Formato_Planeador.docx')

# Cargar el archivo structure.json
with open('structure.json', 'r') as file:
    structure = json.load(file)

# Crear subdocumentos y agregarlos al contexto
context = {}

for key, value in structure.items():
    if isinstance(value, dict) and 'subdoc_file' in value:
        subdoc_file = value['subdoc_file']
        subdoc = doc.new_subdoc(subdoc_file)
        context[key] = str(subdoc)  # Convertir Subdoc a su representación en XML
    else:
        context[key] = value

# Renderizar el documento con el contexto
doc.render(context)

# Guardar el documento final
doc.save('Ciencias_Naturales.docx')
```



Estructura del proyecto
tmp
- md //representa la carpeta para guardar los archivos temporales creados Markdown
- subdoc // representa la carpeta para guardar los archivos temporales convertidos de md a docx
upload
templates
documents
render
FormData // representa la carpeta para guardar los archivos json de los formularios
json
run.py
.env
