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
import json
from typing import List, Dict

class Node:
    def __init__(self, node_id: str, computation_power: float):
        """
        Initializes a new Node instance.

        :param node_id: Unique identifier for the node.
        :param computation_power: The computational power of the node.
        """
        self.node_id = node_id
        self.computation_power = computation_power
        self.rewards = 0.0

    def __repr__(self):
        return f"Node(node_id={self.node_id}, computation_power={self.computation_power}, rewards={self.rewards})"

def calculate_rewards(nodes: List[Node], total_reward: float) -> None:
    """
    Distributes rewards among nodes based on their computational power.

    :param nodes: List of nodes participating in computations.
    :param total_reward: Total reward to be distributed among nodes.
    :raises ValueError: If total_reward is less than or equal to zero.
    """
    if total_reward <= 0:
        raise ValueError("Total reward must be greater than zero.")

    total_power = sum(node.computation_power for node in nodes)
    
    if total_power == 0:
        raise ValueError("Total computation power cannot be zero.")

    for node in nodes:
        # Calculate individual reward based on proportion of computation power
        node.rewards = (node.computation_power / total_power) * total_reward

def serialize_rewards(nodes: List[Node]) -> str:
    """
    Serializes the rewards of the nodes to a JSON formatted string.

    :param nodes: List of nodes whose rewards are to be serialized.
    :return: JSON formatted string representing node rewards.
    """
    reward_data = {node.node_id: node.rewards for node in nodes}
    return json.dumps(reward_data, indent=4)

def main():
    """
    Main function to execute the rewards calculation and serialization.
    This function serves as an entry point for the script.
    """
    try:
        # Example node data
        nodes = [
            Node("node_1", 10.0),
            Node("node_2", 20.0),
            Node("node_3", 30.0)
        ]

        total_reward = 100.0  # Total reward to distribute

        # Calculate rewards
        calculate_rewards(nodes, total_reward)

        # Serialize and print the rewards
        rewards_json = serialize_rewards(nodes)
        print("Node Rewards:")
        print(rewards_json)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
