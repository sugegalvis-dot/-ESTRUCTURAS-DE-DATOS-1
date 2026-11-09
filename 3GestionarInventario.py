def limpiar(texto):
    return texto.strip().capitalize()

def mostrarMenu():
    print()
    print("MENÚ")
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Ordenar productos alfabéticamente")
    print("6. Mostrar número total de productos")
    print("7. Salir")


def agregar_Producto(inventario):
    nombre = limpiar(input("Nombre del producto: "))
    if nombre == "":
        print("El nombre no puede estar vacío.")
    elif nombre in inventario:
        print(f"{nombre} ya está en el inventario.")
    else:
        inventario.append(nombre)
        print(f"{nombre} fue agregado al inventario.")


def agregar_Lote(inventario):
    texto = input("Escribe los productos separados por comas: ")
    agregados = 0
    for parte in texto.split(","):
        nombre = limpiar(parte)
        if nombre != "" and nombre not in inventario:
            inventario.append(nombre)
            agregados += 1
    print(f"Productos nuevos agregados: {agregados}")


def eliminar_Producto(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        nombre = limpiar(input("Nombre del producto a eliminar: "))
        if nombre in inventario:
            inventario.remove(nombre)
            print(f"{nombre} fue eliminado del inventario.")
        else:
            print(f"{nombre} no está en el inventario.")


def eliminar_Reciente(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        eliminado = inventario.pop()
        print(f"Se eliminó el producto más reciente: {eliminado}")


def ordenar_Productos(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        ordenados = sorted(inventario)       # copia ordenada: no cambia el orden de llegada
        print("Productos en orden alfabético:")
        for producto in ordenados:
            print("-", producto)


def mostrar_Total(inventario):
    print(f"Total de productos en el inventario: {len(inventario)}")


inventario = []
opcion = ""

while opcion != "7":
    mostrarMenu()
    opcion = input("Elige una opción (1-7): ").strip()

    if opcion == "1":
        agregar_Producto(inventario)
    elif opcion == "2":
        agregar_Lote(inventario)
    elif opcion == "3":
        eliminar_Producto(inventario)
    elif opcion == "4":
        eliminar_Reciente(inventario)
    elif opcion == "5":
        ordenar_Productos(inventario)
    elif opcion == "6":
        mostrar_Total(inventario)
    elif opcion == "7":
        print("Hasta pronto.")
    else:
        print("Opción no válida. Escribe un número del 1 al 7.")
