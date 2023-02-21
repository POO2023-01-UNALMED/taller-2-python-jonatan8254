class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores=["rojo", "verde", "amarilo", "negro", "blanco"]
        if color in colores:
            self.color = color
        

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo.lower()

    
class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = Motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        numAsientos = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
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