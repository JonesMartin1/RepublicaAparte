import numpy as np

# Definir parámetros
alambique_actual = 60
produccion_lote_actual = 262.5  # litros
botellas_por_lote_actual = produccion_lote_actual / 0.75  # botellas
tiempo_embotellado_por_botella = 25  # segundos
descarte_porcentaje = 23 / 1200  # 1.92%

coste_unitario_botella = 1200 # pesos
venta_unitaria_botella = 18000 # pesos

# Escalado
alambique_escalado = 300
produccion_lote_escalado = (produccion_lote_actual / alambique_actual) * alambique_escalado
botellas_por_lote_escalado = produccion_lote_escalado / 0.75  # botellas

# Función para simular el proceso de embotellado
def simular_embotellado(botellas_por_lote, tiempo_por_botella, descarte_porcentaje):
    tiempo_total = 0
    botellas_descartadas = 0
    botellas_efectivas = 0
    
    for _ in range(int(botellas_por_lote)):
        tiempo_total += tiempo_por_botella
        if np.random.rand() < descarte_porcentaje:
            botellas_descartadas += 1
        else:
            botellas_efectivas += 1
            
    return tiempo_total, botellas_efectivas, botellas_descartadas

def formatear_numero(numero):
    return f"{numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Simulación de la producción actual
tiempo_total_actual, botellas_efectivas_actual, botellas_descartadas_actual = simular_embotellado(
    botellas_por_lote_actual, tiempo_embotellado_por_botella, descarte_porcentaje
)

# Simulación de la producción escalada
tiempo_total_escalado, botellas_efectivas_escalado, botellas_descartadas_escalado = simular_embotellado(
    botellas_por_lote_escalado, tiempo_embotellado_por_botella, descarte_porcentaje
)
# Resultados formateados
costo_total_actual = (botellas_efectivas_actual + botellas_descartadas_actual) * coste_unitario_botella
venta_total_actual = botellas_efectivas_actual * venta_unitaria_botella

costo_total_escalado = (botellas_efectivas_escalado + botellas_descartadas_escalado) * coste_unitario_botella
venta_total_escalado = botellas_efectivas_escalado * venta_unitaria_botella

# Resultados
print("Coste Unitario Botella: {0} pesos".format(formatear_numero(coste_unitario_botella)))
print("Precio de Venta Unitario Botella: {0} pesos".format(formatear_numero(venta_unitaria_botella)))
print("*"*50, "Republica Aparte SIMULACIÓN"+"*"*50)
print("Producción Actual:")
print(f"Tiempo total de embotellado: {tiempo_total_actual / 60:.2f} minutos")
print(f"Botellas efectivas: {botellas_efectivas_actual}")
print(f"Botellas descartadas: {botellas_descartadas_actual}")
print(f"Costo total de botellas: {formatear_numero(costo_total_actual)} pesos")
print(f"Ganancia BRUTA obtenida de ventas del total de botellas: {formatear_numero(venta_total_actual)} pesos")


print("*"*50, "Republica Aparte SIMULACIÓN ESCALADA"+"*"*50)
print("Producción Escalada (Alambique 300 Ltrs):")
print(f"Tiempo total de embotellado: {tiempo_total_escalado / 60:.2f} minutos")
print(f"Botellas efectivas: {botellas_efectivas_escalado}")
print(f"Botellas descartadas: {botellas_descartadas_escalado}")
print(f"Costo total de botellas: {formatear_numero(costo_total_escalado)} pesos")
print(f"Ganancia BRUTA obtenida de ventas del total de botellas: {formatear_numero(venta_total_escalado)} pesos")
# Comparación
tiempo_incremento = (tiempo_total_escalado - tiempo_total_actual) / tiempo_total_actual * 100
produccion_incremento = (botellas_efectivas_escalado - botellas_efectivas_actual) / botellas_efectivas_actual * 100

print("*"*50, "Republica Aparte COMPARACIÓN"+"*"*50)

print("Incremento de Tiempo de Embotellado: {:.2f}%".format(tiempo_incremento))
print("Incremento de Producción de Botellas: {:.2f}%".format(produccion_incremento))
