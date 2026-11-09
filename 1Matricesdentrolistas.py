dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def leerPrecios(cantidad):
    precios = []
    for p in range(cantidad):
        precio = int(input(f"Precio del producto {p + 1}: "))
        precios.append(precio)
    return precios

def llenarMatriz(fils, cols):
    matriz = []
    for f in range(fils):
        fila = []
        for c in range(cols):
            unidades = int(input(f"Unidades vendidas del producto {f + 1} el {dias[c]}: "))
            fila.append(unidades)
        matriz.append(fila)
    return matriz

lstPrecios = leerPrecios(5)
matVentas = llenarMatriz(5, 7)

#Producto con más ingresos a la semana

def lstTotalesProdxSem(ventas, precios):
    fils = len(ventas)
    cols = len(ventas[0])
    lstTotales = []
    for f in range(fils):
        suma = 0
        for c in range(cols):
            suma += ventas[f][c] * precios[f]
        lstTotales.append(suma)

    return lstTotales

lstTotales = lstTotalesProdxSem(matVentas, lstPrecios)

maxTotal = max(lstTotales)
prodVentMax = lstTotales.index(maxTotal) + 1

print(f"El producto {prodVentMax} es el que más vende a la semana con ventas de ${maxTotal:,}")

#Día de la semana con mayor ingreso

def lstTotalesDiaxSem(ventas, precios):
    fils = len(ventas)
    cols = len(ventas[0])
    lstTotales = []
    for c in range(cols):
        suma = 0
        for f in range(fils):
            suma += ventas[f][c] * precios[f]
        lstTotales.append(suma)
 
    return lstTotales
 
lstTotalesDia = lstTotalesDiaxSem(matVentas, lstPrecios)
 
maxTotalDia = max(lstTotalesDia)
diaMax = lstTotalesDia.index(maxTotalDia)
 
print(f"El día {dias[diaMax]} es el de mayor ingreso por ventas, con ${maxTotalDia:,}")
 
