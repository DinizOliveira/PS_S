def verificaAlternado(string_formatada, string1, string2):
    """
    Verifica se os caracteres estão alternando na string formatada
    """
    cond = False
    contador = 0
    if len(string1 + string2) < 4:
        return cond

    if (string1.count(string1[0]) == len(string1)) and (string2.count(string2[0]) == len(string2)):
        if len(string1) < len(string2):
            maior = len(string2)
            string1 = string1 + ' '
        else:
            maior = len(string1)
            string2 = string2 + ' '

        for x in range(maior):
            
            if (string_formatada[contador] == string1[x]) and (string_formatada[contador] and (string2[x] or ' ')):
                cond = True
            else:
                return False
            contador += 2
    else:
        return False
    return cond


def excluiCaracter(string, caracter, lista_caracteres):
    """
    Exclui um caracter quando recebe uma string principal que contém até 3 caracteres únicos
    """
    temp = lista_caracteres[caracter]
    string = string.replace(temp, '')
    return string
    

def excluiCaracteres(string, caracter_1, caracter_2, lista_caracteres):
    """
    Exclui dois caracteres quando recebe uma string principal que contém até 4 caracteres únicos
    """
    primeiro_caracter = lista_caracteres[caracter_1]
    segundo_caracter = lista_caracteres[caracter_2]
    string = string.replace(primeiro_caracter, '')
    string = string.replace(segundo_caracter, '')
    return string


def divideString(string):
    """
    Divide a string principal em duas sub strings 
    A primeira com os indices 0,2,4,6,8...
    E a segunda com os indices 1,3,5,7...
    """
    return string[::2], string[1::2]


def listaCaracteres(string):
    """
    Cria uma lista com tipos únicos de caracteres da string principal
    """
    caracteres = []
    for x in range(len(string)):
        if string[x] not in caracteres:
            caracteres.append(string[x])
    return caracteres
