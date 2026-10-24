import heapq  # Import heapq to implement a priority queue

def dijkstra(graph, start):

    # Initialize distances to infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Initialize priority queue
    priority_queue = [(0, start)]

    # Keep track of visited vertices
    visited = set()

    # Process vertices in the queue
    while priority_queue:

        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if already visited
        if current_vertex in visited:
            continue

        # Mark the vertex as visited
        visited.add(current_vertex)

        # Check all neighboring vertices
        for neighbor, weight in graph[current_vertex].items():

            if neighbor in visited:
                continue

            # Calculate the new distance
            distance = current_distance + weight

            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Create a graph using an adjacency list
graph = {
    'A': {'B': 1, 'D': 4},
    'B': {'A': 1, 'C': 3, 'E': 1},
    'C': {'B': 3, 'F': 5},
    'D': {'A': 4, 'E': 2},
    'E': {'B': 1, 'D': 2, 'F': 6},
    'F': {'C': 5, 'E': 6}
}

# Run Dijkstra's algorithm from vertex A
distances = dijkstra(graph, 'A')

# Display the shortest distances
print("Shortest distances from vertex A:")
print(distances)