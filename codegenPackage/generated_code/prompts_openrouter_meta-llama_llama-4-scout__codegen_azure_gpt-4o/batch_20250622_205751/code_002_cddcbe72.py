"""
Generated Code Metadata:
========================
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Generate code to implement a reward calculator for $BANANA token holders, taking into account the APR, time ranges, and Solana rewards.
Generated: DETERMINISTIC_cddcbe72c86e19bd
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class RewardCalculator:
    """
    A class to calculate rewards for $BANANA token holders based on APR, time ranges, and Solana rewards.
    """

    def __init__(self, apr: float, solana_reward_rate: float):
        """
        Initialize the RewardCalculator.

        :param apr: Annual Percentage Rate (APR) as a percentage (e.g., 12.5 for 12.5% APR).
        :param solana_reward_rate: Solana reward rate per day (e.g., 0.01 SOL per day).
        """
        if apr < 0 or solana_reward_rate < 0:
            raise ValueError("APR and Solana reward rate must be non-negative.")
        self.apr = apr / 100  # Convert APR percentage to decimal
        self.solana_reward_rate = solana_reward_rate

    def calculate_rewards(self, token_balance: float, start_date: str, end_date: str) -> dict:
        """
        Calculate the rewards for a given token balance and time range.

        :param token_balance: The number of $BANANA tokens held.
        :param start_date: Start date in 'YYYY-MM-DD' format.
        :param end_date: End date in 'YYYY-MM-DD' format.
        :return: A dictionary containing the calculated rewards.
        """
        try:
            # Parse the input dates
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.") from e

        if start > end:
            raise ValueError("Start date must be earlier than or equal to end date.")

        # Calculate the number of days in the range
        days_held = (end - start).days + 1

        # Calculate $BANANA rewards based on APR
        banana_rewards = token_balance * self.apr * (days_held / 365)

        # Calculate Solana rewards
        solana_rewards = self.solana_reward_rate * days_held

        return {
            "banana_rewards": round(banana_rewards, 8),  # Rounded for precision
            "solana_rewards": round(solana_rewards, 8),
            "days_held": days_held
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reward calculator with APR and Solana reward rate
        calculator = RewardCalculator(apr=12.5, solana_reward_rate=0.01)

        # Define token balance and date range
        token_balance = 1000  # Example: 1000 $BANANA tokens
        start_date = "2023-01-01"
        end_date = "2023-12-31"

        # Calculate rewards
        rewards = calculator.calculate_rewards(token_balance, start_date, end_date)

        # Print the results
        print("Reward Calculation Results:")
        print(f"Days Held: {rewards['days_held']}")
        print(f"$BANANA Rewards: {rewards['banana_rewards']}")
        print(f"Solana Rewards: {rewards['solana_rewards']}")

    except Exception as e:
        print(f"Error: {e}")
```
