def treeConstructor(pais, filhos):
    """
    Valida a árvore binária
    """
    for i in range (len(pais)):             #Se um nó pai tiver mais de dois filhos, a árvore é considerada inválida
        if pais.count(pais[i]) > 2:
            return '\033[1;31mÁrvore binária inválida\033[m'

    for i in range (len(filhos)):           #Se um nó filho tiver mais de um pai, a árvore é considerada inválida
        if filhos.count(filhos[i]) > 1:
            return '\033[1;31mÁrvore binária inválida\033[m'
        else:
            return '\033[1;32mÁrvore binária válida\033[m'  
