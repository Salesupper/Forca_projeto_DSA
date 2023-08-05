from random import choice
from os import system, name
       

def limpa_tela():
    # Windows
    if name =='nt':
        _ = system('cls')
    # Mac e Linux
    else:
        _ = system('clear')
    

def game():
    
    limpa_tela()
    print('\nBem-vindo ao jogo da forca!')
    print('adivinhe a palavra abaixo:\n')
    
    palavras = ['banana','abacate','uva','morango','laranja']
    palavra = choice(palavras)
    lista_letras_palavras = [letra for letra in palavra]
    #tabuleiro = ['_'] * len(palavra)
    letras_achadas = ['_' for letra in palavra]
    chances = 8
    letras_erradas = []
    
    while chances > 0:
        print(' '.join(letras_achadas))
        print(f'\nChances restantes: {chances}')
        print('Letras erradas:',' '.join(letras_erradas))
        
        tentativa = str(input('\nDigite uma letra: ')).lower().strip()[0]
        
        # checagem de acertos e erros
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_achadas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # verifica se completou a palavra
        if '_' not in letras_achadas:
            print(f'\nParabéns você venceu!!! a palavra era {palavra}')
            break
    
    # Verifica se perdeu o jogo após sair do loop
    if '_' in letras_achadas:
        print(f'\nVocê Perdeu, a palavra era {palavra}')

# Código primário para iniciar as funções
if __name__ == '__main__':
    game()
    print('Fim de jogo')

        



