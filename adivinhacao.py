import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou", chute)
        numero = int(chute)

        if numero < 1 or numero > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == numero
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos}!")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto!")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos
    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
