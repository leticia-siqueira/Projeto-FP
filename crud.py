animais = {}
novo_id = 1

while True:
    print("\n===---===---=== Seja bem vindo ao Adocão+ ===---===---===")
    print("===---===---===---===---=== Menu ===---===---===---===---==")
    print("1. Adicionar animal")
    print("2. Visualizar animais")
    print("3. Sair")

    opcao = int(input("Digite o número da opção escolhida: "))

    if opcao == 1:
        print("===---=== Adicionar animal ===---===")
        nome = input("Nome: ")
        especie = input("Espécie: ")
        raca = input("Raça: ")
        idade = input("Idade: ")
        estado_de_saude = input("Estado de saúde: ")
        comportamento = input("Comportamento: ")
        data = input("Data: ")

        animal = {
            "nome": nome,
            "especie": especie,
            "raça": raca,
            "idade": idade,
            "estado_de_saude": estado_de_saude,
            "comportamento": comportamento,
            "data_de_chegada": data
        }

        animais[novo_id] = animal
        print(f"===---=== Animal cadastrado com o ID {novo_id}")

        novo_id += 1

    elif opcao == 2:
        print("===---=== Lista de animais ===---===")
        if not animais:
            print("\n=== Nenhum animal cadastrado ===")
        else:
            for id_animal, dados in animais.items():
                print(f"\nID: {id_animal}")
                for info, valor in dados.items():
                    print(f"{info.capitalize()}: {valor}")
    elif opcao == 3:
        break

    else:
        print("===---=== Opção inválida ===---===")
