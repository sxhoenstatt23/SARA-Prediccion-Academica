import pandas as pd
import numpy as np
import os

# 1. Configuración inicial
np.random.seed(42) # Fija la semilla para que siempre genere los mismos datos
num_alumnos = 500  # Cantidad de alumnos a simular

print(f"Generando datos simulados para {num_alumnos} alumnos...")

# 2. Generación de variables independientes (Características)
# Promedio general entre 5.0 y 10.0
promedio = np.random.uniform(5.0, 10.0, num_alumnos)

# Porcentaje de asistencia entre 50% y 100%
asistencia = np.random.uniform(50.0, 100.0, num_alumnos)

# Tareas entregadas de un total de 20 por parcial
tareas = np.random.randint(5, 21, num_alumnos)

# 3. Lógica matemática de riesgo (Target)
# Creamos una fórmula oculta ponderada: penaliza promedios bajos, faltas y falta de tareas.
# Esto asegura que el algoritmo de SARA tenga un patrón real que descubrir.
score_riesgo = ((10 - promedio) * 0.4) + ((100 - asistencia) * 0.05) + ((20 - tareas) * 0.1)

# Añadimos un poco de "ruido" aleatorio para simular la impredecibilidad humana real
score_riesgo += np.random.normal(0, 0.5, num_alumnos)

# Determinamos el umbral (percentil 75) para que el 25% de la clase esté en riesgo (1)
umbral = np.percentile(score_riesgo, 75)
riesgo_academico = (score_riesgo >= umbral).astype(int)

# 4. Construcción del DataFrame
df_sara = pd.DataFrame({
    'matricula': [f'ALU-{str(i).zfill(4)}' for i in range(1, num_alumnos + 1)],
    'promedio_general': np.round(promedio, 1),
    'porcentaje_asistencia': np.round(asistencia, 1),
    'tareas_entregadas': tareas,
    'riesgo_academico': riesgo_academico
})

# 5. Guardado del archivo
# Se asegura de guardarlo en la carpeta 'data' que creamos ayer
ruta_salida = os.path.join('data', 'datos_alumnos.csv')
df_sara.to_csv(ruta_salida, index=False)

print(f"¡Éxito! Archivo guardado en: {ruta_salida}")
print(df_sara.head())