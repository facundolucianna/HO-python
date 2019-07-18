# Ejercicio 6: Intente colocar label para los ejes y los datos

#X  	Y
#7,5 	28,66
#4,48 	20,37
#8,60 	22,33
#7,73 	26,35
#5,28 	22,29
#4,25 	21,74
#6,99 	23,11
#6,31 	23,13
#9,15 	24,68
#5,06 	21,89

# Resolucion.
# Autor: Facundo A. Lucianna
# Fecha: 15/07/19

import matplotlib.pyplot as plt
import numpy as np

X = [7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06]
Y = [28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89]

#Realizamos un ajuste lineal
polLineal = np.poly1d(np.polyfit(X, Y, 1))
pol3 = np.poly1d(np.polyfit(X, Y, 3))

#Encontramos los puntos de ajustes para cada caso
Xsorted = X
Xsorted.sort()
AjusteLineal = polLineal(Xsorted)
AjustePol3 = pol3(Xsorted)

fig, ax = plt.subplots()
ax.scatter(X, Y, label='Datos')
ax.plot(X, AjusteLineal, linewidth=1, linestyle='--', color='black', label='Ajuste lineal')
ax.plot(X, AjustePol3, linewidth=1, linestyle='--', color='grey', label='Ajuste Orden 3') #Tendria que haber usado spline para que se vea lindo pero ya fue
legend = ax.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title('X vs Y')
plt.show()
