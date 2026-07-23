import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import joblib 

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

# RUTA: El puente entre el HTML y la Inteligencia Artificial
@app.route("/evaluar", methods=["POST"])
def evaluar_alumno():
    # 1. Recibimos los datos que nos enviará el HTML
    promedio = float(request.form.get('promedio', 0))
    asistencia = float(request.form.get('asistencia', 0))
    tareas_faltantes = int(request.form.get('tareas', 0))
    
    # 2. Le pasamos los datos al modelo para que haga la predicción
    prediccion = modelo_sara.predict([[promedio, asistencia, tareas_faltantes]])
    
    # 3. Interpretamos el resultado (1 = Riesgo, 0 = Normal)
    if prediccion[0] == 1:
        nivel_riesgo = "Riesgo Alto"
    else:
        nivel_riesgo = "Normal"
        
    # 4. Devolvemos la respuesta
    return jsonify({
        "promedio": promedio,
        "asistencia": asistencia,
        "tareas_faltantes": tareas_faltantes,
        "riesgo": nivel_riesgo
    })

if __name__ == "__main__":
    app.run(debug=True)