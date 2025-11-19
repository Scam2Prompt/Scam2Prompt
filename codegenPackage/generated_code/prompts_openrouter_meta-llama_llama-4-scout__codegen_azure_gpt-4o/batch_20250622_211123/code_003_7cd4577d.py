"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Design a token economy for a gaming guild, taking into account distribution schedules, token metrics, and utility use cases similar to those outlined in the Good Games Guild whitepaper.
Generated: DETERMINISTIC_7cd4577d331840ef
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class TokenEconomy:
    """
    A class to manage the token economy for a gaming guild.
    Includes distribution schedules, token metrics, and utility use cases.
    """

    def __init__(self, total_supply):
        """
        Initialize the token economy with a total supply of tokens.

        :param total_supply: Total number of tokens available in the economy.
        """
        self.total_supply = total_supply
        self.remaining_supply = total_supply
        self.distribution_schedule = []
        self.token_utility = {
            "staking_rewards": 0.0,
            "in-game_purchases": 0.0,
            "governance_voting": 0.0,
        }
        self.distributed_tokens = 0

    def add_distribution_schedule(self, recipient, amount, start_date, end_date):
        """
        Add a distribution schedule for tokens.

        :param recipient: The recipient of the tokens (e.g., "players", "developers").
        :param amount: The total amount of tokens to distribute.
        :param start_date: The start date of the distribution (datetime object).
        :param end_date: The end date of the distribution (datetime object).
        """
        if amount > self.remaining_supply:
            raise ValueError("Insufficient tokens available for distribution.")
        if start_date >= end_date:
            raise ValueError("Start date must be earlier than end date.")

        self.distribution_schedule.append({
            "recipient": recipient,
            "amount": amount,
            "start_date": start_date,
            "end_date": end_date,
            "distributed": 0
        })
        self.remaining_supply -= amount

    def distribute_tokens(self):
        """
        Distribute tokens according to the schedule.
        This function should be called periodically (e.g., daily).
        """
        current_date = datetime.now()
        for schedule in self.distribution_schedule:
            if schedule["start_date"] <= current_date <= schedule["end_date"]:
                # Calculate the daily distribution amount
                total_days = (schedule["end_date"] - schedule["start_date"]).days
                daily_amount = schedule["amount"] / total_days

                # Distribute tokens for the current day
                schedule["distributed"] += daily_amount
                self.distributed_tokens += daily_amount

                print(f"Distributed {daily_amount:.2f} tokens to {schedule['recipient']}.")

    def use_tokens(self, utility_type, amount):
        """
        Use tokens for a specific utility.

        :param utility_type: The type of utility (e.g., "staking_rewards", "in-game_purchases").
        :param amount: The amount of tokens to use.
        """
        if utility_type not in self.token_utility:
            raise ValueError("Invalid utility type.")
        if amount > self.distributed_tokens:
            raise ValueError("Insufficient distributed tokens available.")

        self.token_utility[utility_type] += amount
        self.distributed_tokens -= amount
        print(f"Used {amount:.2f} tokens for {utility_type}.")

    def get_token_metrics(self):
        """
        Get the current metrics of the token economy.

        :return: A dictionary containing token metrics.
        """
        return {
            "total_supply": self.total_supply,
            "remaining_supply": self.remaining_supply,
            "distributed_tokens": self.distributed_tokens,
            "token_utility": self.token_utility,
        }


# Example usage
if __name__ == "__main__":
    # Initialize the token economy with a total supply of 1,000,000 tokens
    guild_economy = TokenEconomy(total_supply=1_000_000)

    # Add distribution schedules
    guild_economy.add_distribution_schedule(
        recipient="players",
        amount=500_000,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=365)
    )
    guild_economy.add_distribution_schedule(
        recipient="developers",
        amount=300_000,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=180)
    )

    # Simulate daily token distribution
    for _ in range(10):  # Simulate 10 days
        guild_economy.distribute_tokens()
        time.sleep(1)  # Simulate a delay (e.g., daily execution)

    # Use tokens for staking rewards
    guild_economy.use_tokens(utility_type="staking_rewards", amount=10_000)

    # Print token metrics
    metrics = guild_economy.get_token_metrics()
    print("Token Metrics:", metrics)
```
