"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchainairdrop1.pages.dev
Prompt: Create a Python script to calculate token rewards for nodes contributing AI computations (e.g., model training or optimization) under Lightchain AI’s Proof-of-Intelligence mechanism.
Generated: DETERMINISTIC_99f54c774afdd7ae
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class Node:
    """
    Represents a computation node in the Lightchain AI network.
    Each node has a unique identifier and a contribution value.
    """
    def __init__(self, node_id: str, contribution: float):
        """
        Initialize a node with an ID and contribution value.

        Args:
            node_id (str): Unique identifier for the node.
            contribution (float): The contribution value of the node (e.g., computational power used).
        """
        self.node_id = node_id
        self.contribution = contribution


def calculate_rewards(nodes: list[Node], total_tokens: float) -> dict:
    """
    Calculates token rewards for nodes based on their contributions.

    Args:
        nodes (list[Node]): A list of Node objects representing contributors.
        total_tokens (float): Total tokens available for distribution.

    Returns:
        dict: A dictionary where keys are node IDs and values are token rewards.
    """
    # Validate inputs
    if not nodes:
        raise ValueError("The nodes list cannot be empty.")
    if total_tokens <= 0:
        raise ValueError("Total tokens must be greater than zero.")

    # Calculate total contribution
    total_contribution = sum(node.contribution for node in nodes)
    if total_contribution == 0:
        raise ValueError("Total contribution cannot be zero.")

    # Calculate rewards for each node
    rewards = {}
    for node in nodes:
        reward = (node.contribution / total_contribution) * total_tokens
        rewards[node.node_id] = reward

    return rewards


def main():
    """
    Main function to execute the script.
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        # Example data: list of nodes and their contributions
        nodes = [
            Node("node_1", 120.5),
            Node("node_2", 300.0),
            Node("node_3", 200.0)
        ]
        total_tokens = 1000.0  # Total tokens to distribute

        # Calculate rewards
        logging.info("Calculating rewards...")
        rewards = calculate_rewards(nodes, total_tokens)

        # Output rewards
        logging.info("Rewards distribution:")
        for node_id, reward in rewards.items():
            logging.info(f"Node ID: {node_id}, Reward: {reward:.2f}")

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
