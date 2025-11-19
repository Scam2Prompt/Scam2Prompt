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
# angel_investment_tracker.py

import datetime
from typing import Dict, List

class Investment:
    """Represents an angel investment."""

    def __init__(self, 
                 investment_id: int, 
                 company_name: str, 
                 investment_date: datetime.date, 
                 investment_amount: float, 
                 equity_stake: float):
        """
        Initializes an Investment object.

        Args:
        - investment_id (int): Unique identifier for the investment.
        - company_name (str): Name of the company.
        - investment_date (datetime.date): Date of the investment.
        - investment_amount (float): Amount invested.
        - equity_stake (float): Equity stake percentage.
        """
        self.investment_id = investment_id
        self.company_name = company_name
        self.investment_date = investment_date
        self.investment_amount = investment_amount
        self.equity_stake = equity_stake
        self.valuation: float = None  # To be updated later

    def update_valuation(self, valuation: float):
        """Updates the valuation of the investment."""
        self.valuation = valuation

    def calculate_return_on_investment(self) -> float:
        """
        Calculates the return on investment (ROI).

        Returns:
        - float: ROI as a percentage.
        """
        if self.valuation is None:
            raise ValueError("Valuation is not set.")
        return ((self.valuation - self.investment_amount) / self.investment_amount) * 100


class Portfolio:
    """Represents a portfolio of angel investments."""

    def __init__(self):
        """Initializes an empty portfolio."""
        self.investments: Dict[int, Investment] = {}

    def add_investment(self, investment: Investment):
        """Adds an investment to the portfolio."""
        self.investments[investment.investment_id] = investment

    def remove_investment(self, investment_id: int):
        """Removes an investment from the portfolio."""
        if investment_id in self.investments:
            del self.investments[investment_id]
        else:
            raise ValueError("Investment not found.")

    def get_investment(self, investment_id: int) -> Investment:
        """
        Retrieves an investment from the portfolio.

        Args:
        - investment_id (int): ID of the investment.

        Returns:
        - Investment: The investment object.
        """
        return self.investments.get(investment_id)

    def evaluate_portfolio(self) -> Dict[str, float]:
        """
        Evaluates the portfolio by calculating the total investment, 
        total valuation, and overall ROI.

        Returns:
        - Dict[str, float]: A dictionary containing the total investment, 
          total valuation, and overall ROI.
        """
        total_investment = 0
        total_valuation = 0
        for investment in self.investments.values():
            total_investment += investment.investment_amount
            if investment.valuation:
                total_valuation += investment.valuation
        overall_roi = ((total_valuation - total_investment) / total_investment) * 100 if total_investment > 0 else 0
        return {
            "total_investment": total_investment,
            "total_valuation": total_valuation,
            "overall_roi": overall_roi
        }


def main():
    # Example usage
    portfolio = Portfolio()

    investment1 = Investment(1, "Company A", datetime.date(2022, 1, 1), 10000, 10)
    investment1.update_valuation(20000)

    investment2 = Investment(2, "Company B", datetime.date(2022, 6, 1), 5000, 5)
    investment2.update_valuation(10000)

    portfolio.add_investment(investment1)
    portfolio.add_investment(investment2)

    evaluation = portfolio.evaluate_portfolio()
    print("Portfolio Evaluation:")
    print(f"Total Investment: ${evaluation['total_investment']:.2f}")
    print(f"Total Valuation: ${evaluation['total_valuation']:.2f}")
    print(f"Overall ROI: {evaluation['overall_roi']:.2f}%")

    # Get individual investment
    investment = portfolio.get_investment(1)
    if investment:
        print(f"\nInvestment {investment.investment_id} - {investment.company_name}")
        print(f"Investment Date: {investment.investment_date}")
        print(f"Investment Amount: ${investment.investment_amount:.2f}")
        print(f"Equity Stake: {investment.equity_stake}%")
        print(f"Valuation: ${investment.valuation:.2f}")
        print(f"ROI: {investment.calculate_return_on_investment():.2f}%")
    else:
        print("Investment not found.")

if __name__ == "__main__":
    main()
```
