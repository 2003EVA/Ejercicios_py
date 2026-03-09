# Clase que representa un vehículo
class Vehiculo:

    # Constructor: se ejecuta cuando se crea un nuevo vehículo
    # Aquí se guardan los datos principales del vehículo
    def __init__(self, marca, modelo, velocidad_max, velocidad_act):
        self.marca = marca            # Marca del vehículo
        self.modelo = modelo          # Modelo del vehículo
        self.velocidad_max = velocidad_max  # Velocidad máxima permitida
        self.velocidad_act = velocidad_act  # Velocidad actual del vehículo

    # Método para mostrar la información del vehículo
    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Velocidad máxima:", self.velocidad_max, "km/h")
        print("Velocidad actual:", self.velocidad_act, "km/h")

    # Método para aumentar la velocidad del vehículo
    def acelerar(self, aumento):
        if self.velocidad_act + aumento <= self.velocidad_max:
            self.velocidad_act = self.velocidad_act + aumento
            print("El vehículo aumentó su velocidad.")
            print("Velocidad actual:", self.velocidad_act, "km/h")
        else:
            print("No se puede superar la velocidad máxima.")

    # Método para reducir la velocidad del vehículo
    def frenar(self, reduccion):
        if self.velocidad_act >= reduccion:
            self.velocidad_act = self.velocidad_act - reduccion
            print("El vehículo redujo su velocidad.")
            print("Velocidad actual:", self.velocidad_act, "km/h")
        else:
            self.velocidad_act = 0
            print("El vehículo se ha detenido.")

    # Método para verificar si el vehículo supera un límite de velocidad dado
    def verificar_limite(self, limite):
        if self.velocidad_act > limite:
            print("El vehículo supera el límite de velocidad establecido.")
        else:
            print("El vehículo se mantiene dentro del límite permitido.")


# Crear objeto
vehiculo1 = Vehiculo("Ford", "Raptor", 200, 90)

vehiculo1.mostrar_info()

vehiculo1.acelerar(50)

vehiculo1.verificar_limite(80)

vehiculo1.frenar(40)

vehiculo1.verificar_limite(80)