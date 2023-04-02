numero = int(input())
primo = False
listaP = ''
# ver se o número é primo
def numero_primo():
    global primo
    if numero == 1:
        primo = True
    elif numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                primo = True
                break
# lista dos numeros primos
def lista_primos() :
    global listaP
    for a in range(1, numero+1):
        if a > 1:
            for i in range(2, a):
                if a % i == 0:
                    break
            else:
                if str(a) not in listaP:
                    listaP += f'{a}, '
    else:
        listaP = listaP[:-2]

#rodar as funções
numero_primo()
lista_primos()
if primo:
    print(f'O número {numero} não é primo.')
    if listaP == '':
        print(f'Além disso, não temos primos no intervalo de 1 à {numero}.')
        print('AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')
    else:
        print(f'Entretanto, temos primos no intervalo de 1 à {numero}. Estes são:')
        print(f'{listaP}')
        print(f'AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')
else:
    print(f'O número {numero} é primo.')
    print('AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')