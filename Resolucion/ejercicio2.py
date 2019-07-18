# Ejercicio 2: Cada término en la serie de Fibonacci es generado a partir de la
# suma de los dos términos previos, empezando de 1 y 2, los diez primeros
# términos serán: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … Considerando los términos
# de la serie de Fibonacci que son impares, y por debajo de un millón encuentre
# la suma de dichos términos.

# Resolucion.
# Autor: Facundo A. Lucianna
# Fecha: 15/07/19

# Buscamos tantos numeros de la serie de Fibonacci hasta que llegue al valor de
# n
n = 1000000 

# Creamos la lista con los dos primeros valores, no tiene sentido generarlos
listFibonacci = [1, 1]
lastValue = 0

# Buscamos todo valor de la serie que sea menor a n
while(lastValue < n):
    lastValue = listFibonacci[-1] + listFibonacci[-2]
    listFibonacci.append(lastValue)

# Sacamos el ultimo porque se sobrepasa
listFibonacci.remove(listFibonacci[-1])

# Eliminamos a todos los valores pares
for number in listFibonacci:
    if number % 2 == 0:
        listFibonacci.remove(number)

#Mostramos el resultado
print("La suma total es " + str(sum(listFibonacci)))
#print("La suma total es " + str(sumaTotal))
