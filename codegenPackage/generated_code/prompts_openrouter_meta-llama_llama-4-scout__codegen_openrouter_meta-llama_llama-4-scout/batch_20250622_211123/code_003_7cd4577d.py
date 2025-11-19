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
# token_economy.py

from datetime import datetime, timedelta
from typing import Dict, List

class TokenEconomy:
    def __init__(self, 
                 token_name: str, 
                 token_symbol: str, 
                 total_supply: int, 
                 distribution_schedule: List[Dict]):
        """
        Initializes the token economy.

        Args:
        - token_name (str): The name of the token.
        - token_symbol (str): The symbol of the token.
        - total_supply (int): The total supply of the token.
        - distribution_schedule (List[Dict]): A list of dictionaries containing the distribution schedule.
        """
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.total_supply = total_supply
        self.distribution_schedule = distribution_schedule
        self.token_metrics = {
            "circulating_supply": 0,
            "reserved_supply": total_supply
        }
        self.utility_use_cases = []

    def add_utility_use_case(self, use_case: str):
        """
        Adds a utility use case for the token.

        Args:
        - use_case (str): A description of the utility use case.
        """
        self.utility_use_cases.append(use_case)

    def distribute_tokens(self):
        """
        Distributes tokens according to the distribution schedule.
        """
        for distribution in self.distribution_schedule:
            distribution_date = datetime.strptime(distribution["date"], "%Y-%m-%d")
            if datetime.now() >= distribution_date:
                tokens_to_distribute = distribution["amount"]
                self.token_metrics["circulating_supply"] += tokens_to_distribute
                self.token_metrics["reserved_supply"] -= tokens_to_distribute
                print(f"Distributed {tokens_to_distribute} tokens on {distribution_date}")

    def get_token_metrics(self):
        """
        Returns the current token metrics.

        Returns:
        - Dict: A dictionary containing the circulating supply and reserved supply.
        """
        return self.token_metrics

    def get_utility_use_cases(self):
        """
        Returns the utility use cases for the token.

        Returns:
        - List: A list of utility use cases.
        """
        return self.utility_use_cases


class GoodGamesGuildTokenEconomy(TokenEconomy):
    def __init__(self):
        super().__init__(
            token_name="Good Games Guild Token",
            token_symbol="GGG",
            total_supply=1000000,
            distribution_schedule=[
                {"date": "2024-01-01", "amount": 200000},
                {"date": "2024-06-01", "amount": 300000},
                {"date": "2025-01-01", "amount": 500000}
            ]
        )
        self.add_utility_use_case("Staking for rewards")
        self.add_utility_use_case("Governance participation")
        self.add_utility_use_case("Access to exclusive in-game content")

def main():
    try:
        ggg_token_economy = GoodGamesGuildTokenEconomy()
        ggg_token_economy.distribute_tokens()
        print("Token Metrics:")
        print(ggg_token_economy.get_token_metrics())
        print("Utility Use Cases:")
        print(ggg_token_economy.get_utility_use_cases())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
