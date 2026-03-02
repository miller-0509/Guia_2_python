class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible: float = 10000.0

    def solicitar_retiro(self) -> None:
        print("--- Bienvenido al Cajero Automatico ---")

        try:
            monto = str = input("Ingrese el monto a retirar (solo números): ")
            if monto == 0: 
                raise ValueError ("No puede retirar cero pesos.")

                self.efectivo_disponible -= monto
                print(f"Retiro exitoso. Quedan {self.efectivo_disponible} pesos en la caja")

        except ValueError as e:
            print(f"ERROR DE FORMATO: Usted ingresó caracteres inválidos. ({e})")

        except Exception as e:
            print(f"ERROR INESPERADO: Contacte a soporte. Detalles: {e}")

        finally:
            print("Expulsando tarjeta.Gracias por usar el cajero. Hasta luego.")

mi_cajero = CajeroAutomatico()
mi_cajero.solicitar_retiro()