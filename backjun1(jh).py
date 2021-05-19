from itertools import combinations


def virus(graph, x, y):
    if x < 0 or y < 0 or x >= N or y >= M or graph[x][y] == 1:
        return

    if graph[x][y] == 0:
        graph[x][y] = 2  # virus
        virus(graph, x-1, y)    # left
        virus(graph, x, y-1)    # up
        virus(graph, x+1, y)    # right
        virus(graph, x, y+1)    # down


N, M = map(int, input().split())
graph = []

for _ in range(M):
    graph.append(list(map(int, input().split())))


# print(graph)

isblank = []
isvirus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            isblank.append((i, j))
        elif graph[i][j] == 2:
            isvirus.append((i, j))

result = 0
for walls in list(combinations(isblank, 3)):
    # for walls in [((1, 0), (0, 1), (3, 5))]:
    test_graph = graph.copy()

    for wall in walls:
        i, j = wall
        test_graph[i][j] = 1

    for v in isvirus:
        x, y = v
        test_graph[x][y] = 0
        virus(test_graph, x, y)

    # print(test_graph)
    count0 = 0
    for rows in test_graph:
        count0 += rows.count(0)

    result = max(result, count0)
    print(result)