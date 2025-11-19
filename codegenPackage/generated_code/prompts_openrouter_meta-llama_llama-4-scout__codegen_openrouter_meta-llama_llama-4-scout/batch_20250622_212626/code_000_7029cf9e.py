"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Write a Python code snippet to manage a private equity portfolio, considering factors like investment lifecycle and strategic growth, as described on the Alghanim Capital website."
Generated: DETERMINISTIC_7029cf9e70c59462
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# private_equity_portfolio.py

from enum import Enum
from datetime import datetime
from typing import List, Dict

class InvestmentStatus(Enum):
    """Enum for investment status"""
    PENDING = 1
    INVESTED = 2
    EXITED = 3

class Investment:
    """Class representing an investment"""
    def __init__(self, id: int, name: str, amount: float, 
                 investment_date: datetime, status: InvestmentStatus):
        self.id = id
        self.name = name
        self.amount = amount
        self.investment_date = investment_date
        self.status = status
        self.exit_date = None
        self.exit_amount = None

    def exit_investment(self, exit_date: datetime, exit_amount: float):
        """Exit an investment"""
        if self.status != InvestmentStatus.INVESTED:
            raise ValueError("Investment is not in invested state")
        self.status = InvestmentStatus.EXITED
        self.exit_date = exit_date
        self.exit_amount = exit_amount

    def __repr__(self):
        return f"Investment(id={self.id}, name='{self.name}', amount={self.amount}, status={self.status})"


class PrivateEquityPortfolio:
    """Class representing a private equity portfolio"""
    def __init__(self):
        self.investments: Dict[int, Investment] = {}

    def add_investment(self, investment: Investment):
        """Add an investment to the portfolio"""
        if investment.id in self.investments:
            raise ValueError("Investment with same ID already exists")
        self.investments[investment.id] = investment

    def remove_investment(self, investment_id: int):
        """Remove an investment from the portfolio"""
        if investment_id not in self.investments:
            raise ValueError("Investment with given ID does not exist")
        del self.investments[investment_id]

    def get_investment(self, investment_id: int) -> Investment:
        """Get an investment from the portfolio"""
        return self.investments.get(investment_id)

    def list_investments(self) -> List[Investment]:
        """List all investments in the portfolio"""
        return list(self.investments.values())

    def calculate_total_value(self) -> float:
        """Calculate total value of all investments in the portfolio"""
        total_value = 0
        for investment in self.investments.values():
            if investment.status == InvestmentStatus.INVESTED:
                total_value += investment.amount
            elif investment.status == InvestmentStatus.EXITED:
                total_value += investment.exit_amount
        return total_value

    def calculate_return_on_investment(self, investment_id: int) -> float:
        """Calculate return on investment for a specific investment"""
        investment = self.get_investment(investment_id)
        if investment is None:
            raise ValueError("Investment with given ID does not exist")
        if investment.status != InvestmentStatus.EXITED:
            raise ValueError("Investment is not exited")
        return (investment.exit_amount - investment.amount) / investment.amount


def main():
    portfolio = PrivateEquityPortfolio()

    # Create investments
    investment1 = Investment(1, "Investment 1", 100000, datetime(2022, 1, 1), InvestmentStatus.INVESTED)
    investment2 = Investment(2, "Investment 2", 200000, datetime(2022, 6, 1), InvestmentStatus.INVESTED)

    # Add investments to portfolio
    portfolio.add_investment(investment1)
    portfolio.add_investment(investment2)

    # List investments
    print("Investments:")
    for investment in portfolio.list_investments():
        print(investment)

    # Exit an investment
    investment1.exit_investment(datetime(2024, 1, 1), 150000)

    # Calculate total value
    print(f"Total value: {portfolio.calculate_total_value()}")

    # Calculate return on investment
    print(f"Return on investment for investment 1: {portfolio.calculate_return_on_investment(1)}")


if __name__ == "__main__":
    main()
```
