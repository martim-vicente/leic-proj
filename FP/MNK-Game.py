'''
Project: MNK Game
Author: Martim Vicente
Course: Fundamentos da Programacao (FP)
'''


    


def eh_tabuleiro(tab):
    """
    Summary : eh_tabuleiro {tuple} --> {bool}
    Identifies if 'tab' is a valid board.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.

            
    Returns : bool
        True : If ALL the conditions above are met.
        False : If AT LEAST ONE of the conditions above are NOT met.

        
    Raises:
        Nothing
    """
    
    if type(tab)==tuple and 2 <= len(tab) <= 100:
        for line in tab:
            if type(line)!=tuple or 2>len(line) or len(line)>100 or len(line)!=len(tab[0]):
                return False 
            
            for element in line:
                if type(element)!=int or not(element==1 or element==0 or element==-1):
                    return False    
        return True        
    return False


def eh_jogador(jog):
    """
    Summary : eh_jogador {int} --> {bool}
    Identifies if 'jog' is a valid player.

    
    Arguments : 
        jog : (int) : Represents the player.
            Must be 1 or -1.

            
    Returns : bool
        True : If ALL the conditions above are met.
        False : If AT LEAST ONE of the conditions above are NOT met.

        
    Raises:
        Nothing
    """
    return type(jog)==int and ( jog==1 or jog==-1 )


def eh_nivel(lvl):
    """
    Summary : eh_nivel {int} --> {bool}
    Identifies if 'lvl' is a valid game difficulty.

    
    Arguments : 
        lvl : (string) : Represents the difficulty.
            Must be 'facil', 'normal' or 'dificil'.

            
    Returns : bool
        True : If ALL the conditions above are met.
        False : If AT LEAST ONE of the conditions above are NOT met.

        
    Raises:
        Nothing
    """
    return type(lvl)==str and ( lvl=='facil' or lvl=='normal' or lvl=='dificil') ## String, either ´facil', 'normal' or 'dificil'


def eh_posicao(pos):
    """
    Summary : eh_posicao {int} --> {bool}
    Identifies if 'pos' is a position.

    
    Arguments : 
        pos : (int) : Represents a position.
            Greater or equal to 1
            Less or equal to 10000

            
    Returns : bool
        True : If ALL the conditions above are met.
        False : If AT LEAST ONE of the conditions above are NOT met.

        
    Raises:
        Nothing
    """    
    return type(pos)==int and 1<=pos<=100*100 # 100*100 is highest possible position in a valid board


def eh_k(k):
    """
    Summary : eh_k {int} --> {bool}
    Identifies if 'k' is a valid k-in-a-row value.

    
    Arguments : 
        k : (int) : Represents a k-in-a-row value.
            Greater or equal to 1

            
    Returns : bool
        True : If ALL the conditions above are met.
        False : If AT LEAST ONE of the conditions above are NOT met.

        
    Raises:
        Nothing
    """
    return type(k)==int and 1 <= k 


def obtem_dimensao(tab):
    """
    Summary : obtem_dimensao {tuple} --> {tuple}
    Returns the dimensions of the board 'tab'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.

            
    Returns : tuple : (m, n)
        m : Number of lines in the board.
        n : Number of columns in the board.

        
    Raises:
        Nothing
    """
    lines = len(tab)
    columns = len(tab[0])
    return (lines, columns) 


def obtem_maximo(tab):
    """
    Summary : obtem_maximo {tuple} --> {int}
    Returns the highest possible position on the board 'tab'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.

            
    Returns : int : pos_max
        pos_max : Highest position on the board.
        Given by the product between the number of lines and columns

        
    Raises:
        Nothing
    """
    return obtem_dimensao(tab)[0]*obtem_dimensao(tab)[1]


def obtem_cord(tab,pos):
    """
    Summary : obtem_cord {tuple, int} --> {tuple}
    Returns the highest possible position on the board 'tab'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : tuple : (pos_m, pos_n)
        pos_m : Line of 'pos' on the board .
        pos_n : Column of 'pos' on the board.
        Lines and Columns start on 0.

        
    Raises:
        Nothing
    """
    pos_line = (pos-1) // (obtem_dimensao(tab)[1])
    pos_column = (pos-1) % (obtem_dimensao(tab)[1])
    return (pos_line, pos_column)


def obtem_valor(tab,pos):
    """
    Summary : obtem_valor {tuple,int} --> {int}
    Returns the value assigned to 'pos' on the board 'tab'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : int : pos_value
        pos_value : Value assigned to 'pos' on the board tuple.

        
    Raises:
        Nothing
    """
    return tab[ obtem_cord(tab,pos)[0] ][ obtem_cord(tab,pos)[1] ]


