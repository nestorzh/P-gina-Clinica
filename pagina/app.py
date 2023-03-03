from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Inicio.html")
def Inicio():
    return render_template("Inicio.html")

@app.route("/Especialidades.html")
def Especialidades():
    return render_template("Especialidades.html")

@app.route("/Servicios.html")
def Servicios():
    return render_template("Servicios.html")

@app.route("/Contactanos.html")
def Contactanos():
    return render_template("Contactanos.html")

if __name__ == "__main__":
    app.run(port=4000, host="0.0.0.0")