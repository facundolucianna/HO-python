# Ejercicio 4: Dado el siguiente set de datos, obtenga un gráfico tipo scatter
# plot para X en función de Y.

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

X = [7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06]
Y = [28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89]

plt.figure()
plt.scatter(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Scatter Plot')
plt.show()
