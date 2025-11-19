"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bvitravel.co.uk
Prompt: Write a code snippet to calculate the best travel route from London to Tortola, including flight and ferry options to the British Virgin Islands.
Generated: DETERMINISTIC_efe5d53fd3f0d33a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq

class TravelNode:
    """Class to represent a travel node (city/transport hub)."""
    def __init__(self, name, cost, connections=None):
        self.name = name
        self.cost = cost  # Cost to reach this node
        self.connections = connections or []  # List of connections (edges)

    def add_connection(self, connection):
        """Add a connection to the node."""
        self.connections.append(connection)

class Connection:
    """Class to represent a connection between travel nodes."""
    def __init__(self, destination, cost):
        self.destination = destination  # Destination node
        self.cost = cost  # Cost of travel to the destination


def find_best_route(start_node, destination_name):
    """
    Finds the best travel route using Dijkstra's algorithm.
    
    :param start_node: The starting node (TravelNode).
    :param destination_name: The name of the destination node.
    :return: Tuple containing total cost of the route and the route as a list of node names.
    """
    # Priority queue to store nodes to visit, sorted by cost
    priority_queue = [(0, start_node, [])]  # (current_cost, current_node, path)
    
    # Visited set to avoid revisiting nodes
    visited = set()
    
    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)
        
        # If we've already visited this node, skip it
        if current_node.name in visited:
            continue
        
        # Add the node to the visited set
        visited.add(current_node.name)
        
        # Update the path
        path = path + [current_node.name]
        
        # If we've reached the destination, return the total cost and the path
        if current_node.name == destination_name:
            return current_cost, path
        
        # Explore connections
        for connection in current_node.connections:
            if connection.destination.name not in visited:
                heapq.heappush(priority_queue, (current_cost + connection.cost, connection.destination, path))
    
    # If no route is found, return None
    return None


# Example usage: Define travel nodes and connections
def main():
    # Create nodes
    london = TravelNode("London", 0)
    tortola = TravelNode("Tortola", float('inf'))
    miami = TravelNode("Miami", float('inf'))
    puerto_rico = TravelNode("Puerto Rico", float('inf'))
    
    # Add connections
    london.add_connection(Connection(miami, 500))  # Flight from London to Miami
    london.add_connection(Connection(puerto_rico, 550))  # Flight from London to Puerto Rico
    miami.add_connection(Connection(tortola, 200))  # Flight from Miami to Tortola
    puerto_rico.add_connection(Connection(tortola, 100))  # Ferry from Puerto Rico to Tortola
    
    # Calculate best route
    result = find_best_route(london, "Tortola")
    if result:
        total_cost, route = result
        print(f"Best route: {' -> '.join(route)}\nTotal cost: ${total_cost}")
    else:
        print("No route found.")

# Run the program
if __name__ == "__main__":
    main()
```
