NOME = input("\nINFORME O NOME A SER DESCOBERTO(EX: OBJETO, PESSOAS,ANIMAIS...): \n")
DICA = input("\nDÊ UMA DICA: \n")
CONTROLADOR_TENT = int(input("\nINFORME A QUANTIDADE DE TENTATIVAS QUE O USUARIO TERÁ PARA ENCONTRAR AS PALAVRA: \n"))
TENTATIVAS_RESTANTES = 0
LETRAACERTADA = ''
TENTATIVAS = 0
TODAS_AS_LETRAS_INSERIDAS = ''
while True:
    print(F'DICA:{DICA} ')
    LETRAINSERIDA = input("DIGITE UMA LETRA:\n")
    TENTATIVAS +=1
    TENTATIVAS_RESTANTES = CONTROLADOR_TENT - TENTATIVAS
    print(F'\nQUANTIDADE DE TENTATIVAS: {TENTATIVAS}\n')
    print("---------------------------------------------")
    print(F'TENTATIVAS RESTANTES: {TENTATIVAS_RESTANTES}\n')
    if len(LETRAINSERIDA) > 1:
        print("INFORME APENAS UMA LETRA!")
        continue
    if LETRAINSERIDA!= '':
        TODAS_AS_LETRAS_INSERIDAS+=LETRAINSERIDA
        print(F'TODAS AS LETRAS INSERIDAS:[{TODAS_AS_LETRAS_INSERIDAS}]\n')
    if TENTATIVAS <=CONTROLADOR_TENT:
        if LETRAINSERIDA in NOME:
            LETRAACERTADA += LETRAINSERIDA
        PALAVRA_FORMADA=''
        for I in NOME:
            if I in LETRAACERTADA:
                PALAVRA_FORMADA+=I
        if PALAVRA_FORMADA == NOME:
            print(F"PARABENS!! VOCE ACERTOU A PALAVRA [{NOME}]")
            break
        
        print(F'LETRAS QUE POSSUEM NO NOME \n|{PALAVRA_FORMADA}|')
        print("---------------------------------------------")
    else:
        print("LIMITE DE TENTATIVAS ATINGIDAS!")
        break
   