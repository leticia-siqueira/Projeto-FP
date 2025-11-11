from datetime import datetime

def cadastro_cuidados_atividades(lista_servicos):
    try:
        nome_animal = input("Nome do animal: ").strip().lower()
        descricao = input("Descrição do cuidado/atividade: ").strip().lower()
        responsavel = input("Responsável: ").strip().lower()
        
        while True:
            data_str = input("Data prevista (DD/MM/AAAA): ").strip()
            try:
                data_prevista = datetime.strptime(data_str, "%d/%m/%Y")
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")
                continue

            for servico in lista_servicos:
                if (servico['nome_animal'] == nome_animal and
                    servico['data_prevista'] == data_prevista.strftime("%d/%m/%Y") and
                    servico['responsavel'] == responsavel):
                    print("\nJá existe um serviço marcado para este animal")
                    continuar = input("Deseja cadastrar para OUTRA data? (SIM/NÃO) ").upper()
                    if continuar == "SIM":
                        break 
                    elif continuar == "NAO" or continuar == "NÃO":
                        print("Cadastro cancelado!")
                        return
            else:
                break

        servico = {
            'nome_animal': nome_animal, 'descricao': descricao, 'data_prevista': data_prevista.strftime("%d/%m/%Y"),
            'responsavel': responsavel}
        
        lista_servicos.append(servico)
        print("\nTarefa cadastrada com sucesso!")
    
    except:
        print("\nErro no cadastro, tente novamente!")

lista_servicos = []
cadastro_cuidados_atividades(lista_servicos)

while True:
    try:
        outro_cadastro = input("\nDeseja cadastrar outro serviço? (SIM/NÃO)").upper()
        if outro_cadastro == "SIM":
            cadastro_cuidados_atividades(lista_servicos)
        elif outro_cadastro == "NÃO" or outro_cadastro == "NAO":
            print("\nObrigada pela preferência! Atividade marcada.")
            break
        else:
            print("\nResposta inválida!")
            continue
    except ValueError:
        print("\nErro!")
        continue


