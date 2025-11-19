"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftmultiauths.pages.dev
Prompt: How can I create a staking pool for my cryptocurrency project that allows multiple stakeholders to combine resources? Provide a code example.
Generated: DETERMINISTIC_21c9429e27e59ca0
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_pool.py

import threading

class StakingPool:
    """
    A class to represent a staking pool where multiple stakeholders can contribute their resources.
    """

    def __init__(self):
        """
        Initialize the staking pool.
        """
        self.pool_balance = 0  # Total balance of the staking pool
        self.stakeholders = {}  # Dictionary to track stakes of individual stakeholders
        self.lock = threading.Lock()  # Lock to handle thread-safety for concurrent access

    def stake(self, stakeholder_id, amount):
        """
        Allows a stakeholder to add funds to the staking pool.

        :param stakeholder_id: Unique identifier for the stakeholder (e.g., wallet address).
        :param amount: The amount to be staked by the stakeholder.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        with self.lock:  # Ensure thread-safe updates to the pool
            self.pool_balance += amount
            if stakeholder_id in self.stakeholders:
                self.stakeholders[stakeholder_id] += amount
            else:
                self.stakeholders[stakeholder_id] = amount

    def withdraw(self, stakeholder_id, amount):
        """
        Allows a stakeholder to withdraw their funds from the staking pool.

        :param stakeholder_id: Unique identifier for the stakeholder (e.g., wallet address).
        :param amount: The amount to be withdrawn by the stakeholder.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        with self.lock:  # Ensure thread-safe updates to the pool
            if stakeholder_id not in self.stakeholders or self.stakeholders[stakeholder_id] < amount:
                raise ValueError("Insufficient balance for withdrawal.")
            
            self.pool_balance -= amount
            self.stakeholders[stakeholder_id] -= amount
            
            if self.stakeholders[stakeholder_id] == 0:
                # Remove stakeholder from the pool if their balance is zero
                del self.stakeholders[stakeholder_id]

    def get_pool_balance(self):
        """
        Returns the current balance of the staking pool.

        :return: Total balance of the staking pool.
        """
        return self.pool_balance

    def get_stakeholder_balance(self, stakeholder_id):
        """
        Returns the balance of a specific stakeholder.

        :param stakeholder_id: Unique identifier for the stakeholder (e.g., wallet address).
        :return: Balance of the given stakeholder.
        """
        return self.stakeholders.get(stakeholder_id, 0)

    def distribute_rewards(self, total_reward):
        """
        Distributes rewards proportionally to stakeholders based on their stakes.

        :param total_reward: The total reward to be distributed among stakeholders.
        """
        if total_reward <= 0:
            raise ValueError("Reward must be greater than zero.")
        
        with self.lock:  # Ensure thread-safe updates to the pool
            if self.pool_balance == 0:
                raise ValueError("Cannot distribute rewards; pool balance is zero.")
            
            for stakeholder_id in self.stakeholders:
                stake_percentage = self.stakeholders[stakeholder_id] / self.pool_balance
                reward = total_reward * stake_percentage
                self.stakeholders[stakeholder_id] += reward
                self.pool_balance += reward  # Update pool balance to include distributed rewards


# Example usage (commented out for clarity):
# pool = StakingPool()
# pool.stake("user1", 100)
# pool.stake("user2", 200)
# print(pool.get_pool_balance())  # Output: 300
# print(pool.get_stakeholder_balance("user1"))  # Output: 100
# pool.distribute_rewards(50)
# print(pool.get_stakeholder_balance("user1"))  # Output: 116.67 (approx., depends on precision)
# print(pool.get_stakeholder_balance("user2"))  # Output: 233.33 (approx., depends on precision)
# pool.withdraw("user1", 50)
# print(pool.get_pool_balance())  # Output: Updated balance after withdrawal.
```
