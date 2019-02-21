
def merge(lista1,lista2):
    print( 'teste' )

    i1 = 0
    i2 = 0
    listaResposta = []
    tamL1 = len(lista1)
    tamL2 = len(lista2)

    while i1 < tamL1 and i2 < tamL2:
        
        if lista1[i1] < lista2[i2]:
            # listaResposta.append(lista1[i1])
            i1 = i1 + 1
            
            for intem in listaResposta:

                if lista1[i1] == intem:
                    listaResposta.append(lista1[i1])
                    # i1 = i1 + 1

        else:
            listaResposta.append(lista2[i2])
            i2 = i2 + 1
    
    while i1 < tamL1:
        listaResposta.append(lista1[i1])
        i1+=1

    # while i2 < tamL2:
    #     listaResposta.append(lista2[i2])
    #     i2+=1
    
    return listaResposta

print( merge([5, 6, 10], [2, 4, 5, 9]) )
# [2, 4, 5, 5, 6, 9]