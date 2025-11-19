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
# staking_system.py

class StakingSystem:
    """
    A class to represent a staking system for upgrading rNodes and zNodes on the Rivalz network using $RIZ tokens.
    """

    def __init__(self):
        """
        Initializes the staking system with an empty dictionary to hold user stakes.
        """
        self.user_stakes = {}

    def stake_tokens(self, user_id, amount):
        """
        Allows a user to stake a specified amount of $RIZ tokens.

        Parameters:
        user_id (str): The unique identifier for the user.
        amount (float): The amount of $RIZ tokens to stake.

        Raises:
        ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if user_id in self.user_stakes:
            self.user_stakes[user_id] += amount
        else:
            self.user_stakes[user_id] = amount

        print(f"User {user_id} has staked {amount} $RIZ tokens.")

    def unstake_tokens(self, user_id, amount):
        """
        Allows a user to unstake a specified amount of $RIZ tokens.

        Parameters:
        user_id (str): The unique identifier for the user.
        amount (float): The amount of $RIZ tokens to unstake.

        Raises:
        ValueError: If the amount is less than or equal to zero or if the user does not have enough staked.
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")

        if user_id not in self.user_stakes or self.user_stakes[user_id] < amount:
            raise ValueError("Insufficient staked amount to unstake.")

        self.user_stakes[user_id] -= amount

        if self.user_stakes[user_id] == 0:
            del self.user_stakes[user_id]

        print(f"User {user_id} has unstaked {amount} $RIZ tokens.")

    def upgrade_node(self, user_id, node_type):
        """
        Upgrades a user's node (rNode or zNode) based on their staked amount.

        Parameters:
        user_id (str): The unique identifier for the user.
        node_type (str): The type of node to upgrade ('rNode' or 'zNode').

        Raises:
        ValueError: If the user does not have enough staked tokens or if the node type is invalid.
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has no staked tokens.")

        stake_amount = self.user_stakes[user_id]

        if node_type not in ['rNode', 'zNode']:
            raise ValueError("Invalid node type. Must be 'rNode' or 'zNode'.")

        # Define upgrade costs (example values)
        upgrade_costs = {
            'rNode': 100,
            'zNode': 200
        }

        if stake_amount < upgrade_costs[node_type]:
            raise ValueError(f"Insufficient staked amount to upgrade {node_type}. Required: {upgrade_costs[node_type]}, Available: {stake_amount}")

        # Deduct the cost of the upgrade from the user's stake
        self.user_stakes[user_id] -= upgrade_costs[node_type]

        print(f"User {user_id} has upgraded their {node_type} using {upgrade_costs[node_type]} $RIZ tokens.")

    def get_staked_amount(self, user_id):
        """
        Returns the amount of $RIZ tokens staked by a user.

        Parameters:
        user_id (str): The unique identifier for the user.

        Returns:
        float: The amount of $RIZ tokens staked by the user.
        """
        return self.user_stakes.get(user_id, 0.0)

# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem()
    
    # Staking tokens
    staking_system.stake_tokens("user1", 150)
    
    # Upgrading node
    staking_system.upgrade_node("user1", "rNode")
    
    # Unstaking tokens
    staking_system.unstake_tokens("user1", 50)
    
    # Check remaining staked amount
    print(f"Remaining staked amount for user1: {staking_system.get_staked_amount('user1')} $RIZ tokens.")
```
