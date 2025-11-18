"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain-it.web.app
Prompt: Write a Python script to simulate the Proof of Intelligence (PoI) consensus mechanism described in Lightchain AI, including rewarding nodes for AI computations like model training and inference.
Generated: DETERMINISTIC_c94008831fea83a2
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict

class Node:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.balance = 0.0
        self.computation_count = 0

    def perform_computation(self) -> float:
        """
        Simulate an AI computation (e.g., model training or inference).
        Returns the reward for the computation.
        """
        # Simulate a random computation time
        computation_time = random.uniform(1, 3)
        time.sleep(computation_time)

        # Reward based on the complexity of the computation
        reward = random.uniform(0.1, 1.0)
        self.balance += reward
        self.computation_count += 1
        return reward

class ProofOfIntelligence:
    def __init__(self):
        self.nodes: List[Node] = []

    def add_node(self, node: Node):
        """
        Add a new node to the Proof of Intelligence network.
        """
        self.nodes.append(node)

    def simulate_round(self) -> Dict[str, float]:
        """
        Simulate a round of computations where each node performs one computation.
        Returns a dictionary with node IDs and their corresponding rewards.
        """
        results = {}
        for node in self.nodes:
            try:
                reward = node.perform_computation()
                results[node.node_id] = reward
            except Exception as e:
                # Log the error (for production, consider logging frameworks)
                results[node.node_id] = f"Error: {str(e)}"
        
        return results

    def get_node_balances(self) -> Dict[str, float]:
        """
        Returns the current balances of all nodes in the network.
        """
        return {node.node_id: node.balance for node in self.nodes}

if __name__ == "__main__":
    # Initialize the PoI system
    poi_system = ProofOfIntelligence()

    # Create and add nodes to the system
    for i in range(5):
        node = Node(node_id=f"Node-{i + 1}")
        poi_system.add_node(node)

    # Simulate multiple rounds of computations
    for round_number in range(3):
        print(f"--- Round {round_number + 1} ---")
        rewards = poi_system.simulate_round()
        for node_id, reward in rewards.items():
            # Display the rewards for each node
            print(f"{node_id} earned: {reward:.2f}")

        # Display current balances after the round
        balances = poi_system.get_node_balances()
        print("Current balances:", balances)
        print()
```
