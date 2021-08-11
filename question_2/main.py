from lib.functions import encontraSubString

if __name__ == "__main__":
 
    opcao = input('Digite a string K ou digite 1 para opção: "ahffaksfajeeubsne", ou digite 2 para opção: "aaffhkksemckelloe" ')
    if opcao == '1':
        K = "ahffaksfajeeubsne"
        N = 'jefaa'
    elif opcao == '2':
        K = "aaffhkksemckelloe"
        N = 'fhea'
    else:
        K = opcao
        N = input('Digite a subString N: ')
    print('A menor subString encontrada foi: ')
    print(f'\033[1;32m{encontraSubString(K, N)}\033[m')
 