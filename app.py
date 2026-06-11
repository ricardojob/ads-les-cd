from flask import Flask, render_template, request
from calculator import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operacao = request.form["operacao"]
        resultado = calc(a, b, operacao)
    return render_template(
        "index.html",
        resultado=resultado
    )

def calc(a, b, operacao): 
    if operacao == "soma":
        resultado = soma(a, b)
    elif operacao == "subtracao":
        resultado = subtracao(a, b)
    elif operacao == "multiplicacao":
        resultado = multiplicacao(a, b)
    elif operacao == "divisao":
        resultado = divisao(a, b)
    return resultado

if __name__ == "__main__":
    app.run()