vencedor = False
morte = False
vida_denji = 1000
vida_zombie = 1000
# função que vai conferir os pontos de vida dos participantes
def acompanhamento_vida () :
    global vencedor
    global vida_zombie
    global vida_denji
    global morte
    if vida_zombie <= 0 :
        print('O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!')
        vencedor = True
        morte = True
    elif vida_zombie > 1000 :
        vida_zombie = 1000
    if vida_denji <= 0 :
        print('Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.')
        vencedor = True
        morte = True
    elif vida_denji > 1000:
        vida_denji = 1000
#  vai calcular a porcentagem quando o golpe for 'ataque' e o personagem for 'Denji'
def calculadora_zombie__ataque() :
    global calculoz
    global vida_zombie
    vida_zombie -= dano
    acompanhamento_vida()
    calculoz = int((100*vida_zombie)/1000)
    if vida_zombie > 0 :
        print(f'Uhu, Denji atacou! A porcentagem de vida atual do Zombie Devil é de {calculoz}%.')
# vai calcular a porcentagem quando o golpe for 'ataque' e o personagem for 'Zombie'
def calculadora_denji_ataque () :
    global calculod
    global vida_denji
    vida_denji -= dano
    acompanhamento_vida()
    calculod = int((100*vida_denji)/1000)
    if vida_denji > 0 :
        print(f'Ah não, Denji foi atacado pelo Zombie Devil! A porcentagem de vida atual de Denji é de {calculod}%.')
# calcula a porcentagem dos dois personagens quando o golpe for 'defesa'
def calculadora_defesa() :
    global vida_denji
    global vida_zombie
    global calculod
    global calculoz
    if personagem == 'Denji' :
        vida_denji += dano
        vida_zombie -= dano
        print(f'Isso aê! O feitiço virou contra o feiticeiro. Denji defendeu o golpe do Zombie Devil e ganhou um bônus de vida.')
        acompanhamento_vida()
        calculod = int((100*vida_denji)/1000)
        calculoz = int((100*vida_zombie)/1000)
    else :
        vida_zombie += dano
        vida_denji -= dano
        print('Ops! O Zombie Devil defendeu o ataque de Denji e ganhou um bônus de vida.')
        acompanhamento_vida()
        calculoz = int((100*vida_zombie)/1000)
        calculod = int((100*vida_denji)/1000)

#print inicial
print('Denji fez pacto com Pochita. Que comece a luta.')
while vencedor == False :
    if vencedor == False :
        personagem = input()
        golpe = input()
        dano = int(input())
        #checagem dos valores de input
        if personagem != 'Denji' and personagem != 'ZombieDevil' :
            print('Esse personagem não está lutando, escolha entre Denji ou Zombie Devil.')
        else :
            if golpe == 'ataque' :
                if personagem == 'Denji' :
                    calculadora_zombie__ataque()
                elif personagem == 'ZombieDevil' :
                    calculadora_denji_ataque()
            elif golpe == 'defesa' :
                calculadora_defesa()
                if morte == False:
                    print(f'A porcentagem de vida atual de Denji é de {calculod}% e do Zombie Devil é de {calculoz}%.')
        #checagem dos valores de input
        if golpe != 'ataque' and golpe != 'defesa' :
            print('Esse golpe não existe, escolha entre ataque ou defesa.')
