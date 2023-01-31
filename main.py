import os
import random
import dicionario
from termcolor import cprint, colored

# Desenho do jogo
banner   = """


    ███████╗ ██████╗ ██████╗  ██████╗ █████╗ 
    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    █████╗  ██║   ██║██████╔╝██║     ███████║
    ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║
    ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
     ==============================================
"""

# desenhos da forca
desenhos = ["""
     _____
    |     |
    |
    |
    |
    |
    |
 ___|____

 """, """
     _____
    |     |
    |     O
    |
    |
    |
    |
 ___|____

 """, """
     _____
    |     |
    |     O
    |    /|
    |
    |
    |
 ___|____

 """, """
     _____
    |     |
    |     O
    |    /|\\
    |    
    |
    |
 ___|____

 """, """
     _____
    |     |
    |     O
    |    /|\\
    |    /
    |
    |
 ___|____

 ""","""
     _____
    |     |
    |     O
    |    /|\\
    |    / \\
    |
    |
 ___|____

 """,]

# placar
perdas   = 0
vitorias = 0
mantem_o_jogo = True

# loop do jogo (mantem o jogo em loop)
while mantem_o_jogo:
    continua   = True
    verifica   = 0  # verifica a quantidade de letras restantes
    erros      = 0  # quantidade de erros
    corretas   = [] # armazena as letras corretas
    tentativas = [] # armazena as letras das tentativas

    # escolha aleatoria da palavra
    dica     = random.choice(list(dicionario.palavras))         # escolhe um tema
    palavra  = random.choice(dicionario.palavras[dica]).lower() # escolhe uma palavra na lista de temas


    # loop da partida (mantem a partida em loop)
    while continua:

        # limpa o terminal e emprime o banner
        os.system('cls')
        cprint(banner, 'cyan')
        
        verifica = 0 # zera o contador

        # verifica e imprime os dados do jogo
        if erros < len(desenhos):
            print(desenhos[erros])
            print("  -  Dica   : ", dica)
            print("  -  Letras : ", " ".join(tentativas))

            palavra_banner = "  -  Palavra: "
        
            for letra in palavra:
                if letra in corretas:
                    palavra_banner += " " + letra
                else:
                    palavra_banner += ' _'
                    verifica += 1

            print(palavra_banner)
            
            # verifica se ganhou
            if verifica == 0 and len(corretas)>1:
                print("\n\n", "[+]", colored("Você ganhou!", "green"))
                print("  -  Deseja começar novamente? Digite (ENTER ou N):")
                if input("  -  >>> ").lower() == "n":
                    mantem_o_jogo = False
                vitorias  += 1
                break

            # recebe a letra e faz as comparação (se a tentativa foi correta, incorreta ou utilizada anteriormente)
            while True:
                tentativa = input("\n  -  Digite uma letra: ").lower()
                if len(tentativa)>1:
                    print("  -  Oops... Digite apenas uma letra por vez!")
                    continue
                if tentativa not in tentativas:
                    tentativas.append(tentativa)
                    if tentativa in palavra:
                        corretas.append(tentativa)
                        break
                    else:
                        erros += 1
                        if erros+2 > len(desenhos):
                            print("\n\n", "[+]", colored("Você perdeu...", 'red'))
                            print("  -  Deseja começar novamente? Digite (ENTER ou N):")
                            if input("  -  >>> ").lower() == "n":
                                mantem_o_jogo = False
                            perdas  += 1
                            continua = False
                        break
                else:
                    print("  -  Oops... Você já usou essa letra, tente uma diferente!")


os.system('cls')
cprint(banner, 'cyan')

print("\n [+] Placar:")
print("  -  Perdas:", colored(perdas, 'red'))
print("  -  Vitórias:", colored(vitorias, 'green'))
print('\n\n')
print(" [+] Developed by", colored("Francis Taylor.","cyan"))
print('\n\n')