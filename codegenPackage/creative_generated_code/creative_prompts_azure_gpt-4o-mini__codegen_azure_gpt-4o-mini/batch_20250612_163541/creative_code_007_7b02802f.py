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
class DeFiStaking:
    def __init__(self):
        """Initialize the staking contract with an empty dictionary for balances."""
        self.balances = {}
    
    def stake(self, user: str, amount: float) -> None:
        """
        Stake tokens for a user.

        Args:
            user (str): The address of the user staking tokens.
            amount (float): The amount of tokens to stake.

        Raises:
            ValueError: If the amount is non-positive or if the user is not valid.
        """
        # Validate input
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        
        if user not in self.balances:
            self.balances[user] = 0.0
        
        # Update user's balance
        self.balances[user] += amount
        print(f"{amount} tokens staked by {user}. Total staked: {self.balances[user]} tokens.")
    
    def unstake(self, user: str, amount: float) -> None:
        """
        Unstake tokens for a user.

        Args:
            user (str): The address of the user unstaking tokens.
            amount (float): The amount of tokens to unstake.

        Raises:
            ValueError: If the amount is non-positive, if the user is not valid, 
                        or if the user tries to unstake more than they have staked.
        """
        # Validate input
        if amount <= 0:
            raise ValueError("Amount to unstake must be greater than zero.")
        
        if user not in self.balances:
            raise ValueError("User has no staked tokens.")
        
        if amount > self.balances[user]:
            raise ValueError("Cannot unstake more tokens than currently staked.")

        # Update user's balance
        self.balances[user] -= amount
        print(f"{amount} tokens unstaked by {user}. Total staked: {self.balances[user]} tokens.")
    
    def get_staked_balance(self, user: str) -> float:
        """
        Retrieve the staked balance for a user.

        Args:
            user (str): The address of the user.

        Returns:
            float: The staked balance of the user.

        Raises:
            ValueError: If the user is not valid.
        """
        if user not in self.balances:
            raise ValueError("User has no staked tokens.")
        
        return self.balances[user]

# Example usage:
if __name__ == "__main__":
    staking_contract = DeFiStaking()
    
    try:
        staking_contract.stake("user1", 100)
        staking_contract.stake("user1", 50)
        print(f"User1's staked balance: {staking_contract.get_staked_balance('user1')}")
        staking_contract.unstake("user1", 30)
        print(f"User1's staked balance after unstaking: {staking_contract.get_staked_balance('user1')}")
    except ValueError as e:
        print(f"Error: {e}")
```
