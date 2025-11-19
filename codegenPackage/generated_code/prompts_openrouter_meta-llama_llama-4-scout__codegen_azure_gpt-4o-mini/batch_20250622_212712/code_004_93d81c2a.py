"""
Generated Code Metadata:
========================
Original URL: https://claires.pages.dev
Prompt: Develop a punishment and reward mechanism for a network using Symbiotic's adaptable restaking logic.
Generated: DETERMINISTIC_93d81c2af9c0d3df
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List

class NetworkNode:
    """
    Represents a node in the network that can be rewarded or punished based on its performance.
    """
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.reputation_score = 100  # Initial reputation score
        self.staked_amount = 0  # Amount staked by the node

    def stake(self, amount: float):
        """
        Allows the node to stake a certain amount.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
        self.staked_amount += amount

    def punish(self, penalty: float):
        """
        Applies a punishment to the node by reducing its reputation score.
        """
        if penalty < 0:
            raise ValueError("Penalty must be non-negative.")
        self.reputation_score = max(0, self.reputation_score - penalty)

    def reward(self, reward: float):
        """
        Rewards the node by increasing its reputation score.
        """
        if reward < 0:
            raise ValueError("Reward must be non-negative.")
        self.reputation_score += reward

class Network:
    """
    Represents the network that manages nodes and their rewards/punishments.
    """
    def __init__(self):
        self.nodes: Dict[str, NetworkNode] = {}

    def add_node(self, node_id: str):
        """
        Adds a new node to the network.
        """
        if node_id in self.nodes:
            raise ValueError("Node already exists.")
        self.nodes[node_id] = NetworkNode(node_id)

    def assess_performance(self):
        """
        Randomly assesses the performance of each node and applies rewards or punishments.
        """
        for node in self.nodes.values():
            performance = random.random()  # Simulate performance assessment
            if performance < 0.3:  # 30% chance of being punished
                penalty = random.uniform(5, 20)  # Random penalty between 5 and 20
                node.punish(penalty)
                print(f"Node {node.node_id} punished with penalty: {penalty}. New reputation: {node.reputation_score}.")
            elif performance > 0.7:  # 30% chance of being rewarded
                reward = random.uniform(5, 20)  # Random reward between 5 and 20
                node.reward(reward)
                print(f"Node {node.node_id} rewarded with amount: {reward}. New reputation: {node.reputation_score}.")
            else:
                print(f"Node {node.node_id} performance is stable. Reputation remains: {node.reputation_score}.")

    def get_node_reputation(self, node_id: str) -> float:
        """
        Returns the reputation score of a specific node.
        """
        if node_id not in self.nodes:
            raise ValueError("Node not found.")
        return self.nodes[node_id].reputation_score

# Example usage
if __name__ == "__main__":
    network = Network()
    
    # Adding nodes to the network
    try:
        network.add_node("Node1")
        network.add_node("Node2")
        network.add_node("Node3")
        
        # Staking amounts
        network.nodes["Node1"].stake(100)
        network.nodes["Node2"].stake(150)
        network.nodes["Node3"].stake(200)

        # Assessing performance
        network.assess_performance()

        # Displaying reputations
        for node_id in network.nodes:
            print(f"Reputation of {node_id}: {network.get_node_reputation(node_id)}")
    except ValueError as e:
        print(f"Error: {e}")
```
