# Ejercicio 3: Los factores primos en 13195 son 5, 7, 13 y 29 ¿ Cuál es el
# factor primo más grande en el número 600851475143 ?

# Resolucion.
# Autor: Facundo A. Lucianna
# Fecha: 15/07/19

# Esta funcion busca todos los primos que van desde 2 hasta el valor del
# argumento numero
n = 600851475143

numeroPrimo = 2
numero = n
listaPrimos = []

while(numero != 1):

    if numero % numeroPrimo == 0:
        numero = numero / numeroPrimo  # Vamos reduciendo el numero tantas veces como el numero primo sea multiplo
        listaPrimos.append(numeroPrimo)
    else: #Cuando ya el numeor que se obtnega no sea multiplo del numero primo,
        for primoPosible in range(numeroPrimo + 1, int(numero + 1)):

            # Buscamos el siguiente numero primo
            esPrimo = True

            # Usamos el calculo hasta la raiz de primoPosible porqeu es mas eficiente
            # No es necesario probar todos los numeros de 1 a primoPosible,
            # Sino de 1 a raiz de primoPosible
            for num in range(2, int(primoPosible ** 0.5) + 1):
                if primoPosible % num == 0: #Si el primoPosible es divisible por alguno de los numeros del rango
                    esPrimo = False #No es primo
                    break

            # Si salimos del ciclo for sin que me cambie la bandera, el numero es primo
            if esPrimo:
                numeroPrimo = primoPosible
                break

#Mostramos el resultado
print("El factor primo mas grande es " + str(listaPrimos[-1]))