def obtem_distancia(tab,pos1,pos2):
    """
    Summary : obtem_distancia {tuple,int,int} --> {int}
    Returns the distance between two positions, 'pos1' and 'pos2' on the board 'tab'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos1 / pos2 : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : int : distance
        distance : Chebyshev board distance between 'pos1' and 'pos2'.

        
    Raises:
        Nothing
    """
    delta_lines = obtem_cord(tab,pos1)[0]-obtem_cord(tab,pos2)[0] ## Difference between the line where each position is located in
    delta_columns = obtem_cord(tab,pos1)[1]-obtem_cord(tab,pos2)[1] ## Difference between the column where each position is located in
    return max( abs(delta_lines), abs(delta_columns)) ## Chebyshev Board Distance


def obtem_coluna(tab,pos):
    """
    Summary : obtem_coluna {tuple,int} --> {tuple}
    Returns a tuple with the positions that are in the column which contains 'pos'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : tuple : pos_column
        pos_column : Tuple with the positions on the column which contains 'pos'.

        
    Raises:
        Nothing
    """
    line_len = obtem_dimensao(tab)[1]
    while pos > line_len:
        pos -= line_len ## Obtains the first position of the column
    
    return tuple(range(pos, obtem_maximo(tab)+1, line_len)) ## In a column every position can be attained by adding a multiple of the length of the line (number of columns)


def obtem_linha(tab,pos):
    """
    Summary : obtem_linha {tuple,int} --> {tuple}
    Returns a tuple with the positions that are in the line which contains 'pos'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : tuple : pos_line
        pos_line : Tuple with the positions on the line which contains 'pos'.

        
    Raises:
        Nothing
    """
    line_len = obtem_dimensao(tab)[1]
    inicio = obtem_cord(tab,pos)[0]*line_len + 1 ## The 1st element of every line is given by the line number times the size of the line +1 because positions start on 1 and not 0
    return tuple( range( inicio, inicio + line_len ) )


def soma_cord(tab,pos):
    """
    Summary : soma_cord {tuple,int} --> {int}
    Returns the sum of the line and column of 'pos'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : int : pos_sum
        pos_sum : Sum of the line and column of 'pos'.

        
    Raises:
        Nothing
    """
    pos_line = obtem_cord(tab,pos)[0]
    pos_column = obtem_cord(tab,pos)[1]
    return pos_line + pos_column ## Sum of the line and column of a valid position on the board


def subt_cord(tab,pos):
    """
    Summary : subt_cord {tuple,int} --> {int}
    Returns the subtraction of the line and column of 'pos'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : int : pos_sum
        pos_sum : Subtraction of the line and column of 'pos'.

        
    Raises:
        Nothing
    """
    pos_line = obtem_cord(tab,pos)[0]
    pos_column = obtem_cord(tab,pos)[1]
    return pos_line - pos_column ## Subtraction of the line and column of a valid position on the board

        

def obtem_diagonais(tab,pos):
    """
    Summary : obtem_diagonais {tuple,int} --> {tuple}
    Returns a tuple with the diagonal and anti-diagonal that contain 'pos'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : tuple : (diagonal, anti-diagonal)
        diagonal : 
        anti-diagonal : 

        
    Raises:
        Nothing
    """
    normal=()
    inver=()
    soma_cord_posicao = soma_cord(tab,pos)
    subt_cord_posicao = subt_cord(tab,pos)

    for position in range(1, obtem_maximo(tab)+1):
        if position == pos:
            normal += (position,)
            inver += (position,)
        
        elif soma_cord(tab, position) == soma_cord_posicao: ## If the sum of the coordinates of two positions are equal, they are in the same Anti-Diagonal
            inver += (position,)
        
        elif subt_cord(tab, position) == subt_cord_posicao: ## If the subtraction of the coordinates of two positions are equal, they are in the same Diagonal
            normal += (position,)
    
    return (normal, inver[::-1])


def tabuleiro_para_str(tab):
    """
    Summary : tabuleiro_para_str {tuple} --> {string}
    Returns a string that contains the visual representation of the board 'tab'.
    Replaces the values the following way:
        1 -> 'X'    |   0 -> '+'    |   -1 -> 'O'

        
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
  
            
    Returns : string : tab_print
        tab_print :  String that when printed, represents the board.

        
    Raises:
        Nothing
    """
    tab_print = ''
    line_range = range(obtem_dimensao(tab)[0])
    column_range = range(obtem_dimensao(tab)[1])
    
    for line_index in line_range:
        for column_index in column_range:
            if tab[line_index][column_index] == 1: ## If the position has a 1, it is assigned an 'X' on the board
                tab_print += 'X'                    
            
            elif tab[line_index][column_index] == 0: ## If the position has a 0, it is assigned an '+' on the board
                tab_print += '+'
            
            else: ## If the position has a -1, it is assigned an 'O' on the board
                tab_print += 'O'
        
            if column_index != column_range[-1]: ## The string '---' is added in between symbols, except when the last symbol of a line is added
                tab_print += '---'
                
        if line_index != line_range[-1]: ## The string '|   ' is added in between lines, except when the last line of the board was added
            tab_print += '\n'   + '|   '* column_range[-1] + '|' + '\n'
    
    return tab_print


