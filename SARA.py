import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import joblib 
import pandas as pd

load_dotenv()

modelo_sara = joblib.load('sara_modelo_final.pkl')

def get_connection():
    conexion = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conexion

app = Flask(__name__)

# Ruta 1: Muestra la interfaz visual
@app.route("/")
def inicio():
    return render_template("SARA.html")

@app.route("/evaluar", methods=["POST"])
def evaluar_alumno():
    # 1. Recibimos los datos de la interfaz
    promedio = float(request.form.get('promedio', 0))
    asistencia = float(request.form.get('asistencia', 0))
    tareas_faltantes = float(request.form.get('tareas', 0))
    
    total_tareas = 15
    
    entregadas_reales = total_tareas - tareas_faltantes
    
    porcentaje_entregadas = (entregadas_reales / total_tareas) * 100

    datos_df = pd.DataFrame(
        [[promedio, asistencia, porcentaje_entregadas]], 
        columns=['promedio_general', 'porcentaje_asistencia', 'tareas_entregadas'] 
    )
    prediccion = modelo_sara.predict(datos_df)
    
    if prediccion[0] == 1:
        nivel_riesgo = "Riesgo Alto"
    else:
        nivel_riesgo = "Normal"
        
    if promedio < 7.0 or asistencia < 70.0:
        nivel_riesgo = "Riesgo Alto"
        
    return jsonify({
        "promedio": promedio,
        "asistencia": asistencia,
        "tareas_faltantes": tareas_faltantes,
        "riesgo": nivel_riesgo
    })

if __name__ == "__main__":
    app.run(debug=True)