import heapq
from collections import defaultdict, deque

# Priority Queue using Binary Heap
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0

# Topological Sorting using DFS
def topological_sort(graph):
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Queue for nodes with no incoming edges
    queue = deque([u for u in graph if in_degree[u] == 0])
    sorted_list = []

    while queue:
        u = queue.popleft()
        sorted_list.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(sorted_list) != len(graph):
        raise ValueError("Graph is not a DAG, topological sort not possible.")
    
    return sorted_list

# Example Usage
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
pq = PriorityQueue()
pq.push('Task1', 1)
pq.push('Task2', 2)

print("Priority Queue:")
while not pq.is_empty():
    print(pq.pop())

print("\nTopological Sorting:")
print(topological_sort(graph))
