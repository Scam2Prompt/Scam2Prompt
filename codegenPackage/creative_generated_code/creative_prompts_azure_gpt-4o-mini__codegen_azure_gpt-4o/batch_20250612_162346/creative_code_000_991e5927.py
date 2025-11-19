"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackder.pages.dev
Prompt: How can I implement a staking feature for a cryptocurrency like $BLD with an APR of 200%?
Generated: DETERMINISTIC_991e5927e9d2fdda
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class Staking:
    """
    A class to implement staking functionality for a cryptocurrency.
    """
    def __init__(self, apr_percentage: float):
        """
        Initializes the staking feature with a given APR.

        :param apr_percentage: Annual Percentage Rate in percentage (e.g., 200 for 200%).
        """
        if apr_percentage <= 0:
            raise ValueError("APR must be greater than 0.")
        self.apr = apr_percentage / 100  # Convert APR percentage to a decimal

    def calculate_rewards(self, staked_amount: float, days_staked: int) -> float:
        """
        Calculates staking rewards based on the staked amount and staking duration.

        :param staked_amount: Amount of cryptocurrency staked.
        :param days_staked: Duration of staking in days.
        :return: Rewards earned over the staking period.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than 0.")
        if days_staked < 0:
            raise ValueError("Days staked must be non-negative.")

        # Formula: rewards = principal * (APR/365) * days_staked
        daily_rate = self.apr / 365  # Divide APR by days in a year
        rewards = staked_amount * daily_rate * days_staked
        return rewards

    def stake(self, user_wallet: dict, staked_amount: float):
        """
        Allows a user to stake a specific amount.

        :param user_wallet: A dictionary representing the user's wallet, with keys:
                            'balance': Current wallet balance.
                            'staked': Current staked amount.
                            'stake_start': Start date of staking.
        :param staked_amount: Amount to be staked.
        """
        if user_wallet['balance'] < staked_amount:
            raise ValueError("Insufficient funds to stake.")
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than 0.")

        user_wallet['balance'] -= staked_amount
        user_wallet['staked'] += staked_amount
        user_wallet['stake_start'] = datetime.now()  # Record the start time of staking

    def unstake(self, user_wallet: dict):
        """
        Allows a user to unstake their staked amount and collect rewards.

        :param user_wallet: A dictionary representing the user's wallet, with keys:
                            'balance': Current wallet balance.
                            'staked': Current staked amount.
                            'stake_start': Start date of staking.
        :return: Tuple containing (unstaked amount, rewards earned).
        """
        if user_wallet['staked'] <= 0:
            raise ValueError("No funds are currently staked.")

        # Calculate time staked
        stake_start_date = user_wallet['stake_start']
        days_staked = (datetime.now() - stake_start_date).days

        # Calculate rewards
        rewards = self.calculate_rewards(user_wallet['staked'], days_staked)

        # Transfer staked amount + rewards back to balance
        unstaked_amount = user_wallet['staked']
        user_wallet['balance'] += unstaked_amount + rewards
        user_wallet['staked'] = 0  # Reset staked amount
        user_wallet['stake_start'] = None  # Reset staking start date

        return unstaked_amount, rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize staking feature with 200% APR
        staking_feature = Staking(apr_percentage=200)

        # Example user wallet
        user_wallet = {
            "balance": 1000,  # Balance in the wallet
            "staked": 0,      # Amount staked
            "stake_start": None  # Start date of staking
        }

        # Staking 500 units
        print("Staking 500 units...")
        staking_feature.stake(user_wallet, staked_amount=500)

        print("Wallet after staking:", user_wallet)

        # Simulate waiting for staking rewards (e.g., 30 days later)
        user_wallet['stake_start'] -= timedelta(days=30)  # Mock time manipulation for testing

        # Unstaking funds and collecting rewards
        print("Unstaking...")
        unstaked_amount, rewards = staking_feature.unstake(user_wallet)

        print(f"Unstaked Amount: {unstaked_amount}, Rewards Earned: {rewards}")
        print("Wallet after unstaking:", user_wallet)

    except Exception as e:
        print(f"Error: {e}")
```
