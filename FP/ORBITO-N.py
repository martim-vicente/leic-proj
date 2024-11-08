'''
JOGO: ORBITO-N
AUTOR: MARTIM VICENTE
'''


'''
TIPO ABSTRATO: POSICAO
O TAD imutável e hashable posição é usado para representar uma posição do tabuleiro de Orbito-N.
A representação interna adoptada para o TAD é:
    Strings, em que o 1o caractere é uma letra entre 'a' e 'j' que corresponde à coluna
    e os restantes caracteres são números que correspondem à linha em que a posição está
    situada no tabuleiro. EX: 'a10'
'''
#CONSTRUTORES
def cria_posicao(col,lin):
    """
    cria_posicao(col, lin): str x int --> posicao
    Recebe um caracter e um número inteiro correspondentes à coluna (col) e à linha (lin)
    e devolve a posição correspondente à representação interna adoptada.

    Argumentos:
        col (str): Representa a coluna, apenas pode ser a,b,c,d,e,f,g,h,i,j
        lin (int): Representa a linha, apenas pode estar entre 1 e 10 (inclusivo)

    Retorna:
        posicao : Representação interna da posição.
    """
    if type(col)!=str or len(col)!=1 or col not in 'abcdefghij' or type(lin)!=int or not (1<=lin<=10):
        raise ValueError('cria_posicao: argumentos invalidos') 
    return col + str(lin) ## Retorna uma string

def obtem_pos_col(pos):
    """
    obtem_pos_col(pos): posicao --> str
    Recebe a representação interna de uma posição e devolve a sua coluna.

    Argumentos:
        posicao : Representação interna do TAD posição.

    Retorna:
        col (str): Coluna do tabuleiro em que a posição está localizada.
    """
    return str(pos[0])

def obtem_pos_lin(pos):
    """
    obtem_pos_lin(pos): posicao --> int
    Recebe a representação interna de uma posição e devolve a linha em que a mesma está situada.

    Argumentos:
        posicao : Representação interna do TAD posição.

    Retorna:
        lin (int): Linha do tabuleiro em que a posição está localizada.
    """
    return int(pos[1:])

def eh_posicao(arg):
    """
    eh_posicao(arg): universal --> booleano
    Recebe um argumento e retorna um booleano dependendo de se o argumento é um TAD posicao.
    
    Argumentos:
        arg : Argumento de qualquer tipo.

    Retorna:
        True (bool) : Caso seja um TAD posicao 
        False (bool): Caso NÃO seja um TAD posicao
    """
    return type(arg)==str and arg[1:].isdigit() and 1<=obtem_pos_lin(arg)<=10 and obtem_pos_col(arg) in 'abcdefghij'

def posicoes_iguais(arg1, arg2):
    """
    posicoes_iguais(arg1, arg2): universal x universal --> booleano
    Recebe dois argumentos e retorna um booleano caso ambos sejam TADs posicao e sejam iguais.

    Argumentos:
        arg1 : Argumento de qualquer tipo.
        arg2 : Argumento de qualquer tipo.

    Retorna:
        True (bool) : Caso (arg1) e (arg2) sejam TADs posicao e (arg1) == (arg2).
        False (bool): Caso alguma das condições acima não seja cumprida.
    """
    c1, l1 = obtem_pos_col(arg1), obtem_pos_lin(arg1)
    c2, l2 = obtem_pos_col(arg2), obtem_pos_lin(arg2)
    return eh_posicao(arg1) and eh_posicao(arg2) and cria_posicao(c1,l1)==cria_posicao(c2,l2)

def posicao_para_str(pos):
    """
    posicao_para_str(pos): posicao --> str
    Recebe um TAD posicao e retorna uma posicao_string que representa a posição em formato string.

    Argumentos:
        posicao : TAD posicao.
        
    Retorna:
        pos_str (str): O 1o caractere é uma letra que representa a coluna.
                       Os restantes caracteres são números que representam a linha.
                       ex: 'j10'
    """
    return pos

def str_para_posicao(pos_str):
    """
    posicao_para_str(pos): str --> posicao
    Recebe uma posicao_string e retorna o TAD posicao correspondente.

    Argumentos:
        posicao_str : Representação em string do TAD posicao.
        
    Retorna:
        posicao : TAD posicao
    """
    return pos_str


## FUNCOES AUXILIARES
def posicao_orbital(pos, n):
    """
    posicao_orbital(pos, n): posicao x int --> int
    Recebe um TAD posicao e o número de orbitas do tabuleiro e retorna a órbita
    em que o argumento (pos) se situa no tabuleiro.

    Argumentos:
        pos  : TAD posicao.
        n (int): Número de órbitas do tabuleiro, está entre 2 e 5 (inclusivo)
        
    Retorna:
        orbita_posicao (int) : Órbita em que (pos) se situa no tabuleiro.
    """
    tamanho = n*2
    d_cima = obtem_pos_lin(pos) - 1 ## Distancia à borda superior do tabuleiro
    d_esq = ord(obtem_pos_col(pos))-ord('a') ## Distancia à borda esquerda do tabuleiro
    d_baixo = tamanho - d_cima -1 ## Distancia à borda inferior do tabuleiro
    d_dir = tamanho - d_esq -1 ## Distancia à borda direita do tabuleiro
    return n - min(d_cima, d_baixo, d_esq, d_dir) ## A orbita de uma posicao é dada pela diferenca entre o numero de orbitas e a distancia minima dessa posicao a uma das estremidades da borda

def operacoes_cord(pos):
    """
    operacoes_cord(pos): posicao --> tuplo
    Recebe um TAD posicao e retorna um tuplo onde a 1a entrada é a soma do número correspondente à linha e à coluna
    e a 2a entrada é a subtração do número correspondente à linha e à coluna do TAD posicao.

    Argumentos:
        pos  : TAD posicao.
        
    Retorna:
        soma_subt (tuplo) : 1a entrada é a soma da linha com a coluna. lin + col
                            2a entrada é a subtração entre a linha e a coluna. lin - col
    """
    pos_line = obtem_pos_lin(pos)
    pos_column = ord(obtem_pos_col(pos)) + 1
    return (pos_line+pos_column, pos_line-pos_column)


