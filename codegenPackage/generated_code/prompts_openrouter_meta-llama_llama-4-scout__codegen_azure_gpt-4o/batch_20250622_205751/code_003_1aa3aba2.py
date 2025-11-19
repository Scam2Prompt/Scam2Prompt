"""
Generated Code Metadata:
========================
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: "Design a staking system for upgrading rNodes and zNodes on the Rivalz network using $RIZ tokens."
Generated: DETERMINISTIC_1aa3aba2ae4462ec
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class StakingSystem:
    """
    A staking system for upgrading rNodes and zNodes on the Rivalz network using $RIZ tokens.
    """

    def __init__(self):
        """
        Initialize the staking system with empty records for nodes and stakes.
        """
        self.stakes = {}  # Stores user stakes in the format: {user_id: {"rNodes": amount, "zNodes": amount}}
        self.upgrade_costs = {"rNodes": 100, "zNodes": 200}  # Cost in $RIZ tokens to upgrade each node type

    def stake_tokens(self, user_id, node_type, amount):
        """
        Allows a user to stake $RIZ tokens for upgrading nodes.

        :param user_id: Unique identifier for the user
        :param node_type: Type of node to stake for ("rNodes" or "zNodes")
        :param amount: Amount of $RIZ tokens to stake
        :raises ValueError: If node_type is invalid or amount is non-positive
        """
        if node_type not in self.upgrade_costs:
            raise ValueError("Invalid node type. Must be 'rNodes' or 'zNodes'.")
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Initialize user stake if not already present
        if user_id not in self.stakes:
            self.stakes[user_id] = {"rNodes": 0, "zNodes": 0}

        # Add the staked amount to the user's record
        self.stakes[user_id][node_type] += amount
        print(f"User {user_id} staked {amount} $RIZ tokens for {node_type}.")

    def upgrade_node(self, user_id, node_type):
        """
        Upgrades a node if the user has sufficient staked $RIZ tokens.

        :param user_id: Unique identifier for the user
        :param node_type: Type of node to upgrade ("rNodes" or "zNodes")
        :raises ValueError: If node_type is invalid or user has insufficient stake
        """
        if node_type not in self.upgrade_costs:
            raise ValueError("Invalid node type. Must be 'rNodes' or 'zNodes'.")
        if user_id not in self.stakes or self.stakes[user_id][node_type] < self.upgrade_costs[node_type]:
            raise ValueError(f"Insufficient staked $RIZ tokens to upgrade {node_type}.")

        # Deduct the upgrade cost from the user's stake
        self.stakes[user_id][node_type] -= self.upgrade_costs[node_type]
        print(f"User {user_id} successfully upgraded {node_type}.")

    def get_user_stake(self, user_id):
        """
        Retrieves the current stake information for a user.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing the user's stake for rNodes and zNodes
        """
        return self.stakes.get(user_id, {"rNodes": 0, "zNodes": 0})

    def display_staking_summary(self):
        """
        Displays a summary of all users' stakes in the system.
        """
        print("Staking Summary:")
        for user_id, stake in self.stakes.items():
            print(f"User {user_id}: rNodes: {stake['rNodes']} $RIZ, zNodes: {stake['zNodes']} $RIZ")


# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem()

    try:
        # Users staking tokens
        staking_system.stake_tokens("user1", "rNodes", 150)
        staking_system.stake_tokens("user2", "zNodes", 300)

        # Upgrading nodes
        staking_system.upgrade_node("user1", "rNodes")
        staking_system.upgrade_node("user2", "zNodes")

        # Displaying staking summary
        staking_system.display_staking_summary()

    except ValueError as e:
        print(f"Error: {e}")
```
