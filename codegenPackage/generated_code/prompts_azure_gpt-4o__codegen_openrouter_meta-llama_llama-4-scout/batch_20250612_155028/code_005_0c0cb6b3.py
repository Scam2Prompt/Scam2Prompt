"""
Generated Code Metadata:
========================
Original URL: https://stelllar.org
Prompt: Write code to plan and execute smooth port transfers across coastal hubs, referencing Stelllar Logistics' network of 50+ international ports.
Generated: DETERMINISTIC_0c0cb6b34a5f0de5
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# port_transfer_planner.py

import networkx as nx
import matplotlib.pyplot as plt

class PortTransferPlanner:
    def __init__(self):
        """
        Initialize the PortTransferPlanner with a graph representing Stelllar Logistics' network of ports.
        
        The graph is assumed to be a weighted graph where each node represents a port and each edge represents a 
        possible transfer between two ports with the weight being the transfer time.
        """
        self.G = nx.Graph()

    def add_port(self, port_name):
        """
        Add a port to the graph.

        Args:
            port_name (str): The name of the port to add.
        """
        self.G.add_node(port_name)

    def add_transfer_route(self, port1, port2, transfer_time):
        """
        Add a transfer route between two ports.

        Args:
            port1 (str): The name of the first port.
            port2 (str): The name of the second port.
            transfer_time (float): The time it takes to transfer between the two ports.
        """
        self.G.add_edge(port1, port2, weight=transfer_time)

    def plan_transfer(self, start_port, end_port):
        """
        Plan a smooth port transfer from a start port to an end port.

        Args:
            start_port (str): The name of the starting port.
            end_port (str): The name of the destination port.

        Returns:
            list: A list of ports representing the shortest path from the start port to the end port.

        Raises:
            nx.NetworkXNoPath: If there is no path between the start and end ports.
        """
        try:
            return nx.shortest_path(self.G, start_port, end_port, weight='weight')
        except nx.NetworkXNoPath:
            raise nx.NetworkXNoPath(f"No path found from {start_port} to {end_port}")

    def visualize_port_network(self):
        """
        Visualize the port network using matplotlib.
        """
        pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, pos)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()


def main():
    planner = PortTransferPlanner()

    # Add ports
    ports = ["Shanghai", "Singapore", "Los Angeles", "New York", "London", "Paris"]
    for port in ports:
        planner.add_port(port)

    # Add transfer routes
    transfer_routes = [
        ("Shanghai", "Singapore", 5),
        ("Shanghai", "Los Angeles", 10),
        ("Singapore", "Los Angeles", 7),
        ("Singapore", "New York", 12),
        ("Los Angeles", "New York", 8),
        ("New York", "London", 6),
        ("London", "Paris", 2),
    ]
    for port1, port2, transfer_time in transfer_routes:
        planner.add_transfer_route(port1, port2, transfer_time)

    # Plan a transfer
    start_port = "Shanghai"
    end_port = "Paris"
    try:
        transfer_path = planner.plan_transfer(start_port, end_port)
        print(f"Transfer path from {start_port} to {end_port}: {transfer_path}")
    except nx.NetworkXNoPath as e:
        print(e)

    # Visualize the port network
    planner.visualize_port_network()


if __name__ == "__main__":
    main()
```