## FUNCOES ALTO-NIVEL
def eh_posicao_valida(pos,n):
    """
    eh_posicao_valida(pos, n): posicao x int --> bool
    Recebe um TAD posicao e o número de orbitas do tabuleiro e retorna um booleano relativo
    a se o argumento dado é uma posição válida para um tabuleiro com (n) órbitas.

    Argumentos:
        posicao  : TAD posicao.
        n (int): Número de órbitas do tabuleiro, está entre 2 e 5 (inclusivo)
        
    Retorna:
        True (bool) : Caso (pos) seja uma posição e seja válida em um tabuleiro de (n) órbitas.
        False (bool): Caso uma das condições acima não seja cumprida
    """
    return eh_posicao(pos) and obtem_pos_col(pos) in 'abcdefghij'[:n*2] and 1<=obtem_pos_lin(pos)<=n*2


def obtem_posicoes_adjacentes(pos,n,diagonal):
    """
    obtem_posicoes_adjacentes(pos, n, diagonal): posicao x int x bool --> tuplo
    Recebe um TAD posicao, o número de orbitas do tabuleiro e um booleano (diagonal) e retorna um tuplo com as posições do tabuleiro
     - Adjacentes a (pos) se (diagonal) for True
     - Adjacentes ortogonais a (pos) se (diagonal) for False
    As posições do tuplo são ordenadas em sentido horário começando pela posição acima de (pos).

    Argumentos:
        posicao  : TAD posicao.
        n (int): Número de órbitas do tabuleiro, está entre 2 e 5 (inclusivo).
        diagonal (bool) : Se são ou não aceites as posições adjacentes diagonais.
        
    Retorna:
        pos_adjacentes (tuplo) : Tuplo com as posições adjacentes (ortogonais) ordenadas em sentido horário.
    """
    res, offset_horario = (), ((0, -1), (+1, -1), (+1, 0), (+1, +1), (0, +1), (-1, +1), (-1, 0), (-1, -1)) ## Diferença entre a posicao e 'pos', ordenadas em sentido horário
    floor_lin, ceil_lin = max( obtem_pos_lin(pos)-1, 1), min( obtem_pos_lin(pos)+1, n*2) + 1
    # floor_lin / ceil_lin -> Ou é a linha imediatamente atrás / à frente de 'pos' ou é a primeira / última linha, evitando que hajam linhas que nao existem no tabuleiro
    floor_col, ceil_col = max( ord(obtem_pos_col(pos))-1, ord('a')), min( ord(obtem_pos_col(pos))+1, ord('abcdefghij'[n*2-1])) + 1
    # floor_col / ceil_col -> Ou é a coluna imediatamente atrás / à frente de 'pos' ou é a primeira / última coluna, evitando que hajam colunas que nao existem no tabuleiro
    
    for dif in offset_horario:
        for lin in range(floor_lin, ceil_lin):
            for col in range(floor_col, ceil_col):
                posicao = cria_posicao(chr(col), lin)
                aceita_diagonais =  diagonal or obtem_pos_col(posicao) == obtem_pos_col(pos) or obtem_pos_lin(posicao)==obtem_pos_lin(pos) ## Caso posicao e 'pos' tenham ou uma linha ou uma coluna em comum, elas não estão na diagonal.         
                if aceita_diagonais and (ord(obtem_pos_col(posicao)) - ord(obtem_pos_col(pos)), obtem_pos_lin(posicao) - obtem_pos_lin(pos)) == dif:
                    res += (posicao,)
    return res


def ordena_posicoes(tpl,n):
    """
    ordena_posicoes(tpl, n): tuplo x int --> tuplo
    Recebe um tuplo com TADs posicao e o número de orbitas do tabuleiro, retorna um tuplo com as posições do tabuleiro
    ordenadas pela ordem de leitura do jogo Orbito-N.
    ORDEM DE LEITURA : De menor para maior órbita, De menor para maior linha, De menor para maior coluna.

    Argumentos:
        tpl  : Tuplo com TADs posicao.
        n (int): Número de órbitas do tabuleiro, está entre 2 e 5 (inclusivo).
        
    Retorna:
        pos_ordenadas (tuplo) : Tuplo com os TADs posicao ordenados por ordem de leitura.
    """
    tpl = sorted(tpl, key = lambda pos: (obtem_pos_lin(pos), obtem_pos_col(pos))) ## ordena as posicoes de menor para maior linha e em caso de empate de menor para maior coluna
    tpl = sorted(tpl, key = lambda pos: posicao_orbital(pos,n)) ## ordena as posicoes pela sua orbital, sendo a orbital mais exterior correspondente a n
    return tpl      



'''
TIPO ABSTRATO: PEDRA
O TAD imutável e hashable pedra é usado para representar as pedras do jogo. As pedras podem pertencer ao jogador branco ou ao jogador preto.
A representação interna adoptada para o TAD é:
Inteiros, em que a pedra preta corresponde a 1, a pedra branca corresponde a -1 e a pedra neutra corresponde a 0.
'''
def cria_pedra_preta():
    """
    cria_pedra_preta(): {} --> pedra
    Não recebe nada e retorna o TAD correspondente à pedra preta.

    Argumentos:
        
    Retorna:
        pedra_preta : Representação interna da pedra preta
    """
    return 1

def cria_pedra_branca():
    """
    cria_pedra_branca(): {} --> pedra
    Não recebe nada e retorna o TAD correspondente à pedra branca.

    Argumentos:
        
    Retorna:
        pedra_branca : Representação interna da pedra branca
    """
    return -1

def cria_pedra_neutra():
    """
    cria_pedra_neutra(): {} --> pedra
    Não recebe nada e retorna o TAD correspondente à pedra neutra.

    Argumentos:
        
    Retorna:
        pedra_neutra : Representação interna da pedra neutra
    """
    return 0

def eh_pedra(arg):
    """
    eh_pedra(arg): universal --> bool
    Recebe um argumento e retorna um booleano consoante (arg) seja um TAD pedra

    Argumentos:
        arg : Argumento de qualquer tipo.
        
    Retorna:
        True (bool) : Caso (arg) seja um TAD pedra
        False (bool): Caso (arg) NÃO seja um TAD pedra
    """
    return type(arg)==int and arg in (cria_pedra_preta(), cria_pedra_branca(), cria_pedra_neutra()) ## a pedra tem de ser um inteiro e tem de ser igual a um dos 3 tipos de representacao interna da pedra

