from datetime import datetime

import importlib

crud = importlib.import_module("crud")
cad = importlib.import_module("cadastro_de_cuidados")

animais = getattr(crud, "animais", None)
tarefas = getattr(cad, "tarefas", None)

from contagem_regressiva import contagem_regressiva

contagem_regressiva(animais, tarefas)


def contagem_regressiva(animais, tarefas):
    if not isinstance(animais, dict) or not animais:
        print("\nNenhum animal cadastrado.")
        return
    if not isinstance(tarefas, list) or not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    hoje = datetime.now()
    print("\n=== Contagem regressiva e alertas ===")
    for t in tarefas:
        nome_animal = t.get("nome_animal") or f"ID {t.get('animal_id','?')}"
        descricao = t.get("descricao", "Sem descrição")
        data_str = t.get("data_prevista", "")
        responsavel = t.get("responsavel", "Não informado")

        try:
            data_prevista = datetime.strptime(data_str, "%d/%m/%Y")
            dias = (data_prevista.date() - hoje.date()).days
        except Exception:
            print(f"\nAnimal: {nome_animal}")
            print(f"Descrição: {descricao}")
            print(f"Data prevista: {data_str} (formato inválido)")
            print(f"Responsável: {responsavel}")
            print("Status: Data inválida")
            continue

        if dias < 0:
            status = f"VENCIDO ({-dias} dia(s) atrás)"
        elif dias == 0:
            status = "É hoje"
        elif dias <= 7:
            status = f"Próximo — faltam {dias} dia(s)"
        else:
            status = f"Faltam {dias} dia(s)"

        print(f"\nAnimal: {nome_animal}")
        print(f"Descrição: {descricao}")
        print(f"Data prevista: {data_str}")
        print(f"Responsável: {responsavel}")
        print(f"Status: {status}")
