import numpy as np

# Definir parámetros
alambique_actual = 60
produccion_lote_actual = 262.5  # litros
botellas_por_lote_actual = produccion_lote_actual / 0.75  # botellas
tiempo_embotellado_por_botella = 39.38  # segundos
descarte_porcentaje = 23 / 1200  # 1.92%

coste_unitario_botella = 1200  # pesos
venta_unitaria_botella = 18000  # pesos

# Escalado
alambique_escalado = 300
produccion_lote_escalado = (produccion_lote_actual / alambique_actual) * alambique_escalado
botellas_por_lote_escalado = produccion_lote_escalado / 0.75  # botellas

# Escalado con ambos alambiques
produccion_lote_escalado_ambos = produccion_lote_actual + produccion_lote_escalado
botellas_por_lote_escalado_ambos = produccion_lote_escalado_ambos / 0.75  # botellas

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

# Simulación de la producción escalada con ambos alambiques
tiempo_total_escalado_ambos, botellas_efectivas_escalado_ambos, botellas_descartadas_escalado_ambos = simular_embotellado(
    botellas_por_lote_escalado_ambos, tiempo_embotellado_por_botella, descarte_porcentaje
)

# Resultados formateados
costo_total_actual = (botellas_efectivas_actual + botellas_descartadas_actual) * coste_unitario_botella
venta_total_actual = botellas_efectivas_actual * venta_unitaria_botella

costo_total_escalado = (botellas_efectivas_escalado + botellas_descartadas_escalado) * coste_unitario_botella
venta_total_escalado = botellas_efectivas_escalado * venta_unitaria_botella

costo_total_escalado_ambos = (botellas_efectivas_escalado_ambos + botellas_descartadas_escalado_ambos) * coste_unitario_botella
venta_total_escalado_ambos = botellas_efectivas_escalado_ambos * venta_unitaria_botella

# Resultados
print("Coste Unitario Botella: {0} pesos".format(formatear_numero(coste_unitario_botella)))
print("Precio de Venta Unitario Botella: {0} pesos".format(formatear_numero(venta_unitaria_botella)))
print("*" * 50, "Republica Aparte SIMULACIÓN" + "*" * 50)
print("Producción Actual:")
print(f"Tiempo total de embotellado: {tiempo_total_actual / 60:.2f} minutos")
print(f"Botellas efectivas: {botellas_efectivas_actual}")
print(f"Botellas descartadas: {botellas_descartadas_actual}")
print(f"Costo total de botellas: {formatear_numero(costo_total_actual)} pesos")
print(f"Ganancia BRUTA obtenida de ventas del total de botellas: {formatear_numero(venta_total_actual)} pesos")

print("*" * 50, "Republica Aparte SIMULACIÓN ESCALADA" + "*" * 50)
print("Producción Escalada (Alambique 300 Ltrs):")
print(f"Tiempo total de embotellado: {tiempo_total_escalado / 60:.2f} minutos")
print(f"Botellas efectivas: {botellas_efectivas_escalado}")
print(f"Botellas descartadas: {botellas_descartadas_escalado}")
print(f"Costo total de botellas: {formatear_numero(costo_total_escalado)} pesos")
print(f"Ganancia BRUTA obtenida de ventas del total de botellas: {formatear_numero(venta_total_escalado)} pesos")

print("*" * 50, "Republica Aparte SIMULACIÓN ESCALADA CON AMBOS ALAMBIQUES" + "*" * 50)
print("Producción Escalada (Alambique 60 + 300 Ltrs):")
print(f"Tiempo total de embotellado: {tiempo_total_escalado_ambos / 60:.2f} minutos")
print(f"Botellas efectivas: {botellas_efectivas_escalado_ambos}")
print(f"Botellas descartadas: {botellas_descartadas_escalado_ambos}")
print(f"Costo total de botellas: {formatear_numero(costo_total_escalado_ambos)} pesos")
print(f"Ganancia BRUTA obtenida de ventas del total de botellas: {formatear_numero(venta_total_escalado_ambos)} pesos")

# Comparación
tiempo_incremento = (tiempo_total_escalado - tiempo_total_actual) / tiempo_total_actual * 100
produccion_incremento = (botellas_efectivas_escalado - botellas_efectivas_actual) / botellas_efectivas_actual * 100

