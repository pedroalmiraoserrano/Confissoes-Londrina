from flask import Flask, render_template
import pandas as pd
import os
print("FLASK RODANDO EM:", os.getcwd())
print("LENDO ARQUIVO DE:", os.path.abspath("confissoes.xlsx"))


app = Flask(__name__)

def carregar_dados():
    df = pd.read_excel("confissoes.xlsx")

    # Normaliza nomes das colunas
    df.columns = df.columns.str.strip()

    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

    dias = {dia: [] for dia in dias_semana}

    for _, row in df.iterrows():
        paroquia = row["Paróquia"]
        local = row["Local"]

        for dia in dias_semana:
            if dia in df.columns:
                horario = row[dia]
                if pd.notna(horario) and horario != "":
                    dias[dia].append({
                        "paroquia": paroquia,
                        "local": local,
                        "horario": horario
                    })

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
