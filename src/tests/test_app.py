import os
from src.app import adicionar_medicamento, listar_medicamentos, remover_medicamento

def test_adicionar_medicamento():
    adicionar_medicamento("Dipirona", "08:00")
    meds = listar_medicamentos()
    assert any(m["nome"] == "Dipirona" for m in meds)

def test_remover_medicamento():
    adicionar_medicamento("Paracetamol", "10:00")
    remover_medicamento("Paracetamol")
    meds = listar_medicamentos()
    assert not any(m["nome"] == "Paracetamol" for m in meds)

def test_listar_retorna_lista():
    meds = listar_medicamentos()
    assert isinstance(meds, list)