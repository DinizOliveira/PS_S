from lib.functions import treeConstructor

if __name__ == "__main__":
    pais = []
    filhos = []
    princ = []
    temp = []

    while True:
        temp.append(input('Digite o primeiro valor: '))
        temp.append(input('Digite o segundo valor: '))
        princ.append(temp[:])
        temp.clear()
        resp = input('Deseja continuar? [S/N] ')
        if resp in 'Nn':
            break

    for i in range (len(princ)):
        pais.append(princ[i][1])
        filhos.append(princ[i][0])

    print(treeConstructor(pais, filhos))
