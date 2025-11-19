"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultrasizeprotocol.pages.dev
Prompt: Design a function to stake and unstake tokens while addressing common issues encountered in DeFi farming.
Generated: DETERMINISTIC_7b02802f1d710b9d
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: staking_system.py
# Description: A simplified staking and unstaking system for DeFi farming

class DeFiStaking:
    """
    A class to manage staking and unstaking tokens in a DeFi farming system.
    """

    def __init__(self):
        """
        Initialize the staking system with an empty ledger.
        """
        self.ledger = {}  # Stores user balances: {user_id: staked_amount}

    def stake_tokens(self, user_id, amount):
        """
        Stakes tokens for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to stake (must be positive).
        :return: Success message or an error.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount to stake must be greater than zero.")
            
            # Initialize user's balance if not already present
            if user_id not in self.ledger:
                self.ledger[user_id] = 0

            # Add the staked tokens to the user's balance
            self.ledger[user_id] += amount
            return f"Successfully staked {amount} tokens for user {user_id}."
        
        except Exception as e:
            return f"Error during staking: {str(e)}"

    def unstake_tokens(self, user_id, amount):
        """
        Unstakes tokens for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to unstake (must be positive).
        :return: Success message or an error.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount to unstake must be greater than zero.")
            
            if user_id not in self.ledger:
                raise ValueError("User not found.")
            
            if self.ledger[user_id] < amount:
                raise ValueError("Insufficient staked balance to unstake.")

            # Deduct the unstaked tokens from the user's balance
            self.ledger[user_id] -= amount
            return f"Successfully unstaked {amount} tokens for user {user_id}."
        
        except Exception as e:
            return f"Error during unstaking: {str(e)}"

    def get_staked_balance(self, user_id):
        """
        Gets the staked balance for a user.

        :param user_id: Unique identifier for the user.
        :return: The user's staked balance or an error if the user is not found.
        """
        try:
            if user_id not in self.ledger:
                raise ValueError("User not found.")

            return f"User {user_id} has {self.ledger[user_id]} tokens staked."
        
        except Exception as e:
            return f"Error fetching staked balance: {str(e)}"


# Example usage
if __name__ == "__main__":
    staking_system = DeFiStaking()

    print(staking_system.stake_tokens("user123", 100))  # Stake 100 tokens
    print(staking_system.get_staked_balance("user123"))  # Check balance
    print(staking_system.unstake_tokens("user123", 50))  # Unstake 50 tokens
    print(staking_system.get_staked_balance("user123"))  # Check balance
    print(staking_system.unstake_tokens("user123", 60))  # Attempt to unstake more than balance
```
