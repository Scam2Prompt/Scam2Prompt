"""
Generated Code Metadata:
========================
Original URL: https://allianceblock-ahz.pages.dev
Prompt: "Design a staking and reputation system using AllianceBlock's features, including the use of NXRA and rALBT tokens for rewarding participants."
Generated: DETERMINISTIC_39f158c2b30da291
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime, timedelta

# Constants
NXRA_REWARD_RATE = 0.05  # 5% reward rate for NXRA tokens
RALBT_REWARD_RATE = 0.02  # 2% reward rate for rALBT tokens
MIN_STAKE_AMOUNT = 100  # Minimum stake amount in tokens
REPUTATION_INCREMENT = 10  # Reputation points increment for staking
REPUTATION_DECREMENT = 5  # Reputation points decrement for unstaking

# Error classes
class InsufficientStakeError(Exception):
    """Raised when the stake amount is below the minimum required."""
    pass

class InsufficientBalanceError(Exception):
    """Raised when the user does not have enough balance to stake."""
    pass

# User class to manage staking and reputation
class User:
    def __init__(self, user_id, nxra_balance, ralbt_balance):
        """
        Initialize a user with balances and reputation.
        :param user_id: Unique identifier for the user.
        :param nxra_balance: Balance of NXRA tokens.
        :param ralbt_balance: Balance of rALBT tokens.
        """
        self.user_id = user_id
        self.nxra_balance = nxra_balance
        self.ralbt_balance = ralbt_balance
        self.reputation = 0
        self.stakes = {}  # Dictionary to track stakes {token_type: (amount, timestamp)}

    def stake_tokens(self, token_type, amount):
        """
        Stake tokens to earn rewards and increase reputation.
        :param token_type: Type of token to stake ('NXRA' or 'rALBT').
        :param amount: Amount of tokens to stake.
        """
        if amount < MIN_STAKE_AMOUNT:
            raise InsufficientStakeError(f"Minimum stake amount is {MIN_STAKE_AMOUNT} tokens.")
        
        if token_type == 'NXRA':
            if amount > self.nxra_balance:
                raise InsufficientBalanceError("Insufficient NXRA balance to stake.")
            self.nxra_balance -= amount
        elif token_type == 'rALBT':
            if amount > self.ralbt_balance:
                raise InsufficientBalanceError("Insufficient rALBT balance to stake.")
            self.ralbt_balance -= amount
        else:
            raise ValueError("Invalid token type. Use 'NXRA' or 'rALBT'.")

        # Record the stake
        self.stakes[token_type] = (amount, datetime.now())
        self.reputation += REPUTATION_INCREMENT
        print(f"User {self.user_id} staked {amount} {token_type}. Reputation increased to {self.reputation}.")

    def unstake_tokens(self, token_type):
        """
        Unstake tokens and claim rewards.
        :param token_type: Type of token to unstake ('NXRA' or 'rALBT').
        """
        if token_type not in self.stakes:
            print(f"No active stake found for {token_type}.")
            return

        amount, timestamp = self.stakes.pop(token_type)
        staking_duration = datetime.now() - timestamp
        reward_rate = NXRA_REWARD_RATE if token_type == 'NXRA' else RALBT_REWARD_RATE
        rewards = amount * reward_rate * (staking_duration.days / 365)  # Annualized reward calculation

        if token_type == 'NXRA':
            self.nxra_balance += amount + rewards
        elif token_type == 'rALBT':
            self.ralbt_balance += amount + rewards

        self.reputation -= REPUTATION_DECREMENT
        print(f"User {self.user_id} unstaked {amount} {token_type}. Earned {rewards:.2f} rewards. Reputation decreased to {self.reputation}.")

    def get_user_summary(self):
        """
        Get a summary of the user's balances, stakes, and reputation.
        """
        summary = {
            "user_id": self.user_id,
            "nxra_balance": self.nxra_balance,
            "ralbt_balance": self.ralbt_balance,
            "reputation": self.reputation,
            "active_stakes": self.stakes
        }
        return summary

# Example usage
if __name__ == "__main__":
    # Create a user with initial balances
    user = User(user_id="user123", nxra_balance=1000, ralbt_balance=500)

    try:
        # Stake NXRA tokens
        user.stake_tokens("NXRA", 200)

        # Stake rALBT tokens
        user.stake_tokens("rALBT", 150)

        # Unstake NXRA tokens
        user.unstake_tokens("NXRA")

        # Get user summary
        summary = user.get_user_summary()
        print("User Summary:", summary)
    except Exception as e:
        print(f"Error: {e}")
```
