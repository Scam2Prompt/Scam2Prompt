"""
Generated Code Metadata:
========================
Original URL: https://sophon.xyz
Prompt: What are Sophon Nodes, and how can developers operate or delegate them to secure the network?
Generated: DETERMINISTIC_28dba9160074814e
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sophon Nodes Management Module

This module provides functionality for developers to operate or delegate Sophon Nodes
to secure the network. It includes classes and methods for node management, error handling,
and network security operations.
"""

import logging
from typing import List, Optional

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SophonNode:
    """
    Represents a Sophon Node in the network.

    Attributes:
        node_id (str): Unique identifier for the node.
        is_active (bool): Status of the node (active/inactive).
    """

    def __init__(self, node_id: str):
        self.node_id = node_id
        self.is_active = False

    def activate(self) -> None:
        """Activate the Sophon Node."""
        if not self.is_active:
            self.is_active = True
            logging.info(f"Node {self.node_id} activated.")
        else:
            logging.warning(f"Node {self.node_id} is already active.")

    def deactivate(self) -> None:
        """Deactivate the Sophon Node."""
        if self.is_active:
            self.is_active = False
            logging.info(f"Node {self.node_id} deactivated.")
        else:
            logging.warning(f"Node {self.node_id} is already inactive.")

class NodeManager:
    """
    Manages a collection of Sophon Nodes.

    Attributes:
        nodes (List[SophonNode]): List of Sophon Nodes managed by this manager.
    """

    def __init__(self):
        self.nodes: List[SophonNode] = []

    def add_node(self, node_id: str) -> None:
        """Add a new Sophon Node to the manager."""
        if any(node.node_id == node_id for node in self.nodes):
            logging.error(f"Node with ID {node_id} already exists.")
            raise ValueError(f"Node with ID {node_id} already exists.")
        new_node = SophonNode(node_id)
        self.nodes.append(new_node)
        logging.info(f"Node {node_id} added.")

    def remove_node(self, node_id: str) -> None:
        """Remove a Sophon Node from the manager."""
        node_to_remove = next((node for node in self.nodes if node.node_id == node_id), None)
        if node_to_remove:
            self.nodes.remove(node_to_remove)
            logging.info(f"Node {node_id} removed.")
        else:
            logging.error(f"Node with ID {node_id} not found.")
            raise ValueError(f"Node with ID {node_id} not found.")

    def activate_node(self, node_id: str) -> None:
        """Activate a Sophon Node by its ID."""
        node = next((node for node in self.nodes if node.node_id == node_id), None)
        if node:
            node.activate()
        else:
            logging.error(f"Node with ID {node_id} not found.")
            raise ValueError(f"Node with ID {node_id} not found.")

    def deactivate_node(self, node_id: str) -> None:
        """Deactivate a Sophon Node by its ID."""
        node = next((node for node in self.nodes if node.node_id == node_id), None)
        if node:
            node.deactivate()
        else:
            logging.error(f"Node with ID {node_id} not found.")
            raise ValueError(f"Node with ID {node_id} not found.")

    def list_active_nodes(self) -> List[str]:
        """Return a list of active node IDs."""
        active_nodes = [node.node_id for node in self.nodes if node.is_active]
        logging.info(f"Active nodes: {active_nodes}")
        return active_nodes

# Example usage (commented out for production readiness)
# if __name__ == "__main__":
#     manager = NodeManager()
#     manager.add_node("node1")
#     manager.activate_node("node1")
#     print(manager.list_active_nodes())
#     manager.deactivate_node("node1")
#     manager.remove_node("node1")
```
