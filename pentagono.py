#pedir, adicionar ou remover prisioneiros da lista
def add_demo(a,b,c):
    global lista_prisioneiros
    inserido = False
    tentativas = 0
    while not inserido and tentativas < b:
        c = c%b
        if lista_prisioneiros[c] == '':
            lista_prisioneiros[c] = a[1]
            inserido = True
        else:
            c += 1
            tentativas += 1
    else:
        #todas as células ocupadas
        if not inserido:
            print('CHEIO')

def remove_demo(a,b,c,d):
    global lista_prisioneiros
    removido = False
    tentativas = 0
    while not removido and tentativas < d:
        c = c%b
        if lista_prisioneiros[c] == a[1]:
            lista_prisioneiros[c] = ''
            removido = True
        else:
            c += 1
            tentativas += 1
    else:
        # ele nunca foi adicionado
        if not removido:
            print('NAO EXISTE')

#imprimir lista final
def imprimir(a):
    resultado = ' '
    for i in a:
        if i != '':
            resultado += f' {i}'
    resultado = resultado.replace('  ','')
    return(resultado)

#entradas fixas
entrada_inicial = input().split()
num_celas = int(entrada_inicial[0])
num_ordens = int(entrada_inicial[1])
lista_prisioneiros = []

for _ in range(num_celas):
    lista_prisioneiros.append('')

for _ in range(num_ordens):
    ordem = input().split()
    codigo = 0
    # transformar pela tabela ascii
    for i in ordem[1]:
        codigo += ord(i)
    cod_cela = codigo%num_celas
    contador = cod_cela
    if ordem[0] == 'ADICIONAR':
        add_demo(ordem,num_celas,contador)
    elif ordem[0] == 'REMOVER':
        remove_demo(ordem,num_celas,contador,num_ordens)
#outpus
else:
    print(imprimir(lista_prisioneiros))
