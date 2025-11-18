"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-dashboards-inqubeta.pages.dev
Prompt: Provide an example of how to integrate $QUBE token staking reward calculations into a custom cryptocurrency portfolio tracker.
Generated: DETERMINISTIC_ce64af4135175a24
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from decimal import Decimal
from typing import List, Dict

# Constants
SECONDS_IN_YEAR = Decimal(31536000)  # Seconds in a year used for APY calculation

class QubeTokenStaking:
    """
    A class to calculate staking rewards for $QUBE tokens.
    """
    def __init__(self, annual_percentage_yield: Decimal):
        """
        Initialize the staking reward calculator.

        :param annual_percentage_yield: Annual percentage yield (APY) for staking $QUBE tokens.
        """
        self.apy = annual_percentage_yield

    def calculate_daily_reward(self, amount_staked: Decimal, days_staked: int) -> Decimal:
        """
        Calculate the daily staking reward based on the APY and the amount of tokens staked.

        :param amount_staked: Amount of $QUBE tokens staked.
        :param days_staked: Number of days the tokens were staked.
        :return: The total reward earned for the given staking period.
        """
        daily_rate = self.apy / Decimal(365)  # Convert APY to daily rate
        total_reward = amount_staked * daily_rate * Decimal(days_staked)
        return total_reward

    def calculate_reward(self, amount_staked: Decimal, start_date: datetime.date, end_date: datetime.date) -> Decimal:
        """
        Calculate the total reward earned for staking $QUBE tokens over a given period.

        :param amount_staked: Amount of $QUBE tokens staked.
        :param start_date: The start date of the staking period.
        :param end_date: The end date of the staking period.
        :return: The total reward earned for the given staking period.
        """
        if end_date < start_date:
            raise ValueError("End date cannot be earlier than start date.")
        days_staked = (end_date - start_date).days
        return self.calculate_daily_reward(amount_staked, days_staked)


class CryptoPortfolioTracker:
    """
    A portfolio tracker for managing cryptocurrency holdings, including $QUBE staking.
    """
    def __init__(self):
        """
        Initialize the portfolio tracker with an empty holdings dictionary.
        """
        self.holdings: Dict[str, Decimal] = {}
        self.staking_rewards: List[Dict[str, Decimal]] = []

    def add_holding(self, token_name: str, amount: Decimal):
        """
        Add or update holdings to the portfolio.

        :param token_name: Name of the cryptocurrency token.
        :param amount: Amount of tokens to add.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        if token_name in self.holdings:
            self.holdings[token_name] += amount
        else:
            self.holdings[token_name] = amount

    def calculate_qube_staking_rewards(self, qube_staking: QubeTokenStaking, amount_staked: Decimal, start_date: datetime.date, end_date: datetime.date):
        """
        Calculate staking rewards for $QUBE tokens and update the portfolio tracker.

        :param qube_staking: An instance of QubeTokenStaking.
        :param amount_staked: Amount of $QUBE tokens staked.
        :param start_date: The start date of the staking period.
        :param end_date: The end date of the staking period.
        """
        if "QUBE" not in self.holdings or self.holdings["QUBE"] < amount_staked:
            raise ValueError("Insufficient $QUBE tokens in holdings for staking.")

        reward = qube_staking.calculate_reward(amount_staked, start_date, end_date)
        self.staking_rewards.append({
            "token": "QUBE",
            "amount_staked": amount_staked,
            "start_date": start_date,
            "end_date": end_date,
            "reward": reward
        })

    def display_portfolio(self):
        """
        Display the current holdings and staking rewards in the portfolio.
        """
        print("Portfolio Holdings:")
        for token, amount in self.holdings.items():
            print(f"{token}: {amount}")

        print("\nStaking Rewards:")
        for reward in self.staking_rewards:
            print(f"Token: {reward['token']}, Staked: {reward['amount_staked']}, "
                  f"Start Date: {reward['start_date']}, End Date: {reward['end_date']}, "
                  f"Reward: {reward['reward']}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize portfolio tracker and staking reward calculator
        portfolio_tracker = CryptoPortfolioTracker()
        qube_staking = QubeTokenStaking(annual_percentage_yield=Decimal("0.15"))  # 15% APY
        
        # Add $QUBE tokens to portfolio
        portfolio_tracker.add_holding("QUBE", Decimal("1000"))
        
        # Calculate staking rewards for $QUBE tokens
        staking_start_date = datetime.date(2023, 1, 1)
        staking_end_date = datetime.date(2023, 12, 31)
        portfolio_tracker.calculate_qube_staking_rewards(
            qube_staking,
            amount_staked=Decimal("500"),
            start_date=staking_start_date,
            end_date=staking_end_date
        )
        
        # Display portfolio and staking rewards
        portfolio_tracker.display_portfolio()
    except Exception as e:
        print(f"Error: {e}")
```
