import mysql.connector
from flask import Flask, render_template

def get_connection():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="K1mpata7a",
        database="sara"
    )
    return conexion

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("SARA.html")

if __name__ == "__main__":
    app.run(debug=True)