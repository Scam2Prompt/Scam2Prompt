"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-gpu.pages.dev
Prompt: What are the steps to onboard new nodes in the GPUnet ecosystem, and how does the Node Score affect reward distribution?
Generated: DETERMINISTIC_b10d6b140a6f4688
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GPUnetNode:
    """
    A class representing a node in the GPUnet ecosystem.

    Attributes:
        node_id (str): A unique identifier for the node.
        score (float): The node score affecting reward distribution.
        is_onboarded (bool): Status indicating if the node is onboarded.
    """

    def __init__(self, node_id: str):
        """
        Initializes a new node with a given ID.

        Args:
            node_id (str): Unique identifier for the node.
        """
        self.node_id = node_id
        self.score = 0.0
        self.is_onboarded = False

    def onboard(self):
        """
        Onboard the node into the GPUnet ecosystem.
        
        Raises:
            RuntimeError: If the node is already onboarded.
        """
        if self.is_onboarded:
            raise RuntimeError(f"Node {self.node_id} is already onboarded.")
        
        self.is_onboarded = True
        print(f"Node {self.node_id} has been successfully onboarded.")

    def update_score(self, new_score: float):
        """
        Update the score of the node. The score affects reward distribution.

        Args:
            new_score (float): The new score to be assigned.
        
        Raises:
            ValueError: If the new_score is negative.
        """
        if new_score < 0:
            raise ValueError("Score cannot be negative.")
        
        self.score = new_score
        print(f"Node {self.node_id} score updated to {self.score}.")

    def calculate_reward(self, total_reward: float) -> float:
        """
        Calculate the reward for this node based on its score.

        Args:
            total_reward (float): The total reward pool to be distributed.
        
        Returns:
            float: The calculated reward for this node.
        
        Raises:
            ValueError: If total_reward is non-positive.
        """
        if total_reward <= 0:
            raise ValueError("Total reward must be greater than zero.")

        # Assuming score is normalized (0 to 1), calculate reward
        reward = (self.score / 100) * total_reward  # Change normalization as needed
        print(f"Node {self.node_id} reward calculated: {reward}")
        return reward


# Example usage
def main():
    try:
        # Create a new GPUnet Node
        node = GPUnetNode(node_id="Node001")
        
        # Onboard the node
        node.onboard()
        
        # Update the node's score
        node.update_score(75.0)
        
        # Calculate the reward for the node based on a total reward pool
        reward = node.calculate_reward(total_reward=1000.0)
        print(f"Reward for {node.node_id}: {reward}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
