# Definimos una clase para los artículos
class Articulo:
    def __init__(self, tipo, descripcion, precio_compra):
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    
    # Método para calcular el precio de venta con un margen de ganancia del 30%
    def calcular_precio_venta(self):
        return self.precio_compra * 1.30
    
    # Método para mostrar la información del artículo
    def mostrar_informacion(self):
        print(f"\nTipo: {self.tipo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio de compra: {self.precio_compra:.2f}")
        print(f"Precio de venta: {self.precio_venta:.2f}")

# Lista para almacenar los artículos registrados
articulos_registrados = []

# Función para registrar un cuaderno
def registrar_cuaderno():
    hojas = input("¿El cuaderno tiene 50 o 100 hojas?: ")
    descripcion = f"Cuaderno {hojas} hojas, Marca: HOJITAS"
    precio_compra = float(input("Precio de compra del cuaderno: "))
    
    cuaderno = Articulo("Cuaderno", descripcion, precio_compra)
    articulos_registrados.append(cuaderno)

# Función para registrar un lápiz
def registrar_lapiz():
    tipo_lapiz = input("¿El lápiz es de grafito o de colores?: ")
    descripcion = f"Lápiz {tipo_lapiz}, Marca: RAYAS"
    precio_compra = float(input("Precio de compra del lápiz: "))
    
    lapiz = Articulo("Lápiz", descripcion, precio_compra)
    articulos_registrados.append(lapiz)

# Función para mostrar todos los artículos registrados
def mostrar_articulos():
    if not articulos_registrados:
        print("\nNo hay artículos registrados aún.")
    else:
        print("\nLista de artículos registrados:")
        for articulo in articulos_registrados:
            articulo.mostrar_informacion()

# Menú principal
def menu():
    while True:
        print("\n--- Menú Papelería ---")
        print("1. Registrar un cuaderno")
        print("2. Registrar un lápiz")
        print("3. Ver artículos registrados")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_cuaderno()
        elif opcion == "2":
            registrar_lapiz()
        elif opcion == "3":
            mostrar_articulos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Iniciamos el programa
menu()