def eh_posicao_valida(tab,pos):
    """
    Summary : eh_posicao_valida {tuple,int} --> {bool}
    Identifies if 'pos' is a valid position.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : bool
        To return a boolean these conditions must be met : 
            'tab' is a valid board AND 'pos' is a position
        
        True :  'pos' is less or equal to the highest position on the board.
        False : 'pos' is NOT less or equal to the highest position on the board.

        
    Raises:
        ValueError : 'tab' is not a valid board OR 'pos' is not a position
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    
    return pos <= obtem_maximo(tab) ## To be valid it needs to less or equal to the highest position on the board
    

def eh_posicao_livre(tab,pos):
    """
    Summary : eh_posicao_livre {tuple,int} --> {bool}
    Identifies if 'pos' is an empty position.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : bool
        To return a boolean these conditions must be met : 
            'tab' is a valid board AND 'pos' is a position AND 'pos' is a valid position
        
        True : The value assigned to 'pos' is 0
        False : The value assigned to 'pos' is NOT 0

        
    Raises:
        ValueError : 'tab' is a valid board OR 'pos' is a position OR 'pos' is a valid position
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    
    return obtem_valor(tab,pos) == 0 ## To be empty the value assigned to it must be 0
    

def obtem_posicoes_livres(tab):
    """
    Summary : obtem_posicoes_livres {tuple} --> {tuple}
    Returns a tuple with all the empty positions on the board.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.

                
    Returns : tuple : pos_empty
        To return pos_empty these conditions must be met :
            'tab' is a valid board

        pos_empty : Tuple with all the board positions that have a 0 assigned to it 

        
    Raises:
        ValueError : 'tab' is not a valid board
    """
    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')     
    
    pos_empty = ()
    for position in range(1, obtem_maximo(tab)+1):
        if eh_posicao_livre(tab, position):
            pos_empty += (position,)
    
    return pos_empty



def obtem_posicoes_jogador(tab,jog):
    """
    Summary : obtem_posicoes_jogador {tuple,int} --> {tuple}
    Returns a tuple with all the moves made by player 'jog'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        jog : (int) : Represents the player.
            Must be 1 or -1.

    
    Returns : tuple : pos_player
        pos_jog : Tuple with all the board positions that have 'jog' assigned to it 

    
    Raises:
        ValueError : 'tab' is not a valid board OR 'jog' is not a valid player.
    """
    if not eh_tabuleiro(tab) or not eh_jogador(jog):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    
    pos_player = ()
    for position in range(1, obtem_maximo(tab)+1): 
        if obtem_valor(tab, position)==jog: ## If the value assigned to the position is the same as 'jog', it is added to 'pos_player'
            pos_player += (position,)
    
    return pos_player
    

