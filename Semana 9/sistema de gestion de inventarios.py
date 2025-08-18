# inventory_management_system.py

class Producto:
    """
    Representa un producto en el inventario.

    Atributos:
        id (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible en stock.
        precio (float): Precio del producto.
    """

    def __init__(self, id, nombre, cantidad, precio):
        """Constructor de la clase Producto."""
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        """Retorna el ID del producto."""
        return self.id

    def get_nombre(self):
        """Retorna el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Retorna la cantidad del producto."""
        return self.cantidad

    def get_precio(self):
        """Retorna el precio del producto."""
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto."""
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def set_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        if nuevo_precio >= 0:
            self.precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")

    def __str__(self):
        """
        Retorna una representación en cadena del objeto Producto.
        Útil para mostrar la información del producto de forma legible.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    """
    Gestiona la colección de productos en el inventario.

    Atributos:
        productos (dict): Un diccionario que almacena los productos.
                          Las claves son los IDs de los productos para
                          un acceso más rápido y eficiente, y los valores
                          son los objetos Producto.
    """

    def __init__(self):
        """Constructor de la clase Inventario."""
        self.productos = {}

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Verifica que el ID no exista para asegurar su unicidad.
        """
        if producto.get_id() in self.productos:
            print(f"Error: El producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto '{producto.get_nombre()}' añadido con éxito.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        """
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró ningún producto con el ID {id}.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        """
        if id in self.productos:
            producto = self.productos[id]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print(f"Producto con ID {id} actualizado con éxito.")
        else:
            print(f"Error: No se encontró ningún producto con el ID {id}.")

    def buscar_producto_por_nombre(self, nombre_buscado):
        """
        Busca productos por nombre (no distingue entre mayúsculas y minúsculas).
        Retorna una lista de productos que coinciden total o parcialmente.
        """
        resultados = []
        nombre_buscado_lower = nombre_buscado.lower()
        for producto in self.productos.values():
            if nombre_buscado_lower in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos_los_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n--- Listado de Productos en el Inventario ---")
        for producto in self.productos.values():
            print(producto)
        print("-------------------------------------------\n")


def menu_principal():
    """
    Función principal que ejecuta el menú interactivo en la consola.
    """
    inventario = Inventario()

    # Datos de ejemplo para probar la funcionalidad
    inventario.añadir_producto(Producto(1, "Laptop", 10, 1200.50))
    inventario.añadir_producto(Producto(2, "Mouse", 50, 25.00))
    inventario.añadir_producto(Producto(3, "Teclado", 30, 75.99))

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo_producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para ID, cantidad y precio.")

        elif opcion == '2':
            try:
                id = int(input("Ingrese ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Entrada inválida. Ingrese un número para el ID.")

        elif opcion == '3':
            try:
                id = int(input("Ingrese ID del producto a actualizar: "))
                print("¿Qué desea actualizar?")
                print("1. Cantidad")
                print("2. Precio")
                sub_opcion = input("Seleccione una opción (1 o 2): ")

                if sub_opcion == '1':
                    nueva_cantidad = int(input("Ingrese nueva cantidad: "))
                    inventario.actualizar_producto(id, nueva_cantidad=nueva_cantidad)
                elif sub_opcion == '2':
                    nuevo_precio = float(input("Ingrese nuevo precio: "))
                    inventario.actualizar_producto(id, nuevo_precio=nuevo_precio)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")

        elif opcion == '4':
            nombre_buscado = input("Ingrese nombre o parte del nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre_buscado)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for producto in resultados:
                    print(producto)
                print("----------------------------------")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Punto de entrada principal del script
if __name__ == "__main__":
    menu_principal()