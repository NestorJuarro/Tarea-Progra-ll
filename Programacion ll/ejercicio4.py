# Definimos una clase Dispositivo
class Dispositivo:
    def __init__(self, tipo, modelo, procesador, ram, almacenamiento, pantalla, precio_compra):
        self.tipo = tipo  # Celular, tablet, portátil
        self.modelo = modelo  # Modelo del dispositivo
        self.procesador = procesador  # Tipo de procesador
        self.ram = ram  # Memoria RAM
        self.almacenamiento = almacenamiento  # Almacenamiento interno
        self.pantalla = pantalla  # Tamaño de la pantalla
        self.precio_compra = precio_compra  # Precio de compra del dispositivo
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta con el margen de ganancia del 70%
    
    # Método para calcular el precio de venta con un margen del 70%
    def calcular_precio_venta(self):
        return self.precio_compra * 1.7
    
    # Método para mostrar la información del dispositivo
    def mostrar_informacion(self):
        print(f"\nTipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Tamaño de pantalla: {self.pantalla}")
        print(f"Precio de compra: {self.precio_compra:.2f}")
        print(f"Precio de venta: {self.precio_venta:.2f}")

# Lista para almacenar los dispositivos registrados
dispositivos_registrados = []

# Función para registrar un dispositivo
def registrar_dispositivo():
    tipo = input("Tipo de dispositivo (celular, tablet, portátil): ")
    modelo = input("Modelo del dispositivo: ")
    procesador = input("Procesador del dispositivo: ")
    ram = input("Cantidad de RAM (en GB): ")
    almacenamiento = input("Almacenamiento (en GB): ")
    pantalla = input("Tamaño de la pantalla (en pulgadas): ")
    precio_compra = float(input("Precio de compra del dispositivo: "))
    
    # Crear una instancia de la clase Dispositivo
    dispositivo = Dispositivo(tipo, modelo, procesador, ram, almacenamiento, pantalla, precio_compra)
    
    # Agregar el dispositivo a la lista de dispositivos registrados
    dispositivos_registrados.append(dispositivo)
    
    # Mostrar la información del dispositivo registrado
    dispositivo.mostrar_informacion()

# Función para mostrar todos los dispositivos registrados
def mostrar_dispositivos_registrados():
    if not dispositivos_registrados:
        print("\nNo hay dispositivos registrados aún.")
    else:
        print("\nLista de dispositivos registrados:")
        for dispositivo in dispositivos_registrados:
            dispositivo.mostrar_informacion()

# Menú principal
def menu():
    while True:
        print("\n--- Menú Almacén de Dispositivos PHR ---")
        print("1. Registrar un dispositivo")
        print("2. Ver dispositivos registrados")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_dispositivo()
        elif opcion == "2":
            mostrar_dispositivos_registrados()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Iniciamos el programa
menu()