def obtem_posicoes_adjacentes(tab,pos):
    """
    Summary : obtem_posicoes_adjacentes {tuple,int} --> {tuple}
    Returns a tuple with all the adjacent positions to 'pos'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1.
            Less or equal to 10000.

            
    Returns : tuple : pos_adj
        pos_adj : Tuple with all the adjacent board positions to 'pos'.
        A position is adjacent to other if its Chebyshev Distance is equal to 1 

        
    Raises:
        ValueError : 'tab' is not a valid board OR 'pos' is not a position / valid position.
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    
    pos_adj = ()
    pos_options = (obtem_coluna(tab,pos) + obtem_linha(tab,pos) + obtem_diagonais(tab,pos)[0] + obtem_diagonais(tab,pos)[1]) ## (column + line + diagonal + anti-diagonal)
    
    for position in pos_options:
        if obtem_distancia(tab, position, pos)==1: ## If the Chebyshev Distance between the two positions is 1, they are adjacent
            pos_adj += (position,)
    
    return tuple(sorted(pos_adj))



def eh_tpl(tab,tpl):
    """
    Summary : eh_tpl {tuple} --> {bool}
    Identifies if 'tpl' is a valid positions tuple.

    
    Arguments : 
        tpl : (tuple) : Tuple with valid positions
            Each entry must be a position
            Each entry must be a valid position

            
    Returns : bool
        True : If ALL conditions above must be met.
        False : If AT LEAST ONE of the conditions above are NOT met.

        
    Raises:
        ValueError : 'tab' is not a valid board OR 'tpl' is not a valid position tuple.
    """
    if type(tpl)!=tuple: 
        return False
    
    for position in tpl:
        if not eh_posicao(position) or not eh_posicao_valida(tab, position): ## If the entry is not a position or a valid positon, tpl is not valid
            return False
    
    return True
     


def ordena_posicoes_tabuleiro(tab,tpl):
    """
    Summary : ordena_posicoes_tabuleiro {tuple,tuple} --> {tuple}
    Returns a tuple all the positions inside 'tpl' sorted from closest to farthest from the center of the board.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        tpl : (tuple) : Tuple with valid positions
            Each entry must be a position
            Each entry must be a valid position

            
    Returns : tuple : pos_sorted
        pos_sorted : Tuple with all the positions sorted.

        
    Raises:
        ValueError : 'tab' is not a valid board OR 'tpl' is not a valid position tuple.
    """
    if not eh_tabuleiro(tab) or not eh_tpl(tab,tpl):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    
    pos_sorted = ()
    pos_options = tuple(sorted(tpl))
    center = (obtem_dimensao(tab)[0]//2)*obtem_dimensao(tab)[1]+obtem_dimensao(tab)[1]//2+1
    
    ## CENTER OF THE BOARD CALCULATIONS
    line_center = obtem_cord(tab, center)[0]
    column_center = obtem_cord(tab, center)[1]
    max_distance = max( line_center, column_center ) ## The maximum distance possible on the board relative to a postion is given by max( pos_line, pos_column)
    
    for distance in range (max_distance + 1): ## Distance starts on 0 and goes on until the max_distance, sorting the positions by distance
        for position in pos_options:
            if obtem_distancia(tab, center, position)==distance: 
                pos_sorted += (position,)
        
    return pos_sorted



def marca_posicao(tab,pos,jog):
    """
    Summary : marca_posicao {tuple,int,int} --> {tuple}
    Returns a board tuple with the value of 'pos' modified to 'jog'.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1
            Less or equal to 10000
        
        jog : (int) : Represents the player.
            Must be 1 or -1.

            
    Returns : tuple : tab_new
        tab_new : Board where the value of 'pos' was changed to 'jog'

        
    Raises:
        ValueError : 'tab' is not a valid board OR 'pos' is not a position OR 'pos' is not a valid position OR 'pos' is not an empty position
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_jogador(jog) or not eh_posicao_valida(tab,pos) or not eh_posicao_livre(tab,pos):
        raise ValueError('marca_posicao: argumentos invalidos')  
    
    line_index = obtem_cord(tab,pos)[0]
    column_index = obtem_cord(tab,pos)[1]
    
    line_new = tab[line_index][:column_index] + (jog,) + tab[line_index][column_index+1:] ## Slicing to replace the entry of 'pos' with 'jog'
    return tab[:line_index] + (line_new,) + tab[line_index+1:]



