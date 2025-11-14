from abc import ABC, abstractmethod

class categoria(ABC):
    @abstractmethod
    def categoria(self):
        pass


class vehiculo():
    def __init__(self, marca, modelo, anio, color, tipo_comb):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.tipo_comb = tipo_comb
    def __str__(self):
        return (f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n" 
                f"Año: {self.anio}\n"
                f"Color: {self.color}\n" 
                f"Tipo de Combustible: {self.tipo_comb}")
    

class Particular(vehiculo, categoria):
    def __init__(self, marca, modelo, anio, color, tipo_comb,no_pasajeros,no_cilindros):
        vehiculo.__init__(self, marca, modelo, anio, color, tipo_comb)
        self.no_pasajeros = no_pasajeros
        self.no_cilindros = no_cilindros
    def __str__ (self):
        return (f"{vehiculo.__str__(self)}\n"
                f"Número de Pasajeros: {self.no_pasajeros}\n"
                f"Número de Cilindros: {self.no_cilindros}\n"
                f"Categoría: {self.categoria()}")
    def categoria(self):
        if self.no_cilindros <= 4:
            return "chico"

