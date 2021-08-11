def encontraSubString(K, N):
 
    len1 = len(K)
    len2 = len(N)
    caracteres = 256

    if len1 < len2:
 
        print("\033[1;31mString inválida\033[m")
        return ""
 
    hash_N = [0] * caracteres
    hash_K = [0] * caracteres
 
    for i in range(0, len2):
        hash_N[ord(N[i])] += 1
 
    start, start_index, min_len = 0, -1, float('inf')
 
    #conta o número de caracteres
    count = 0            
    for j in range(0, len1):
 
        #conta os caracteres da string
        hash_K[ord(K[j])] += 1
 
        if (hash_K[ord(K[j])] <= hash_N[ord(K[j])]):
            count += 1

        if count == len2:
 
            while (hash_K[ord(K[start])] > hash_N[ord(K[start])] or hash_K[ord(K[start])] == 0):
 
                if (hash_K[ord(K[start])] > hash_N[ord(K[start])]):
                    hash_K[ord(K[start])] -= 1
                start += 1
 
            len_window = j - start + 1

            if min_len > len_window:
 
                min_len = len_window
                start_index = start
    
    if start_index == -1:
        print("\033[1;31mNão existe subString válida nesta string\033[m")
        return ""
 
    #retorna a menor subString
    return K[start_index: start_index + min_len]
 