def verifica_k_linhas(tab,pos,jog,k):
    """
    Summary : verifica_k_linhas {tuple,int,int,int} --> {bool}
    Identifies if there is a line that goes through 'pos' that has k-in-a-row.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1
            Less or equal to 10000
        
        jog : (int) : Represents the player.
            Must be 1 or -1.

        k : (int) : Represents a k-in-a-row value.
            Greater or equal to 1
    
            
    Returns : bool
        To return a boolean these conditions must be met : 
            'tab' is a valid board AND 'pos' is a position AND 'pos' is a valid position AND 'k' is a valid k-value AND 'jog' is a valid player.
        
        True :  If the player has k-in-a-row in a line that goes through 'pos'.
        False : If the player has NOT k-in-a-row in a line that goes through 'pos'.

        
    Raises:
        ValueError : 'tab' is NOT a valid board OR 'pos' is NOT a position OR 'pos' is NOT a valid position OR 'k' is NOT a valid k OR 'jog' is NOT a valid player.
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_jogador(jog) or not eh_k(k) or not eh_posicao_valida(tab,pos):
        raise ValueError('verifica_k_linhas: argumentos invalidos')
        
    if obtem_valor(tab,pos)!=jog: ## If the position where the function is checking for k-in-a-row doesnt doesnt have 'jog' assigned to it, Return False
        return False
    
    line_options = (obtem_linha(tab,pos), obtem_coluna(tab,pos),obtem_diagonais(tab,pos)[0],obtem_diagonais(tab,pos)[1])

    for option in line_options:
        pos_index = list(option).index(pos) ## Obtains the index of 'pos' in the line that is being used.
        option = option[ max(pos_index - k + 1 , 0) : pos_index + k] ## Slicing to create a tuple that has (k-1) entries to the left and to the right of 'pos'
        count = 0

        for position in option:
            if obtem_valor(tab, position) == jog: ## If the position has 'jog' assigned to it, count is increased by 1
                count += 1
                if count == k: ## If count equals 'k', there are in fact k-in-a-row in this line, Return True
                    return True
            
            else:  ## If the position DOESNT have 'jog' assigned to it, count goes back to 0
                count = 0
    
    return False ## If there are not k-in-a-row in any line, Return False
    


def eh_fim_jogo(tab,k):
    """
    Summary : eh_fim_jogo {tuple,int} --> {bool}
    Identifies if the game has ended.
    The game ends if there are no more empty positions.
    The game ends if one player has made k-in-a-row.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        k : (int) : Represents a k-in-a-row value.
            Greater or equal to 1
    
            
    Returns : bool
        To return a boolean these conditions must be met : 
            'tab' is a valid board AND 'k' is a valid k-value.
        
        True :  If there are no more empty positions
                If one of the players has k-in-a-row.

        False : If the player has NOT k-in-a-row in a line that goes through 'pos'.

        
    Raises:
        ValueError : 'tab' is NOT a valid board OR 'k' is NOT a valid k-value.
    """
    if not eh_tabuleiro(tab) or not eh_k(k):
        raise ValueError('eh_fim_jogo: argumentos invalidos')

    pos_player_1 = obtem_posicoes_jogador(tab, 1)
    pos_player_2 = obtem_posicoes_jogador(tab, -1)

    if obtem_posicoes_livres(tab)==(): ## If there are no more positions to play in the board, the game is over
        return True  
    
    for position in pos_player_1:
        if verifica_k_linhas(tab, position, 1, k): ## If 'jog' == 1 has k-in-a-row, the game is over
            return True
    
    for position in pos_player_2:
        if verifica_k_linhas(tab, position, -1, k): ## If 'jog' == -1 has k-in-a-row, the game is over
            return True
    
    return False ## If no one has made k-in-a-row and there are empty positions, the game is NOT over



def eh_vencedor(tab,k):
    """
    Summary : eh_vencedor {tuple,int} --> {int}
    Identifies who has won the game.
    Can only be called if the game has ended.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        k : (int) : Represents a k-in-a-row value.
            Greater or equal to 1
    
            
    Returns : int : 1, 0, -1
        To return a value these conditions must be met : 
            'tab' is a valid board AND 'k' is a valid k-value AND the game has ended.
        
         1 : If player 1 has won the game by making k-in-a-row

        -1 : If player -1 has won the game by making k-in-a-row

         0 : If the game was a draw

        
    Raises:
        ValueError : 'tab' is NOT a valid board OR 'k' is NOT a valid k-value OR the game is not finished.
    """
    if not eh_tabuleiro(tab) or not eh_fim_jogo(tab,k): ## Should only be used when the game is finished
        raise ValueError('eh_vencedor: jogo nao terminado')
    
    pos_player_1 = obtem_posicoes_jogador(tab, 1)
    pos_player_2 = obtem_posicoes_jogador(tab, -1)

    for position in pos_player_1:
        if verifica_k_linhas(tab, position, 1, k): ## If jog == 1 has k-in-a-row, Return 1
            return 1
    
    for position in pos_player_2:
        if verifica_k_linhas(tab, position, -1, k): ## If jog == -1 has k-in-a-row, Return -1
            return -1
    
    return 0 ## If neither player has made k-in-a-row, it is a draw, Return 0




def escolhe_posicao_manual(tab):
    """
    Summary : escolhe_posicao_manual {tuple} --> {int}
    Asks the user for an empty position on the board.
    

    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
    Returns : int : pos
        To return 'pos' this condition must be met : 
            'tab' is a valid board AND 'pos' is a position AND 'pos' is a valid position AND 'pos' is an empty position
        
        pos : Empty position chosen by the user.

        
    Raises:
        ValueError : 'tab' is NOT a valid board.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
   
    pos = ''
    while not pos.isdigit() or not eh_posicao(int(pos)) or not eh_posicao_valida(tab,int(pos)) or not eh_posicao_livre(tab,int(pos)) : ## Keeps requesting input until valid
        pos = input('Turno do jogador. Escolha uma posicao livre: ')

    
    return int(pos)

   
