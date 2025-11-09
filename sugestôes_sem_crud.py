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

                if animal["espécie"] == "cachorro":

                    if animal["comportamento"] == "raivoso" or animal["comportamento"] == "agressivo":
                        print("É fortemente recomendado o uso de focinheira ao sair para passear, além disso, a ida a centros de treinamento de cães também é altamente recomenado")

                    elif animal["comportamento"] == "dócil": 
                            print("Existem três pessoas buscando um cachorro dócil, segue o nome deles e telefone para contato: \n" \
                                "1. Nome: Davi Maltez | 8199999999 \n" \
                                "2. Nome: Letícia Maria | 818888888 \n " \
                                "3. Nome: Ariana Grande | 817777777 ")
                    
                    elif animal["comportamento"] == "tímido": 
                        print("Como este cachoro é tímido, atividades de socialização com outros animais não tímidos pode ser interessante")
                    
                    elif animal["comportamento"] == "medroso":
                        print("Para cachorros medrosos, evite punições e nunca force o contato. Em vez disso, crie associações positivas com reforços como petiscos e carinho,\n" \
                        "exponha-o gradualmente a situações que o assustam (dessensibilização) e crie um ambiente seguro")


                    if int(animal["idade"]) > 7:
                            print("Como este cachorro já é idoso ele precisa de uma série de cuidados especiais: \n" \
                            "1. alimentação adequada (ração sênior, menos gordura, mais fibras) \n" \
                            "2. exercícios leves e regulares \n" \
                            "3. higiene redobrada (especialmente dental e de orelhas) \n" \
                            "4. visitas veterinárias frequentes (check-ups semestrais)")
                    else:
                        print("Para cachorros novos, as recomendações incluem: manter um ambiente seguro e confortável, oferecer uma dieta adequada para filhotes,\n" \
                        " seguir um cronograma de vacinação e vermifugação com um veterinário, além de investir em socialização e treinamento desde cedo")
                
                
                #---------------- Pássaros -----------------------
                
                elif animal["espécie"] == "pássaro":
                    
                    if animal["comportamento"] == "medroso" or animal["comportamento"] == "assutado":
                        print(" Pássaros assustados/medrosos devem ser manuseados com calma e em ambientes silenciosos")

                    elif animal["comportamento"] == "brincalhão":
                        print("Este pássaro brincalhão adora estímulos, forneça brinquedos coloridos, sinos e interações diárias para ele gastar energia")

                    elif animal["comportamento"] == "tímido":
                        print("Coloque o viveiro em local tranquilo e evite muitas visitas e com o tempo, ele ganhará confiança")

                    if int(animal["idade"]) > 5:
                        print("Como este pássaro é mais velho, garanta alimentação rica em cálcio e mantenha consultas veterinárias anuais.")
                        print("Além disso, há algumas pessoas interessadas em adotar pássaros com esta faixa etária: \n" \
                        "1. Nome: Carol | Telefone: 819999999 \n" \
                        "2. Nome: Marcelo | Telefone: 818888888")
                    else:
                        print("Como este pássaro é mais jovem, ofereça sementes variadas e espaço para voar ou se exercitar")
                        print("Além disso, há algumas pessoas interessadas em adotar pássaros nessa faixa etária: \n" \
                        "1. Nome: Elon Musk | Telefone: 816666666 \n" \
                        "2. Nome: Taylor Swift | Telefone: 815555555")

                # ------------------- HAMSTERS -------------------
                elif animal["espécie"] == "hamster":

                    if animal["comportamento"] == "agitado":
                        print("Hamsters agitados precisam de rodinhas, túneis e brinquedos para gastar suas energias")
                    
                    elif animal["comportamento"] == "tímido":
                        print("Manuseie com cuidado e evite barulhos altos, aos poucos ele irá se acostumar com o dono")
                    
                    elif animal["comportamento"] == "dócil":
                        print("Perfeito para famílias com crianças! Lembre-se de deixá-lo explorar fora da gaiola sob supervisão")

                    if int(animal["idade"]) > 2:
                        print("Hamsters idosos necessitam de ambiente mais quentinho, alimentação leve e observação de possíveis dificuldades de locomoção")
                    else:
                        print("Como é um Hamster jovem, ele precisa de uma alimentação rica em proteínas e rotina de brincadeiras diárias")

                # ------------------- OUTROS ANIMAIS -------------------
                else:
                    print("Este animal não está entre as espécies listadas, mas seguem recomendações gerais:")
                    print("1. Observe sempre o comportamento e procure um veterinário especializado;\n"
                          "2. Mantenha o ambiente limpo, seguro e adequado ao tamanho e natureza do animal;\n"
                          "3. Ofereça enriquecimento ambiental — brinquedos, estímulos e interações;\n"
                          "4. Mantenha vacinação e alimentação específicas para a espécie;\n"
                          "5. Em caso de adoção, busque pessoas com experiência na espécie ou dispostas a aprender;")
                    
            
            while True:
                continuar = input("\nDeseja ver sugestões de outro animal? (s/n): ").lower()

                if continuar != "s" and continuar !="n":
                    print("Digite uma opção válida")
                    continue
                else: 
                    break
            
            if continuar == "n":
                break