def eh_pedra_branca(pedra):
    """
    eh_pedra_branca(pedra): universal --> bool
    Recebe um argumento e retorna um booleano consoante (pedra) seja um TAD pedra branca.

    Argumentos:
        pedra : Argumento de qualquer tipo.
        
    Retorna:
        True (bool) : Caso (pedra) seja um TAD pedra branca
        False (bool): Caso (pedra) NÃO seja um TAD pedra branca
    """
    return eh_pedra(pedra) and pedra == cria_pedra_branca() ## tem de ser uma pedra e tem de ser igual a representacao interna da pedra branca
    
def eh_pedra_preta(pedra):
    """
    eh_pedra_preta(pedra): universal --> bool
    Recebe um argumento e retorna um booleano consoante (pedra) seja um TAD pedra preta.

    Argumentos:
        pedra : Argumento de qualquer tipo.
        
    Retorna:
        True (bool) : Caso (pedra) seja um TAD pedra preta.
        False (bool): Caso (pedra) NÃO seja um TAD pedra preta.
    """
    return eh_pedra(pedra) and pedra == cria_pedra_preta() ## tem de ser uma pedra e tem de ser igual a representacao interna da pedra preta

def pedras_iguais(pedra1,pedra2):
    """
    pedras_iguais(pedra1, pedra2): pedra x pedra --> bool
    Recebe um argumento e retorna um booleano consoante (arg) seja um TAD pedra

    Argumentos:
        pedra1 : Argumento de qualquer tipo.
        pedra2 : Argumento de qualquer tipo.
        
    Retorna:
        True (bool) : Caso (pedra1) e (pedra2) sejam TADs pedra e pedra1 == pedra2
        False (bool): Caso uma das condições acima não seja cumprida.
    """
    return eh_pedra(pedra1) and eh_pedra(pedra2) and pedra1==pedra2 ## ambas tem de ser pedras e estas tem de ser iguais entre si

def pedra_para_str(pedra):
    """
    pedra_para_str(pedra): pedra --> str
    Recebe um TAD pedra e retorna a cadeia de caracteres que representa o jogador dono
    da pedra, isto é, 'O', 'X' ou ' ' para pedras do jogador branco, preto ou neutra respetivamente.

    Argumentos:
        pedra : TAD pedra.
        
    Retorna:
        pedra_str (str) : 'X', 'O', ' ' consoante (pedra) seja uma pedra preta, branca ou neutra respectivamente.
    """
    if eh_pedra(pedra):
        if eh_pedra_preta(pedra): ## Caso seja uma pedra preta, corresponde a 'X'
            return 'X'
        elif eh_pedra_branca(pedra): ## Caso seja uma pedra branca, corresponde a 'O'
            return 'O'
        else: ## Caso nao seja nem preta nem branca, como eh_pedra, e neutra, corresponde a ' '
            return ' '

## FUNCOES DE ALTO NIVEL
def eh_pedra_jogador(arg):
    """
    eh_pedra_jogador(arg): universal --> bool
    Recebe um argumento (arg) e retorna um booleano caso (arg) seja um TAD pedra e corresponda a um jogador.

    Argumentos:
        arg : Pode ser de qualquer tipo.
        
    Retorna:
        True (bool) : Caso (arg) seja um TAD pedra e (arg) seja uma pedra preta ou branca.
        False (bool): Caso uma das condições acima não seja cumprida.
    """
    return eh_pedra(arg) and (pedras_iguais(arg, cria_pedra_preta()) or pedras_iguais(arg, cria_pedra_branca())) ## Tem de ser pedra e tem de ser igual a representacao interna da pedra preta ou da pedra branca

def pedra_para_int(pedra):
    """
    pedra_para_str(pedra): pedra --> str
    Recebe um TAD pedra e retorna a cadeia de caracteres que representa o jogador dono
    da pedra, isto é, -1, 1 ou 0 para pedras do jogador branco, preto ou neutra respetivamente.

    Argumentos:
        pedra : TAD pedra.
        
    Retorna:
        pedra_int (int) : 1, -1, 0 consoante (pedra) seja uma pedra preta, branca ou neutra respectivamente.
    """
    if eh_pedra(pedra):
        if eh_pedra_preta(pedra): ## Se e uma pedra preta, corresponde a 1
            return 1
        elif eh_pedra_branca(pedra): ## Se e uma pedra branca, corresponde a -1
            return -1
        else: ## Se nao e nem preta nem branca, como e uma pedra, e neutra, corresponde a 0
            return 0 



def eh_jog(jog): ## usado apenas na funcao orbito
    """
    eh_jog(jog): pedra --> bool
    Recebe uma representação em string de um TAD pedra e retorna um booleano caso seja um TAD pedra válido.

    Argumentos:
        jog (str) : Representação externa do TAD pedra.
        
    Retorna:
        True (bool) : Caso (jog) seja uma representação externa de um TAD pedra e seja a pedra de um jogador.
        False (bool): Caso uma das condições acima não seja cumprida.
    """
    if type(jog)==str and jog in ('X','O',' '): ## Caso o argumento seja a representação externa da pedra
        jog = {'X':cria_pedra_preta(), 'O':cria_pedra_branca(), ' ':cria_pedra_neutra()}[jog]
        return eh_pedra_jogador(jog) ## Verifica se jog e uma pedra valida para um jogador
    return False




'''
TIPO ABSTRATO: TABULEIRO
O TAD mutável tabuleiro é usado para representar um tabuleiro do jogo Orbito-n e as pedras dos jogadores que nele são colocadas.
A representação interna adoptada para o TAD é:
Dicionário, em que cada chave corresponde a uma posição e o valor associado a essa chave é o valor
'''
def eh_n(n):
    """
    eh_n(n): int --> bool
    Recebe o número de órbitas de um tabuleiro e retorna um booleano caso n seja um número de órbitas válido.

    Argumentos:
        n (int) : Número de órbitas do tabuleiro.
        
    Retorna:
        True (bool) : Caso n seja um número inteiro entre 2 e 5 (inclusivo).
        False (bool): Caso uma das condições acima não seja cumprida.
    """
    return type(n)==int and 2<=n<=5

def cria_tabuleiro_vazio(n):
    """
    cria_tabuleiro_vazio(n): int --> tabuleiro
    Recebe o número de órbitas de um tabuleiro e cria um TAD tabuleiro baseado em (n).

    Argumentos:
        n (int) : Número de órbitas do tabuleiro.
        
    Retorna:
        tab (dict) : TAD tabuleiro.
    """
    if not eh_n(n):
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')

    tab = {}
    for index_lin in range(n*2):
        for index_col in range(n*2):
            posicao = cria_posicao('abcdefghij'[index_col], index_lin+1)
            tab[posicao] = cria_pedra_neutra() ## Para cada posição é lhe atribuida uma pedra neutra (vazia)
    return tab