def estrategia_facil(tab,jog):
    """
    Summary : estrategia_facil {tuple,int} --> {int}
    A position is chosen taking into account the easy difficulty, rules:
        If, on the board exists at least one position that is empty and adjacent to a position
            already played by the bot, play in one that is closer to the center of the board.

        Else, play in the empty position closer to the center of the board.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        jog : (int) : Represents the player.
            Must be 1 or -1.
    
            
    Returns : int : position_easy
        position_easy :  Position chosen by the easy difficulty bot

        
    Raises:
        Nothing
    """
    pos_empty = obtem_posicoes_livres(tab)
    pos_player = obtem_posicoes_jogador(tab,jog)        
    possible_moves = ()
    used = ()

    for move in pos_player:
        for pos_adj in obtem_posicoes_adjacentes(tab, move):
            if pos_adj in pos_empty and pos_adj not in used:
                possible_moves += (pos_adj,)
            
            used += (pos_adj,)
    
    if possible_moves != (): ## If there are possible moves, play the one closer to the center
        return ordena_posicoes_tabuleiro(tab,possible_moves)[0]
    
    return ordena_posicoes_tabuleiro(tab, pos_empty)[0] ## If there are not, play on the empty position closest to the center
    


def estrategia_normal(tab,jog,k):
    """
    Summary : estrategia_normal {tuple,int,int} --> {int}
    A position is chosen taking into account the normal difficulty, rules:
        Determine the highest L, such that L <= K, where L represents the number of pieces
        the bot and the opponent can put in a row in the next play.
       
            If, L-Attack is greater or equal than L-Defense, play in the position that is the
            closest to the center of the board and lets the bot have L-Attack-in-a-row pieces

            Else, play in a position that doesn't allow the opponent to have
            L-Defense-in-a-row pieces.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        jog : (int) : Represents the player.
            Must be 1 or -1.
        
        k : (int) : Represents a k-in-a-row value.
            Greater or equal to 1
    
            
    Returns : int : position_normal
        position_normal :  Position chosen by the normal difficulty bot

        
    Raises:
        Nothing
    """

    pos_empty = obtem_posicoes_livres(tab)
    pos_player = obtem_posicoes_jogador(tab,jog)
    pos_opponent = obtem_posicoes_jogador(tab,-jog)
    moves_attack = ()
    moves_defense = ()
    L_attack = k
    L_defense = k
    
    
    ## GATHERS ALL THE POSSIBLE MOVES FOR ATTACK
    used = ()
    for position in pos_player:
        for pos_adj in obtem_posicoes_adjacentes(tab, position):
            if pos_adj in pos_empty and pos_adj not in used:
                moves_attack += (pos_adj,)
            used += (pos_adj,)
    
    ## GATHERS ALL THE POSSIBLE MOVES FOR DEFENSE
    used = ()
    for position in pos_opponent:
        for pos_adj in obtem_posicoes_adjacentes(tab, position):
            if pos_adj in pos_empty and pos_adj not in used:
                moves_defense += (pos_adj,)
            used += (pos_adj,)
    
    ## SORTS THE MOVES BY CLOSEST TO THE CENTER OF THE BOARD
    moves_attack = ordena_posicoes_tabuleiro(tab, moves_attack)
    moves_defense = ordena_posicoes_tabuleiro(tab, moves_defense)
    

    ## CHECKS THE HIGHEST L-IN-A-ROW THE BOAT CAN MAKE
    while L_attack > 1:
        for move in moves_attack:
            if verifica_k_linhas(marca_posicao(tab, move, jog), move, jog, L_attack):
                    moves_attack = move
                    break
        
        if type(moves_attack) == tuple:
            L_attack -=1
        else:
            break
    
    ## CHECKS THE HIGHEST L-IN-A-ROW THE OPPONENT CAN MAKE
    while L_defense > 1:
        for move in moves_defense:
            if verifica_k_linhas(marca_posicao(tab, move, -jog), move, -jog, L_defense):
                    moves_defense = move
                    break
        
        if type(moves_defense) == tuple:
            L_defense -=1
        else:
            break
    
    if obtem_posicoes_jogador(tab,jog) == () and type(moves_defense) == tuple: ## If the bot hasnt played and there is no position to defend, play the empty position that is the closest to the center
        return ordena_posicoes_tabuleiro(tab,pos_empty)[0]
    
    if L_attack >= L_defense: ## PRIORITIZE THE ATTACK OF THE DEFENSE
        return moves_attack
    return moves_defense



