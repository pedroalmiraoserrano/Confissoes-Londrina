from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def carregar_dados():
    df = pd.read_excel("confissoes.xlsx")
    # Agrupa por dia da semana
    dias = {}
    for dia in df["dia_semana"].unique():
        dias[dia] = df[df["dia_semana"] == dia].to_dict(orient="records")
    return dias

@app.route("/")
def index():
    dados = carregar_dados()
    # Ordenação opcional dos dias
    ordem = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    dados_ordenados = {dia: dados.get(dia, []) for dia in ordem}
    return render_template("index.html", dias=dados_ordenados)

if __name__ == "__main__":
    app.run(debug=True)
