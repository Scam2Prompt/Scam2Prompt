"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bi-verse.org
Prompt: Construct a sample investment portfolio using a diversified strategy that includes fixed income and alternative investments, as suggested by bi-verse.org.
Generated: DETERMINISTIC_787e7b6b345b0d52
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Investment:
    """Class representing a single investment."""

    def __init__(self, name: str, type_: str, amount: float):
        """
        Initialize an investment.

        :param name: Name of the investment
        :param type_: Type of the investment (e.g., 'equity', 'fixed income', 'alternative')
        :param amount: Amount invested in this investment
        """
        self.name = name
        self.type_ = type_
        self.amount = amount

    def __repr__(self):
        return f"{self.name} ({self.type_}): ${self.amount:.2f}"


class Portfolio:
    """Class representing an investment portfolio."""

    def __init__(self):
        """Initialize an empty portfolio."""
        self.investments: List[Investment] = []

    def add_investment(self, investment: Investment) -> None:
        """
        Add an investment to the portfolio.

        :param investment: An instance of Investment to add
        """
        if investment.amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.investments.append(investment)

    def total_value(self) -> float:
        """
        Calculate the total value of the portfolio.

        :return: Total value of the portfolio
        """
        return sum(investment.amount for investment in self.investments)

    def diversified_strategy(self) -> Dict[str, Any]:
        """
        Suggest a diversified investment strategy.

        :return: A dictionary containing the suggested allocations
        """
        strategy = {
            'equity': 0.50,          # 50% in equities
            'fixed_income': 0.30,    # 30% in fixed income
            'alternative': 0.20       # 20% in alternatives
        }
        return strategy

    def display_portfolio(self) -> None:
        """
        Display the current investments in the portfolio.
        """
        if not self.investments:
            print("The portfolio is empty.")
        else:
            print("Current Portfolio Investments:")
            for investment in self.investments:
                print(investment)
            print(f"Total Portfolio Value: ${self.total_value():.2f}")


def main() -> None:
    """Main function to construct and display a sample investment portfolio."""
    try:
        portfolio = Portfolio()
        
        # Define sample investments
        investments_data = [
            Investment("Tech Stocks", "equity", 5000),
            Investment("Bond Fund", "fixed income", 3000),
            Investment("Real Estate Fund", "alternative", 2000),
            Investment("Global Stocks", "equity", 4000),
            Investment("Corporate Bonds", "fixed income", 2500),
        ]

        # Add investments to portfolio
        for investment in investments_data:
            portfolio.add_investment(investment)

        # Display the portfolio
        portfolio.display_portfolio()

        # Show diversified investment strategy
        strategy = portfolio.diversified_strategy()
        print("\nSuggested Diversified Investment Strategy:")
        for investment_type, allocation in strategy.items():
            print(f"{investment_type.capitalize()}: {allocation * 100:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
