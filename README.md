# funcoes_python
<h2>Batalha</h2>
Input

Enquanto não houver um ganhador, você receberá três entradas:

personagem → O nome do personagem que está atacando ou defendendo.

golpe → O tipo de golpe, se é ataque ou defesa.

dano → O valor do dano do golpe (número inteiro).

Output

Antes de iniciar a luta você deverá imprimir:

"Denji fez pacto com Pochita. Que comece a luta.”.

Caso o personagem não seja Denji ou Zombie Devil imprima:

"Esse personagem não está lutando, escolha entre Denji ou Zombie Devil.”

Caso o tipo de golpe não seja ataque ou defesa, imprima:

"Esse golpe não existe, escolha entre ataque ou defesa.”

OBS.: Mesmo que o nome ou o ataque seja inválido, você deverá sempre receber a entrada completa como informado.

Em seguida, se o tipo do golpe for ataque, verifique qual foi o personagem. Se Denji, decremente o valor atual da vida do Zombie Devil com o valor do dano e imprima:

"Uhu, Denji atacou! A porcentagem de vida atual do Zombie Devil é de {calcular_porcentagem(vida_ZombieDevil)}%.”

• calcular_porcentagem() → função que calculará a porcentagem de vida atual do personagem atacado.

• vida_ZombieDevil → vida atual do personagem atacado.

Se Zombie Devil, decremente o valor atual da vida do Denji com o valor do dano e imprima:

"Ah não, Denji foi atacado pelo Zombie Devil! A porcentagem de vida atual de Denji é de {calcular_porcentagem(vida_Denji)}%.”

Lembre-se de sempre verificar se a vida atual dos personagens é menor ou igual a 0 a cada decremento e se é maior que 1000 a cada incremento.

Se for menor ou igual a 0 e o personagem for Zombie Devil, imprima e termine a luta:

"O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!”

Se for maior ou igual a 0 e o personagem for Denji, imprima e termine a luta:

"Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.”

Se for maior que 1000, atribua a vida do personagem a 1000 (máximo).

Se o tipo do golpe for defesa, o defensor irá ganhar (incremento) um bônus extra na quantidade de vida atual e o oponente perderá vida (decremento). Tanto o bônus quanto a perda será o valor do dano do golpe. Portanto, verifique se o personagem foi Denji ou Zombie Devil. Se Denji, imprima:

"Isso aê! O feitiço virou contra o feiticeiro. Denji defendeu o golpe do Zombie Devil e ganhou um bônus de vida.”

Se Zombie Devil, imprima:

"Ops! O Zombie Devil defendeu o ataque de Denji e ganhou um bônus de vida.”

Independente do personagem, em seguida, imprima a nova porcentagem de vida deles:

"A porcentagem de vida atual de Denji é de {calcular_porcentagem(vida_Denji)}% e do Zombie Devil é de {calcular_porcentagem(vida_ZombieDevil)}%.”
<h2>Enfrentando Monstros </h2>
A cada rodada, receberemos ações que poderão indicar powerups nos valores de ataque e defesa de Denji e do demônio, essas ações podem ser:

• “Nada aconteceu.” → a rodada não possui powerups para determinado personagem

Ou, para Denji:

• “Denji ganhou um beijo de Makima” → Denji ganha +50 pontos de vida

• “Pochita chegou para a batalha!” → Denji ganha +50 pontos de ataque

• “Makima disse que ME AMA!!!” → Denji tem seus pontos de vida multiplicados por 1,5 (o resultado deve ser um inteiro)

E para os demônios:

• “O demônio achou um escudo no chão!” → demônio ganha +25 pontos de vida

• “Onde ele arrumou essa espada?” → demônio ganha +20 pontos de ataque

• “Como assim ele se duplicou??!!” → O demônio se duplica e agora Denji enfrentará o dobro de demônios ao mesmo tempo na rodada.

ATENÇÃO: Considere que, ao duplicar, os dois demônios se comportam como um único Mega Demônio que possui o dobro de vida e ataque..

EXEMPLO: Caso a entrada seja:
VIDA_DENJI: 200

VIDA_DEMONIOS: 100

ATAQUE_DENJI: 300

ATAQUE_DEMONIOS: 75

Como assim ele se duplicou??!!

Após receber esta última entrada, a vida do Mega Demônio passa a ser 200 e o ataque passa a ser 150. Caso Denji mate o demônio, o número de demônios mortos é acrescido em 2.
Obs.: Isso se mantém até apenas enquanto os demônios da rodada estiverem vivos. Caso eles morram, o próximo demônio não virá duplicado.