def coloca_pedra(tab,pos,pedra):
    """
    coloca_pedra(tab, pos, pedra): tabuleiro x posicao x pedra --> tabuleiro
    Recebe um TAD tabuleiro, um TAD posicao e um TAD pedra e retorna um TAD tabuleiro onde
    a posicao (pos) tem o valor (pedra).

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str) : TAD posicao
        pedra (int): TAD pedra
        
    Retorna:
        tab (dict) : TAD tabuleiro onde (pos) teve o seu valor alterado para (pedra).
    """
    tab[pos] = pedra
    return tab

def remove_pedra(tab,pos):
    """
    remove_pedra(tab, pos): tabuleiro x posicao --> tabuleiro
    Recebe um TAD tabuleiro e um TAD posicao e retorna um TAD tabuleiro onde
    a posicao (pos) tem o valor (pedra_neutra).

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str) : TAD posicao

    Retorna:
        tab (dict) : TAD tabuleiro onde (pos) teve o seu valor alterado para (pedra_neutra).
    """
    tab[pos] = cria_pedra_neutra()
    return tab

def cria_tabuleiro(n,t_pretas,t_brancas):
    """
    cria_tabuleiro(n, t_pretas, t_brancas): int x tuplo x tuplo --> tabuleiro
    Recebe o número de órbitas do tabuleiro e dois tuplos em que as posições em cada um deles são
    TADs posicao que possuem o valor cria_pedra_branca() ou cria_pedra_preta().

    Argumentos:
        n (int): Número de órbitas do tabuleiro.
        t_pretas (tuple) : Tuplo que contém TADs posicao que possuem o valor cria_pedra_preta()
        t_brancas (tuple): Tuplo que contém TADs posicao que possuem o valor cria_pedra_branca()
        
    Retorna:
        tab (dict) : TAD tabuleiro modificado.
    """
    if not eh_n(n) or type(t_pretas)!=tuple or len(t_pretas)>(n*2)**2 or type(t_brancas)!=tuple or len(t_brancas)>(n*2)**2:
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    tab, usado = cria_tabuleiro_vazio(n), () ## Cria um tabuleiro vazio com n orbitas
    for posicao in t_pretas:
        if not eh_posicao(posicao) or not eh_posicao_valida(posicao,n) or posicao in t_brancas or posicao in usado:
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        
        tab = coloca_pedra(tab, posicao, cria_pedra_preta()) ## Coloca na posicao 'posicao' uma pedra preta
        usado += (posicao,) ## Regista que 'posicao' ja foi usada
    
    usado = ()
    for posicao in t_brancas:
        if not eh_posicao(posicao) or not eh_posicao_valida(posicao,n) or posicao in t_pretas or posicao in usado:
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        
        tab = coloca_pedra(tab, posicao, cria_pedra_branca()) ## Coloca na posicao 'posicao' uma pedra branca
        usado +=(posicao,) ## Regista que 'posicao' ja foi usada
    
    return tab

def cria_copia_tabuleiro(tab):
    """
    cria_copia_tabuleiro(tab): tabuleiro --> tabuleiro
    Recebe um TAD tabuleiro e retorna uma cópia do TAD tabuleiro

    Argumentos:
        tab (dict): TAD tabuleiro

    Retorna:
        tab_copia (dict) : Cópia do TAD tabuleiro.
    """
    tb_copia = {}
    for posicao in tab:
        tb_copia[posicao] =tab[posicao] ## Copia o tabuleiro 'tab' sem manter vinculo ao tabuleiro original
    return tb_copia

