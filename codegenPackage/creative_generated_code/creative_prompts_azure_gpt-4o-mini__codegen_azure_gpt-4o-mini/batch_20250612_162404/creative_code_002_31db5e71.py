"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-bitcoinminetrix.pages.dev
Prompt: Can you explain the Stake-to-Mine concept and how it simplifies Bitcoin mining for everyday users on the Bitcoin Minetrix platform?
Generated: DETERMINISTIC_31db5e71f0453a9a
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakeToMine:
    """
    The StakeToMine class implements the Stake-to-Mine concept for the Bitcoin Minetrix platform,
    simplifying the Bitcoin mining process for everyday users.

    Attributes:
        user_balance (float): The amount of cryptocurrency staked by the user.
        mining_power (float): The mining power earned based on the user's stake.
    """
    
    def __init__(self, initial_balance: float):
        """
        Initializes the StakeToMine instance with a user balance.

        Args:
            initial_balance (float): The initial amount of cryptocurrency staked by the user.

        Raises:
            ValueError: If the initial balance is negative.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.user_balance = initial_balance
        self.mining_power = 0.0
        self.update_mining_power()
    
    def update_mining_power(self):
        """
        Updates the mining power based on the current user balance.
        The mining power is calculated as a fraction of the user balance.
        """
        # Assuming a fixed conversion rate for simplicity
        self.mining_power = self.user_balance * 0.1  # 10% of the stake

    def stake_more(self, amount: float):
        """
        Allows the user to stake more cryptocurrency.

        Args:
            amount (float): The additional amount of cryptocurrency to stake.

        Raises:
            ValueError: If the amount to stake is negative.
        """
        if amount < 0:
            raise ValueError("Amount to stake cannot be negative.")
        self.user_balance += amount
        self.update_mining_power()

    def withdraw_stake(self, amount: float):
        """
        Allows the user to withdraw a portion of their staked cryptocurrency.

        Args:
            amount (float): The amount of cryptocurrency to withdraw.

        Raises:
            ValueError: If the amount exceeds the user balance or is negative.
        """
        if amount < 0:
            raise ValueError("Amount to withdraw cannot be negative.")
        if amount > self.user_balance:
            raise ValueError("Withdrawal amount exceeds user balance.")
        self.user_balance -= amount
        self.update_mining_power()

    def get_user_status(self):
        """
        Returns the current status of the user including balance and mining power.

        Returns:
            dict: A dictionary containing the user balance and mining power.
        """
        return {
            "user_balance": self.user_balance,
            "mining_power": self.mining_power
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize user with a balance of 100 units
        user = StakeToMine(100.0)
        
        # User stakes an additional 50 units
        user.stake_more(50.0)
        
        # User withdraws 30 units
        user.withdraw_stake(30.0)
        
        # Display user status
        status = user.get_user_status()
        print("User Status:", status)

    except ValueError as e:
        print(f"Error: {e}")
```
