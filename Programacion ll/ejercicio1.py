# Definimos una clase Perro
class Perro:
    def __init__(self, nombre, raza, edad, color, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso
        self.estado = "NO ATENDIDO"  # Estado inicial es NO ATENDIDO
        self.tamanio = self.clasificar_tamanio()  # Clasificamos el tamaño del perro
    
    # Método para clasificar el tamaño del perro según su peso
    def clasificar_tamanio(self):
        if self.peso < 10:
            return "Perro pequeño"
        else:
            return "Perro grande"
    
    # Método para cambiar el estado del perro a ATENDIDO
    def atender(self):
        self.estado = "ATENDIDO"
    
    # Método para mostrar la información del perro
    def mostrar_informacion(self):
        print("\nInformación del perro:")
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamanio}")
        print(f"Estado: {self.estado}")

# Función principal para registrar y atender a un perro
def registrar_perro():
    # Pedimos la información básica del perro
    nombre = input("Nombre del perro: ")
    raza = input("Raza del perro: ")
    edad = input("Edad del perro (en años): ")
    color = input("Color del perro: ")
    peso = float(input("Peso del perro (en kg): "))
    
    # Creamos una instancia de la clase Perro
    perro = Perro(nombre, raza, edad, color, peso)
    
    # Cambiamos el estado a ATENDIDO
    perro.atender()
    
    # Mostramos la información del perro
    perro.mostrar_informacion()

# Llamamos a la función para registrar un perro
registrar_perro()
