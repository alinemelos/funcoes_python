def checagem(n, p) :
    n=nome
    p=prob
    ok=da_certo
    erro=da_errado
    lista_p=lista_prob
    if n == 'Makima' :
        print('Woof Woof')
    if n == 'Makima' or p <= 50 :
        print(f'Beleza {n}!! Essa é uma boa pretendente!')
        ok += [n]
        lista_p += [p]
    else:
        print(f'{n}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?')
        erro += [n]
nome = ''
prob = 0
entra = True
lista = ''
da_certo = []
da_errado = []
lista_prob = []
while nome != 'cabo' :
    nome = input()
    if nome != 'cabo' :
        if len(nome) > 7 :
            print(f'Er {nome[0]}{nome[1]}.. errr... nao consigo lembrar, melhor deixar para la')
        else :
            prob = int(input())
            checagem(nome, prob)
else :
    if len(da_certo) > len(da_errado) :
        print('Epa ai sim! E hoje pochita!!')
        if len(da_errado) == 0:
            tamanho1 = len(da_certo)
            tamanho2 = len(lista_prob)
            casa1 = 0
            casa2 = 0
            while tamanho1 > 0 and tamanho2 > 0:
                lista += 'nome: ' + str(da_certo[casa1]) + ' - chances de morrer: ' + str(lista_prob[casa2]) +'%' + '\n'
                casa1 += 1
                casa2 += 1
                tamanho1 -= 1
                tamanho2 -= 1
            print(f'{lista}'[:-1])
    else :
        print('Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos')