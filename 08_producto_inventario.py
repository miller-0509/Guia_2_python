class Producto:

    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            self.stock -= cantidad
            print(f"✅ Venta exitosa: {cantidad} unidad(es) de '{self.nombre}'.")
            print(f"   Stock restante: {self.stock} unidad(es).")

        except ValueError as e:
            print(f"⚠️  Advertencia: {e}. Se intentaron vender {cantidad} unidad(es) de '{self.nombre}', pero solo hay {self.stock} disponible(s).")


class ProductoPerecedero(Producto):

    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = dias_vencimiento

    def vender(self, cantidad: int) -> None:
        print(f"📦 Producto perecedero - Vence en {self.dias_vencimiento} día(s).")
        super().vender(cantidad)

print("=" * 50)
print("  SISTEMA RESILIENTE DE INVENTARIO")
print("=" * 50)

laptop = Producto(nombre="Laptop", precio=1500.00, stock=5)

print("\n--- Producto: Laptop ---")
print(f"Precio: ${laptop.precio:.2f} | Stock inicial: {laptop.stock}")

laptop.vender(2)

laptop.vender(10)

leche = ProductoPerecedero(nombre="Leche", precio=2.50, stock=20, dias_vencimiento=7)

print("\n--- Producto Perecedero: Leche ---")
print(f"Precio: ${leche.precio:.2f} | Stock inicial: {leche.stock}")

leche.vender(5)

leche.vender(100)

print("\n" + "=" * 50)
print("  Programa finalizado correctamente.")
print("=" * 50)