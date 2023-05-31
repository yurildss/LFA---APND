import time
import matplotlib.pyplot as plt

class Estado:
    numero = 0
    inicial = False
    final = False
    lido = False
    estado_atual = 0
    palavra_lida = ''
    a = []
    b = []
    c = []
    d = []
    e = []

estados = ['0', '1']
alfabeto = ['a', 'b']
alfabeto_pilha = ['A']
n_transicoes = 3
transicoes = [['0', 'a', '*', '0', 'A'],
              ['0', '*', '*', '1', '*'],
              ['1', 'b', 'A', '1', '*']]
estado_inicial = 0
estados_finais = ['1']
palavras_teste = ['ab', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']

fila_estados = []
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
            fila_estados[j].a.append(transicoes[i][0])
            fila_estados[j].b.append(transicoes[i][1])
            fila_estados[j].c.append(transicoes[i][2])
            fila_estados[j].d.append(transicoes[i][3])
            fila_estados[j].e.append(transicoes[i][4])

tempos_execucao = []
tamanhos_palavras = []

for palavra in palavras_teste:
    start_time = time.time()

    flag = False
    pilha = []

    while len(palavra) > 0:
        for i in range(0, len(fila_estados)):
            if fila_estados[i].inicial == True and fila_estados[i].lido == False:
                estado_inicial = fila_estados[i]

        if palavra[0] in estado_inicial.b:
            index = estado_inicial.b.index(palavra[0])
            palavra = palavra[1:]

            if estado_inicial.e[index] != "*":
                pilha.append(estado_inicial.e[index])

            if estado_inicial.c[index] != "*" and len(pilha) > 0:
                if estado_inicial.c[index] in pilha:
                    pilha.remove(estado_inicial.c[index])
                else:
                    print('N')
                    break
            elif estado_inicial.c[index] != "*" and len(pilha) == 0:
                print('N')
                break

            proximo_estado_index = estado_inicial.d[index]
            for i in range(0, len(fila_estados)):
                if fila_estados[i].numero == proximo_estado_index:
                    proximo_estado = fila_estados[i]

            if proximo_estado.final == True and len(pilha) == 0 and palavra == '':
                print('S')
                break
            elif palavra == '' and proximo_estado.final == False:
                print('N')
                break
            elif palavra == '' and len(pilha) != 0:
                print('N')
                break

            proximo_estado2 = None

            if palavra[0] not in estado_inicial.b and '*' in estado_inicial.b:
                for i in range(0, len(estado_inicial.a)):
                    if estado_inicial.b[i] == "*":
                        proximo_estado2 = estado_inicial.d[i]
                for i in range(0, len(fila_estados)):
                    if fila_estados[i].numero == proximo_estado2:
                        proximo_estado2 = fila_estados[i]
                        estado_inicial.lido = True
            else:
                estado_inicial.lido = True
                estado_inicial = proximo_estado

        else:
            print('N')
            break

        if proximo_estado2 is not None:
            estado_inicial = proximo_estado2

    end_time = time.time()
    tempo_execucao = end_time - start_time
    tempos_execucao.append(tempo_execucao)
    tamanhos_palavras.append(len(palavra))

plt.plot(tamanhos_palavras, tempos_execucao, 'o-')
plt.xlabel('Tamanho da Palavra')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução em Função do Tamanho da Palavra')
plt.show()
