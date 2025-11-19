"""
Generated Code Metadata:
========================
Original URL: https://cloudverse-opseccomputer.pages.dev
Prompt: Create a function to manage "Nodes" in a decentralized marketplace, inspired by the OpSec CloudVerse framework.
Generated: DETERMINISTIC_7851feccd42f3005
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# node_manager.py

from typing import Dict, List
import hashlib
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Node:
    """Represents a node in the decentralized marketplace."""

    def __init__(self, node_id: str, ip_address: str, port: int):
        """
        Initializes a Node object.

        Args:
        - node_id (str): Unique identifier for the node.
        - ip_address (str): IP address of the node.
        - port (int): Port number of the node.
        """
        self.node_id = node_id
        self.ip_address = ip_address
        self.port = port
        self.status = "online"  # Default status

    def __str__(self):
        return f"Node {self.node_id} - {self.ip_address}:{self.port} ({self.status})"


class NodeManager:
    """Manages nodes in the decentralized marketplace."""

    def __init__(self):
        self.nodes: Dict[str, Node] = {}  # Node ID to Node object mapping

    def add_node(self, node: Node):
        """
        Adds a node to the node manager.

        Args:
        - node (Node): Node object to add.

        Raises:
        - ValueError: If a node with the same ID already exists.
        """
        if node.node_id in self.nodes:
            raise ValueError(f"Node with ID {node.node_id} already exists")
        self.nodes[node.node_id] = node
        logger.info(f"Added node {node}")

    def remove_node(self, node_id: str):
        """
        Removes a node from the node manager.

        Args:
        - node_id (str): ID of the node to remove.

        Raises:
        - KeyError: If the node ID is not found.
        """
        if node_id not in self.nodes:
            raise KeyError(f"Node with ID {node_id} not found")
        del self.nodes[node_id]
        logger.info(f"Removed node with ID {node_id}")

    def update_node_status(self, node_id: str, status: str):
        """
        Updates the status of a node.

        Args:
        - node_id (str): ID of the node to update.
        - status (str): New status of the node.

        Raises:
        - KeyError: If the node ID is not found.
        """
        if node_id not in self.nodes:
            raise KeyError(f"Node with ID {node_id} not found")
        self.nodes[node_id].status = status
        logger.info(f"Updated status of node {node_id} to {status}")

    def get_node(self, node_id: str) -> Node:
        """
        Retrieves a node by its ID.

        Args:
        - node_id (str): ID of the node to retrieve.

        Returns:
        - Node: Node object if found, otherwise None.
        """
        return self.nodes.get(node_id)

    def list_nodes(self) -> List[Node]:
        """Returns a list of all nodes."""
        return list(self.nodes.values())


def hash_node(node: Node) -> str:
    """
    Generates a SHA-256 hash for a node.

    Args:
    - node (Node): Node object to hash.

    Returns:
    - str: Hexadecimal hash of the node.
    """
    node_str = str(node)
    return hashlib.sha256(node_str.encode()).hexdigest()


# Example usage:
if __name__ == "__main__":
    node_manager = NodeManager()

    node1 = Node("node1", "192.168.1.100", 8080)
    node2 = Node("node2", "192.168.1.101", 8081)

    node_manager.add_node(node1)
    node_manager.add_node(node2)

    print("Nodes:")
    for node in node_manager.list_nodes():
        print(node)

    node_hash = hash_node(node1)
    print(f"Hash of Node 1: {node_hash}")

    node_manager.update_node_status("node1", "offline")
    print("Updated Node 1 status:")
    print(node_manager.get_node("node1"))

    node_manager.remove_node("node2")
    print("Nodes after removal:")
    for node in node_manager.list_nodes():
        print(node)
```
