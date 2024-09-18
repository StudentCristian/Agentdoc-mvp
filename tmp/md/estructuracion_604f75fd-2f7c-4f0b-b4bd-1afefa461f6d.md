```python
class Sustantivo:
    """
    Representa un sustantivo en el lenguaje.

    Atributos:
        nombre (str): El nombre del sustantivo.
        clase (str): La clase del sustantivo (común, propio, concreto, abstracto, etc.).
        genero (str): El género del sustantivo (masculino, femenino, neutro).
        numero (str): El número del sustantivo (singular, plural).
        definido (bool): Indica si el sustantivo está definido (el, la, los, las) o no.
        descripcion (str): Una breve descripción del sustantivo.
    """

    def __init__(self, nombre, clase, genero=None, numero=None, definido=False, descripcion=None):
        """
        Inicializa un objeto Sustantivo.

        Args:
            nombre (str): El nombre del sustantivo.
            clase (str): La clase del sustantivo.
            genero (str, optional): El género del sustantivo. Defaults to None.
            numero (str, optional): El número del sustantivo. Defaults to None.
            definido (bool, optional): Indica si el sustantivo está definido. Defaults to False.
            descripcion (str, optional): Una breve descripción del sustantivo. Defaults to None.
        """
        self.nombre = nombre
        self.clase = clase
        self.genero = genero
        self.numero = numero
        self.definido = definido
        self.descripcion = descripcion

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Sustantivo.
        """
        return f"Sustantivo: {self.nombre}, Clase: {self.clase}, Género: {self.genero}, Número: {self.numero}, Definido: {self.definido}, Descripción: {self.descripcion}"

    def get_nombre(self):
        """
        Devuelve el nombre del sustantivo.
        """
        return self.nombre

    def get_clase(self):
        """
        Devuelve la clase del sustantivo.
        """
        return self.clase

    def get_genero(self):
        """
        Devuelve el género del sustantivo.
        """
        return self.genero

    def get_numero(self):
        """
        Devuelve el número del sustantivo.
        """
        return self.numero

    def get_definido(self):
        """
        Devuelve si el sustantivo está definido.
        """
        return self.definido

    def get_descripcion(self):
        """
        Devuelve la descripción del sustantivo.
        """
        return self.descripcion

    def set_nombre(self, nombre):
        """
        Establece el nombre del sustantivo.
        """
        self.nombre = nombre

    def set_clase(self, clase):
        """
        Establece la clase del sustantivo.
        """
        self.clase = clase

    def set_genero(self, genero):
        """
        Establece el género del sustantivo.
        """
        self.genero = genero

    def set_numero(self, numero):
        """
        Establece el número del sustantivo.
        """
        self.numero = numero

    def set_definido(self, definido):
        """
        Establece si el sustantivo está definido.
        """
        self.definido = definido

    def set_descripcion(self, descripcion):
        """
        Establece la descripción del sustantivo.
        """
        self.descripcion = descripcion
```

**Uso:**

```python
# Crear un sustantivo
perro = Sustantivo("perro", "común", "masculino", "singular", False, "Un animal doméstico")

# Mostrar información del sustantivo
print(perro)

# Acceder a los atributos del sustantivo
print(f"Nombre: {perro.get_nombre()}")
print(f"Clase: {perro.get_clase()}")
print(f"Género: {perro.get_genero()}")
print(f"Número: {perro.get_numero()}")
print(f"Definido: {perro.get_definido()}")
print(f"Descripción: {perro.get_descripcion()}")

# Modific