def obtem_numero_orbitas(tab):
    """
    obtem_numero_orbitas(tab): tabuleiro --> int
    Recebe um TAD tabuleiro e retorna o número de orbitas do tabuleiro.

    Argumentos:
        tab (dict): TAD tabuleiro

    Retorna:
        n (int) : Número de órbitas do tabuleiro.
    """
    return int(len(tab)**(1/2) // 2 )
    ## Em um tabuleiro de dimensões (n*2) x (n*2)
    ## o tamanho de um dicionário (tab) será len(tab) == (n*2)**2.
    ## Logo é possível obter o tamanho de uma linha do tabuleiro fazendo a raiz quadrada de len(tab)
    ## ao dividir esse valor por 2, temos o número de órbitas pois tamanho_linha = n * 2.

def obtem_pedra(tab,pos):
    """
    obtem_pedra(tab, pos): tabuleiro x posicao --> pedra
    Recebe um TAD tabuleiro e um TAD posicao e retorna um TAD pedra correspondente a essa posicao no tabuleiro.

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str): TAD posicao

    Retorna:
        pedra : TAD pedra correspondente à posicao (pos) no tabuleiro (tab).
    """
    return tab[pos]

def obtem_linha_horizontal(tab,pos):
    """
    obtem_linha_horizontal(tab, pos): tabuleiro x posicao --> tuplo
    Recebe um TAD tabuleiro e um TAD posicao e retorna um tuplo com as posicoes e a sua respectiva pedra

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str): TAD posicao

    Retorna:
        horizontal (tuplo) : Tuplo que possui as posicoes e os seus valores na mesma linha que (pos) no tabuleiro (tab).
    """
    horizontal = ()
    for posicao in tab:
        if obtem_pos_lin(posicao)==obtem_pos_lin(pos): ## Duas posicoes estao na mesma linha horizontal se estiverem na mesma linha do tabuleiro.
            horizontal += ((posicao, obtem_pedra(tab,posicao)),)
    return horizontal

def obtem_linha_vertical(tab,pos):
    """
    obtem_linha_vertical(tab, pos): tabuleiro x posicao --> tuplo
    Recebe um TAD tabuleiro e um TAD posicao e retorna um tuplo com as posicoes e a sua respectiva pedra

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str): TAD posicao

    Retorna:
        vertical (tuplo) : Tuplo que possui as posicoes e os seus valores na mesma coluna que (pos) no tabuleiro (tab).
    """
    vertical = ()
    for posicao in tab:
        if obtem_pos_col(posicao)==obtem_pos_col(pos): ## Duas posicoes estao na mesma linha vertical se estiverem na mesma coluna do tabuleiro.
            vertical += ((posicao, obtem_pedra(tab, posicao)),)
    return vertical

def obtem_linhas_diagonais(tab,pos):
    """
    obtem_linhas_diagonais(tab, pos): tabuleiro x posicao --> tuplo
    Recebe um TAD tabuleiro e um TAD posicao e retorna um tuplo com a diagonal e anti-diagonal e as posicoes e a sua respectiva pedras

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str): TAD posicao

    Retorna:
        (diagonal, inversa) (tuplo) : Tuplo com a diagonal e anti-diagonal e as posicoes e a sua respectiva pedras.
    """
    normal,inversa =(),()
    soma_cord_pos,subt_cord_pos = operacoes_cord(pos)

    for posicao in tab:
        soma_cord_posicao,subt_cord_posicao = operacoes_cord(posicao)
        if soma_cord_posicao == soma_cord_pos: ## Se a soma das coordenadas das duas posicoes forem iguais, estao na mesma anti-diagonal.
            inversa += ( ( posicao, obtem_pedra(tab, posicao)) ,) 
        
        if subt_cord_posicao == subt_cord_pos: ## Se a subtracao das coordenadas das duas posicoes forem iguais, estao na mesma diagonal.
            normal += (( posicao, obtem_pedra(tab, posicao)),)
    
    return (normal, inversa[::-1])

def obtem_posicoes_pedra(tab,pedra):
    """
    obtem_posicoes_pedra(tab, pedra): tabuleiro x pedra --> tuplo
    Recebe um TAD tabuleiro e um TAD pedra e retorna um tuplo as posicoes às quais corresponde o TAD pedra

    Argumentos:
        tab (dict): TAD tabuleiro
        pedra (int): TAD pedra

    Retorna:
        posicoes_pedra (tuplo) : Tuplo com as posicoes a que corresponde à pedra dada como argumento.
    """
    tuplo_pedras = ()
    for posicao in tab:
        if pedras_iguais(obtem_pedra(tab, posicao), pedra): ## Caso a pedra na posicao seja igual à pedra dada como argumento, adicionar ao tuplo.
            tuplo_pedras += (posicao,)
    return ordena_posicoes(tuplo_pedras, obtem_numero_orbitas(tab))

def eh_tabuleiro(tab):
    """
    eh_tabuleiro(tab): tabuleiro --> booleano
    Recebe um TAD tabuleiro retorna um booleano consoante (tab) é um tabuleiro válido.

    Argumentos:
        tab (dict): TAD tabuleiro

    Retorna:
        True (bool) : Caso (tab) seja um TAD tabuleiro válido.
        False (bool): Caso (tab) NÃO seja um TAD tabuleiro válido.
    """
    if type(tab)!=dict or not eh_n(obtem_numero_orbitas(tab)) or len(tab) not in (4**2, 6**2, 8**2, 10**2):
        ## Caso não seja um dicionário
        ## Caso o tamanho do tabuleiro não seja 4x4, 6x6, 8x8 ou 10x10
        return False
    
    usado = ()
    for pos in tab:
        if pos in usado or not eh_posicao(pos) or not eh_posicao_valida(pos, obtem_numero_orbitas(tab)) or not eh_pedra( obtem_pedra(tab,pos) ) or len(obtem_linha_horizontal(tab, pos))!=len(obtem_linha_vertical(tab, pos))!=obtem_numero_orbitas(tab)*2:
            ## Caso a posição seja duplicada, nao seja uma posicao (valida) ou o tamanho da linha e da coluna não seja igual
            return False
        usado +=(pos,)
    
    return True

def tabuleiros_iguais(tab1,tab2):
    """
    tabuleiros_iguais(tab1, tab2): tabuleiro x tabuleiro --> booleano
    Recebe dois argumentos e retorna um booleano consoante os dois argumentos são TADs tabuleiro e são iguais entre si.

    Argumentos:
        tab1 (dict): TAD tabuleiro
        tab2 (dict): TAD tabuleiro

    Retorna:
        True (bool) : Caso (tab1) e (tab2) sejam TADs tabuleiro e tab1 == tab2
        False (bool): Caso uma das condições acima não se aplique
    """
    return eh_tabuleiro(tab1) and eh_tabuleiro(tab2) and tab1==tab2

def tabuleiro_para_str(tab):
    """
    tabuleiro_para_str(tab): tabuleiro --> str
    Recebe um TAD tabuleiro e retorna a cadeia de caracteres que representa o tabuleiro.

    Argumentos:
        tab (dict): TAD tabuleiro

    Retorna:
        tab_str (string): Cadeia de caracteres que representa o tabuleiro visualmente
    """
    tab_print = ''
    n = obtem_numero_orbitas(tab)

    letras = '    '
    for ltr in 'abcdefghij'[:obtem_numero_orbitas(tab)*2]:
        letras += ltr + '   ' ## Cria uma string com todas as letras / colunas presentes no tabuleiro
        
    for pos in tab:
        if obtem_pos_col(pos)=='a':
            if obtem_pos_lin(pos)<10:
                tab_print += '0'+str(obtem_pos_lin(pos)) + ' '
            else:
                tab_print += str(obtem_pos_lin(pos)) + ' '
                
        tab_print += '[' + pedra_para_str(obtem_pedra(tab, pos)) + ']' ## Adiciona a representação externa correspondente ao TAD pedra na posição.
        
        if obtem_pos_col(pos) != 'abcdefghij'[n*2-1]: ## Caso nao seja a ultima posicao da linha, adicionar -
            tab_print += '-'
          
        if obtem_pos_col(pos) == 'abcdefghij'[n*2-1] and pos != cria_posicao('abcdefghij'[n*2-1],n*2): ## Caso seja a ultima posicao da linha mas nao seja a ultima do tabuleiro, adicionar:
            tab_print += '\n   '   + ' |  '* (n*2-1) + ' |' + '\n'
    
    return letras.rstrip()+'\n'+tab_print


## FUNCOES DE ALTO NIVEL
def move_pedra(tab,pos1,pos2):
    """
    move_pedra(tab, pos1, pos2): tabuleiro x posicao x posicao --> tabuleiro
    Recebe um TAD tabuleiro e dois TAD posicao e retorna um TAD tabuleiro com a pedra de (pos1) movida para (pos2)

    Argumentos:
        tab (dict): TAD tabuleiro
        pos1 (str): TAD posicao
        pos2 (str): TAD posicao

    Retorna:
        tab_movido (dict): Tabuleiro onde a pedra da posição pos1 foi movida para a pos2 e removida de pos1.
    """
    return remove_pedra(coloca_pedra(tab, pos2, obtem_pedra(tab,pos1)), pos1)
    
def obtem_posicao_seguinte(tab,pos,horario):
    """
    obtem_posicao_seguinte(tab, pos, horario): tabuleiro x posicao x booleano --> posicao
    Recebe um TAD tabuleiro, TAD posicao e booleano (horario) e retorna um TAD posicao.

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str): TAD posicao
        horario (bool): Caso a rotação se efetue no sentido horário (True) ou anti-horário (False)

    Retorna:
        posicao_seguinte (str): TAD posicao seguinte a (pos) segundo o booleano (horario).
    """
    
    cand = list( filter(lambda x: posicao_orbital(x, obtem_numero_orbitas(tab))==posicao_orbital(pos, obtem_numero_orbitas(tab)), obtem_posicoes_adjacentes(pos, obtem_numero_orbitas(tab),False)))
    ## As posicoes seguintes são as posicoes adjancentes ortogonais que estão na mesma orbita que 'pos'
    if operacoes_cord(pos)[0] > operacoes_cord( cria_posicao('a',obtem_numero_orbitas(tab)*2) )[0]:
        cand = cand[::-1] ## para as posicoes à direita da anti-diagonal principal, é necessário inverter a ordem devido às posições adjacentes serem ordenadas em sentido horário.
    return cand[ not horario ] ## A posição em sentido horário é a 1a entrada e a posição em sentido anti-horário é a 2a entrada.
 
def roda_tabuleiro(tab):
    """
    roda_tabuleiro(tab): tabuleiro --> tabuleiro
    Recebe um TAD tabuleiro e modifica destrutivamente o tabuleiro t rodando todas as pedras uma posição em sentido anti-horário, e devolve o próprio tabuleiro.

    Argumentos:
        tab (dict): TAD tabuleiro

    Retorna:
        tab_rodado (dict): TAD tabuleiro onde todas as posições foram rodadas 1x em sentido anti-horário.
    """
    tab_pedras, n = cria_copia_tabuleiro(tab), obtem_numero_orbitas(tab) 
    for lin in range(1, n*2+1):
        for col in range(ord('a'), ord('abcdefghij'[n*2-1])+1):
            posicao_atual = cria_posicao(chr(col), lin)
            coloca_pedra(tab, obtem_posicao_seguinte(tab, posicao_atual, False), obtem_pedra(tab_pedras, posicao_atual)) ## Coloca a pedra na posicao seguinte
            ## Ao fazer isto para todas as pedras, todas as posições vão ser movidas 1x no sentido anti-horário.
    return tab

def verifica_linha_pedras(tab, pos, pedra, k):
    """
    verifica_linha_pedras(tab, pos, pedra, k): tabuleiro x posicao x pedra x int --> booleano
    Recebe um TAD tabuleiro, um TAD posicao, um TAD pedra e um número de k-em-linha devolve True se existe pelo menos uma linha 
    (horizontal, vertical ou diagonal) que contenha a posição p com k ou mais pedras
    consecutivas do jogador com pedras j, e False caso contrário

    Argumentos:
        tab (dict): TAD tabuleiro
        pos (str): TAD posicao
        pedra (int): TAD pedra
        k (int): Número de k-em-linha

    Retorna:
        True (bool) : Caso se verifiquem k-em-linha na horizontal / vertical / diagonal
        False (bool): Caso as condições acima não se verifiquem.
    """
    if obtem_pedra(tab,pos)!=pedra: 
        return False
    
    linhas_opcoes = (obtem_linha_horizontal(tab,pos), obtem_linha_vertical(tab,pos),obtem_linhas_diagonais(tab,pos)[0],obtem_linhas_diagonais(tab,pos)[1])

    for linha in linhas_opcoes:
        intervalo_posicoes = [elemento[0] for elemento in linha] ## Coloca todas as posicoes da linha em um tuplo
        pos_index = intervalo_posicoes.index(pos) ## obtem o index da posicao 'pos'
        intervalo_posicoes = intervalo_posicoes[ max(pos_index - k + 1 , 0) : pos_index + k] ## Cria um tuplo com (k-1) posicões à esquerda e à direita de 'pos'
        contador = 0

        for posicao in intervalo_posicoes:
            if pedras_iguais(obtem_pedra(tab, posicao), pedra):
                contador += 1
                if contador == k:
                    return True
            else:
                contador = 0
    return False 


## ADICIONAIS

def eh_vencedor(tab, pedra):
    """
    eh_vencedor(tab, pedra): tabuleiro x pedra --> booleano
    recebe um tabuleiro e uma pedra de jogador, e devolve True se existe uma linha completa do
    tabuleiro de pedras do jogador ou False caso contrário

    Argumentos:
        tab (dict): TAD tabuleiro
        pedra (int): TAD pedra

    Retorna:
        True (bool) : Caso se o jogador com a pedra (pedra) tenha feito k-em-linha em alguma das suas posições jogadas.
        False (bool): Caso as condições não se verifiquem.
    """
    pos_jogador, k = obtem_posicoes_pedra(tab, pedra), obtem_numero_orbitas(tab)*2
    
    for posicao in pos_jogador:
        if verifica_linha_pedras(tab, posicao, pedra, k): 
            return True
    return False

def eh_fim_jogo(tab):
    """
    eh_fim_jogo(tab): tabuleiro --> booleano
    recebe um tabuleiro e devolve True se o jogo já terminou ou False caso contrário.

    Argumentos:
        tab (dict): TAD tabuleiro

    Retorna:
        True (bool) : O jogo já terminou
        False (bool): O jogo ainda não terminou
    """
    return eh_vencedor(tab, cria_pedra_preta()) or eh_vencedor(tab, cria_pedra_branca())

def escolhe_movimento_manual(tab):
    """
    escolhe_movimento_manual(tab): tabuleiro --> posicao
    recebe um tabuleiro (tab) e permite escolher uma posição livre do tabuleiro onde colocar uma pedra. A função não modifica
    o seu argumento e devolve a posição escolhida. A função deve apresentar as mensagens
    do exemplo a seguir, repetindo as mensagens at ́e o jogador introduzir a representação externa de uma jogada válida.

    Argumentos:
        tab (dict): TAD tabuleiro

    Retorna:
        posicao (str): TAD posicao
    """
    pos = str_para_posicao(input('Escolha uma posicao livre:'))
    while not eh_posicao(pos) or not eh_posicao_valida(pos, obtem_numero_orbitas(tab)) or pos not in obtem_posicoes_pedra(tab, cria_pedra_neutra()):
        ## Enquanto a posicao escolhida não for um TAD posicao (válido) e não for uma posição livre, continuar a pedir.
        pos = str_para_posicao(input('Escolha uma posicao livre:'))
    return pos

def estrategia_facil(tab,pedra):
    """
    estrategia_facil(tab, pedra): tabuleiro x pedra --> posicao
    A posição para colocar a pedra própria é escolhida da seguinte maneira:
    Se existir no tabuleiro pelo menos uma posição livre que no fim do turno (após
    rotação) fique adjacente a uma pedra própria, jogar numa dessas posições;
    Se não, jogar numa posição livre

    Argumentos:
        tab (dict): TAD tabuleiro
        pedra (int): TAD pedra

    Retorna:
        posicao (str): TAD posicao
    """
    tab_bot = roda_tabuleiro(cria_copia_tabuleiro(tab))
    livres_bot, jogadas_bot = obtem_posicoes_pedra(tab_bot, cria_pedra_neutra()), obtem_posicoes_pedra(tab_bot,pedra)
    usadas, candidatas = (),()

    for p_jogada in jogadas_bot:
        for p_adj in obtem_posicoes_adjacentes(p_jogada, obtem_numero_orbitas(tab_bot), True):
            if p_adj in livres_bot and p_adj not in usadas:
                candidatas += (p_adj,)
                ## Coloca todas as posições adjacentes às posições jogadas no tabuleiro rodado em uma lista de candidatas.
            usadas += (p_adj,)
 
    if len(candidatas) != 0:
        ## Caso hajam candidatas.
        candidata = [obtem_posicao_seguinte(tab_bot, posicao, True) for posicao in candidatas]
        ## Criar um tuplo com a posição a ser jogada no tabuleiro atual (tabuleiro que não foi rodado)
        return ordena_posicoes(candidata, obtem_numero_orbitas(tab_bot))[0] ## Jogar na 1a posição por ordem de leitura.
    else:
        return ordena_posicoes(livres_bot, obtem_numero_orbitas(tab_bot))[0] ## Jogar na 1a posição livre por ordem de leitura.

def estrategia_normal(tab,pedra):
    """
    estrategia_normal(tab, pedra): tabuleiro x pedra --> posicao
    A posição para colocar a pedra própria é escolhida da seguinte maneira:
    Determinar o maior valor de L <= k tal que o pr ́oprio jogador conseguir colocar L
    peças consecutivas que contenha essa jogada no fim do turno atual, ou seja, após
    uma rotação; ou que o conseguir o adverário no fim do seu seguinte turno, ou
    seja, após duas rotações. Para esse valor:
    Se existir pelo menos uma posição que permita no fim do turno obter uma
        linha que contenha essa posição com L pedras consecutivas próprias, jogar numa dessas posições;
    Se não, jogar numa posição que impossibilite o adversário no final do seu próximo turno de obter L pedras
        consecutivas numa linha que contenha essa posição.

    Argumentos:
        tab (dict): TAD tabuleiro
        pedra (int): TAD pedra

    Retorna:
        posicao (str): TAD posicao
    """
    n = obtem_numero_orbitas(tab)
    p_livres = obtem_posicoes_pedra(tab, cria_pedra_neutra())
    pedra_ataque, pedra_defesa = {cria_pedra_preta():(cria_pedra_preta(),cria_pedra_branca()), cria_pedra_branca():(cria_pedra_branca(), cria_pedra_preta())}[pedra]
    tabuleiro_ataque, tabuleiro_defesa = roda_tabuleiro(cria_copia_tabuleiro(tab)), roda_tabuleiro(roda_tabuleiro(cria_copia_tabuleiro(tab)))

    def obtem_solucao(tabuleiro, pedra, eh_defesa):
        n, jogadas, livres = obtem_numero_orbitas(tabuleiro), obtem_posicoes_pedra(tabuleiro, pedra), obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra())
        L, candidatas, usadas, solucao =  n*2, (), (), []

        ## Selecionar as possiveis posicoes
        for p_jogada in jogadas:
            for p_adj in obtem_posicoes_adjacentes(p_jogada, n, True):
                if p_adj in livres and p_adj not in usadas:
                    candidatas += (p_adj,)
                usadas += (p_adj,)
        ## candidatas sao as possiveis posicoes que podem se vir a tornar na solucao
        while L >= 1:
            for pos in candidatas:
                tab_simul = coloca_pedra(cria_copia_tabuleiro(tabuleiro), pos, pedra)
                if verifica_linha_pedras(tab_simul, pos, pedra, L):
                    solucao += [pos,]
            
            if len(solucao)==0:
                ## Caso ainda não haja uma pedra para realizar k-em-linha, continuar.
                L -= 1
            else:
                ## Caso haja, parar.
                break
        ## obtem a posicao para colocar no tabuleiro atual
        for index in range(len(solucao)):
            ## Ordenar as soluções de forma a serem jogadas no tabuleiro não rodado.
            solucao[index] = obtem_posicao_seguinte(tab, solucao[index], True)
            if eh_defesa:
                ## Como na defesa o tabuleiro foi rodado 2x, é preciso obter a posição seguinte 2x.
                solucao[index] = obtem_posicao_seguinte(tab, solucao[index], True)
        return solucao, L

    ataque, L_ataque = obtem_solucao(tabuleiro_ataque, pedra_ataque, False)
    defesa, L_defesa = obtem_solucao(tabuleiro_defesa, pedra_defesa, True)
   
    if len(obtem_posicoes_pedra(tab, pedra))==0 and len(defesa)==0:
        ## Caso o bot ainda não tenha jogado e não tenha movimentos para defesa.
        ## Jogar na 1a posicao livre por ordem de leitura
        return ordena_posicoes(p_livres, n)[0]
    
    elif L_ataque >= L_defesa:
        ## Caso tenha uma posicao de ataque, jogar na 1a por ordem de leitura
        return ordena_posicoes(tuple(ataque),n)[0]
    else:
        ## Caso tenha uma posicao de defesa, jogar na 1a por ordem de leitura.
        return ordena_posicoes(tuple(defesa),n)[0]

