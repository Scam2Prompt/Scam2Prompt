"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: Develop a program to track and evaluate angel investments, similar to the portfolio management described by Memetic Digital.
Generated: DETERMINISTIC_e89c4e69869f651b
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Investment:
    """
    Class to represent an angel investment.
    """
    def __init__(self, name: str, amount: float, date: str, valuation: float):
        """
        Initialize an investment instance.

        :param name: Name of the startup.
        :param amount: Amount invested.
        :param date: Date of investment in 'YYYY-MM-DD' format.
        :param valuation: Valuation of the startup at the time of investment.
        """
        self.name = name
        self.amount = amount
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.valuation = valuation

    def __repr__(self) -> str:
        return f"Investment(name={self.name}, amount={self.amount}, date={self.date.date()}, valuation={self.valuation})"

class Portfolio:
    """
    Class to manage a portfolio of angel investments.
    """
    def __init__(self):
        """
        Initialize an empty portfolio.
        """
        self.investments: List[Investment] = []

    def add_investment(self, investment: Investment) -> None:
        """
        Add an investment to the portfolio.

        :param investment: Investment instance to add.
        """
        self.investments.append(investment)

    def evaluate_portfolio(self) -> Dict[str, Any]:
        """
        Evaluate the portfolio and return a summary.

        :return: A dictionary containing total investments and average valuation.
        """
        total_invested = sum(investment.amount for investment in self.investments)
        average_valuation = (sum(investment.valuation for investment in self.investments) / 
                             len(self.investments)) if self.investments else 0

        return {
            "total_invested": total_invested,
            "average_valuation": average_valuation,
            "number_of_investments": len(self.investments)
        }

    def save_to_file(self, filename: str) -> None:
        """
        Save the portfolio to a JSON file.

        :param filename: Name of the file to save the portfolio.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([investment.__dict__ for investment in self.investments], file, default=str)
        except IOError as e:
            print(f"Error saving portfolio to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load the portfolio from a JSON file.

        :param filename: Name of the file to load the portfolio from.
        """
        try:
            with open(filename, 'r') as file:
                investments_data = json.load(file)
                self.investments = [Investment(**data) for data in investments_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading portfolio from file: {e}")

# Example usage
if __name__ == "__main__":
    portfolio = Portfolio()
    
    # Adding investments
    portfolio.add_investment(Investment("Startup A", 50000, "2023-01-15", 2000000))
    portfolio.add_investment(Investment("Startup B", 75000, "2023-02-20", 3000000))
    
    # Evaluating portfolio
    evaluation = portfolio.evaluate_portfolio()
    print("Portfolio Evaluation:", evaluation)
    
    # Saving portfolio to file
    portfolio.save_to_file("portfolio.json")
    
    # Loading portfolio from file
    new_portfolio = Portfolio()
    new_portfolio.load_from_file("portfolio.json")
    print("Loaded Portfolio:", new_portfolio.investments)
```