Depois de receber as entradas, Denji sempre ataca primeiro, descontando o seu valor de ataque, da vida do demônio com quem está lutando naquela rodada e só depois, se ainda restarem demônios vivos, o demônio da vez ataca o Denji, realizando a mesma ação e assim segue para uma nova rodada até que a quantidade de demônios derrotados seja igual ou maior que a quantidade prevista inicialmente por Denji ou que ele tenha morrido na batalha.

Input

Primeiro, vamos receber a quantidade de demônios que Denji prevê que irá derrotar:

QUANTIDADE_DEMONIOS

Em seguida, caso QUANTIDADE_DEMONIOS seja maior que zero, receberemos os valores de vida e ataque de Denji e dos demônios, que vão servir durante todo o funcionamento do código:

VIDA_DENJI

VIDA_DEMONIOS

ATAQUE_DENJI

ATAQUE_DEMONIOS

Obs.: os inputs dos demônios representam os valores com os quais cada novo demônio deve iniciar sua luta contra Denji.

E por último, para cada rodada, vamos receber as 2 ações que poderão indicar powerups para os personagens: uma para o Denji e outra para o demônio que ele irá enfrentar.

ACAO_DENJI

ACAO_DEMONIO

Output

Inicialmente, caso a quantidade de demônios declarada no início seja 0, apenas imprima a seguinte frase e encerre seu código:

“Uhuuul um dia só para relaxar!”

Caso a quantidade seja diferente de 0, ao iniciar a batalha e depois de cada rodada, deverá ser impresso o seguinte conjunto de estatísticas sobre a batalha:

"DENJI"

"Vida: {VIDA_DENJI}"

"Ataque atual: {ATAQUE_DENJI}"

"DEMÔNIO"

"Vida: {VIDA_ATUAL_DEMÔNIO}"

"Ataque atual: {ATAQUE_ATUAL_DEMÔNIO}"

Nas rodadas em que Denji derrotar algum demônio, deverá ser impressa a frase:

"Matei um!!!"

Obs.: Nessas rodadas em que Denji derrotar algum demônio, as estatísticas de vida e ataque impressos devem ser do próximo demônio a ser enfrentado e isso só não acontece quando o último demônio é derrotado, nesse caso, não se deve indicar que você o matou nem mostrar as estatísticas ao final.

Caso ele morra durante a batalha printe:

