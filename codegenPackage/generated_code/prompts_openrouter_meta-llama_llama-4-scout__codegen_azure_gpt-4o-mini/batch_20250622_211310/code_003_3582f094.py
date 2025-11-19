"""
Generated Code Metadata:
========================
Original URL: https://immediatefrontier.app
Prompt: "Design a simple investment portfolio tracker using a programming language of your choice, inspired by the investment essentials discussed on Immediate Frontier."
Generated: DETERMINISTIC_3582f0940278afbf
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Investment:
    """Class to represent an individual investment."""
    
    def __init__(self, name: str, amount: float, price_per_unit: float):
        """
        Initialize an investment.

        :param name: Name of the investment (e.g., stock name).
        :param amount: Number of units owned.
        :param price_per_unit: Current price per unit of the investment.
        """
        self.name = name
        self.amount = amount
        self.price_per_unit = price_per_unit

    def total_value(self) -> float:
        """Calculate the total value of the investment."""
        return self.amount * self.price_per_unit

    def __str__(self) -> str:
        """String representation of the investment."""
        return f"{self.name}: {self.amount} units at ${self.price_per_unit:.2f} each"

class Portfolio:
    """Class to represent an investment portfolio."""
    
    def __init__(self):
        """Initialize an empty portfolio."""
        self.investments: List[Investment] = []

    def add_investment(self, investment: Investment):
        """
        Add an investment to the portfolio.

        :param investment: An instance of Investment to add.
        """
        self.investments.append(investment)

    def total_portfolio_value(self) -> float:
        """Calculate the total value of the portfolio."""
        return sum(investment.total_value() for investment in self.investments)

    def display_portfolio(self):
        """Display the details of the portfolio."""
        print("Investment Portfolio:")
        for investment in self.investments:
            print(investment)
        print(f"Total Portfolio Value: ${self.total_portfolio_value():.2f}")

    def save_to_file(self, filename: str):
        """
        Save the portfolio to a JSON file.

        :param filename: The name of the file to save the portfolio.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([investment.__dict__ for investment in self.investments], file)
            print(f"Portfolio saved to {filename}.")
        except IOError as e:
            print(f"Error saving portfolio to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load the portfolio from a JSON file.

        :param filename: The name of the file to load the portfolio from.
        """
        try:
            with open(filename, 'r') as file:
                investments_data = json.load(file)
                self.investments = [Investment(**data) for data in investments_data]
            print(f"Portfolio loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading portfolio from file: {e}")

# Example usage
if __name__ == "__main__":
    portfolio = Portfolio()
    
    # Adding investments
    portfolio.add_investment(Investment("AAPL", 10, 150.00))
    portfolio.add_investment(Investment("GOOGL", 5, 2800.00))
    
    # Displaying portfolio
    portfolio.display_portfolio()
    
    # Saving portfolio to a file
    portfolio.save_to_file("portfolio.json")
    
    # Loading portfolio from a file
    new_portfolio = Portfolio()
    new_portfolio.load_from_file("portfolio.json")
    new_portfolio.display_portfolio()
```
