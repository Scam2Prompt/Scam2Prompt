"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain.netlify.app
Prompt: Provide an example of how to implement a region-based sharding system in a blockchain network, where nodes are grouped based on geographic proximity, as outlined in PulseChain's architecture.
Generated: DETERMINISTIC_cb6f32a9d64b39a1
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Node:
    """Represents a node in the blockchain network."""
    
    def __init__(self, node_id: str, location: str):
        """
        Initializes a Node instance.

        Args:
            node_id (str): Unique identifier for the node.
            location (str): Geographic location of the node.
        """
        self.node_id = node_id
        self.location = location

class Shard:
    """Represents a shard that contains nodes grouped by geographic proximity."""
    
    def __init__(self, shard_id: str):
        """
        Initializes a Shard instance.

        Args:
            shard_id (str): Unique identifier for the shard.
        """
        self.shard_id = shard_id
        self.nodes = []  # List of nodes in this shard

    def add_node(self, node: Node):
        """Adds a node to the shard."""
        self.nodes.append(node)

class RegionBasedSharding:
    """Manages the sharding of nodes based on their geographic locations."""
    
    def __init__(self):
        """Initializes the sharding system with an empty list of shards."""
        self.shards: Dict[str, Shard] = {}

    def create_shard(self, shard_id: str):
        """Creates a new shard if it doesn't already exist."""
        if shard_id not in self.shards:
            self.shards[shard_id] = Shard(shard_id)
        else:
            raise ValueError(f"Shard ID {shard_id} already exists.")

    def add_node_to_shard(self, node: Node, shard_id: str):
        """
        Adds a node to the specified shard.

        Args:
            node (Node): The node to be added.
            shard_id (str): The ID of the shard to which the node will be added.
        """
        if shard_id in self.shards:
            self.shards[shard_id].add_node(node)
        else:
            raise ValueError(f"Shard ID {shard_id} does not exist.")

    def get_shards(self) -> Dict[str, List[Node]]:
        """
        Retrieves the current state of all shards.

        Returns:
            Dict[str, List[Node]]: A dictionary where keys are shard IDs and values are lists of nodes.
        """
        return {shard_id: shard.nodes for shard_id, shard in self.shards.items()}

# Example usage
if __name__ == "__main__":
    try:
        sharding_system = RegionBasedSharding()
        
        # Create shards based on geographic regions
        sharding_system.create_shard("us-west")
        sharding_system.create_shard("us-east")
        sharding_system.create_shard("eu-central")

        # Randomly create nodes and assign them to shards
        locations = ["us-west", "us-east", "eu-central"]
        for i in range(10):
            location = random.choice(locations)
            node = Node(node_id=f"node-{i}", location=location)
            sharding_system.add_node_to_shard(node, location)
        
        # Output the current shards and their nodes
        shards_status = sharding_system.get_shards()
        for shard_id, nodes in shards_status.items():
            print(f"Shard ID: {shard_id}, Nodes: {[node.node_id for node in nodes]}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
