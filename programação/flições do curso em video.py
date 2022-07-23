from random import randint

querjoga = 0
numerojogadas = 20
aleatorio = randint(1,100)



jogando = input('Deseja jogar?[S/N]:  ')

if jogando != 'S':
    querjoga = False
    print('entao va se fuder')
else:
    querjoga = True
    

while querjoga == True:
    jogada = int(input('digite um numero: '))
    if jogada > aleatorio:
        print('Numero errado, sua jogada foi acima do numero selecionado!')
        numerojogadas = numerojogadas -1 
        print('Agora voce tem {} jogadas'.format(numerojogadas))
    elif jogada < aleatorio:
        print('Numero errado, sua jogada foi abaixo do numero selecionado!')
        numerojogadas = numerojogadas -1 
        print('Agora voce tem {} jogadas'.format(numerojogadas))
    else:
        print('parabens, voce ganhou!')
        print('acabou!')
        break







