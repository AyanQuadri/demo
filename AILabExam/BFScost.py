def best_first_search(actual_Src, target, n):
    visited = [False for i in range(n)]
    pq = PriorityQueue()
    pq.put((0, actual_Src)) 
    visited[actual_Src] = True
    while pq.empty() == False:
        u = pq.get()[1]
        output.append(u)
        if u == target:
            break
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                parent[v] = u
                pq.put((c, v))

def cost_path(path):
    cost = 0
    for i in range(len(path)):
        for j, c in graph[path[i]]:
            if (i+1 < len(path)) and path[i+1] == j:
                cost += c
    print("The cost of the path is: ", cost)

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

from queue import PriorityQueue
v = 12
graph = [[] for i in range(v)]
output = []
parent = {}

for node in range(len(graph)): 
    parent[node] = None

addedge(0, 1, 2)
addedge(0, 2, 5)
addedge(0, 3, 15)
addedge(1, 4, 6)
addedge(2, 6, 1)
addedge(2, 7, 3)
addedge(2, 5, 7)
addedge(3, 8, 4)
addedge(3, 9, 8)
addedge(4, 10, 12)
addedge(4, 11, 10)

source = 0
target = 7

best_first_search(source, target, v)

print('Output: ', output)
path = []
next = output[len(output)-1]

while next != output[0]:
    path.append(next)
    next = parent[next]

path.append(output[0])
path.reverse()
print('Path: ', path)

cost_path(path)