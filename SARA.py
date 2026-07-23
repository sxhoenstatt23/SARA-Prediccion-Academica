import os
import mysql.connector
from flask import Flask, render_template
from dotenv import load_dotenv

# Esto carga las variables secretas del archivo .env
load_dotenv()

def get_connection():
    # Ahora Python buscará la contraseña en el archivo oculto
    conexion = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conexion

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("SARA.html")

if __name__ == "__main__":
    app.run(debug=True)