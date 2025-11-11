from datetime import datetime
import os; os.system('cls')

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


#----------------------------------------------Sugestões Personalizadas----------------------------------------------------


def sugestões_personalizadas(animais):
    while True: 
        confirmação_sugestão = input("Você deseja ver algumas sugestões personalizadas dos animais cadastrados?(s/n): ").lower()

        if confirmação_sugestão != "s" and confirmação_sugestão != "n":
            print("Digite uma opção válida")
            continue
        else: 
            break
    if confirmação_sugestão == "n":
        return
    else:
        while True:
            while True:
                try:
                    id_sugestão = int(input("Digite o ID do animal que você deseja ver uma sugestão personalizada: "))
                    break
                except ValueError:
                    print("Apenas números são permitidos")


            if id_sugestão not in animais: 
                print("===ID não encontrado===")
            else: 
                animal = animais[id_sugestão]
                print(f"Ótimo, agora estamos acessando os dados de {animal['nome']}")
                print()

                if animal["espécie"] == "cachorro":

                    if animal["comportamento"] == "raivoso" or animal["comportamento"] == "agressivo":
                        print("É fortemente recomendado o uso de focinheira ao sair para passear, além disso, a ida a centros de treinamento de cães também é altamente recomenado")
                        print()

                    elif animal["comportamento"] == "dócil": 
                            print("Existem três pessoas buscando um cachorro dócil, segue o nome deles e telefone para contato: \n" \
                                "1. Nome: Davi Maltez | 8199999999 \n" \
                                "2. Nome: Letícia Maria | 818888888 \n" \
                                "3. Nome: Ariana Grande | 817777777 ")
                            print()
                    
                    elif animal["comportamento"] == "tímido": 
                        print("Como este cachoro é tímido, atividades de socialização com outros animais não tímidos pode ser interessante")
                        print()

                    elif animal["comportamento"] == "medroso":
                        print("Para cachorros medrosos, evite punições e nunca force o contato. Em vez disso, crie associações positivas com reforços como petiscos e carinho,\n" \
                        "exponha-o gradualmente a situações que o assustam (dessensibilização) e crie um ambiente seguro")
                        print()


                    if int(animal["idade"]) > 7:
                            print("Como este cachorro já é idoso ele precisa de uma série de cuidados especiais: \n" \
                            "1. alimentação adequada (ração sênior, menos gordura, mais fibras) \n" \
                            "2. exercícios leves e regulares \n" \
                            "3. higiene redobrada (especialmente dental e de orelhas) \n" \
                            "4. visitas veterinárias frequentes (check-ups semestrais)")
                            print()
                    else:
                        print("Para cachorros novos, as recomendações incluem: manter um ambiente seguro e confortável, oferecer uma dieta adequada para filhotes,\n" \
                        " seguir um cronograma de vacinação e vermifugação com um veterinário, além de investir em socialização e treinamento desde cedo")
                        print()
                
                #---------------- Pássaros -----------------------
                
                elif animal["espécie"] == "pássaro":
                    
                    if animal["comportamento"] == "medroso" or animal["comportamento"] == "assutado":
                        print(" Pássaros assustados/medrosos devem ser manuseados com calma e em ambientes silenciosos")
                        print()

                    elif animal["comportamento"] == "brincalhão":
                        print("Este pássaro brincalhão adora estímulos, forneça brinquedos coloridos, sinos e interações diárias para ele gastar energia")
                        print()
                    elif animal["comportamento"] == "tímido":
                        print("Coloque o viveiro em local tranquilo e evite muitas visitas e com o tempo, ele ganhará confiança")
                        print()

                    if int(animal["idade"]) > 5:
                        print("Como este pássaro é mais velho, garanta alimentação rica em cálcio e mantenha consultas veterinárias anuais.")
                        print("Além disso, há algumas pessoas interessadas em adotar pássaros com esta faixa etária: \n" \
                        "1. Nome: Carol | Telefone: 819999999 \n" \
                        "2. Nome: Marcelo | Telefone: 818888888")
                        print()
                    else:
                        print("Como este pássaro é mais jovem, ofereça sementes variadas e espaço para voar ou se exercitar")
                        print("Além disso, há algumas pessoas interessadas em adotar pássaros nessa faixa etária: \n" \
                        "1. Nome: Elon Musk | Telefone: 816666666 \n" \
                        "2. Nome: Taylor Swift | Telefone: 815555555")
                        print()

                # ------------------- HAMSTERS -------------------
                elif animal["espécie"] == "hamster":

                    if animal["comportamento"] == "agitado":
                        print("Hamsters agitados precisam de rodinhas, túneis e brinquedos para gastar suas energias")
                        print()
                    
                    elif animal["comportamento"] == "tímido":
                        print("Manuseie com cuidado e evite barulhos altos, aos poucos ele irá se acostumar com o dono")
                        print()
                    
                    elif animal["comportamento"] == "dócil":
                        print("Perfeito para famílias com crianças! Lembre-se de deixá-lo explorar fora da gaiola sob supervisão")
                        print()

                    if int(animal["idade"]) > 2:
                        print("Hamsters idosos necessitam de ambiente mais quentinho, alimentação leve e observação de possíveis dificuldades de locomoção")
                        print()
                    else:
                        print("Como é um Hamster jovem, ele precisa de uma alimentação rica em proteínas e rotina de brincadeiras diárias")
                        print()
                # ------------------- OUTROS ANIMAIS -------------------
                else:
                    print("Este animal não está entre as espécies listadas, mas seguem recomendações gerais:")
                    print()
                    print("1. Observe sempre o comportamento e procure um veterinário especializado;\n"
                          "2. Mantenha o ambiente limpo, seguro e adequado ao tamanho e natureza do animal;\n"
                          "3. Ofereça enriquecimento ambiental — brinquedos, estímulos e interações;\n"
                          "4. Mantenha vacinação e alimentação específicas para a espécie;\n"
                          "5. Em caso de adoção, busque pessoas com experiência na espécie ou dispostas a aprender;")
                    print()
                    
            
            while True:
                continuar = input("\nDeseja ver sugestões de outro animal? (s/n): ").lower()

                if continuar != "s" and continuar !="n":
                    print("Digite uma opção válida")
                    continue
                else: 
                    break
            
            if continuar == "n":
                break

sugestões_personalizadas(animais)