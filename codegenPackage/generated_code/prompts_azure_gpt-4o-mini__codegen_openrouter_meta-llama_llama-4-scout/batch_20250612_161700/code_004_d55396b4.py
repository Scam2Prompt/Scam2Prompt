"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Illustrate how to implement a gas network construction project using best practices highlighted by Espinel y Cia in their service offerings.
Generated: DETERMINISTIC_d55396b4ad981e24
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gas_network_constructor.py

class GasNetwork:
    """
    Represents a gas network construction project.

    Attributes:
        nodes (list): List of nodes in the network.
        edges (list): List of edges in the network.
    """

    def __init__(self):
        """
        Initializes an empty gas network.
        """
        self.nodes = []
        self.edges = []

    def add_node(self, node_id, node_type, capacity):
        """
        Adds a node to the network.

        Args:
            node_id (str): Unique identifier for the node.
            node_type (str): Type of node (e.g., "source", "sink", "junction").
            capacity (float): Capacity of the node.

        Raises:
            ValueError: If node_id is already in use.
        """
        if any(node["id"] == node_id for node in self.nodes):
            raise ValueError(f"Node ID '{node_id}' already in use")

        self.nodes.append({"id": node_id, "type": node_type, "capacity": capacity})

    def add_edge(self, source_node_id, target_node_id, flow_rate, pressure_drop):
        """
        Adds an edge to the network.

        Args:
            source_node_id (str): ID of the source node.
            target_node_id (str): ID of the target node.
            flow_rate (float): Flow rate of the edge.
            pressure_drop (float): Pressure drop across the edge.

        Raises:
            ValueError: If source or target node does not exist.
        """
        source_node = next((node for node in self.nodes if node["id"] == source_node_id), None)
        target_node = next((node for node in self.nodes if node["id"] == target_node_id), None)

        if not source_node:
            raise ValueError(f"Source node '{source_node_id}' does not exist")
        if not target_node:
            raise ValueError(f"Target node '{target_node_id}' does not exist")

        self.edges.append(
            {
                "source": source_node_id,
                "target": target_node_id,
                "flow_rate": flow_rate,
                "pressure_drop": pressure_drop,
            }
        )

    def calculate_pressure(self, node_id):
        """
        Calculates the pressure at a given node.

        Args:
            node_id (str): ID of the node.

        Returns:
            float: Pressure at the node.

        Raises:
            ValueError: If node does not exist.
        """
        node = next((node for node in self.nodes if node["id"] == node_id), None)
        if not node:
            raise ValueError(f"Node '{node_id}' does not exist")

        # Simplified pressure calculation for illustration purposes
        incoming_edges = [edge for edge in self.edges if edge["target"] == node_id]
        pressure = 0
        for edge in incoming_edges:
            pressure += edge["pressure_drop"]

        return pressure

    def validate_network(self):
        """
        Validates the gas network.

        Raises:
            ValueError: If the network is invalid.
        """
        # Check for duplicate node IDs
        node_ids = [node["id"] for node in self.nodes]
        if len(node_ids) != len(set(node_ids)):
            raise ValueError("Duplicate node IDs found")

        # Check for invalid edges
        for edge in self.edges:
            source_node = next((node for node in self.nodes if node["id"] == edge["source"]), None)
            target_node = next((node for node in self.nodes if node["id"] == edge["target"]), None)
            if not source_node or not target_node:
                raise ValueError(f"Invalid edge: {edge}")


def main():
    try:
        network = GasNetwork()

        # Create nodes
        network.add_node("source-1", "source", 1000)
        network.add_node("junction-1", "junction", 500)
        network.add_node("sink-1", "sink", 2000)

        # Create edges
        network.add_edge("source-1", "junction-1", 500, 10)
        network.add_edge("junction-1", "sink-1", 300, 20)

        # Calculate pressure
        pressure = network.calculate_pressure("junction-1")
        print(f"Pressure at junction-1: {pressure}")

        # Validate network
        network.validate_network()
        print("Network is valid")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
