#transicao <a,b,c,d,e>
#<estado de origem, caractere lido, simbolo a ser desempilhado, estado de destinho, palavra a ser empilhada>
#1. Leitura e entrada na entrada/saída padrão.
#2. Qualquer divergência da saída com o formato especificado implicará em nota zero.
#3. A implementação não pode fazer uso de recursão.
#4. Critério de reconhecimento: pilha vazia e estado final.
class Estado:
        numero = 0 #numero do estado
        inicial = False #se o estado é inicial
        final = False #se o estado é final
        lido = False #se o estado já foi lido
        estado_atual = 0 #estado atual
        palavra_lida = '' #palavra que foi lida pelo estado
        #membros da tupla
        a = []
        b = []
        c = []
        d = []
        e = []

fila_transicoes = []
# Lê a entrada
estados = input().split()
alfabeto = input().split()
alfabeto_pilha = input().split()
n_transicoes = int(input())
transicoes = [input("").split() for _ in range(n_transicoes)]
estado_inicial = int(input())
estados_finais = input().split()
palavras_teste = input().split()

fila_estados = [] #onde os objetos Estados estao sendo armazenados
for i in estados:
    estado = Estado()
    estado.numero = estados[int(i) - 1]
    estado.a = []
    estado.b = []
    estado.c = []
    estado.d = []
    estado.e = []
    fila_estados.append(estado)

for i in range(0, len(fila_estados)):
    if estado_inicial == int(fila_estados[i].numero):
        fila_estados[i].inicial = True

for i in range(0, len(estados_finais)):
    for j in range(0, len(fila_estados)):
        if int(estados_finais[i]) == int(fila_estados[j].numero):
            fila_estados[j].final = True

for i in range(0, len(transicoes)):
    for j in range(0, len(fila_estados)):
        if fila_estados[j].numero == transicoes[i][0]:
            fila_estados[j].a.append( transicoes[i][0] ) # estado de origem
            fila_estados[j].b.append( transicoes[i][1] ) # caractere lido
            fila_estados[j].c.append( transicoes[i][2] ) # simbolo a ser desempilhado
            fila_estados[j].d.append( transicoes[i][3] ) # estado de destinho
            fila_estados[j].e.append(transicoes[i][4] ) # palavra a ser empilhada

flag = False
pilha = []
novaPalavra = False
#enquanto tiver palavra para testar
while len(palavras_teste) > 0:
    #pegamos a primeira palavra
    palavra = palavras_teste[0]
    novaPalavra = True
    #enquanto a palavra que estamos testando nao terminar
    while len(palavra) > 0:
        for i in range(0, len(fila_estados)):
            if (fila_estados[i].inicial == True and fila_estados[i].lido == False):
                #encontramos o estado inicial
                estado_inicial = fila_estados[i]
            if (fila_estados[i].inicial == True and novaPalavra == True and fila_estados[i].lido == True):
                #encontramos o estado inicial
                estado_inicial = fila_estados[i]
        if(palavra == "*" and estado_inicial.final == True and len(pilha) == 0):
            print('S')
            palavras_teste = palavras_teste[1:]
            novaPalavra = True
            break
        #comparaos o primeiro caractere da palavra ao caracter lido do estado inicial
        if(palavra[0] in estado_inicial.b):
            #indice do caractere
            index = estado_inicial.b.index(palavra[0])
            # Removendo o primeiro caractere
            palavra = palavra[1:]
            novaPalavra = False
            #empilhar o caractere se o caractere a ser empilhado nao for o nulo
            if (estado_inicial.e[index] != "*"):
                pilha.append(estado_inicial.e[index])
            #desempilhar o caractere se o caractere a ser desempilhado nao for nulo
            if (estado_inicial.c[index] != "*" and len(pilha) > 0):
                if(estado_inicial.c[index] in pilha):
                    pilha.remove(estado_inicial.c[index])
                else:
                    print('N')
                    palavras_teste = palavras_teste[1:]
                    novaPalavra = True
                    break
            elif (estado_inicial.c[index] != "*" and len(pilha) == 0):
                print('N')
                palavras_teste = palavras_teste[1:]
                novaPalavra = True
                break
            # descobre para qual estado iremos
            proximo_estado_index = estado_inicial.d[index]
            for i in range(0, len(fila_estados)):
                if(fila_estados[i].numero == proximo_estado_index):
                    proximo_estado = fila_estados[i]
            if(proximo_estado.final == True and len(pilha) == 0 and palavra == ''):
                print('S')
                palavras_teste = palavras_teste[1:]
                novaPalavra = True
                break
            elif(palavra == '' and proximo_estado.final == False):
                print('N')
                palavras_teste = palavras_teste[1:]
                novaPalavra = True
                break
            elif (palavra == '' and len(pilha) != 0):
                print('N')
                palavras_teste = palavras_teste[1:]
                novaPalavra = True
                break
            proximo_estado2 = None
            #trabalhando agora com transição vazia no estado inicial
            #se o caractere lido não estiver mais sendo aceito
            if (palavra[0] not in estado_inicial.b and '*' in estado_inicial.b):
                #e se tivermos uma transição onde se ler nada e vai para algum estado
                for i in range(0, len(estado_inicial.a)):
                    #se o numero do estado atual for igual ao numero x em a:
                    if(estado_inicial.b[i] == "*"):
                        proximo_estado2 = estado_inicial.d[i]
                for i in range(0, len(fila_estados)):
                    if(fila_estados[i].numero == proximo_estado2):
                        proximo_estado2 = fila_estados[i]
                        estado_inicial.lido = True
            else:
                estado_inicial.lido = True
                estado_inicial = proximo_estado
        else:
            print('N')
            palavras_teste = palavras_teste[1:]
            novaPalavra = True
            break
        if(proximo_estado2 is not None):
            estado_inicial = proximo_estado2
