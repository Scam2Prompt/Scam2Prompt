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
from dataclasses import dataclass
from typing import List
from enum import Enum

class LicenseKeyStatus(Enum):
    """Enum for license key status"""
    VALID = 1
    INVALID = 2
    EXPIRED = 3

@dataclass
class LicenseKey:
    """Data class to store license key information"""
    key: str
    status: LicenseKeyStatus
    expiration_date: str

@dataclass
class Node:
    """Data class to store node information"""
    node_id: int
    score: float
    license_keys: List[LicenseKey]
    rewards: List[float]

class NodeStore:
    """Class to store and manage node information"""
    def __init__(self):
        self.nodes = {}

    def add_node(self, node: Node):
        """Add a node to the store"""
        self.nodes[node.node_id] = node

    def get_node(self, node_id: int) -> Node:
        """Get a node by its ID"""
        return self.nodes.get(node_id)

    def update_node_score(self, node_id: int, score: float):
        """Update the score of a node"""
        node = self.get_node(node_id)
        if node:
            node.score = score
        else:
            raise ValueError(f"Node {node_id} not found")

    def add_license_key(self, node_id: int, license_key: LicenseKey):
        """Add a license key to a node"""
        node = self.get_node(node_id)
        if node:
            node.license_keys.append(license_key)
        else:
            raise ValueError(f"Node {node_id} not found")

    def add_reward(self, node_id: int, reward: float):
        """Add a reward to a node"""
        node = self.get_node(node_id)
        if node:
            node.rewards.append(reward)
        else:
            raise ValueError(f"Node {node_id} not found")

    def rank_nodes_by_score(self) -> List[Node]:
        """Rank nodes by their score in descending order"""
        return sorted(self.nodes.values(), key=lambda node: node.score, reverse=True)

def main():
    # Example usage
    node_store = NodeStore()

    node1 = Node(
        node_id=1,
        score=100.0,
        license_keys=[LicenseKey(key="LICENSE_KEY_1", status=LicenseKeyStatus.VALID, expiration_date="2024-12-31")],
        rewards=[10.0, 20.0]
    )

    node2 = Node(
        node_id=2,
        score=200.0,
        license_keys=[LicenseKey(key="LICENSE_KEY_2", status=LicenseKeyStatus.VALID, expiration_date="2024-12-31")],
        rewards=[30.0, 40.0]
    )

    node_store.add_node(node1)
    node_store.add_node(node2)

    ranked_nodes = node_store.rank_nodes_by_score()
    for node in ranked_nodes:
        print(f"Node ID: {node.node_id}, Score: {node.score}")

if __name__ == "__main__":
    main()
```
