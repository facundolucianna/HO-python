# Graficar el siguiente polinomio, su derivada y puntos extremos:
# f(x)=x³+x²-4x+4

# Ejercicio 7: Colocar titulo a los ejes y agregarle una grilla en ambos.
# Definir el rango de la función entre -10 y 10.
# Ejercicio 8: Colocar titulo y colores distintos para la función y la derivada.

# Resolucion.
# Autor: Facundo A. Lucianna
# Fecha: 15/07/19

import matplotlib.pyplot as plt
import numpy as np

#Creamos el polinomio
polinomio = np.poly1d([1, 1, -4, 4])

#Obtenemos los coeficientes de la derivada del polinomio
polinomioDerivada = np.poly1d.deriv(polinomio)

# Obtenemos 1000 puntos entre -10 y 10
X = np.linspace(-10, 10, num=1000)

# Obtenemos la funcion para los 1000 puntos
Y = polinomio(X)

#Obtenemos la derivada verdadera
YPrimaVerdadera = polinomioDerivada(X)

#Obtenemos la derivada numerica. La derivada es mediante esquema upwinding
YPrima = np.diff(Y)/(X[1] - X[0])

#Buscamos los puntos criticos

#Para el caso de la deriada verdadera, buscamos donde la derida es cero.
abcsisaPuntosCriticosVerdaderos = np.roots(polinomioDerivada)
ordenadasPuntosCriticosVerdadero = polinomio(abcsisaPuntosCriticosVerdaderos)

# Derivada con metodo numerico, buscamos los valores criticos
# Para ello, buscamos donde cambia de signo la derivada.
signoDeriavada = np.sign(YPrima)
ultimoSigno = signoDeriavada[0]
puntoCriticos = []

for index, signo in enumerate(signoDeriavada):
    if (signo != ultimoSigno):
        puntoCriticos.append(index)
    ultimoSigno = signo

abcsisaPuntosCriticos = X[puntoCriticos]
ordenadaPuntosCriticos = Y[puntoCriticos]

#Graficamos primero el caso mediante metodo numerico
plt.figure()
fig =  plt.subplot(2,1,1)
fig.scatter(abcsisaPuntosCriticos, ordenadaPuntosCriticos, color='orchid', label='Valores Criticos', zorder=20)
legend = fig.legend()
fig.plot(X, Y, linewidth=2, label='F(x)', zorder=10, color='darkslateblue')
plt.grid(linestyle='--')
plt.title("Polinomio f(x)=x³+x²-4x+4")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2,1,2)
plt.plot(X[0:len(YPrima)], YPrima, linewidth=2, color='darkorange' ,label='F\'(x)')
plt.title("Derivada del polinomio f(x)=x³+x²-4x+4")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(linestyle='--')

#plt.show()

#Graficamos usando el metodo analitico
plt.figure()
fig =  plt.subplot(2,1,1)
fig.scatter(abcsisaPuntosCriticosVerdaderos, ordenadasPuntosCriticosVerdadero, color='orchid', label='Valores Criticos', zorder=20)
legend = fig.legend()
fig.plot(X, Y, linewidth=2, label='F(x)', zorder=10, color='darkslateblue')
plt.grid(linestyle='--')
plt.title("Polinomio f(x)=x³+x²-4x+4")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2,1,2)
plt.plot(X, YPrimaVerdadera, linewidth=2, color='darkorange' ,label='F\'(x)')
plt.title("Derivada del polinomio f(x)=x³+x²-4x+4")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(linestyle='--')

plt.show()
