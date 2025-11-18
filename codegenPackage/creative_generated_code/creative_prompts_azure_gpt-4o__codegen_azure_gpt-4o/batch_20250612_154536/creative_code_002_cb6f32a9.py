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
import geopy.distance
from collections import defaultdict

class Node:
    """
    Represents a single node in the blockchain network.
    """
    def __init__(self, node_id, latitude, longitude):
        self.node_id = node_id
        self.latitude = latitude
        self.longitude = longitude

class RegionShard:
    """
    Represents a region-based shard in the blockchain network.
    """
    def __init__(self, shard_id):
        self.shard_id = shard_id
        self.nodes = []

    def add_node(self, node):
        """
        Adds a node to the shard.
        """
        self.nodes.append(node)

    def __repr__(self):
        """
        Returns a string representation of the shard.
        """
        return f"Shard {self.shard_id} - Nodes: {[node.node_id for node in self.nodes]}"

class ShardingManager:
    """
    Manages region-based sharding for the blockchain network.
    """
    def __init__(self, shard_distance_km):
        self.shard_distance_km = shard_distance_km  # Distance threshold for shard grouping
        self.shards = defaultdict(RegionShard)  # Mapping of shard_id to RegionShard
        self.next_shard_id = 0  # Counter to assign unique shard IDs
    
    def calculate_distance(self, node_a, node_b):
        """
        Calculates the geodesic distance between two nodes.
        """
        coords_a = (node_a.latitude, node_a.longitude)
        coords_b = (node_b.latitude, node_b.longitude)
        return geopy.distance.geodesic(coords_a, coords_b).km

    def assign_shard(self, node):
        """
        Assigns a node to the appropriate shard based on geographic proximity.
        """
        for shard_id, shard in self.shards.items():
            # Check proximity to the first node in the shard
            if shard.nodes:
                distance = self.calculate_distance(node, shard.nodes[0])
                if distance <= self.shard_distance_km:
                    shard.add_node(node)
                    return
        
        # Create a new shard if no existing shard is within proximity
        new_shard = RegionShard(self.next_shard_id)
        new_shard.add_node(node)
        self.shards[self.next_shard_id] = new_shard
        self.next_shard_id += 1
    
    def get_shards(self):
        """
        Returns all the shards in the network.
        """
        return self.shards.values()

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize sharding manager with a distance threshold of 100 km
        sharding_manager = ShardingManager(shard_distance_km=100)

        # Example nodes (node_id, latitude, longitude)
        nodes = [
            Node("Node1", 40.7128, -74.0060),  # New York
            Node("Node2", 34.0522, -118.2437), # Los Angeles
            Node("Node3", 41.8781, -87.6298),  # Chicago
            Node("Node4", 40.7306, -73.9352),  # Nearby New York
        ]

        # Assign nodes to shards
        for node in nodes:
            sharding_manager.assign_shard(node)

        # Display the resulting shards
        for shard in sharding_manager.get_shards():
            print(shard)
    except Exception as e:
        print(f"An error occurred: {e}")
```
