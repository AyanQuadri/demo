from queue import Queue
adj_list = {
        '1': ['2', '3'],
        '2': ['1', '5'],
        '3': ['1', '8', '4'],
        '4': ['7', '5', '3'],
        '5': ['4', '2'],
        '6': ['7', '10', '13'],
        '7': ['4', '6', '8', '9'],
        '8': ['3', '7', '9'],
        '9': ['8', '7', '11'],
        '10': ['11', '6', '12'],
        '11': ['10', '12', '9'],
        '12': ['10', '13', '11'],
        '13': ['6', '12']
    }
visited = {}
output = []
q = Queue()

for node in adj_list.keys():
    visited[node] = False

s = '1'
visited[s] = True
q.put(s)

while not q.empty():
    u = q.get()
    output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            q.put(v)

print('The BFS for the given adj_list is :',output)