def estrategia_dificil(tab,jog,k):
    """
    Summary : estrategia_dificil {tuple,int,int} --> {int}
    A position is chosen taking into account the hard difficulty, rules:
    
    If there exists a position that lets the bot have a line with k-in-a-row pieces,
    thus winning the game, play in the position that is the closest to the center of the board.
    
    If the bot can't win, If there exists a position that lets the opponent have a 
    line with k-in-a-row pieces, making the bot lose the game, play in the position 
    that is the closest to the center of the board.
    
    If none of the above apply, for every empty position, simulate a game where the
    empty position is played by the bot, after that, the simulation is made between two
    normal difficulty bots until the game gets to an end.

        If there are positions that had as outcome a winning simulation, play the position closest to the center.
    
        If not, If there are positions that had as outcome a draw simulation, play the position closest to the center.
        
        Else, play in the empty position closest to the center.

    
    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        jog : (int) : Represents the player.
            Must be 1 or -1.
        
        k : (int) : Represents a k-in-a-row value.
            Greater or equal to 1
    
            
    Returns : int : position_hard
        position_hard :  Position chosen by the hard difficulty bot

        
    Raises:
        Nothing
    """

    ## VITORIA IMEDIATA / PREVENIR VITORIA
    pos_empty = obtem_posicoes_livres(tab)
    moves_win = ()
    moves_defense = ()
    pos_bot = obtem_posicoes_jogador(tab,jog)
    pos_opponent = obtem_posicoes_jogador(tab,-jog)
    
    ## GATHERS ALL THE POSSIBLE MOVES TO WIN
    used = ()
    for position in pos_bot:
        for pos_adj in obtem_posicoes_adjacentes(tab, position):
            if pos_adj in pos_empty and pos_adj not in used and verifica_k_linhas( marca_posicao(tab, pos_adj, jog), pos_adj, jog, k):
                moves_win += (pos_adj,)
            used += (pos_adj,)
    
    ## GATHERS ALL THE POSSIBLE MOVES TO PREVENT A LOSS
    used = ()
    for position in pos_opponent:
        for pos_adj in obtem_posicoes_adjacentes(tab, position):
            if pos_adj in pos_empty and pos_adj not in used and verifica_k_linhas( marca_posicao(tab, pos_adj, -jog), pos_adj, -jog, k):
                moves_defense += (pos_adj,)
            used += (pos_adj,)

   ## SORTS THE POSITIONS BY CLOSEST TO THE CENTER
    moves_win = ordena_posicoes_tabuleiro(tab,moves_win)
    moves_defense = ordena_posicoes_tabuleiro(tab,moves_defense)
    if moves_win != ():
        return moves_win[0]
    
    elif moves_defense != ():
        return moves_defense[0]
    
    ## SIMULATION
    pos_empty = ordena_posicoes_tabuleiro(tab,pos_empty)
    moves_draw_sim = ()
    
    for position in pos_empty:
        tab_sim = marca_posicao(tab,position,jog)

        ## GAME SIMULATION
        while not eh_fim_jogo(tab_sim, k):
            ## OUTRO JOGADOR EM 1 LUGAR
            tab_sim = marca_posicao(tab_sim, escolhe_posicao_auto(tab_sim, -jog, k, 'normal'), -jog)
            ## CHECKUP
            if eh_fim_jogo(tab_sim, k):
                break
            ## BOT EM 2 LUGAR
            tab_sim = marca_posicao(tab_sim, escolhe_posicao_auto(tab_sim, jog, k, 'normal'), jog)
        
        ## SIMULATION WINNER
        result_sim = eh_vencedor(tab_sim, k)

        if result_sim == jog:
            return position
        elif result_sim == 0:
            moves_draw_sim += (position,)
        
    if moves_draw_sim != ():
        return moves_draw_sim[0]
    return pos_empty[0]



def escolhe_posicao_auto(tab,jog,k,lvl):
    """
    Summary : escolhe_posicao_auto {tuple,int,int,int} --> {int}
    Chooses a position based on the difficulty.
    

    Arguments : 
        tab : (tuple) : Represents the board.
            Tuple of tuples.
            Has between 2 and 100 lines.
            Each line has between 2 and 100 columns.
            Every line must be of the same size.
            Every entry must be 1, 0 or -1.
        
        pos : (int) : Represents a position.
            Greater or equal to 1
            Less or equal to 10000
        
        jog : (int) : Represents the player.
            Must be 1 or -1.

        k : (int) : Represents a k-in-a-row value.
            Greater or equal to 1
        
    Returns : int : pos
        To return 'pos' this condition must be met : 
            'tab' is a valid board AND 'jog' is a valid player AND 'k' is a valid k-value AND 'lvl' is a valid level AND the game is not finished.
        
        pos : Position chosen by the bot of the difficulty chosen by the user.

    
    Raises:
        ValueError :'tab' is NOT a valid board
                    'jog' is NOT a valid player
                    'k' is NOT a valid k-value
                    'lvl' is a valid level
                    The game is finished.
    """
    if not eh_tabuleiro(tab) or not eh_jogador(jog) or not eh_k(k) or not eh_nivel(lvl) or eh_fim_jogo(tab,k):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    
    if lvl == 'facil': ## Play bot_facil
        return estrategia_facil(tab,jog)
        
    elif lvl == 'normal': ## Play bot_normal
        return estrategia_normal(tab,jog,k)
        
    else: ## Play bot_dificil
        return estrategia_dificil(tab,jog,k)



