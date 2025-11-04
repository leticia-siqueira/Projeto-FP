from datetime import datetime

def cadastro_cuidados_atividades(lista_servicos):
    try:
        nome_animal = input("Nome do animal: ").strip()
        descricao = input("Descrição do cuidado/atividade: ").strip()
        data_str = input("Data prevista (DD/MM/AAAA): ").strip()
        responsavel = input("Responsável: ").strip()
        data_prevista = datetime.strptime(data_str, "%d/%m/%Y")
        
        for servico in lista_servicos:
            if servico['nome_animal'] == nome_animal and servico['data_prevista'] == data_prevista.strftime("%d/%m/%Y") and servico['responsavel'] == responsavel:
                print("\nJá existe um serviço marcado para este animal nesse dia.")
                continuar_cadastro = input("Deseja continuar e cadastrar outro serviço para esse animal (SIM/NÃO)? ")
                if continuar_cadastro == "SIM":
                    continue
                elif continuar_cadastro == "NÃO" or continuar_cadastro == "NAO":
                    return
                else:
                    print("Resposta inválida, cadastro cancelado!")
                    return 
            
        servico = {'nome_animal': nome_animal, 'descricao': descricao, 'data_prevista': data_prevista.strftime("%d/%m/%Y"), 
                  'responsavel': responsavel
                  }
        lista_servicos.append(servico)
        print("\nTarefa cadastrada com sucesso!")

    except Exception as e:
        print(f"\nErro no cadastro: {e}")

tarefas = []
cadastro_cuidados_atividades(tarefas)

while True:
    try:
        outro_cadastro = input("\nDeseja cadastrar outro serviço? (SIM/NÃO)").upper()
        if outro_cadastro == "SIM":
            cadastro_cuidados_atividades(tarefas)
        elif outro_cadastro == "NÃO" or outro_cadastro == "NAO":
            print("\nObrigada pela preferência!")
            break
        else:
            print("\nResposta inválida! Responda corretamente.")
            continue
    except Exception as e:
        print(f"\nErro: {e}")
        continue


