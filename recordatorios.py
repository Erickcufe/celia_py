# Funciones

def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Celia"))

# Listas
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# Diccionarios
persona = {
    "nombre": "Celia",
    "edad": 25
}
print(persona["nombre"])


# Clases y programación Orientada a Objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Alice", 25)
print(persona1.saludar())
