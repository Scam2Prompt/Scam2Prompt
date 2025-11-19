"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Explain the process of claiming rewards in the BurnedFi ecosystem, including how $build proofs reset after claiming.
Generated: DETERMINISTIC_7b0c60d6813032c0
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BurnedFiRewardSystem:
    """
    A class to manage the process of claiming rewards in the BurnedFi ecosystem.
    """

    def __init__(self):
        self.user_balances = {}  # Dictionary to hold user reward balances
        self.claimed_proofs = {}  # Dictionary to hold claimed proofs for users

    def add_user(self, user_id):
        """
        Add a new user to the reward system.
        
        Parameters:
            user_id (str): Unique identifier for the user.
        """
        if user_id in self.user_balances:
            raise ValueError(f"User {user_id} already exists.")
        self.user_balances[user_id] = 0
        self.claimed_proofs[user_id] = []

    def add_rewards(self, user_id, amount):
        """
        Add rewards to a user's balance.
        
        Parameters:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of rewards to add.
        """
        if user_id not in self.user_balances:
            raise ValueError(f"User {user_id} does not exist.")
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")
        
        self.user_balances[user_id] += amount

    def claim_rewards(self, user_id, proof):
        """
        Claim rewards for a user if the proof is valid and reset their proofs.
        
        Parameters:
            user_id (str): Unique identifier for the user.
            proof (str): A proof string that validates the claim.

        Returns:
            float: The amount of rewards claimed.
        """
        if user_id not in self.user_balances:
            raise ValueError(f"User {user_id} does not exist.")
        if proof in self.claimed_proofs[user_id]:
            raise ValueError("This proof has already been claimed.")

        # Assuming a simplistic reward claiming mechanism
        rewards_to_claim = self.user_balances[user_id]
        if rewards_to_claim <= 0:
            raise ValueError("No rewards available to claim.")

        # Update claimed proofs and reset the user's balance
        self.claimed_proofs[user_id].append(proof)
        self.user_balances[user_id] = 0  # Reset balance after claiming

        return rewards_to_claim

    def get_user_balance(self, user_id):
        """
        Get the current reward balance for a user.
        
        Parameters:
            user_id (str): Unique identifier for the user.
        
        Returns:
            float: The current reward balance of the user.
        """
        if user_id not in self.user_balances:
            raise ValueError(f"User {user_id} does not exist.")
        return self.user_balances[user_id]


# Example usage:
if __name__ == "__main__":
    reward_system = BurnedFiRewardSystem()
    try:
        reward_system.add_user("user1")
        reward_system.add_rewards("user1", 100.0)
        claimed_amount = reward_system.claim_rewards("user1", "proof_123")
        print(f"Claimed rewards: {claimed_amount}")
        
        current_balance = reward_system.get_user_balance("user1")
        print(f"Current balance after claiming: {current_balance}")

    except ValueError as e:
        print(f"Error: {e}")
```
