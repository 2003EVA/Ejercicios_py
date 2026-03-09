# Clase que representa a un estudiante
class Estudiante:

    # Constructor: se ejecuta cuando creamos un nuevo estudiante
    # Aquí se guardan los datos iniciales del estudiante
    def __init__(self, nombre, edad, notas_fil):
        self.nombre = nombre          # Guarda el nombre del estudiante
        self.edad = edad              # Guarda la edad del estudiante
        self.notas_fil = float(notas_fil)  # Guarda la nota final como número decimal

    # Método para mostrar la información del estudiante
    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Nota Final:", self.notas_fil)

    # Método para verificar si el estudiante aprobó o reprobó
    def ver_aprobacion(self):
        if self.notas_fil >= 3.0:   # Si la nota es mayor o igual a 3 aprueba
            print(self.nombre, "aprobo la materia")
        else:                       # Si la nota es menor a 3 reprueba
            print(self.nombre, "reprobo la materia")


# Crear el primer objeto estudiante
Estudiante1 = Estudiante("Eva", "22", 5.0)

# Mostrar información del estudiante
Estudiante1.mostrar_info()

# Verificar si aprobó o no
Estudiante1.ver_aprobacion()


# Crear el segundo objeto estudiante
Estudiante2 = Estudiante("Sofia", "19", 2.0)

# Mostrar información del segundo estudiante
Estudiante2.mostrar_info()

# Verificar si aprobó o reprobó
Estudiante2.ver_aprobacion()