“Infelizmente Denji foi de comes e bebes :(”

Obs.: nessa ocasião não se deve printar os stats de vida e ataque e o programa se encerra

No final, se Denji conseguir derrotar mais demônios do que havia sido previsto, imprima:

“Foi mais do que eu esperava mas finalmente terminei…”

Caso ele derrote a quantidade declarada inicialmente na entrada, você deverá printar:

“Ufa, agora posso descansar em paz!”
<h2>Número Primo</h2>
Input

Você receberá um número N positivo, sendo N>0

Output

Para o output, temos os seguintes casos:

Caso1: Caso o número digitado seja primo, você deve imprimir a seguinte mensagem:

A - “O número {N} é primo.”

Caso 2: Caso o número digitado não seja primo, você deve imprimir as seguintes mensagens:

B - “O número {N} não é primo.”

Além disso, se houverem número primos de 1 à N, você imprimir na tela dessa maneira:

C - “Entretanto, temos primos no intervalo de 1 à {N}. Estes são:”

D - “{primo1}, {primo2}, {primoN}”

Caso não tenha números primos no intervalo citado. Imprima juntamente com o print B:

E - “Além disso, não temos primos no intervalo de 1 à {N}.”

Ao final, independente do caso, você deve exibir na tela:

F - “AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!”
<h2>Pentagono</h2>
O governo dos Estados Unidos da América solicitou ao Japão o envio de demônios para serem armazenados numa prisão especial localizada no Pentágono. Logo, a função de transferir e alocar foi designada para Makima, Líder da Divisão de Caçadores de Demônios da Defensoria Pública Japonesa. Por gostar de algoritmos, ela opta por fazer a prisão do Pentágono de Hash Table.

Hash Table ou Tabela de Dispersão é uma estrutura de dados que permite armazenar e acessar informações de forma rápida e eficiente. Funciona através da aplicação de uma função hash que transforma a chave de busca em um índice da tabela, onde o valor correspondente pode ser encontrado de forma direta.

gif

Portanto, a fórmula para encontrar o índice das celas no Pentágono de cada demônio é dada por:

x mod c

x = soma dos valores correspondentes às letras no nome do demônio de acordo com a tabela ASCII;

c = quantidade de celas;

Se a cela que o demônio deveria ser alocado já estiver sendo ocupada, ele deve ser alocado na próxima cela vazia à direita de sua respectiva cela, estratégia chamada de Linear Probing.

gif

obs.1: O uso de funções é obrigatório na questão.

obs.2: Os nomes dos demônios conterão apenas letras de “a” a “z”.

obs.3: Use as funções ord e char de python para obter os valores dos caracteres na tabela ASCII”.

Input

Inicialmente serão fornecidos em uma linha, separados por um espaço, inteiros referentes ao número total de celas e quantas ordens você receberá:

quantidade_celas quantidade_ordens

depois, n linhas, contendo a ação a ser realizada (a ordem) e o nome do demônio com o qual a ação deve ser feita, também separados por um espaço:

ordem nome_demônio;

Makima irá dar ordens para seu subordinado (você) "ADICIONAR" ou “REMOVER” demônios.

Output

Se ela ordenar para "ADICIONAR" e a prisão estiver cheia você deve informá-la com “CHEIO”, e se ela ordenar para “REMOVER” e o demônio não existir você deve informá-la com “NAO EXISTE”.

obs.4: na hora de remover elementos, atente-se para a diferença de lugares vazios nunca ocupados e em que já foi removido algum elemento, caso não encontre o demônio na primeira cela acessada.

obs.5: as funções ADICIONAR e REMOVER devem ser criadas por você, de acordo com a lógica que foi explicada no enunciado.

No fim, informe a lista de demônios na ordem que foram alocados.
<h2>tinder</h2>
Ele precisa da sua ajuda para fazer um código que armazene o nome das garotas que ele conhece e a chance em % que elas têm de querer matar ele, armazenadas de 0% a 100%, em uma lista com as possíveis candidatas. Denji já está acostumado com essa situação, então, caso a chance seja menor ou igual 50%, ela é um bom partido, do contrário ela deve ser melhor evitar. Existe outro problema, Denji não só é ruim em matemática como também tem dificuldade de memorizar nomes, por isso caso o nome da garota passe de 7 letras, ele não será capaz de decorar o nome e não colocará ela na lista. Além disso, caso o nome da garota seja "Makima" ele ignora as possibilidades de ser assasinado e a considera um bom partido.

denji2

VOCÊ DEVE UTILIZAR FUNÇÕES PARA REALIZAR CADA ETAPA DO CÓDIGO, CRIE MAIS DE UMA FUNÇÃO PARA NÃO REPETIR O MESMO PROCEDIMENTO VÁRIAS VEZES

Input

Primeiro, você receberá um input contendo o nome de uma mulher ou a string "cabo" para encerrar o código

nome

Em seguida, você receberá um número inteiro representando a probabilidade entre 0 e 100 de Denji ser morto por ela.

probabilidade

OBS: Caso a entrada seja o nome de uma garota com mais do que 7 letras, você deve descartá-la sem receber a probabilidade de ser morto por ela.

Output

Ao receber o nome da garota, você deverá imprimir:

Caso o nome dela tenha mais do que 7 letras:

"Er {as duas primeiras letras do nome dela}.. errr... nao consigo lembrar, melhor deixar para la"

OBS: você não deve se preocupar com espaços em branco no nome das garotas.

Caso o nome dela seja "Makima":

"Woof Woof"

Após ver a chance, Denji dirá:

Caso a probabilidade seja favorável (menor ou igual a 50) ou o nome seja "Makima":

"Beleza {nome}!! Essa é uma boa pretendente!"

Do contrário, a probabilidade será muito alta, então você deve imprimir:

"{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?"

Ao receber a string "cabo", você deverá imprimir uma linha:

Caso o número de relacionamentos que dão certo seja maior do que o de relacionamentos onde a mulher tem altas chances de matar Denji, imprima:

"Epa ai sim! E hoje pochita!!"

Caso o contrário (não existe chance de empate):

"Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos"

Por fim, caso a lista seja totalmente favorável, você deverá imprimi-la no seguinte modelo:

"nome: {nome 1} - chances de morrer: {chance 1}%"

...

"nome: {nome n} - chances de morrer: {chance n}%"
