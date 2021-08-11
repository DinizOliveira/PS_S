from lib.functions import *
     
#verifica se a string possui menos de um tipo de caracter
while True:
    opcao = input('Digite uma string ou digite "1" para a string exemplo:[abaacdabd] ').lower()
    string = ''
    if opcao == '1':
        string = 'abaacdabd'
        break
    else:
        string = opcao
        break

print(f'\nA string digitada foi: \033[1;32m{string}\033[m')   

#Função que lista caracteres únicos na string (máximo: 4 caracteres diferentes)   
caracteres = listaCaracteres(string) 

#Variável auxiliar para guardar o maior valor da string
aux = '' 

#Verifica se a string possui apenas um tipo de caractere, ou se está vazia
if len(caracteres) <=1:
    print('\033[1;31m0')
    print('String Inválida\033[m')
    exit()


#Verifica a string que possui dois tipos de caracteres
elif len(caracteres) == 2:
    string1, string2 = divideString(string)

    if verificaAlternado(string, string1, string2) is True:
        aux = string
    else:
        print('\033[1;31mString Inválida\033[m')
        exit()
        

#Verifica a string que possui três tipos de caracteres    
if len(caracteres) == 3:
    x=0

    while x < (len(caracteres)):
        string_formatada = excluiCaracter(string, x, caracteres)
        string1, string2 = divideString(string_formatada)
        alternado = verificaAlternado(string_formatada, string1, string2)

        if (alternado == True) and (len(aux) < len(string_formatada)):
            aux = string_formatada
        x +=1
            

#verifica a string que possui quatro tipos de caracteres
if len(caracteres) == 4:
    x = cont = 0

    while cont < len(caracteres):
        x = cont +1

        while x < len(caracteres):
            string_formatada = excluiCaracteres(string, cont, x, caracteres) 
            string1, string2 = divideString(string_formatada) 
            alternado = verificaAlternado(string_formatada, string1, string2)

            if (alternado == True) and (len(aux) < len(string_formatada)):
                aux = string_formatada
            x += 1
        cont += 1

if aux is None:
    print('\033[1;31m0 - Padrão não encrontrado\033[m')
else:
    print(f'O comprimento da strig válida é: {len(aux)} \nA string válida é: \033[1;32m{aux}\033[m\n')
