from models.animal import Animal


class Boa(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuesto):
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen
        self.impuesto = impuesto

    def hacer_sonido(self):
        return "¡Tsss!"
