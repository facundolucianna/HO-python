# Graficar el siguiente polinomio, su derivada y puntos extremos:
# f(x)=x³+x²-4x+4

# Ejercicio 9: Guardar los resultados de evaluar la función en el rango del
# punto a cada 0.1 unidades en un archivo de texto.

# Resolucion.
# Autor: Facundo A. Lucianna
# Fecha: 15/07/19

import matplotlib.pyplot as plt
import numpy as np

# Creamos el archivo a guardar los datos
file = open("datos.txt", "w")

#Creamos el polinomio
polinomio = np.poly1d([1, 1, -4, 4])

# Obtenemos las absisas separadas a 0.1 entre ellas
X = np.arange(-10.0, 10.1, 0.1)

# Obtenemos la funcion para las absisas
Y = polinomio(X)

#Guardamos en el archivo
XandY = np.c_[X, Y]
np.savetxt(file, XandY, fmt='%f', delimiter='\t', header="x\t# f(x)")

file.close()
