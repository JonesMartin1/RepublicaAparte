import datetime
import numpy as np
import scipy.stats as stats
import random

#Variables globales con respecto al tiempo en minutos
macerado = 4320
goteado = 20
EnfriarChiller1 = 50
EnfriarChiller2 = 70
CalentarSolucion = 60
Cabeza = 40
Corazon = 210
Homogeneizacion1 = 15
Homogeneizacion2 = 20

#Variables globales con respecto a la producción en litros
SolucionCondensada = 50
LitrosGin = 350*0.75

#Variables globales con respecto a temperatura
Evaporacion = 80

#Variables globales con respecto a la temperatura
Chiller = random.randrange(4,15)


def chiCuadrado(numeros: list, rango=10, E=0.005):
    # Convertir los números a una escala de 0 a 1 si es necesario
    numerosEscalados = [(x / 10) + 0.01 for x in numeros]
    
    # Definir los límites de los bins
    RangosEntre = np.linspace(0, 1, rango+1)
    
    # Crear un histograma con los números escalados
    frecuenciaObservada, _ = np.histogram(numerosEscalados, bins=RangosEntre)
    #print(frecuenciaObservada)
    
    # Calcular la frecuencia esperada
    frecuenciaEsperada = len(numerosEscalados) / rango
    
    # Calcular el estadístico chi-cuadrado
    estadistico = np.sum((frecuenciaObservada - frecuenciaEsperada) ** 2 / frecuenciaEsperada)
    
    # Obtener el valor crítico de la distribución chi-cuadrado
    valorCritico = stats.chi2.ppf(1 - E, rango - 1)
    
    # Retornar el resultado de la prueba
    return estadistico <= valorCritico

def generador_aleatorio_mixto1(semilla: int, a, c, m, p):
    resultados = []
    while len(resultados) < p:
        semilla = ((a * semilla + c) % m) + datetime.datetime.now().microsecond
        for digit in str(semilla):
            if len(resultados) < p:
                resultados.append(int(digit))
    if chiCuadrado(resultados):
        return [((((x / m)*345000000))) for x in resultados]
    else:
       return generador_aleatorio_mixto1(semilla, a, c, m, p)
   
def clasificar_numeros(lista):
    # Clasifica cada número de la lista y lo posiciona según la distribución proporcionada por el escenario
    clasificados = []
    for valor in lista:
        if  valor < 0.036:
            clasificados.append(12)
        elif 0.037 < valor <= 0.188:
            clasificados.append(13)
        elif 0.189 < valor <= 0.224:
            clasificados.append(14)
        elif 0.225 < valor <= 0.605:
            clasificados.append(15)
        elif 0.606 < valor <= 0.659:
            clasificados.append(16)
        elif 0.660 < valor <= 0.887:
            clasificados.append(17)
        elif 0.888 < valor:
            clasificados.append(18)
        else:
            clasificados.append(17)
    # Transforma cada número aleatorio en una marca de clase la cuál está relacionada por una distribución 
    return clasificados

clima = random.randrange(12,18)

def procesar_y_sumar(clima):
    contador = 0
    tiempo = 0
    
    for valor in clima:
        contador += 1
        if valor == 12:
            tiempo +=  (goteado + EnfriarChiller1 + CalentarSolucion + Cabeza + Corazon + Homogeneizacion1 + Homogeneizacion2)
            print("Día normal de trabajo donde todo funciona correctamente")
        elif valor == 13:
            tiempo +=  (goteado + EnfriarChiller1 + CalentarSolucion + Cabeza + Corazon + Homogeneizacion1 + Homogeneizacion2)
            print("Día normal de trabajo donde todo funciona correctamente")
        elif valor == 14:
            tiempo +=  (goteado + EnfriarChiller1 + CalentarSolucion + Cabeza + Corazon + Homogeneizacion1 + Homogeneizacion2)
            print("Día normal de trabajo donde todo funciona correctamente")
        elif valor == 15:
            tiempo +=  (goteado + EnfriarChiller1 + CalentarSolucion + Cabeza + Corazon + Homogeneizacion1 + Homogeneizacion2)
            print("Día normal de trabajo donde todo funciona correctamente")
        elif valor == 16:
            tiempo +=  (goteado + EnfriarChiller1 + CalentarSolucion + Cabeza + Corazon + Homogeneizacion1 + Homogeneizacion2)
            print("Día normal de trabajo donde todo funciona correctamente")
        elif valor == 17:
            tiempo +=  (goteado + EnfriarChiller1 + CalentarSolucion + Cabeza + Corazon + Homogeneizacion1 + Homogeneizacion2)
            print("Día normal de trabajo donde todo funciona correctamente")
        elif valor == 18:
            tiempo +=  (goteado + EnfriarChiller2 + CalentarSolucion + Cabeza + Corazon + Homogeneizacion1 + Homogeneizacion2)
            print("Día lento de trabajo donde el chiller tarda en enfríar debido a las altas temperaturas")
            
    return tiempo/60 + contador * macerado/60


# Introducir valores desde la entrada del usuario
p = int(input("Introducir el número de iteraciones de tiempo: "))

# Llamar a la función generador_aleatorio_mixto1 con los valores introducidos por el usuario
aleatorios = generador_aleatorio_mixto1(9999, 1103515244, 12345, (2**31-1), p)

# Llamar a las funciones siguientes con los resultados
resultado_clasificacion = clasificar_numeros(aleatorios)
resultado_procesamiento = procesar_y_sumar(resultado_clasificacion)

print("Resultado final:", resultado_procesamiento, "horas para producir", p, "lotes de República Aparte")