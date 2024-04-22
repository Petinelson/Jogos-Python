import adivinhacao
import forca

def executar():
    print("********************************")
    print("**Bem vindo a seleção de jogos**")
    print("********************************")

    print("Qual jogo vc quer??")
    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Selecione o jogo: "))

    if (jogo == 1):
        print("vc selecionou adivinhação")
        adivinhacao.jogar_adivinhacao()
    elif(jogo == 2):
        print("vc selecionou adivinhação")
        forca.jogar_forca()
    else:
        print("vc deve selecionar um jogo")

if(__name__ == "__main__"):
    executar()