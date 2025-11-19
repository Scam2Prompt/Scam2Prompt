"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rangersprotocol.gitbook.io
Prompt: Can you write a function to calculate the block rewards for proposal nodes based on the RPG staking ratio in the Rangers Protocol?
Generated: DETERMINISTIC_1b1ba9393fd37a5e
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProposalNode:
    """
    A class to represent a proposal node in the Rangers Protocol.
    """

    def __init__(self, total_staked: float, node_staked: float):
        """
        Initializes a ProposalNode instance.

        :param total_staked: Total amount of RPG staked in the protocol.
        :param node_staked: Amount of RPG staked by this specific node.
        """
        if total_staked <= 0:
            raise ValueError("Total staked amount must be greater than zero.")
        if node_staked < 0:
            raise ValueError("Node staked amount cannot be negative.")

        self.total_staked = total_staked
        self.node_staked = node_staked

    def calculate_block_reward(self, total_reward: float) -> float:
        """
        Calculates the block rewards for the proposal node based on the RPG staking ratio.

        :param total_reward: Total block reward to be distributed among nodes.
        :return: The block reward allocated to this proposal node.
        """
        if total_reward < 0:
            raise ValueError("Total reward must be non-negative.")

        staking_ratio = self.node_staked / self.total_staked
        block_reward = staking_ratio * total_reward
        
        return block_reward


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize total and node staked values
        total_staked_amount = 10000.0  # Example total staked amount
        node_staked_amount = 2500.0     # Example node staked amount
        total_block_reward = 500.0      # Example total block reward

        # Create a proposal node instance
        proposal_node = ProposalNode(total_staked_amount, node_staked_amount)

        # Calculate the block reward for this node
        reward = proposal_node.calculate_block_reward(total_block_reward)

        print(f"The block reward for the proposal node is: {reward:.2f} RPG")
    
    except ValueError as e:
        print(f"Error: {e}")
```
