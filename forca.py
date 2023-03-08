import random

def jogar():
    imprime_mensagem_bem_vindo()

    listaPalavras = get_palavras_arquivo()

    palavra_secreta = random.choice(listaPalavras).upper()

    letras_acertadas = letras_acertadas_jogo(palavra_secreta)
    letras_jogadas = []

    enforcou = False
    acertou = False
    erros = 0
    max_erros = 7

    while not enforcou and not acertou:
        letra = campo_para_usuario_digitar_letra(letras_acertadas)

        if letra in letras_jogadas:
            print(f'A letra {letra} já foi. Escolha outra!')
        else:
            if letra in palavra_secreta:
                verifica_letra_na_palavra_secreta(letra, letras_acertadas, palavra_secreta)
                acertou = "_" not in letras_acertadas
            else:
                erros += 1
                desenha_forca(erros)
                enforcou = verifica_situacao_erro(erros, max_erros, enforcou)

            letras_jogadas.append(letra)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")
    verifica_jogar_novamente()


def campo_para_usuario_digitar_letra(letras_acertadas):
    print(letras_acertadas)
    letra = input('Digite uma letra: ').strip().upper()
    while not letra.isalpha() or len(letra) != 1:
        print('Digite uma letra de A a Z!')
        letra = input('Digite uma letra: ').strip().upper()
    return letra


def verifica_letra_na_palavra_secreta(letra, letras_acertadas, palavra_secreta):
    for index, letraPalavra in enumerate(palavra_secreta):
        if letra == letraPalavra:
            letras_acertadas[index] = letra


def letras_acertadas_jogo(palavra):
    return ["_" for letra in palavra]


def verifica_situacao_erro(erros, max_erros, enforcou):
    if erros >= max_erros:
        enforcou = True

    if 0 < erros < 7:
        print(f'Você ainda tem: {max_erros - erros} tentativas')
    return enforcou


def verifica_jogar_novamente():
    opcao = 0
    while opcao == 0:
        opcao = int(input('Gostaria de jogar novamente?\n[1] SIM\n[2] NÃO\nResposta:'))
    if opcao == 1:
        jogar()
    else:
        print('Até a próxima!')


def imprime_mensagem_bem_vindo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def get_palavras_arquivo():
    with open('palavra.txt', "r") as arquivo:
        palavras = arquivo.read()
        listaPalavras = list(map(str, palavras.split()))
        return listaPalavras


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if __name__ == "__main__":
    jogar()
