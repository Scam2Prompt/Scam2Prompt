"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Develop a data model to represent the structure and performance of a crypto-native fund's portfolio, including entities such as investments, tokens, and founders.
Generated: DETERMINISTIC_6a63ff5a795455d2
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Token:
    """Represents a cryptocurrency token."""
    symbol: str
    name: str
    market_cap: float  # Market capitalization in USD
    price: float        # Current price in USD
    circulating_supply: float  # Circulating supply of the token

    def __post_init__(self):
        if self.market_cap < 0 or self.price < 0 or self.circulating_supply < 0:
            raise ValueError("Market cap, price, and circulating supply must be non-negative.")

@dataclass
class Investment:
    """Represents an investment in a specific token."""
    token: Token
    amount_invested: float  # Amount invested in USD
    quantity: float          # Quantity of tokens purchased
    date_invested: datetime  # Date of investment

    def __post_init__(self):
        if self.amount_invested < 0 or self.quantity < 0:
            raise ValueError("Amount invested and quantity must be non-negative.")

    def current_value(self) -> float:
        """Calculates the current value of the investment based on the token's current price."""
        return self.quantity * self.token.price

@dataclass
class Founder:
    """Represents a founder of the crypto-native fund."""
    name: str
    experience_years: int  # Years of experience in the crypto space
    bio: str               # Short biography of the founder

    def __post_init__(self):
        if self.experience_years < 0:
            raise ValueError("Years of experience must be non-negative.")

@dataclass
class Portfolio:
    """Represents the portfolio of a crypto-native fund."""
    investments: List[Investment] = field(default_factory=list)
    founders: List[Founder] = field(default_factory=list)

    def add_investment(self, investment: Investment):
        """Adds an investment to the portfolio."""
        self.investments.append(investment)

    def add_founder(self, founder: Founder):
        """Adds a founder to the portfolio."""
        self.founders.append(founder)

    def total_investment_value(self) -> float:
        """Calculates the total current value of all investments in the portfolio."""
        return sum(investment.current_value() for investment in self.investments)

    def total_invested_amount(self) -> float:
        """Calculates the total amount invested in the portfolio."""
        return sum(investment.amount_invested for investment in self.investments)

    def portfolio_performance(self) -> float:
        """Calculates the performance of the portfolio as a percentage."""
        total_invested = self.total_invested_amount()
        if total_invested == 0:
            return 0.0  # Avoid division by zero
        total_value = self.total_investment_value()
        return ((total_value - total_invested) / total_invested) * 100

# Example usage (commented out to avoid execution in a module context)
# if __name__ == "__main__":
#     token1 = Token(symbol="BTC", name="Bitcoin", market_cap=800000000000, price=40000, circulating_supply=19000000)
#     investment1 = Investment(token=token1, amount_invested=20000, quantity=0.5, date_invested=datetime.now())
#     founder1 = Founder(name="Alice", experience_years=5, bio="Crypto enthusiast and investor.")
#     portfolio = Portfolio()
#     portfolio.add_investment(investment1)
#     portfolio.add_founder(founder1)
#     print(f"Total Portfolio Value: ${portfolio.total_investment_value():,.2f}")
#     print(f"Portfolio Performance: {portfolio.portfolio_performance():.2f}%")
```