def eh_cfg(cfg):
    """
    Summary : eh_cfg {tuple} --> {bool}
    Identifies if 'cfg' is a valid MNK Game configuration.

    
    Arguments : 
        cfg : (tuple) : Represents the MNK Game config.
            Tuple with 3 entries that
            represent, in order, M,N,K

    Returns : bool
        True : If type(cfg)==tuple AND len(cfg)==3 AND type(m)==int AND type(n)==int AND 2 <= m,n <= 100 AND k is a valid k-value
        False : If AT LEAST ONE of the conditions above are NOT met.
        

    Raises:
        Nothing
    """    
    if type(cfg)==tuple and len(cfg)==3:
        m = cfg[0]
        n = cfg[1]
        k = cfg[2]

        return type(m)==int and 2 <= m <= 100 and type(n)==int and 2 <= n <= 100 and eh_k(k) ## Same conditions as eh_tabuleiro(tab) and eh_k(k)
    return False


def criar_tabuleiro(cfg):
    """
    Summary : criar_tabuleiro {tuple} --> {tuple}
    Creates a board based on the 'cfg' configuration.
    Must only be called is 'cfg' is a valid configuration.

    
    Arguments : 
        cfg : (tuple) : Represents the MNK Game config.
            Tuple with 3 entries that
            represent, in order, M,N,K

    Returns : tuple : tab
        tab : Tuple of tuples, every entry is 0. Is a valid board.
        
    
    Raises:
        Nothing
    """  
    m = cfg[0]
    n = cfg[1]
    tab = ()
    linha = ()
    for colunas in range(n):
        linha += (0,)
    for linhas in range(m):
        tab += (linha,)
    
    return tab




def jogo_mnk(cfg,jog,lvl):
    """
    Summary : jogo_mnk {tuple,int,int} --> {int}
    Main function, executes the game against a bot.
    The player that has 'jog'==1 always starts.

    
    Arguments : 
        cfg : (tuple) : Represents the MNK Game config.
            Tuple with 3 entries that
            represent, in order, M,N,K
        
        jog : (int) : Represents the player.
            Must be 1 or -1.
        
        lvl : (string) : Represents the difficulty.
            Must be 'facil', 'normal' or 'dificil'.
        

    Returns : int : 1,0,-1
         1 : If the player 1 has won.
        -1 : If the player -1 has won.
         0 : If it is a draw.
        
        
    Raises:
        ValueError : 'cfg' is NOT a valid configuration OR 'jog' is NOT a valid player OR 'lvl' is NOT a valid difficulty.
    """  
    if not eh_cfg(cfg) or not eh_jogador(jog) or not eh_nivel(lvl):
        raise ValueError('jogo_mnk: argumentos invalidos')
    
    ## Variables
    tab = criar_tabuleiro(cfg)
    k = cfg[2]
    lvl_symbol = '('+lvl+'):'
    if jog == 1:
        player_symbol = "'X'."
    else:
        player_symbol = "'O'."
    
    ## Prints
    print('Bem-vindo ao JOGO MNK.')
    print('O jogador joga com', player_symbol)
    print(tabuleiro_para_str(tab))
   
    ## PLAYER 1 ALWAYS STARTS
    if jog == 1:
        while not eh_fim_jogo(tab,k):        
            ## PLAYER TURN
            tab = marca_posicao(tab, escolhe_posicao_manual(tab), jog)
            print(tabuleiro_para_str(tab))
            
            ## CHECKUP if the game has ended
            if eh_fim_jogo(tab,k):
                break
                
            ## BOT TURN 
            print('Turno do computador',lvl_symbol)
            tab = marca_posicao(tab, escolhe_posicao_auto(tab, -jog, k, lvl), -jog)
            print(tabuleiro_para_str(tab))
        
    else:
        while not eh_fim_jogo(tab,k):
            ## BOT TURN
            print('Turno do computador',lvl_symbol)
            tab = marca_posicao(tab,escolhe_posicao_auto(tab, -jog, k, lvl), -jog)
            print(tabuleiro_para_str(tab))
            
            ## CHECKUP if the game has ended
            if eh_fim_jogo(tab,k):
                break

            ## PLAYER TURN 
            tab = marca_posicao(tab,escolhe_posicao_manual(tab), jog)
            print(tabuleiro_para_str(tab))
        
    
    game_result = eh_vencedor(tab,k)
    if game_result == jog:
        print('VITORIA')
        return jog

    elif game_result == -jog:
        print('DERROTA')
        return -jog
    
    print('EMPATE')
    return 0