def escolhe_movimento_auto(tab, pedra, lvl):
    """
    escolhe_movimento_auto(tab, pedra, lvl): tabuleiro x pedra x str --> posicao
    Recebe um tabuleiro t (em que o jogo n ̃ao terminou ainda), uma pedra j, e a cadeia de carateres lvl correspondente
    à estratégia, e devolve a posição escolhida automaticamente de acordo com a estratégia
    selecionada para o jogador com pedras j. A função não modifica nenhum dos seus argumentos

    Argumentos:
        tab (dict): TAD tabuleiro
        pedra (int): TAD pedra
        lvl (str): Nível de dificuldade 'facil' ou 'normal'

    Retorna:
        escolha (int) : TAD posicao escolhido com base na dificuldade selecionada.
    """
    if lvl=='facil':
        return estrategia_facil(tab,pedra)
    elif lvl=='normal':
        return estrategia_normal(tab,pedra)

def eh_lvl(lvl):
    """
    eh_lvl(lvl): string --> bool
    Recebe um nível e retorna um booleano caso seja um nível valido.

    Argumentos:
        lvl (str): Uma string que pode ser 'facil', 'normal', '2jogadores'.

    Retorna:
        True (bool) : Caso passe em todos os critérios.
        False (bool): Caso não passe em todos os critérios.
    """
    return type(lvl)==str and lvl in ('facil','normal','2jogadores')


