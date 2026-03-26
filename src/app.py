from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

ARQUIVO = "data/medicamentos.json"


# -------------------------
# Funções para o JSON
# -------------------------

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


# -------------------------
# ROTAS DA API
# -------------------------

# Listar medicamentos
@app.route("/medicamentos", methods=["GET"])
def listar_medicamentos():
    return jsonify(carregar_dados())


# Adicionar medicamento
@app.route("/medicamentos", methods=["POST"])
def adicionar_medicamento():
    dados = carregar_dados()

    novo = request.json

    if not novo.get("nome") or not novo.get("horario"):
        return jsonify({"erro": "Dados inválidos"}), 400

    dados.append(novo)
    salvar_dados(dados)

    return jsonify({"mensagem": "Medicamento adicionado com sucesso"}), 201


# Remover medicamento
@app.route("/medicamentos/<nome>", methods=["DELETE"])
def remover_medicamento(nome):
    dados = carregar_dados()

    novos = [m for m in dados if m["nome"] != nome]
    salvar_dados(novos)

    return jsonify({"mensagem": "Medicamento removido com sucesso"})


# -------------------------
# Rodar servidor
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)