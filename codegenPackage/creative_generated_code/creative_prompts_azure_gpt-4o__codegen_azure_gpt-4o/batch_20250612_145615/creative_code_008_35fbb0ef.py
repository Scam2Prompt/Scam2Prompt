"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain.live-apps.com
Prompt: Write a script to calculate rewards for nodes performing AI computations under Lightchain AI’s Proof of Intelligence (PoI) mechanism.
Generated: DETERMINISTIC_35fbb0ef4dd9eb1d
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Dict, Tuple


class Node:
    """
    Represents a node in the Lightchain AI network.
    """
    def __init__(self, id: str, computations: float, accuracy: float):
        """
        Initializes a Node instance.

        :param id: Unique identifier for the node.
        :param computations: Number of AI computations performed by the node.
        :param accuracy: Accuracy percentage (0 to 100) of the node's computations.
        """
        self.id = id
        self.computations = computations
        self.accuracy = accuracy


class RewardCalculator:
    """
    Calculates rewards for nodes based on Proof of Intelligence (PoI) metrics.
    """

    def __init__(self, base_reward: float):
        """
        Initializes the RewardCalculator instance.

        :param base_reward: The base reward multiplier per computation unit.
        """
        self.base_reward = base_reward

    def calculate_rewards(self, nodes: List[Node]) -> Dict[str, float]:
        """
        Calculates rewards for all nodes.

        :param nodes: List of nodes participating in the AI computation network.
        :return: Dictionary with node IDs as keys and their rewards as values.
        """
        rewards = {}
        for node in nodes:
            try:
                # Ensure accuracy is between 0 and 100
                if not (0 <= node.accuracy <= 100):
                    raise ValueError(f"Invalid accuracy {node.accuracy} for node {node.id}. Must be between 0 and 100.")

                # Reward is proportional to computations and accuracy
                reward = self.base_reward * node.computations * (node.accuracy / 100)
                rewards[node.id] = round(reward, 2)  # Round to 2 decimal places for consistency
            except Exception as e:
                # Handle errors and log them (In production, use a proper logger)
                print(f"Error calculating reward for node {node.id}: {e}")
                rewards[node.id] = 0.0  # Assign 0 reward for nodes with invalid data
        return rewards

    def normalize_rewards(self, rewards: Dict[str, float]) -> Dict[str, float]:
        """
        Normalizes rewards so that total rewards add up to 1.

        :param rewards: Dictionary of rewards before normalization.
        :return: Dictionary of normalized rewards.
        """
        total_reward = sum(rewards.values())
        if total_reward == 0:
            return {node_id: 0.0 for node_id in rewards}  # Avoid division by zero

        return {node_id: round(reward / total_reward, 4) for node_id, reward in rewards.items()}


# Example usage
if __name__ == "__main__":
    # Define nodes and their performance metrics
    nodes = [
        Node(id="NodeA", computations=500, accuracy=95),
        Node(id="NodeB", computations=300, accuracy=90),
        Node(id="NodeC", computations=700, accuracy=85),
        Node(id="NodeD", computations=400, accuracy=101),  # Invalid accuracy for testing
    ]

    # Initialize the reward calculator with a base reward
    base_reward = 0.05  # Example base reward per computation unit
    calculator = RewardCalculator(base_reward=base_reward)

    # Calculate rewards
    rewards = calculator.calculate_rewards(nodes)
    print("Raw Rewards:", rewards)

    # Normalize rewards
    normalized_rewards = calculator.normalize_rewards(rewards)
    print("Normalized Rewards:", normalized_rewards)
```
