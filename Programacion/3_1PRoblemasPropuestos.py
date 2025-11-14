from abc import ABC, abstractmethod

class categoria(ABC):
    @abstractmethod
    def tipo_categoria(self):
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
                f"Categoría: {self.tipo_categoria()}")
    def tipo_categoria(self):
        if self.no_cilindros <= 4:
            return "chico"
        elif self.no_cilindros <= 6:
            return "mediano"
        else:
            return "grande"
        
class Pasajeros(vehiculo, categoria):
    def __init__(self, marca, modelo, anio, color, tipo_comb,no_pasajeros, origen, destino, costo):
        vehiculo.__init__(self, marca, modelo, anio, color, tipo_comb)
        self.no_pasajeros = no_pasajeros
        self.origen = origen
        self.destino = destino
        self.costo = costo
    def __str__ (self):
        return (f"{vehiculo.__str__(self)}\n"
                f"Número de Pasajeros: {self.no_pasajeros}\n"
                f"Origen: {self.origen}\n"
                f"Destino: {self.destino}\n"
                f"Costo: {self.costo}\n"
                f"Categoría: {self.tipo_categoria()}")
    def tio_categoria(self):
        if self.no_pasajeros <= 19:
            return "Microbus"
        elif self.no_pasajeros <= 30:
            return "Buseta"
        else:
            return "Autobús"
        

class Carga(vehiculo, categoria):
    def __init__(self, marca, modelo, anio, color, tipo_comb, peso, carga_max):
        vehiculo.__init__(self, marca, modelo, anio, color, tipo_comb)
        self.peso = peso
        self.carga_max = carga_max
    def __str__ (self):
        return (f"{vehiculo.__str__(self)}\n"
                f"Peso de Carga: {self.peso}\n"
                f"Volumen de Carga: {self.carga_maz}\n"
                f"Categoría: {self.tipo_categoria()}")
    def tipo_categoria(self):
        if self.peso <= 15:
            return " Camion Chico"
        elif self.peso <= 35:
            return "Camion grande o Semiremolque"
        else:
            return "Semiremolque o doble o trimple remolque"
