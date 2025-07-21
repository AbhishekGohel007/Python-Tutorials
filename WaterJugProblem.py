from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def min_steps_with_graph(m, n, d):
    if d > max(m, n):
        return -1

    q = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))

    G = nx.DiGraph()  

    while q:
        jug1, jug2 = q.popleft()

        if jug1 == d or jug2 == d:
            break

        current = (jug1, jug2)

        next_states = []

        
        next_states.append((m, jug2))
        
        next_states.append((jug1, n))
        
        next_states.append((0, jug2))
        
        next_states.append((jug1, 0))
        
        pour1to2 = min(jug1, n - jug2)
        next_states.append((jug1 - pour1to2, jug2 + pour1to2))
        
        pour2to1 = min(jug2, m - jug1)
        next_states.append((jug1 + pour2to1, jug2 - pour2to1))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                q.append(state)
                G.add_edge(current, state)

    
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): '' for u, v in G.edges()})
    plt.title(f"Water Jug State Transitions to reach {d}L")
    plt.show()

if __name__ == "__main__":
    m, n, d = 5, 3, 4
    min_steps_with_graph(m, n, d)
