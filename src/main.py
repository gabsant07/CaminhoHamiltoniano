def hamiltonian_path(graph, path, visited, n):

    if len(path) == n:
        return True

    current = path[-1]

    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)

            if hamiltonian_path(graph, path, visited, n):
                return True

            # backtrack
            visited[neighbor] = False
            path.pop()

    return False


def find_hamiltonian_path(graph):
    n = len(graph)
    for start in range(n):
        visited = [False] * n
        path = [start]
        visited[start] = True

        if hamiltonian_path(graph, path, visited, n):
            return path

    return None


def main():

    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }

    result = find_hamiltonian_path(graph)

    if result:
        print("Caminho Hamiltoniano encontrado:")
        print(result)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")


if name == "main":
    main()