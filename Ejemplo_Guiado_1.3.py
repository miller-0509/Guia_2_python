def calcular_iva(precio_base: float) -> float:
    iva: float = precio_base * 0.19
    precio_final: float = precio_base + iva
    return precio_final