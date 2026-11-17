import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph}
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, predecessors

def get_shortest_path(predecessors, start, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path

if __name__ == "__main__":
    # Graph representation based on Figure 1 connections and edge weights
    graph = {
        'A': {'D': 4},
        'B': {'D': 8, 'C': 2},
        'C': {'B': 2, 'E': 5, 'J': 10},
        'D': {'A': 4, 'B': 8, 'F': 6, 'G': 3, 'H': 9, 'K': 6},
        'E': {'C': 5, 'H': 4, 'I': 9, 'J': 2},
        'F': {'D': 6, 'G': 1, 'K': 7},
        'G': {'D': 3, 'F': 1, 'K': 4},
        'H': {'D': 9, 'E': 4, 'I': 3, 'K': 6},
        'E_node': {'H': 4, 'I': 7, 'J': 7}, # placeholder check for node I connections
        'I': {'E': 9, 'H': 3, 'J': 7},
        'J': {'C': 10, 'E': 2, 'I': 7, 'L': 1},
        'K': {'D': 6, 'F': 7, 'G': 4, 'H': 6},
        'L': {'J': 1}
    }
    
    start_vertex = 'A'
    target_vertex = 'L'
    
    distances, predecessors = dijkstra(graph, start_vertex)
    path = get_shortest_path(predecessors, start_vertex, target_vertex)
    
    print(f"--- Dijkstra's Algorithm from Vertex '{start_vertex}' ---")
    print("Shortest distances to all vertices:", distances)
    print(f"Lowest cost path from {start_vertex} to {target_vertex}: {' -> '.join(path)}")
    print(f"Total cost (shortest distance) to {target_vertex}: {distances[target_vertex]}")