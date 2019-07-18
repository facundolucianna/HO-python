# Ejercicio 1: Si hacemos una lista de todos los números naturales debajo de 10
# que sean múltiplos de 3 o 5 obtendríamos 3, 5, 6 y 9. La suma de los múltiplos
# es 23. Encuentre la suma de todos los múltiplos de 3 o 5 debajo de 1000
# (o sea, 3+5+6+9+10+12+15+18+...)

# Resolucion.
# Autor: Facundo A. Lucianna
# Fecha: 15/07/19

# Definimos la cantidad de multiplos de cada uno de 3 y 5 a buscar
n = 1000

#Buscamos los multiplos
multiploTres = range(0, n, 3)
multiploCinco = range(0, n, 5)

#Busco el minimo comun multiplo, como son numeros primos, solo multipico ambos
minimoComunMultiplo = 3*5

#Encuentro todos los multiplos comunes entre 3 y 5
multiplosComunes = range(0, n, minimoComunMultiplo)

#Realizamos la suma.
sumaMultiploTres = sum(multiploTres)
sumaMultiploCinco = sum(multiploCinco)
sumamultiplosComunes = sum(multiplosComunes)

#Sumamos todo, y restamos los multiplos comunes ya que sino se sumarian dos
# veces
sumaTotal = sumaMultiploTres + sumaMultiploCinco - sumamultiplosComunes

#Mostramos el resultado
print("La suma total es " + str(sumaTotal))
