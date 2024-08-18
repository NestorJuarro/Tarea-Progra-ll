# Clase para representar un estudiante
class Estudiante:
    def __init__(self, nombre, identificacion, curso):
        self.nombre = nombre
        self.identificacion = identificacion
        self.curso = curso
        self.notas = {}
    
    # Método para agregar una nota en una asignatura
    def agregar_nota(self, asignatura, nota):
        self.notas[asignatura] = nota
    
    # Método para calcular el promedio de las notas
    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)
    
    # Método para mostrar si el estudiante aprobó o no
    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        resultado = "Aprobado" if promedio >= 5 else "Reprobado"
        print(f"Estudiante: {self.nombre}, Promedio: {promedio:.2f}, Resultado: {resultado}")

# Clase para gestionar los estudiantes
class GestionEstudiantes:
    def __init__(self):
        self.estudiantes = []
    
    # Método para agregar un estudiante
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado.")
    
    # Método para mostrar la lista de estudiantes
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for estudiante in self.estudiantes:
                estudiante.mostrar_resultado()

# Función del menú interactivo
def menu():
    gestion = GestionEstudiantes()

    while True:
        print("\n--- Menú de Gestión de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Agregar nota a estudiante")
        print("3. Ver resultados de estudiantes")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            identificacion = input("Identificación del estudiante: ")
            curso = input("Curso del estudiante: ")
            estudiante = Estudiante(nombre, identificacion, curso)
            gestion.agregar_estudiante(estudiante)
        
        elif opcion == "2":
            nombre_estudiante = input("Nombre del estudiante: ")
            asignatura = input("Asignatura: ")
            nota = float(input("Nota: "))
            
            # Buscar el estudiante
            estudiante_encontrado = None
            for estudiante in gestion.estudiantes:
                if estudiante.nombre == nombre_estudiante:
                    estudiante_encontrado = estudiante
                    break
            
            if estudiante_encontrado:
                estudiante_encontrado.agregar_nota(asignatura, nota)
                print(f"Nota agregada en {asignatura} para {nombre_estudiante}.")
            else:
                print("Estudiante no encontrado.")
        
        elif opcion == "3":
            gestion.mostrar_estudiantes()
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Iniciar el programa
menu()
