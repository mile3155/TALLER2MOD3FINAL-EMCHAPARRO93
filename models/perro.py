from models.animal import Animal


class Perro(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, raza: str):
        super().__init__(nombre, peso, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau, guau!"

    def dar_raza(self):
        return self.raza

    def dar_informacion(self):
        return self.nombre + "(" + self.raza + "):" + str(self.peso) + "/" + str(self.edad) + ")"
