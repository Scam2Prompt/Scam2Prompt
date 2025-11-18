"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memetic.digital
Prompt: Develop a program to track and evaluate angel investments, similar to the portfolio management described by Memetic Digital.
Generated: DETERMINISTIC_e89c4e69869f651b
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict

class AngelInvestment:
    """
    Represents an angel investment in a startup.
    """
    def __init__(self, startup_name: str, amount_invested: float, equity_percentage: float):
        self.startup_name = startup_name
        self.amount_invested = amount_invested
        self.equity_percentage = equity_percentage
        self.date_invested = datetime.now()

    def __repr__(self):
        return f"AngelInvestment(startup_name='{self.startup_name}', amount_invested={self.amount_invested}, equity_percentage={self.equity_percentage}, date_invested={self.date_invested})"


class InvestmentPortfolio:
    """
    Manages a collection of angel investments.
    """
    def __init__(self):
        self.investments: List[AngelInvestment] = []

    def add_investment(self, investment: AngelInvestment):
        """
        Adds a new investment to the portfolio.

        :param investment: An instance of AngelInvestment to be added.
        """
        if not isinstance(investment, AngelInvestment):
            raise ValueError("Investment must be an instance of AngelInvestment.")
        self.investments.append(investment)

    def evaluate_portfolio(self) -> Dict[str, float]:
        """
        Evaluates the total investments and returns a summary.

        :return: A dictionary summarizing total investments and average equity.
        """
        if not self.investments:
            return {"total_investment": 0.0, "average_equity": 0.0}

        total_investment = sum(investment.amount_invested for investment in self.investments)
        average_equity = sum(investment.equity_percentage for investment in self.investments) / len(self.investments)

        return {
            "total_investment": total_investment,
            "average_equity": average_equity
        }

    def save_portfolio_to_file(self, file_path: str):
        """
        Saves the current portfolio to a JSON file.

        :param file_path: The path to the file where the portfolio will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([investment.__dict__ for investment in self.investments], file, default=str)
        except IOError as e:
            raise RuntimeError(f"An error occurred while saving the portfolio: {e}")

    def load_portfolio_from_file(self, file_path: str):
        """
        Loads the portfolio from a JSON file.

        :param file_path: The path to the file from which the portfolio will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                investments_data = json.load(file)
                self.investments = [AngelInvestment(**data) for data in investments_data]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"An error occurred while loading the portfolio: {e}")


if __name__ == "__main__":
    # Example usage of the InvestmentPortfolio class
    portfolio = InvestmentPortfolio()

    # Adding investments
    portfolio.add_investment(AngelInvestment("Startup A", 50000, 10))
    portfolio.add_investment(AngelInvestment("Startup B", 30000, 15))

    # Evaluating the portfolio
    evaluation = portfolio.evaluate_portfolio()
    print("Portfolio Evaluation:", evaluation)

    # Saving the portfolio
    portfolio.save_portfolio_to_file("portfolio.json")

    # Loading the portfolio
    new_portfolio = InvestmentPortfolio()
    new_portfolio.load_portfolio_from_file("portfolio.json")
    print("Loaded Portfolio:", new_portfolio.investments)
```
