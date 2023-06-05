import random
def jogar():

    print('*** Bem vindo ao jogo de advinhação ***')    

    numero_secreto = random.randrange(1, 101)
    tentativa = 0
    pontos = 1000
    saldo = pontos
    
    print('Nivel 1 = 20 tentativas')
    print('Nivel 2 = 10 tentativas')
    print('Nivel 3 = 05 tentativas')

    numeros = [1, 2, 3]

    print('Escolha um númeo da lista:', numeros)
    escolha = int(input('Digue o número correspondente ao nível que você deseja jogar: '))

    if escolha == 1:
        nivel = 'fácil'
        tentativa = 15

    if escolha == 2:
        nivel = 'médio'
        tentativa = 10
   
    if escolha == 3:
        nivel = 'difícil'
        tentativa = 5

    if escolha not in numeros:
        print('Escolha inválida. Por favor escolha um número correspondente ao nível em que você deseja jogar')
        
    
    else:
        print('Você escolheu o nível {}. Boa sorte!'.format(nivel))

    for rodada in range(1, tentativa +1):
        print('Rodada {} de {}'.format(rodada, tentativa))
        chute = int(input('Escolha seu número da sorte: '))
    
        if chute < 1 or chute > 100:
            print('Você deve digitar um número válido entre 0 e 100')
            
        
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print('Você acertou! O número secreto foi {}'.format(numero_secreto))
        
        else:
            if maior:
                print('Você errou! O número secreto é menor que o número escolhido.')
            
            elif menor:
                print('Você errou! O número secreto é maior do que o número escolhido.')

        pontos_perdidos = abs(chute - numero_secreto)
        saldo -= pontos_perdidos

    print('Sua pontuação final: {}'.format(saldo))   

if(__name__ == "__main__"):
    jogar()