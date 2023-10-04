# AIM:- Implement the DFS algorithm and analyze its performance and characteristics.

# Graph represented using adjacency list
graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
 'F': [] }
visited = set() # To keep track of visited nodes
def dfs(node):
 if node not in visited:
  print(node, end=' ')
 visited.add(node)
 for neighbor in graph[node]:
  dfs(neighbor)
# Starting DFS from node 'A'
dfs('A')
def dfs(graph, start, visited=None):
 if visited is None:
  visited = set()
 visited.add(start)
 print(start)
 for next in graph[start] - visited:
  dfs(graph, next, visited)
 return visited
graph = {'0': set(['1', '2']),
 '1': set(['0', '3', '4']),
 '2': set(['0']),
 '3': set(['1']),
 '4': set(['2', '3'])}
dfs(graph, '0')
