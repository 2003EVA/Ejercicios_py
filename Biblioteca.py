# Clase que representa un libro
class Libro:

    # Constructor: se ejecuta cuando se crea un nuevo libro
    # Aquí se guardan los datos iniciales del libro
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo      # Guarda el título del libro
        self.autor = autor        # Guarda el nombre del autor
        self.paginas = paginas    # Guarda el número de páginas del libro

    # Método para mostrar la información del libro
    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Páginas:", self.paginas)

    # Método para modificar la cantidad de páginas del libro
    def modificar_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas   # Se reemplaza el número de páginas anterior
        print("El número de páginas fue cambiado")


# Crear el primer objeto libro
libro1 = Libro("El principito", "Antoine de Saint-Exupery", 96)

# Mostrar información del primer libro
libro1.mostrar_info()

# Cambiar el número de páginas del primer libro
libro1.modificar_paginas(120)

# Mostrar nuevamente la información del libro para ver el cambio
libro1.mostrar_info()


# Crear el segundo objeto libro
libro2 = Libro("Cumbres borrascosas", "Emily Bronte", 420)

# Mostrar información del segundo libro
libro2.mostrar_info()

# Cambiar el número de páginas del segundo libro
libro2.modificar_paginas(390)

# Mostrar nuevamente la información del libro para ver el cambio
libro2.mostrar_info()