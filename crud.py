animais = {}
novo_id = 1

def exibir_menu():
    print("\n===---===---=== Seja bem vindo ao Adoção+ ===---===---===")
    print("===---===---===---===---=== Menu ===---===---===---===---==")
    print("1. Adicionar animal")
    print("2. Editar animal")
    print("3. Excluir animal")
    print("4. Visualizar animais")
    print("5. Sair")

def adicionar_animal(animais, id_atual):
    print("===---=== Adicionar animal ===---===")
    nome = input("Nome: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    estado_de_saude = input("Estado de saúde: ")
    comportamento = input("Comportamento: ")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    animal = {
        "nome": nome,
        "espécie": especie,
        "raça": raca,
        "idade": idade,
        "estado de saúde": estado_de_saude,
        "comportamento": comportamento,
        "data de chegada": data
    }

    animais[id_atual] = animal
    print(f"===---=== Animal cadastrado com o ID {id_atual}")
    return id_atual + 1

def editar_animal(animais):
    if not animais:
        print("\n=== Nenhum animal cadastrado ===")
        return

    print("\n===---=== Editar Animal ===---===")
    visualizar_animais(animais)

    try:
        id_editar = int(input("\nDigite o ID do animal que deseja editar: "))
        if id_editar not in animais:
            print("=== ID não encontrado ===")
            return

        animal = animais[id_editar]
        print("\n=== Deixe em branco se não quiser alterar o valor atual ===")
        for chave, valor in animal.items():
            novo_valor = input(f"{chave.capitalize()} ({valor}): ")
            if novo_valor.strip():
                animal[chave] = novo_valor

        print("=== Animal atualizado com sucesso ===")

    except ValueError:
        print("Entrada inválida. Digite um número de ID válido.")

def excluir_animal(animais):
    if not animais:
        print("\n=== Nenhum animal cadastrado ===")
        return

    print("\n===---=== Excluir Animal ===---===")
    visualizar_animais(animais)

    try:
        id_excluir = int(input("\nDigite o ID do animal que deseja excluir: "))
        if id_excluir not in animais:
            print("=== ID não encontrado ===")
            return

        confirmar = input(f"Tem certeza que deseja excluir '{animais[id_excluir]['nome']}'? (s/n): ").lower()
        if confirmar == "s":
            del animais[id_excluir]
            print("=== Animal excluído com sucesso ===")
        else:
            print("=== Operação cancelada ===")

    except ValueError:
        print("Entrada inválida. Digite um número de ID válido.")

def visualizar_animais(animais):
    print("===---=== Lista de animais ===---===")
    if not animais:
        print("\n=== Nenhum animal cadastrado ===")
    else:
        for id_animal, dados in animais.items():
            print(f"\nID: {id_animal}")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")

while True:
    exibir_menu()
    opcao = int(input("Digite o número da opção escolhida: "))

    if opcao == 1:
        novo_id = adicionar_animal(animais, novo_id)
    elif opcao == 2:
        editar_animal(animais)
    elif opcao == 3:
        excluir_animal(animais)
    elif opcao == 4:
        visualizar_animais(animais)
    elif opcao == 5:
        break
    else:
        print("===---=== Opção inválida ===---===")
