def dfs(u):
    if not visited[u]:
        visited[u] = True
        output.append(u)
        for v in adj_list[u]:
            dfs(v)

adj_list = {
    '0': ['1', '3', '8'],
    '1': ['0', '7'],
    '2': ['7', '3', '5'],
    '3': ['0', '2', '4'],
    '4': ['3', '8'],
    '5': ['6', '2'],
    '6': ['5'],
    '7': ['2', '1'],
    '8': ['0', '4']
}

visited = {}
output = []

for node in adj_list.keys():
    visited[node] = False

dfs("0")
print('The DFS for the given adj_list is :', output)
