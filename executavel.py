import random

num = random.randint(1, 10)
ranking1 = "Gesboss"
hit = 100
cont = 0

print("Bem-vindo ao Jogo!\n")
opcao = input("Para iniciar digite 1;\nPara ver o ranking digite 2;\nPara sair digite 3.\n")

if opcao != "3":
    if opcao == "1":
        print("Muito bem!")
        print("Pensei em um número aleatório, de 1 a 30 e quero ver em quantas tentativas você acerta.\nA cada paupite, direi se o número é maior ou menor.\nBoa Sorte!")
        while hit != num:
            hit = int(input("Digite o número: "))
            if hit < num:
                print("Não foi dessa vez!\nO número é maior!")
            else:
                print("Não foi dessa vez!\nO número é menor!")
        cont = cont + 1
        print("Parabéns! Você conseguiu!\nSeu número de tentativas foi: ")
        print(cont)
        input("Digite seu nome para cadastrá-lo no rankink do jogo: ")
        print("Obrigado pela participação!")
        opcao = input("Para jogar novamente digite 1;\nPara ver o ranking digite 2;\nPara sair digite 3.\n")
    else:
        print(ranking1)
        opcao = input("Para iniciar digite 1;\nPara sair digite 3.\n")

else:
    print("Falou, Valeu! xD")