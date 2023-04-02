quant_inicial = int(input())
duplica = False
quant_demo = quant_inicial
v_denji = 0
v_demo = 0
ataque_denji = 0
v_demo_atual = 0
ataque_demo_atual = 0
mortos = 0
morte = False

def estatistica() :
    print('DENJI')
    print(f'Vida: {v_denji}')
    print(f'Ataque atual: {ataque_denji}')
    print(f'DEMÔNIO')
    print(f'Vida: {v_demo_atual}')
    print(f'Ataque atual: {ataque_demo_atual}')

if quant_inicial > 0 :
    v_denji = int(input())
    v_demo = int(input())
    ataque_denji = int(input())
    ataque_demo = int(input())
    ataque_demo_atual = ataque_demo
    v_demo_atual = v_demo
    estatistica()
else :
    print('Uhuuul um dia só para relaxar!')

while v_denji > 0 and quant_demo > 0 and morte != True:
    acao_denji = input()
    acao_demo = input()

    if acao_denji == 'Denji ganhou um beijo de Makima' :
        v_denji += 50
    elif acao_denji == 'Pochita chegou para a batalha!' :
        ataque_denji += 50
    elif acao_denji == 'Makima disse que ME AMA!!!' :
        v_denji = int(v_denji*1.5)

    if acao_demo == 'O demônio achou um escudo no chão!' :
        v_demo_atual += 25
    elif acao_demo == 'Onde ele arrumou essa espada?':
        ataque_demo_atual += 20
    elif acao_demo == 'Como assim ele se duplicou??!!' :
        duplica = True
        v_demo_atual = 2*v_demo_atual
        ataque_demo_atual = 2*ataque_demo_atual

    v_demo_atual -= ataque_denji
    if v_demo_atual <= 0 :
        morte = True
        quant_demo -= 1
        if acao_demo == 'Como assim ele se duplicou??!!' :
            mortos += 2
        elif acao_demo != 'Como assim ele se duplicou??!!' :
            mortos += 1
        if quant_demo > 0 :
            v_demo_atual = v_demo
            ataque_demo_atual = ataque_demo
        if quant_demo >= 1 :
            print('Matei um!!!')

    if v_demo_atual >= 0 :
        v_denji -= ataque_demo_atual

    if v_denji <= 0 :
        morte = True
        print('Infelizmente Denji foi de comes e bebes :(')
        break

    if v_denji > 0 and v_demo_atual > 0 :
        estatistica()
    morte = False

else :
    if quant_inicial > 0 and duplica == True:
        print('Foi mais do que eu esperava mas finalmente terminei…')
    elif mortos == quant_inicial and quant_inicial > 0:
        print('Ufa, agora posso descansar em paz!')
