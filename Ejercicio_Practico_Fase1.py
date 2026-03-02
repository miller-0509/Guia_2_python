def calcular_iva(precio_base: float) -> float:
    iva: float = precio_base * 0.19
    precio_final: float = precio_base + iva
    return precio_final



factura_1: float = calcular_iva(10000.0)
factura_2: float = calcular_iva(50000.0)

print(f"Total a pagar factura 1: ${factura_1}")
print(f"Total a pagar factura 2: ${factura_2}")


def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

edad_usuario: int = int(input("Ingrese su edad: "))

if es_mayor_de_edad(edad_usuario):
    print("Es mayor de edad")
else:
    print("Es menor de edad")