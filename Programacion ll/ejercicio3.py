# Definimos una clase Vehiculo
class Vehiculo:
    def __init__(self, tipo, marca, modelo, año, color, cilindrada, tipo_combustible, transmision, puertas, precio_compra):
        self.tipo = tipo  # Nacional o importado
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.cilindrada = cilindrada
        self.tipo_combustible = tipo_combustible
        self.transmision = transmision
        self.puertas = puertas
        self.capacidad_pasajeros = 5  # Siempre 5 pasajeros
        self.ruedas = 4  # Siempre 4 ruedas
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    
    # Método para calcular el precio de venta con margen de ganancia del 40%
    def calcular_precio_venta(self):
        return self.precio_compra * 1.4
    
    # Método para mostrar la información del vehículo
    def mostrar_informacion(self):
        print("\nCaracterísticas del vehículo:")
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Cilindrada: {self.cilindrada}")
        print(f"Tipo de combustible: {self.tipo_combustible}")
        print(f"Transmisión: {self.transmision}")
        print(f"Puertas: {self.puertas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Precio de compra: {self.precio_compra:.2f}")
        print(f"Precio de venta: {self.precio_venta:.2f}")

# Lista para almacenar los vehículos registrados
vehiculos_registrados = []

# Función para registrar un vehículo
def registrar_vehiculo():
    tipo = input("¿El vehículo es nacional o importado?: ")
    marca = input("Marca del vehículo: ")
    modelo = input("Modelo del vehículo: ")
    año = input("Año del vehículo: ")
    color = input("Color del vehículo: ")
    cilindrada = input("Cilindrada del vehículo: ")
    tipo_combustible = input("Tipo de combustible (gasolina, diésel, etc.): ")
    transmision = input("Transmisión (manual o automática): ")
    puertas = input("Número de puertas: ")
    precio_compra = float(input("Precio de compra del vehículo: "))
    
    # Crear una instancia de la clase Vehiculo
    vehiculo = Vehiculo(tipo, marca, modelo, año, color, cilindrada, tipo_combustible, transmision, puertas, precio_compra)
    
    # Agregar el vehículo a la lista de vehículos registrados
    vehiculos_registrados.append(vehiculo)
    
    # Mostrar la información del vehículo registrado
    vehiculo.mostrar_informacion()

# Función para mostrar todos los vehículos registrados
def mostrar_vehiculos_registrados():
    if not vehiculos_registrados:
        print("\nNo hay vehículos registrados aún.")
    else:
        print("\nLista de vehículos registrados:")
        for vehiculo in vehiculos_registrados:
            vehiculo.mostrar_informacion()

# Menú principal
def menu():
    while True:
        print("\n--- Menú Concesionario ---")
        print("1. Registrar un vehículo")
        print("2. Ver vehículos registrados")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_vehiculo()
        elif opcion == "2":
            mostrar_vehiculos_registrados()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Iniciamos el programa
menu()
