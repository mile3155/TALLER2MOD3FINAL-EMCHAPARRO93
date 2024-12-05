from models.animal import Animal


class Gato(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, color: str):
        super().__init__(nombre, peso, edad)
        self.color = color

    def hacer_sonido(self):
        return "¡Miau, miau!"

    def dar_color(self):
        return self.color

    def dar_informacion(self):
        return self.nombre + "(" + self.color + "):" + str(self.peso) + "/" + str(self.edad) + ")"
