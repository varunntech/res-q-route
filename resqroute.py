# ResQRoute — Dijkstra's Shortest Path + All Possible Routes

import heapq

# Graph setup
nodes = {
    0: "City Incident",
    1: "Junction A",
    2: "Junction B",
    3: "Junction C",
    4: "Hospital North",
    5: "Hospital South",
    6: "Rescue Base"
}

graph = {i: [] for i in nodes}

def add_edge(u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))

add_edge(0, 1, 4)
add_edge(0, 2, 6)
add_edge(1, 2, 3)
add_edge(1, 3, 5)
add_edge(2, 3, 4)
add_edge(3, 4, 7)
add_edge(3, 5, 5)
add_edge(4, 6, 8)
add_edge(5, 6, 6)


# ── Dijkstra's Algorithm ──────────────────────────────
def dijkstra(src, dst):
    dist = {n: float('inf') for n in nodes}
    prev = {n: None for n in nodes}
    dist[src] = 0
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    # Reconstruct shortest path
    path, cur = [], dst
    while cur is not None:
        path.insert(0, cur)
        cur = prev[cur]

    if path[0] != src:
        return [], float('inf')
    return path, dist[dst]


# ── DFS — Find ALL Possible Routes ───────────────────
def find_all_routes(src, dst):
    all_routes = []

    def dfs(current, destination, visited, path, cost):
        if current == destination:
            all_routes.append((list(path), cost))
            return
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, destination, visited, path, cost + weight)
                path.pop()
                visited.remove(neighbor)

    dfs(src, dst, {src}, [src], 0)

    # Sort by distance
    all_routes.sort(key=lambda x: x[1])
    return all_routes


# ── Main ──────────────────────────────────────────────
print("=" * 52)
print("  ResQRoute — Ambulance Shortest Path Finder")
print("=" * 52)

print("\n  Available Locations:")
for i, name in nodes.items():
    print(f"    [{i}] {name}")

try:
    print()
    src = int(input("  Enter Source Node ID      : "))
    dst = int(input("  Enter Destination Node ID : "))

    if src not in nodes or dst not in nodes:
        print("\n  Invalid node ID.")
    elif src == dst:
        print("\n  Source and destination cannot be the same.")
    else:
        # All possible routes (DFS)
        all_routes = find_all_routes(src, dst)

        print(f"\n  From : {nodes[src]}")
        print(f"  To   : {nodes[dst]}")

        # ── All Routes ──────────────────────────────
        print(f"\n  All Possible Routes ({len(all_routes)} found):")
        print(f"  {'─'*52}")

        for i, (path, cost) in enumerate(all_routes, 1):
            route_str = " → ".join(nodes[n] for n in path)
            print(f"  Route {i}: {route_str}")
            print(f"          Distance = {cost} km")
            print()

        # ── Shortest Route (Dijkstra) ───────────────
        short_path, km = dijkstra(src, dst)
        eta = round((km / 60) * 60, 1)

        print(f"  {'─'*52}")
        print(f"  SHORTEST ROUTE (Dijkstra's Algorithm)")
        print(f"  {'─'*52}")
        print(f"  Path : {' → '.join(nodes[n] for n in short_path)}")
        print(f"  Dist : {km} km")
        print(f"  ETA  : ~{eta} minutes  (@ 60 km/h)")
        print(f"  {'─'*52}")

        # ── Comparison Table ────────────────────────
        print(f"\n  Route Comparison Table:")
        print(f"  {'─'*52}")
        print(f"  {'#':<4} {'Distance':<12} {'Status':<12} {'Hops'}")
        print(f"  {'─'*52}")
        for i, (path, cost) in enumerate(all_routes, 1):
            tag  = " SHORTEST" if cost == km else ""
            hops = len(path) - 1
            print(f"  {i:<4} {str(cost)+' km':<12} {tag:<12} {hops} hop(s)")
        print(f"  {'─'*52}\n")

except ValueError:
    print("\n  Please enter a valid number.")
