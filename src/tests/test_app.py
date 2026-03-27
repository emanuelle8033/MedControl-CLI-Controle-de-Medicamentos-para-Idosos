from src.app import carregar_dados, salvar_dados


def test_carregar_dados_retorna_lista():
    dados = carregar_dados()
    assert isinstance(dados, list)


def test_salvar_dados_funciona():
    dados_teste = [
        {
            "nome": "Dipirona",
            "horario": "08:00"
        }
    ]

    salvar_dados(dados_teste)
    dados = carregar_dados()

    assert dados == dados_teste


def test_salvar_e_ler_varios_medicamentos():
    dados_teste = [
        {"nome": "Dipirona", "horario": "08:00"},
        {"nome": "Paracetamol", "horario": "12:00"},
        {"nome": "Omeprazol", "horario": "07:00"}
    ]

    salvar_dados(dados_teste)
    dados = carregar_dados()

    assert len(dados) == 3
