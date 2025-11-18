"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Write code to generate a leaderboard of top investors based on their investment amounts, similar to the "Top Investors" section on Finance Impact Pro.
Generated: DETERMINISTIC_3255b1b0e0592292
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

import json
from typing import List, Dict

class Investor:
    """Class representing an investor with a name and total investment amount."""
    
    def __init__(self, name: str, investment_amount: float):
        """
        Initializes an Investor object.

        Args:
            name (str): The name of the investor.
            investment_amount (float): The total investment amount of the investor.
        """
        self.name = name
        self.investment_amount = investment_amount

    def __repr__(self):
        """Returns a string representation of the Investor object."""
        return f"{self.name}: ${self.investment_amount:,.2f}"


class Leaderboard:
    """Class to manage a leaderboard of investors."""
    
    def __init__(self):
        """Initializes an empty leaderboard."""
        self.investors: List[Investor] = []

    def add_investor(self, name: str, investment_amount: float):
        """
        Adds an investor to the leaderboard.

        Args:
            name (str): The name of the investor.
            investment_amount (float): The investment amount to add.

        Raises:
            ValueError: If investment_amount is negative.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount cannot be negative.")
        
        investor = Investor(name, investment_amount)
        self.investors.append(investor)

    def get_top_investors(self, top_n: int = 10) -> List[Investor]:
        """
        Retrieves the top investors sorted by investment amount.

        Args:
            top_n (int): The number of top investors to retrieve.

        Returns:
            List[Investor]: A list of the top investors.
        """
        # Sort investors by investment amount in descending order
        sorted_investors = sorted(self.investors, key=lambda x: x.investment_amount, reverse=True)
        return sorted_investors[:top_n]

    def to_json(self) -> str:
        """Converts the leaderboard to a JSON string."""
        leaderboard_data = [{"name": investor.name, "investment_amount": investor.investment_amount} for investor in self.investors]
        return json.dumps(leaderboard_data, indent=4)


def main():
    """Main function to demonstrate leaderboard functionality."""
    leaderboard = Leaderboard()
    
    # Sample data for investors
    sample_investors = [
        ("Alice", 50000),
        ("Bob", 75000),
        ("Charlie", 30000),
        ("David", 120000),
        ("Eve", 65000),
    ]

    # Adding investors to the leaderboard
    for name, amount in sample_investors:
        try:
            leaderboard.add_investor(name, amount)
        except ValueError as e:
            print(f"Error adding investor {name}: {e}")

    # Display the top investors
    top_investors = leaderboard.get_top_investors(3)
    print("Top Investors:")
    for investor in top_investors:
        print(investor)

    # Output the leaderboard in JSON format
    print("\nLeaderboard in JSON format:")
    print(leaderboard.to_json())


if __name__ == "__main__":
    main()
```
