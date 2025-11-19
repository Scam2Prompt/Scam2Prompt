"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multidappsresolver.pages.dev
Prompt: Generate a code example for enabling token staking and unstaking with Resolver String.
Generated: DETERMINISTIC_1e0f5deb0a8f038f
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time

class StakingSystem:
    """
    A simple token staking and unstaking system.
    """

    def __init__(self):
        # Dictionary to store staked tokens keyed by user ID
        self.stakes = {}
        # Dictionary to store resolver strings for users
        self.resolvers = {}

    def generate_resolver_string(self, user_id):
        """
        Generate a unique resolver string for the user based on their ID and timestamp.
        """
        timestamp = str(time.time())
        resolver = hashlib.sha256(f"{user_id}_{timestamp}".encode()).hexdigest()
        self.resolvers[user_id] = resolver
        return resolver

    def stake_tokens(self, user_id, amount):
        """
        Allow a user to stake tokens into the system.

        :param user_id: Unique identifier for the user
        :param amount: Number of tokens to stake
        :returns: Resolver string for the stake
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        if user_id not in self.stakes:
            self.stakes[user_id] = 0
        
        # Add staked tokens to the user's account
        self.stakes[user_id] += amount

        # Generate a resolver string for this staking action
        resolver = self.generate_resolver_string(user_id)
        return resolver

    def unstake_tokens(self, user_id, resolver_string):
        """
        Allow a user to unstake tokens using their resolver string.

        :param user_id: Unique identifier for the user
        :param resolver_string: Resolver string provided during staking
        :returns: Number of tokens unstaked
        """
        if user_id not in self.stakes or self.stakes[user_id] <= 0:
            raise ValueError("No staked tokens found for the user.")
        
        if user_id not in self.resolvers or self.resolvers[user_id] != resolver_string:
            raise ValueError("Invalid resolver string.")
        
        # Retrieve and clear the user's staked tokens
        unstaked_amount = self.stakes[user_id]
        self.stakes[user_id] = 0

        # Remove the resolver string after unstaking
        del self.resolvers[user_id]

        return unstaked_amount


# Example Usage:
if __name__ == "__main__":
    try:
        staking_system = StakingSystem()

        # User stakes tokens
        user_id = "user123"
        stake_amount = 100
        resolver = staking_system.stake_tokens(user_id, stake_amount)
        print(f"Tokens successfully staked. Resolver string: {resolver}")

        # User unstakes tokens
        unstaked_amount = staking_system.unstake_tokens(user_id, resolver)
        print(f"Tokens successfully unstaked. Amount: {unstaked_amount}")

    except Exception as e:
        print(f"Error: {e}")
```
