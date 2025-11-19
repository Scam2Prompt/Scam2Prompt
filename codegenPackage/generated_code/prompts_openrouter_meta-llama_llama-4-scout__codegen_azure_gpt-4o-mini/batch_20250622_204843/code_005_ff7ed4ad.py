"""
Generated Code Metadata:
========================
Original URL: https://dashboard-gpu.pages.dev
Prompt: "Design a data structure to store node information, including node score, license keys, and rewards, for efficient querying and ranking."
Generated: DETERMINISTIC_ff7ed4ad03438307
Batch ID: 20250622_204843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Node:
    """
    A class to represent a node with its associated information.

    Attributes:
        node_id (str): Unique identifier for the node.
        score (float): Score of the node.
        license_keys (list): List of license keys associated with the node.
        rewards (list): List of rewards associated with the node.
    """

    def __init__(self, node_id: str, score: float, license_keys: list, rewards: list):
        """
        Initializes a Node instance.

        Args:
            node_id (str): Unique identifier for the node.
            score (float): Score of the node.
            license_keys (list): List of license keys associated with the node.
            rewards (list): List of rewards associated with the node.
        """
        self.node_id = node_id
        self.score = score
        self.license_keys = license_keys
        self.rewards = rewards

    def __repr__(self):
        """Return a string representation of the Node."""
        return f"Node(node_id={self.node_id}, score={self.score}, license_keys={self.license_keys}, rewards={self.rewards})"


class NodeManager:
    """
    A class to manage a collection of nodes for efficient querying and ranking.

    Attributes:
        nodes (dict): A dictionary to store nodes with node_id as the key.
    """

    def __init__(self):
        """Initializes the NodeManager with an empty node collection."""
        self.nodes = {}

    def add_node(self, node: Node):
        """
        Adds a new node to the collection.

        Args:
            node (Node): The node to be added.

        Raises:
            ValueError: If a node with the same node_id already exists.
        """
        if node.node_id in self.nodes:
            raise ValueError(f"Node with id {node.node_id} already exists.")
        self.nodes[node.node_id] = node

    def get_node(self, node_id: str) -> Node:
        """
        Retrieves a node by its ID.

        Args:
            node_id (str): The ID of the node to retrieve.

        Returns:
            Node: The node associated with the given ID.

        Raises:
            KeyError: If no node with the given ID exists.
        """
        if node_id not in self.nodes:
            raise KeyError(f"No node found with id {node_id}.")
        return self.nodes[node_id]

    def rank_nodes(self) -> list:
        """
        Ranks nodes based on their scores in descending order.

        Returns:
            list: A list of nodes sorted by score.
        """
        return sorted(self.nodes.values(), key=lambda node: node.score, reverse=True)

    def get_all_nodes(self) -> list:
        """
        Retrieves all nodes in the collection.

        Returns:
            list: A list of all nodes.
        """
        return list(self.nodes.values())


# Example usage
if __name__ == "__main__":
    manager = NodeManager()
    
    # Adding nodes
    try:
        manager.add_node(Node("node1", 85.5, ["key1", "key2"], ["reward1"]))
        manager.add_node(Node("node2", 90.0, ["key3"], ["reward2", "reward3"]))
        manager.add_node(Node("node3", 75.0, ["key4"], []))
        
        # Retrieving a node
        node = manager.get_node("node1")
        print(node)

        # Ranking nodes
        ranked_nodes = manager.rank_nodes()
        print("Ranked Nodes:", ranked_nodes)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
