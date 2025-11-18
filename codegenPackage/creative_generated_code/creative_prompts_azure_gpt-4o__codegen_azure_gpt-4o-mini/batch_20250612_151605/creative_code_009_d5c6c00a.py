"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Write code to simulate the diversification of investment portfolios through exclusive IPO access, inspired by Grade World Investment Limited's approach.
Generated: DETERMINISTIC_d5c6c00a8d0df143
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class InvestmentPortfolio:
    def __init__(self, investor_name: str):
        """
        Initializes the investment portfolio for a given investor.

        :param investor_name: The name of the investor.
        """
        self.investor_name = investor_name
        self.portfolio: Dict[str, float] = {}  # Portfolio stores stock names and their respective amounts

    def add_investment(self, stock: str, amount: float) -> None:
        """
        Adds an investment to the portfolio.

        :param stock: The name of the stock.
        :param amount: The amount invested in the stock.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")
        self.portfolio[stock] = self.portfolio.get(stock, 0) + amount

    def diversify_portfolio(self, ipo_stocks: List[str], total_investment: float) -> None:
        """
        Diversifies the portfolio by allocating the total investment across available IPO stocks.

        :param ipo_stocks: List of available IPO stocks.
        :param total_investment: Total amount to invest in IPOs.
        """
        if total_investment <= 0:
            raise ValueError("Total investment must be greater than 0.")
        if not ipo_stocks:
            raise ValueError("No IPO stocks available for investment.")

        # Allocate investments randomly across IPOs
        for stock in ipo_stocks:
            investment_amount = round(random.uniform(0, total_investment / len(ipo_stocks)), 2)
            if investment_amount > 0:
                self.add_investment(stock, investment_amount)
                total_investment -= investment_amount

    def display_portfolio(self) -> None:
        """
        Displays the current investment portfolio.
        """
        print(f"Investment Portfolio for {self.investor_name}:")
        for stock, amount in self.portfolio.items():
            print(f" - {stock}: ${amount:.2f}")

def main():
    try:
        # Example usage
        ipo_stocks = ["TechCo", "HealthInc", "EcoEnergy", "FinServ"]
        portfolio = InvestmentPortfolio("Alice Johnson")

        # Simulating an investment of $1000 in IPOs
        portfolio.diversify_portfolio(ipo_stocks, 1000)
        portfolio.display_portfolio()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
