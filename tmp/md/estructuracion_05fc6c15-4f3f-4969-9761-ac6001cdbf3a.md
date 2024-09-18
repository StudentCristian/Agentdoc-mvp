```python
class Sustantivo:
    """
    Representa un sustantivo en el lenguaje.

    Atributos:
        nombre (str): El nombre del sustantivo.
        clase (str): La clase del sustantivo (ej: "común", "propio", "concreto", "abstracto").
        genero (str, opcional): El género del sustantivo (ej: "masculino", "femenino").
        numero (str, opcional): El número del sustantivo (ej: "singular", "plural").

    Métodos:
        __init__(self, nombre, clase, genero=None, numero=None): Constructor de la clase.
        get_nombre(self): Devuelve el nombre del sustantivo.
        get_clase(self): Devuelve la clase del sustantivo.
        get_genero(self): Devuelve el género del sustantivo.
        get_numero(self): Devuelve el número del sustantivo.
        set_genero(self, genero): Establece el género del sustantivo.
        set_numero(self, numero): Establece el número del sustantivo.
    """

    def __init__(self, nombre, clase, genero=None, numero=None):
        """
        Inicializa un objeto Sustantivo.

        Args:
            nombre (str): El nombre del sustantivo.
            clase (str): La clase del sustantivo.
            genero (str, opcional): El género del sustantivo. Defaults to None.
            numero (str, opcional): El número del sustantivo. Defaults to None.
        """
        self.nombre = nombre
        self.clase = clase
        self.genero = genero
        self.numero = numero

    def get_nombre(self):
        """Devuelve el nombre del sustantivo."""
        return self.nombre

    def get_clase(self):
        """Devuelve la clase del sustantivo."""
        return self.clase

    def get_genero(self):
        """Devuelve el género del sustantivo."""
        return self.genero

    def get_numero(self):
        """Devuelve el número del sustantivo."""
        return self.numero

    def set_genero(self, genero):
        """Establece el género del sustantivo."""
        self.genero = genero

    def set_numero(self, numero):
        """Establece el número del sustantivo."""
        self.numero = numero
```

**Ejemplo de uso:**

```python
# Crea un sustantivo común, singular y masculino
libro = Sustantivo("libro", "común", "masculino", "singular")

# Imprime las propiedades del sustantivo
print(f"Nombre: {libro.get_nombre()}")
print(f"Clase: {libro.get_clase()}")
print(f"Género: {libro.get_genero()}")
print(f"Número: {libro.get_numero()}")

# Cambia el número a plural
libro.set_numero("plural")

# Imprime las propiedades del sustantivo nuevamente
print(f"Nombre: {libro.get_nombre()}")
print(f"Clase: {libro.get_clase()}")
print(f"Género: {libro.get_genero()}")
print(f"Número: {libro.get_numero()}")
```

**Salida:**

```
Nombre: libro
Clase: común
Género: masculino
Número: singular
Nombre: libro
Clase: común
Género: masculino
Número: plural
```

**Explicación:**

* La clase `Sustantivo` define un objeto que representa un sustantivo en el lenguaje.
* El constructor `__init__` inicializa los atributos del objeto.
* Los métodos `get_` devuelven los valores de los atributos.
* Los métodos `set_` modifican los valores de los atributos.
* El ejemplo muestra cómo crear un objeto `Sustantivo` y acceder a sus propiedades. También muestra cómo modificar el número del sustantivo utilizando el método `set_numero`.
