import math
import matplotlib.pyplot as plt
import numpy as np

masa = 115  # kgs
alturaMaximaCaidaLibre = 30  # m
coeficienteResorte = 15  # N/m
coeficienteAmortiguamiento = 15  # N/(m/s)

tiempoFinalCaidaLibre = math.sqrt(2 * alturaMaximaCaidaLibre / 9.81)  # s
posicionFinalCaidaLibre = 0
velocidadFinalCaidaLibre = 9.81 * tiempoFinalCaidaLibre  # m/s

lambdaAmortiguamiento = coeficienteAmortiguamiento / (2 * masa)  # 1/s
omegaAmortiguamiento = math.sqrt(9.81 / alturaMaximaCaidaLibre)  # 1/s
print("lambda al cuadrado: ", lambdaAmortiguamiento ** 2)
print("omega al cuadrado: ", omegaAmortiguamiento ** 2)

coeficiente = math.sqrt(abs(omegaAmortiguamiento ** 2 -
                        lambdaAmortiguamiento ** 2))  # 1/s

constante1 = (velocidadFinalCaidaLibre + lambdaAmortiguamiento *
              posicionFinalCaidaLibre)/coeficiente  # m/s
constante2 = posicionFinalCaidaLibre  # m


def x(t): return constante1 * math.exp(-lambdaAmortiguamiento * t) * math.sin(coeficiente *
                                                                              t) + constante2 * math.exp(-lambdaAmortiguamiento * t) * math.cos(coeficiente * t)  # m


def v(t): return -constante1 * (lambdaAmortiguamiento * math.exp(-lambdaAmortiguamiento * t) * math.sin(coeficiente * t) + coeficiente * math.exp(-lambdaAmortiguamiento * t) * math.cos(coeficiente * t)
                                ) + constante2 * (lambdaAmortiguamiento * math.exp(-lambdaAmortiguamiento * t) * math.cos(coeficiente * t) - coeficiente * math.exp(-lambdaAmortiguamiento * t) * math.sin(coeficiente * t))  # m/s


def x1(t): return (9.81 * t ** 2)/2  # m


def v1(t): return 9.81 * t  # m/s


posiciones = []
velocidades = []

for i in range(0, 5000):
    posiciones.append(-1*x(i/100) - alturaMaximaCaidaLibre)
    velocidades.append(-1*v(i/100))

plt.plot(posiciones)
plt.plot(velocidades)
plt.hlines(0, 0, 5000, colors='g', linestyles='dashed')
plt.hlines(-30, 0, 5000, colors='g', linestyles='dashed')
plt.legend(['Posición', 'Velocidad'])
plt.show()
