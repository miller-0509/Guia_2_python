def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    descuento_salud_pension: float = salario_base * 0.08
    salario_final: float = salario_base - descuento_salud_pension + bonificacion
    return salario_final



salario_1: float = calcular_salario_neto(2000000.0)
salario_2: float = calcular_salario_neto(2000000.0, 200000.0)

print(f"Salario sin bonificación: ${salario_1}")
print(f"Salario con bonificación: ${salario_2}")