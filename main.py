class Asiento:
    def __init__(self):
        self.color = ""
        self.precio = 0
        self.registro = 0

    def cambiarColor(self, color):
        self.color = color.lower()
        

class Motor:
    def __init__(self):
        self.numeroCilindros = 0
        self.tipo = ""
        self.registro = 0

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo.lower()

    
class Auto:
    cantidadCreados = 0

    def __init__(self, marca, modelo, precio):
        self.modelo = modelo
        self.precio = precio
        self.asientos = [Asiento() for i in range(5)]
        self.marca = marca
        self.motor = Motor()
        self.registro = 0
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        numAsientos = 0
        for asiento in self.asientos:
            if asiento.color != "":
                numAsientos += 1
        return numAsientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento.registro != self.registro and asiento.color != "":
                    return "Las piezas no son originales"
        else:
            return "Las piezas no son originales"
        return "Auto original"