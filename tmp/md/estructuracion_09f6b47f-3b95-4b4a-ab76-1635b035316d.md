```python
class Sustantivo:
    """
    Representa un sustantivo en el lenguaje.

    Atributos:
        nombre (str): El nombre del sustantivo.
        clase (str): La clase gramatical del sustantivo (común, propio, abstracto, concreto).
        genero (str): El género del sustantivo (masculino, femenino, neutro).
        numero (str): El número del sustantivo (singular, plural).

    Métodos:
        __init__(self, nombre, clase, genero, numero): Constructor de la clase.
        get_nombre(self): Devuelve el nombre del sustantivo.
        get_clase(self): Devuelve la clase gramatical del sustantivo.
        get_genero(self): Devuelve el género del sustantivo.
        get_numero(self): Devuelve el número del sustantivo.
        set_nombre(self, nuevo_nombre): Modifica el nombre del sustantivo.
        set_clase(self, nueva_clase): Modifica la clase gramatical del sustantivo.
        set_genero(self, nuevo_genero): Modifica el género del sustantivo.
        set_numero(self, nuevo_numero): Modifica el número del sustantivo.
        imprimir_informacion(self): Imprime la información del sustantivo.
    """

    def __init__(self, nombre, clase, genero, numero):
        """
        Inicializa un nuevo objeto Sustantivo.

        Args:
            nombre (str): El nombre del sustantivo.
            clase (str): La clase gramatical del sustantivo.
            genero (str): El género del sustantivo.
            numero (str): El número del sustantivo.
        """

        self.nombre = nombre
        self.clase = clase
        self.genero = genero
        self.numero = numero

    def get_nombre(self):
        """Devuelve el nombre del sustantivo."""
        return self.nombre

    def get_clase(self):
        """Devuelve la clase gramatical del sustantivo."""
        return self.clase

    def get_genero(self):
        """Devuelve el género del sustantivo."""
        return self.genero

    def get_numero(self):
        """Devuelve el número del sustantivo."""
        return self.numero

    def set_nombre(self, nuevo_nombre):
        """Modifica el nombre del sustantivo."""
        self.nombre = nuevo_nombre

    def set_clase(self, nueva_clase):
        """Modifica la clase gramatical del sustantivo."""
        self.clase = nueva_clase

    def set_genero(self, nuevo_genero):
        """Modifica el género del sustantivo."""
        self.genero = nuevo_genero

    def set_numero(self, nuevo_numero):
        """Modifica el número del sustantivo."""
        self.numero = nuevo_numero

    def imprimir_informacion(self):
        """Imprime la información del sustantivo."""
        print(f"Nombre: {self.nombre}")
        print(f"Clase: {self.clase}")
        print(f"Género: {self.genero}")
        print(f"Número: {self.numero}")
```

**Explicación:**

* **Clase `Sustantivo`**: Define un objeto que representa un sustantivo.
* **Atributos**:
    * `nombre`: Almacena el nombre del sustantivo.
    * `clase`: Almacena la clase gramatical del sustantivo (común, propio, abstracto, concreto).
    * `genero`: Almacena el género del sustantivo (masculino, femenino, neutro).
    * `numero`: Almacena el número del sustantivo (singular, plural).
* **Métodos**:
    * `__init__()`: Constructor de la clase. Inicializa los atributos del sustantivo.
    * `get_nombre()`, `get_clase()`, `get_genero()`, `get_numero()`: Devuelven el valor de los atributos correspondientes.
    * `set_nombre()`, `set_clase()`, `set_genero()`, `set_numero()`: Permiten modificar los valores de los atributos.
    * `imprimir_informacion()`: Imprime la información del sustantivo en la consola.

**Ejemplo de uso:**

```python
# Crea un objeto Sustantivo
