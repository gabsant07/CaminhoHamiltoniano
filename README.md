# CaminhoHamiltoniano
Este projeto tem como objetivo implementar um algoritmo em Python para encontrar um **Caminho Hamiltoniano** em um grafo (orientado ou não orientado). O Caminho Hamiltoniano é uma sequência de vértices que visita cada vértice do grafo **exatamente uma vez**.

## Descrição do Projeto (passo a passo)

### Função recursiva que tenta construir um caminho Hamiltoniano a partir de um vértice inicial

def hamiltonian_path(graph, path, visited, n):

### Se o comprimento do caminho for igual ao número total de vértices, encontramos um caminho Hamiltoniano

if len(path) == n:
        return True

### Pega o último vértice adicionado ao caminho

current = path[-1]

### Itera sobre os vizinhos do vértice atual

for neighbor in graph[current]:

### Se o vizinho ainda não foi visitado, marca como visitado e adiciona ao caminho

if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)

### Faz chamada recursiva com o novo caminho

if hamiltonian_path(graph, path, visited, n):
                return True

### Caso a chamada recursiva falhe, desfaz a escolha anterior (backtracking)

visited[neighbor] = False
            path.pop()

### Função que inicia o processo tentando encontrar o caminho a partir de cada vértice do grafo

def find_hamiltonian_path(graph):

### Testa todas as possibilidades de vértice inicial

for start in range(n):

### Função principal. Define o grafo e imprime o resultado

def main():

## Como executar o projeto

### 1. Ter o Python instalado na máquina

### 2. Clone o repositório
git clone [https://github.com/](https://github.com/gabsant07/CaminhoHamiltoniano)

### 3. Execute o código
python main.py

## Relatório técnico

### Análise da Complexidade Computacional
O problema do Caminho Hamiltoniano pertence à classe dos problemas NP-Completos, pois um problema está em NP se uma solução proposta pode ser verificada em tempo polinomial. No caso do Caminho Hamiltoniano, dado um caminho, é possível verificar que ele visita todos os vértices exatamente uma vez. Além disso, como o Caminho Hamiltoniano é ao mesmo tempo NP e NP-Hard, ele é considerado NP-Completo. 

Em relação ao Problema do Caixeiro Viajante, o TSP busca o menor ciclo Hamiltoniano ponderado, enquanto o Caminho Hamiltoniano busca qualquer caminho que passe por todos os vértices. Ambos são difíceis de resolver, pois envolvem a verificação de um número exponencial de combinações possíveis de vértices.

### Análise da Complexidade Assintótica de Tempo
A complexidade temporal do algoritmo é O(n!), onde n é o número de vértices do grafo.

Foi possível chegar a esse resultado, uma vez que o algoritmo tenta construir todos os caminhos possíveis a partir de cada vértice e, a cada etapa, ele tenta escolher um próximo vértice entre os que ainda não foram visitados. Além disso, como há n escolhas iniciais e até (n-1)! permutações possíveis dos vértices seguintes, temos complexidade de ordem fatorial.

### Aplicação do Teorema Mestre
Não é possível aplicar o Teorema Mestre nesse caso, pois só é aplicável a algoritmos recursivos que seguem o padrão

T(n) = aT(n/b) + f(n)

Onde a>= 1, b > 1 e f(n) é função polinomial.

O algoritmo do Caminho Hamiltoniano não possui esse formato de recorrência, pois a recursão não divide o problema em subproblemas menores com proporção fixa. Em vez disso, ele gera uma árvore de possibilidades baseada em permutações, característica típica de problemas combinatórios e não estruturados para o Teorema Mestre.

### Análise dos casos de complexidade
1. Pior caso: Nenhum caminho Hamiltoniano é encontrado. O algoritmo tenta todas as possibilidades.
Complexidade: O(n!).

Caso médio: Encontra um caminho após explorar uma fração das possibilidades.
Complexidade: Menor que O(n!), mas ainda exponencial.

Melhor caso: O primeiro caminho testado já é Hamiltoniano.
Complexidade: O(n).

2. No melhor caso, o desempenho é muito bom e rápido.

No pior caso, o tempo explode exponencialmente, tornando o algoritmo impraticável para grafos com muitos vértices.

O algoritmo é viável apenas para grafos pequenos (até cerca de 10 vértices).
