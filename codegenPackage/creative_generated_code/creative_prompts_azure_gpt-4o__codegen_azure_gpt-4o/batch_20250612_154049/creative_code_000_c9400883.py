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
import hashlib
import random
import time
from typing import List, Dict

# Constants
MAX_REWARD = 100  # Maximum reward for a node
DIFFICULTY = 4    # Number of leading zeros required in the hash for consensus
MODEL_TRAINING_TIME = 5  # Simulated time for model training (seconds)
MODEL_INFERENCE_TIME = 2  # Simulated time for inference (seconds)


class Node:
    """
    Represents a node in the network.
    Each node performs AI computations and participates in the PoI consensus mechanism.
    """
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.computation_power = random.uniform(0.5, 1.5)  # Simulated computation power
        self.reward = 0

    def perform_ai_computation(self, computation_type: str) -> float:
        """
        Simulates AI computation (model training or inference).
        
        :param computation_type: Type of computation ('training' or 'inference').
        :return: Computation score based on power and type.
        """
        try:
            if computation_type == 'training':
                print(f"Node {self.node_id} performing model training...")
                time.sleep(MODEL_TRAINING_TIME / self.computation_power)
                return random.uniform(0.8, 1.2) * self.computation_power
            elif computation_type == 'inference':
                print(f"Node {self.node_id} performing model inference...")
                time.sleep(MODEL_INFERENCE_TIME / self.computation_power)
                return random.uniform(0.5, 1.0) * self.computation_power
            else:
                raise ValueError(f"Unknown computation type: {computation_type}")
        except Exception as e:
            print(f"Error in Node {self.node_id} during computation: {e}")
            return 0.0

    def calculate_nonce(self, data: str) -> int:
        """
        Simulates proof-of-work by finding a nonce for the given data.
        
        :param data: Input data for hashing.
        :return: Valid nonce that satisfies the PoI condition.
        """
        nonce = 0
        while True:
            hash_result = hashlib.sha256((data + str(nonce)).encode()).hexdigest()
            if hash_result.startswith('0' * DIFFICULTY):
                return nonce
            nonce += 1


class LightchainAI:
    """
    Represents the Lightchain AI network.
    Manages nodes, consensus, and rewards.
    """
    def __init__(self, num_nodes: int):
        self.nodes = [Node(node_id=i) for i in range(num_nodes)]

    def simulate_consensus(self):
        """
        Simulates the Proof of Intelligence consensus mechanism.
        Rewards nodes based on their contribution to AI computations.
        """
        for node in self.nodes:
            print(f"\nNode {node.node_id} participating in consensus...")

            # Perform AI computations (training and inference)
            training_score = node.perform_ai_computation('training')
            inference_score = node.perform_ai_computation('inference')

            # Aggregate computation scores
            total_score = training_score + inference_score

            # Find valid nonce through Proof of Work
            data = f"Node {node.node_id} | Score: {total_score:.2f}"
            nonce = node.calculate_nonce(data)
            print(f"Node {node.node_id} found nonce {nonce} with data: {data}")

            # Reward calculation
            node.reward = min(MAX_REWARD, total_score * 10)  # Scale rewards based on score
            print(f"Node {node.node_id} rewarded {node.reward:.2f} tokens.")

    def display_node_rewards(self):
        """
        Displays the rewards for all nodes.
        """
        print("\n--- Node Rewards ---")
        for node in self.nodes:
            print(f"Node {node.node_id}: {node.reward:.2f} tokens")


if __name__ == "__main__":
    # Initialize the Lightchain AI network with a given number of nodes
    num_nodes = 5
    lightchain_ai = LightchainAI(num_nodes)

    # Simulate the Proof of Intelligence consensus mechanism
    lightchain_ai.simulate_consensus()

    # Display final rewards for all nodes
    lightchain_ai.display_node_rewards()
```
