class Producto:
    # Constructor: se ejecuta cuando se crea un nuevo producto
    # Aquí se guardan los datos principales del producto
    def __init__(self, nom_producto, precio_uni, stock):
        self.nom_producto = nom_producto   # Nombre del producto
        self.precio_uni = precio_uni       # Precio por unidad del producto
        self.stock = stock                 # Cantidad disponible en inventario

    # Método que verifica si hay suficiente stock para una compra
    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            print("Stock disponible para realizar la operación.")
            return True
        else:
            print("La cantidad solicitada supera el stock disponible.")
            return False

    # Método que realiza la venta y descuenta la cantidad del inventario
    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock = self.stock - cantidad
            print("Venta realizada correctamente.")
            print("Stock restante:", self.stock)
        else:
            print("No fue posible completar la venta.")

    # Método para agregar más unidades al inventario
    def restablecer(self, cantidad):
        self.stock = self.stock + cantidad
        print("Se agregaron unidades al inventario.")
        print("Stock actualizado:", self.stock)


# Crear objeto
producto1 = Producto("Laptop", 1200, 10)

# Verificar si hay suficientes unidades
producto1.verificar_disponibilidad(5)

# Realizar una venta
producto1.vender(3)

# Verificar disponibilidad nuevamente
producto1.verificar_disponibilidad(8)

# Intentar vender más unidades
producto1.vender(8)

# Agregar más stock al producto
producto1.restablecer(10)

# Verificar disponibilidad otra vez
producto1.verificar_disponibilidad(8)

# Realizar una nueva venta
producto1.vender(8)

# Crear otro objeto
producto1 = Producto("Audifinos", 500, 5)

# Verificar si hay suficientes unidades
producto1.verificar_disponibilidad(3)

# Realizar una venta
producto1.vender(2)

# Verificar disponibilidad nuevamente
producto1.verificar_disponibilidad(8)

# Intentar vender más unidades
producto1.vender(8)

# Agregar más stock al producto
producto1.restablecer(14)

# Verificar disponibilidad otra vez
producto1.verificar_disponibilidad(8)

# Realizar una nueva venta
producto1.vender(8)