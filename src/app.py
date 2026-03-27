from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

ARQUIVO = "data/medicamentos.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


@app.route("/medicamentos", methods=["GET"])
def listar_medicamentos():
    return jsonify(carregar_dados())


@app.route("/medicamentos", methods=["POST"])
def adicionar_medicamento():
    dados = carregar_dados()
    novo = request.json

    if not novo.get("nome") or not novo.get("horario"):
        return jsonify({"erro": "Dados inválidos"}), 400

    dados.append(novo)
    salvar_dados(dados)

    return jsonify({"mensagem": "Medicamento adicionado com sucesso"}), 201


@app.route("/medicamentos/<nome>", methods=["DELETE"])
def remover_medicamento(nome):
    dados = carregar_dados()
    novos = [m for m in dados if m["nome"] != nome]
    salvar_dados(novos)

    return jsonify({"mensagem": "Medicamento removido com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
