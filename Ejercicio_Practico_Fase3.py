class Vehiculo:

    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.anio: int = anio


vehiculo_1 = Vehiculo("Toyota", "Corolla", 2022)
vehiculo_2 = Vehiculo("Mazda", "CX-5", 2021)

print(f"Vehículo 1: {vehiculo_1.marca} {vehiculo_1.modelo} - Año {vehiculo_1.anio}")
print(f"Vehículo 2: {vehiculo_2.marca} {vehiculo_2.modelo} - Año {vehiculo_2.anio}")