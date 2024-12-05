from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre:str, peso:float, edad:int):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    def obtener_nombre(self):
        return self.nombre

    def obtener_peso(self):
        return self.peso

    def obtener_edad(self):
        return self.edad
