import random

def jogar_adivinhacao():
    print("********************************")
    print("Bem vindo ao jodo da adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # while (total_tentativas >= rodada):
    for rodada in range(rodada, total_tentativas + 1):
        print("Tentativa numero {} de {} ".format(rodada, total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Vc digitigou: ", chute)

        if (chute < 1 or chute > 100):
            print("Vc precisa digitar numero entre 1 e 100!!!!")
            continue

        acertou = chute == numero_secreto
        maior   = chute  > numero_secreto
        menor   = chute  < numero_secreto

        if (acertou):
            print("vc acertou e fez 600 pontos!")
            pontos += 60
            break
        else:
            if(maior):
                print("vc errou, o numero que vc chutou é maior que o numero secreto")
            elif(menor):
                print("vc errou, o numero que vc chutou é menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada += 1

    print(f"O número secreto é {numero_secreto}")

if(__name__ == "__main__"):
    jogar_adivinhacao()