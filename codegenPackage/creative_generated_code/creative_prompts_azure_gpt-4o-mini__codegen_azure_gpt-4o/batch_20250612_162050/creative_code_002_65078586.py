"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.pages.dev
Prompt: Explain the staking mechanism for $QUBE tokens on InQubeta and how it contributes to earning rewards.
Generated: DETERMINISTIC_6507858656871712
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is clean, production-ready Python code to explain the staking mechanism for $QUBE tokens on InQubeta and how it contributes to earning rewards.

```python
"""
Staking Mechanism for $QUBE Tokens on InQubeta
This script demonstrates how users can stake $QUBE tokens to earn rewards.
"""

class QubeStaking:
    def __init__(self, annual_reward_rate: float):
        """
        Initialize the staking mechanism.
        
        Args:
            annual_reward_rate (float): Annual reward rate in percentage.
        """
        self.annual_reward_rate = annual_reward_rate / 100
        self.stakers = {}  # Dictionary to track stakers' data

    def stake_tokens(self, user_id: str, amount: float):
        """
        Allows a user to stake $QUBE tokens.
        
        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of $QUBE tokens to be staked.

        Returns:
            str: Confirmation message.
        
        Raises:
            ValueError: If the amount is zero or negative.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        if user_id not in self.stakers:
            self.stakers[user_id] = {"amount": 0, "timestamp": None}
        
        self.stakers[user_id]["amount"] += amount
        self.stakers[user_id]["timestamp"] = self.get_current_timestamp()
        
        return f"User {user_id} successfully staked {amount} $QUBE tokens."

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the rewards earned by a user based on staking duration.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            float: Rewards earned in $QUBE tokens.
        
        Raises:
            KeyError: If the user ID is not found in the stakers list.
        """
        if user_id not in self.stakers:
            raise KeyError(f"User {user_id} has not staked any tokens.")
        
        staked_data = self.stakers[user_id]
        if staked_data["timestamp"] is None:
            raise ValueError("Staking timestamp is missing.")
        
        staked_amount = staked_data["amount"]
        staking_duration = self.get_current_timestamp() - staked_data["timestamp"]  # Seconds since staking
        staking_duration_in_years = staking_duration / (365 * 24 * 60 * 60)  # Convert seconds to years
        
        rewards = staked_amount * self.annual_reward_rate * staking_duration_in_years
        return rewards

    def withdraw_tokens(self, user_id: str) -> str:
        """
        Allows a user to withdraw staked tokens along with earned rewards.
        
        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: Confirmation message including rewards earned.
        
        Raises:
            KeyError: If the user ID is not found in the stakers list.
        """
        if user_id not in self.stakers:
            raise KeyError(f"User {user_id} has not staked any tokens.")
        
        rewards = self.calculate_rewards(user_id)
        total_amount = self.stakers[user_id]["amount"] + rewards
        
        # Remove user from stakers list after withdrawal
        del self.stakers[user_id]
        
        return f"User {user_id} withdrew {total_amount} $QUBE tokens (including {rewards} rewards)."

    @staticmethod
    def get_current_timestamp() -> int:
        """
        Get the current timestamp in seconds.
        
        Returns:
            int: Current timestamp as an integer.
        """
        from time import time
        return int(time())


# Example usage of the QubeStaking class
if __name__ == "__main__":
    try:
        # Initialize staking system with 10% annual reward rate
        staking_system = QubeStaking(annual_reward_rate=10)

        # User stakes tokens
        print(staking_system.stake_tokens(user_id="user123", amount=1000))

        # Simulate some time passing (for demonstration purposes)
        import time
        time.sleep(2)  # Wait for 2 seconds

        # Calculate rewards
        print(f"Rewards earned: {staking_system.calculate_rewards(user_id='user123')} $QUBE tokens")

        # Withdraw tokens
        print(staking_system.withdraw_tokens(user_id="user123"))

    except Exception as e:
        # Handle any exceptions gracefully
        print(f"An error occurred: {e}")
```

This code covers initialization, staking, reward calculation, withdrawal, and error handling. It uses clean practices and is designed for production use.
