class Libro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Páginas:", self.paginas)

    def modificar_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas
        print("El número de páginas fue cambiado")


# Crear objeto
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 96)

libro1.mostrar_info()

libro1.modificar_paginas(120)

libro1.mostrar_info()

libro2 = Libro("cumbres borrascosas", "emily bronte", 420)

libro2.mostrar_info()

libro2.modificar_paginas(390)

libro2.mostrar_info()