def orbito(n, lvl, jog):
    """
    orbito(n,lvl, jog): int x str x str --> int
    É a função principal que permite jogar um jogo completo de Orbito-n. 
    A função recebe o número de órbitas do tabuleiro, uma cadeia de carateres que
    representa o modo de jogo, e a representação externa de uma pedra (preta ou branca),
    e devolve um inteiro identificando o jogador vencedor (1 para preto ou -1 para branco),
    ou 0 em caso de empate

    Argumentos:
        n (int): Número de orbitas do tabuleiro
        lvl (str): Nível de dificuldade.
        jog (str): Representação externa de uma pedra.

    Retorna:
        vencedor (int) : Representação em número inteiro do vencedor.
    """
    if not eh_n(n) or not eh_lvl(lvl) or not eh_jog(jog):
        raise ValueError('orbito: argumentos invalidos')
    
    tab = cria_tabuleiro_vazio(n)
    pedra_jogador, pedra_oponente, jogador_comeca = {'X':(cria_pedra_preta(),cria_pedra_branca(),True), 'O':(cria_pedra_branca(), cria_pedra_preta(),False)}[jog]

    print('Bem-vindo ao ORBITO-' + str(n) + '.')

    if lvl=='facil' or lvl=='normal': ## JOGO CONTRA O BOT
        print('Jogo contra o computador ('+lvl+').')
        print("O jogador joga com '"+ jog +"'.")
        print(tabuleiro_para_str(tab))

        while not eh_fim_jogo(tab):
            if jogador_comeca: ## JOGADOR COMECA
                print('Turno do jogador.')
                tab = roda_tabuleiro(coloca_pedra(tab, escolhe_movimento_manual(tab), cria_pedra_preta())) ## roda tabuleiro
                print(tabuleiro_para_str(tab)) ## printa

                if eh_fim_jogo(tab):
                    break
                
                print('Turno do computador ('+lvl+'):')
                tab = roda_tabuleiro(coloca_pedra(tab, escolhe_movimento_auto(tab, cria_pedra_branca(), lvl), cria_pedra_branca())) ## roda tabuleiro
                print(tabuleiro_para_str(tab)) ## printa
                        
            else: ## BOT
                print('Turno do computador ('+lvl+'):')
                tab = roda_tabuleiro(coloca_pedra(tab, escolhe_movimento_auto(tab, cria_pedra_preta(), lvl), cria_pedra_preta())) ## roda tabuleiro
                print(tabuleiro_para_str(tab)) ## printa

                if eh_fim_jogo(tab):
                    break
                    
                print('Turno do jogador.')
                tab = roda_tabuleiro(coloca_pedra(tab, escolhe_movimento_manual(tab), cria_pedra_branca())) ## roda tabuleiro
                print(tabuleiro_para_str(tab)) ## printa
                
        
        ## VENCEDORES
        if eh_vencedor(tab, pedra_jogador) and eh_vencedor(tab, pedra_oponente): ## AMBOS Ganharam
            print('EMPATE')
            return 0
    
        elif eh_vencedor(tab, pedra_jogador): ## jogador ganhou
            print('VITORIA')
            return pedra_para_int(pedra_jogador)
    
        else:
            print('DERROTA')
            return pedra_para_int(pedra_oponente)
    
    else: ## 2JOGADORES
        print('Jogo para dois jogadores.')
        print(tabuleiro_para_str(tab))

        while not eh_fim_jogo(tab):
            ## JOGADOR
            print("Turno do jogador '"+pedra_para_str(cria_pedra_preta())+"'.")
            tab = coloca_pedra(tab, escolhe_movimento_manual(tab), cria_pedra_preta()) ## coloca pedra
            tab = roda_tabuleiro(tab) ## roda tabuleiro
            print(tabuleiro_para_str(tab)) ## printa
            
            if eh_fim_jogo(tab):
                break
                
            ## ADV
            print("Turno do jogador '"+pedra_para_str(cria_pedra_branca())+"'.")
            tab = coloca_pedra(tab, escolhe_movimento_manual(tab), cria_pedra_branca()) ## coloca pedra
            tab = roda_tabuleiro(tab) ## roda tabuleiro
            print(tabuleiro_para_str(tab)) ## printa
        
        ## VENCEDORES
        if eh_vencedor(tab, cria_pedra_preta()) and eh_vencedor(tab, cria_pedra_branca()): ## AMBOS Ganharam
            print('EMPATE')
            return pedra_para_int(cria_pedra_neutra())
    
        elif eh_vencedor(tab, cria_pedra_preta()): ## jogador ganhou
            print("VITORIA DO JOGADOR '"+pedra_para_str(cria_pedra_preta())+"'")
            return pedra_para_int(cria_pedra_preta())
    
        else:
            print("VITORIA DO JOGADOR '"+pedra_para_str(cria_pedra_branca())+"'")
            return pedra_para_int(cria_pedra_branca())

