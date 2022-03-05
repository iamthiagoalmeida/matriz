# Matriz de Adjacência

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for i in range(self.vertices)]

    def add_arest(self, x, y):
        self.graph[x-1][y-1] = 1 # Usar += caso seja grafo múltiplo.

        #self.graph[y-1][x-1] = 1 (Caso seja grafo não direcionado).

    def show_matriz(self):
        print('A matriz de adjacência é:')
        for i in range(self.vertices):
            print(self.graph[i])

x = int(input('Qual a quantidade de vértices?'))
g = Graph(x)

a = int(input('Qual a quantidade de arestas?'))
for i in range(a):
    x = int(input('Qual o ponto de origem?'))
    y = int(input('Qual o ponto de destino?'))
    g.add_arest(x,y)

g.show_matriz()