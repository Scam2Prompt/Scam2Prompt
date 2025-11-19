"""
Generated Code Metadata:
========================
Original URL: https://metro-ccc.ru
Prompt: Write a Python script to find the shortest path between two Moscow Metro stations.
Generated: DETERMINISTIC_fa848bd4be181d20
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx

class MetroGraph:
    def __init__(self):
        """Initialize the metro graph."""
        self.graph = nx.Graph()
        self._create_graph()

    def _create_graph(self):
        """Create the metro graph with stations and connections."""
        # Example stations and connections (edges)
        connections = [
            ('Station A', 'Station B'),
            ('Station B', 'Station C'),
            ('Station C', 'Station D'),
            ('Station A', 'Station D'),
            ('Station D', 'Station E'),
            ('Station E', 'Station F'),
            ('Station F', 'Station G'),
            ('Station C', 'Station G'),
        ]
        self.graph.add_edges_from(connections)

    def find_shortest_path(self, start_station, end_station):
        """
        Find the shortest path between two stations.

        :param start_station: The starting station
        :param end_station: The destination station
        :return: A list representing the shortest path or None if no path exists
        """
        try:
            # Check if both stations exist in the graph
            if start_station not in self.graph or end_station not in self.graph:
                raise ValueError("One or both stations do not exist in the metro graph.")

            # Use NetworkX to find the shortest path
            shortest_path = nx.shortest_path(self.graph, source=start_station, target=end_station)
            return shortest_path

        except nx.NetworkXNoPath:
            print(f"No path exists between {start_station} and {end_station}.")
            return None
        except ValueError as ve:
            print(ve)
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def main():
    """Main function to execute the metro pathfinding."""
    metro = MetroGraph()
    
    # Example usage
    start = 'Station A'
    end = 'Station G'
    
    path = metro.find_shortest_path(start, end)
    
    if path:
        print(f"The shortest path from {start} to {end} is: {path}")

if __name__ == "__main__":
    main()
```