print("*" * 50, "Republica Aparte COMPARACIÓN" + "*" * 50)
print("Incremento de Tiempo de Embotellado: {:.2f}%".format(tiempo_incremento))
print("Incremento de Producción de Botellas: {:.2f}%".format(produccion_incremento))
print("Incremento de Tiempo de Embotellado con Ambos Alambiques: {:.2f}%".format((tiempo_total_escalado_ambos - tiempo_total_actual) / tiempo_total_actual * 100))
print("Incremento de Producción de Botellas con Ambos Alambiques: {:.2f}%".format((botellas_efectivas_escalado_ambos - botellas_efectivas_actual) / botellas_efectivas_actual * 100))


from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Crear subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Tiempo de Embotellado", "Botellas Efectivas", "Producción Con Ambos Alambiques", "Ganancia Bruta"),
    specs=[[{"type": "xy"}, {"type": "xy"}],
           [{"type": "domain"}, {"type": "xy"}]]
)

# Grafico 1: Tiempo de Embotellado
fig.add_trace(
    go.Bar(name='Actual', x=['Tiempo de Embotellado'], y=[tiempo_total_actual/60], text=[f'{tiempo_total_actual/60:.2f} horas'], textposition='auto'),
    row=1, col=1
)
fig.add_trace(
    go.Bar(name='Escalado', x=['Tiempo de Embotellado'], y=[tiempo_total_escalado/60], text=[f'{tiempo_total_escalado/60:.2f} horas'], textposition='auto'),
    row=1, col=1
)
fig.add_trace(
    go.Bar(name='Escalado con Ambos Alambiques', x=['Tiempo de Embotellado'], y=[tiempo_total_escalado_ambos/60], text=[f'{tiempo_total_escalado_ambos/60:.2f} horas'], textposition='auto'),
    row=1, col=1
)

# Grafico 2: Botellas Efectivas
fig.add_trace(
    go.Bar(name='Actual', x=['Botellas Efectivas'], y=[botellas_efectivas_actual], text=[f'{botellas_efectivas_actual}'], textposition='auto'),
    row=1, col=2
)
fig.add_trace(
    go.Bar(name='Escalado', x=['Botellas Efectivas'], y=[botellas_efectivas_escalado], text=[f'{botellas_efectivas_escalado}'], textposition='auto'),
    row=1, col=2
)
fig.add_trace(
    go.Bar(name='Escalado con Ambos Alambiques', x=['Botellas Efectivas'], y=[botellas_efectivas_escalado_ambos], text=[f'{botellas_efectivas_escalado_ambos}'], textposition='auto'),
    row=1, col=2
)

# Grafico 3: Producción Con Ambos Alambiques (gráfico de torta)
fig.add_trace(
    go.Pie(labels=['Botellas Efectivas', 'Botellas Descartadas'], values=[botellas_efectivas_escalado_ambos, botellas_descartadas_escalado_ambos], textinfo='label+percent+value',
           marker=dict(colors=['#FFA07A', '#87CEEB'], line=dict(color='#FFFFFF', width=2))),
    row=2, col=1
)


# Grafico 4: Ganancia Bruta
fig.add_trace(
    go.Bar(name='Actual', x=['Ganancia Bruta'], y=[venta_total_actual - costo_total_actual], text=[f'{venta_total_actual - costo_total_actual} pesos'], textposition='auto'),
    row=2, col=2
)
fig.add_trace(
    go.Bar(name='Escalado', x=['Ganancia Bruta'], y=[venta_total_escalado - costo_total_escalado], text=[f'{venta_total_escalado - costo_total_escalado} pesos'], textposition='auto'),
    row=2, col=2
)
fig.add_trace(
    go.Bar(name='Escalado con Ambos Alambiques', x=['Ganancia Bruta'], y=[venta_total_escalado_ambos - costo_total_escalado_ambos], text=[f'{venta_total_escalado_ambos - costo_total_escalado_ambos} pesos'], textposition='auto'),
    row=2, col=2
)

# Actualizar layout
fig.update_layout(title_text="Comparación de Resultados")
fig.show()
