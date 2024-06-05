import random
from colorama import init, Fore, Style, Back


# Inicia o colorama
init()

print(Style.BRIGHT + Fore.WHITE + Back.RED + f"Iniciando o jogo de adivinhar{Style.RESET_ALL}")
print()

# Variaveis importantes
numero_secreto = random.randint(1, 100)
total_de_tentativas_nivel_1, total_de_tentativas_nivel_2, total_de_tentativas_nivel_3 = 20, 10, 5
rodada = 1
nivel_1, nivel_2, nivel_3 = 20, 10, 5

# Variaveis de textos com cores
texto_dos_niveis = Fore.WHITE + Back.BLUE + f"Selecione um nivel:{Style.RESET_ALL}\n{Fore.WHITE + Back.GREEN}1. 20 tentativas{Style.RESET_ALL}\n{Fore.WHITE + Back.YELLOW}2. 10 tentativas{Style.RESET_ALL}\n{Fore.WHITE + Back.RED}3. 5 tentativas{Style.RESET_ALL}\n"
input_do_usuario = (Fore.BLACK + Back.YELLOW + "Nivel: ")

# Input do usuário
print(f"{texto_dos_niveis}\n")
selecionar_nivel = int(input(f"{Fore.YELLOW}{input_do_usuario}{Style.RESET_ALL}"))
print()


if selecionar_nivel == 1:
    print(Fore.BLACK + Back.LIGHTBLUE_EX + "Voce selecionou o nivel 1", Style.RESET_ALL)
    for rodada in range(1, nivel_1 + 1):
        
        fazer_pergunta = int(input("\nDigite um número: "))
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas_nivel_1))
        print("Voce digitou o número: ", fazer_pergunta)

        # Variaveis de comparação
        acertou = fazer_pergunta == numero_secreto
        maior = fazer_pergunta > numero_secreto
        menor = fazer_pergunta < numero_secreto

        # Comparações
        if(acertou):
            print("Voce acertou!")
            break
        elif(maior):
            print("Voce errou, seu chute foi maior que o número secreto!")
        elif(menor):
            print("Voce errou, seu chute foi menor que o número secreto")
        
        rodada = rodada + 1
        

elif selecionar_nivel == 2:
    print("Voce selecionou o nivel 2")
    for rodada in range(1, nivel_2 + 1):
        
        fazer_pergunta = int(input("\nDigite um número: "))
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas_nivel_2))
        print("Voce digitou o número: ", fazer_pergunta)

        # Variaveis de comparação
        acertou = fazer_pergunta == numero_secreto
        maior = fazer_pergunta > numero_secreto
        menor = fazer_pergunta < numero_secreto

        # Comparações
        if(acertou):
            print("Voce acertou!")
            break
        elif(maior):
            print("Voce errou, seu chute foi maior que o número secreto!")
        elif(menor):
            print("Voce errou, seu chute foi menor que o número secreto")
        
        rodada = rodada + 1


elif selecionar_nivel == 3:
    print("Voce selecionou o nivel 3")
    for rodada in range(1, nivel_3 + 1):

        fazer_pergunta = int(input("\nDigite um número: "))
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas_nivel_3))
        print("Voce digitou o número: ", fazer_pergunta)

        # Variaveis de comparação
        acertou = fazer_pergunta == numero_secreto
        maior = fazer_pergunta > numero_secreto
        menor = fazer_pergunta < numero_secreto

        # Comparações
        if(acertou):
            print("Voce acertou!")
            break
        elif(maior):
            print("Voce errou, seu chute foi maior que o número secreto!")
        elif(menor):
            print("Voce errou, seu chute foi menor que o número secreto")
        
        rodada = rodada + 1


print(f"\n{Fore.BLACK + Back.GREEN}Fim do jogo!!!!", f"o número secreto era:{Style.RESET_ALL}{Fore.BLACK + Back.RED}{numero_secreto}", Style.RESET_ALL)
