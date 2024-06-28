import random

def matriz():
    lin = int(input("\n  insira a qtd de linhas da matriz:"))
    col = int(input("\n  insira a qtd de colunas da matriz:"))

    if lin > 0 and col > 0:
        Matriz = []  #inicializa uma matriz vazia
        for i in range(lin):   #passa pelas linhas a serem criadas
            Linha = []
            for j in range(col):  #passa pela colunas
                num = random.randint(0, 50)  #o comando randint gera valores aleatórios INTEIROS(do grupo dos inteiros){rand(random) int(inteiro)}
                Linha.append(num)   #adiciona o número na linha, já que a amatriz é lida como uma lista 
            Matriz.append(Linha)       #adiciona os valores da linha na matriz, a matriz é uma lista de listas
    return Matriz


def multimatriz(matrizA, matrizB):
    linha = len(matrizA)  #a quantidade de linha se dá no tamanho da lista matriz
    coluna = len(matrizB[0])  #a quantidade de linha se dá no tamanho do tamanho do primeiro elemento 
    linhaA = len(matrizA[0])   #como é uma lista de listas, o primeiro elemento da lista matriz é a primeira lista linha
    MatrizC = [[0 for _ in range(coluna)] for _ in range(linha)] #quando eu apenas inicializei uma lista vazia de error, desse jeito já se cria uma lista do tamanho desejados, com todos os valores 0
    for i in range(linha):
        for j in range(coluna):
            for k in range(linhaA):
                MatrizC[i][j] = MatrizC[i][j]+ matrizA[i][k] * matrizB[k][j]   #aqui é onde se calcula o valor, juntamente com o "for k...""
    return MatrizC

A = matriz()
B = matriz()

print("Matriz A:\n",A)
print("Matriz B:\n",B)
C = multimatriz(A, B)
print("Matriz C:\n",C)

