"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eggdex.online
Prompt: Create a step-by-step guide for integrating margin and derivative trading into a decentralized exchange on MultiversX, focusing on portfolio risk management rather than individual contract risk.
Generated: DETERMINISTIC_f5f8f7b353ae25d0
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for integrating portfolio risk management into a decentralized exchange (DEX) on MultiversX for margin and derivative trading. It provides a streamlined structure for managing portfolio-level risk, with implementations for tracking positions, calculating risk, and enforcing limits.

```python
from typing import List, Dict, Optional
from decimal import Decimal, getcontext

# Set precision for Decimal to handle financial calculations accurately
getcontext().prec = 18

class Position:
    """
    Represents an individual trading position for a user.
    """
    def __init__(self, asset: str, quantity: Decimal, price: Decimal, leverage: Decimal):
        self.asset = asset
        self.quantity = quantity  # Positive for long, negative for short
        self.price = price  # Entry price
        self.leverage = leverage  # Leverage used for the position

    def calculate_value(self) -> Decimal:
        """Calculates the value of the position."""
        return self.quantity * self.price


class Portfolio:
    """
    Represents a user's portfolio and manages all trading positions.
    """
    def __init__(self, user_id: str, margin_balance: Decimal, risk_limit: Decimal):
        self.user_id = user_id
        self.margin_balance = margin_balance  # Funds available for trading
        self.positions: List[Position] = []  # Track all open positions
        self.risk_limit = risk_limit  # Max allowable portfolio risk as a percentage of margin balance

    def add_position(self, position: Position) -> Optional[str]:
        """
        Adds a position to the portfolio after verifying risk.
        Returns an error message if risk limit is exceeded, otherwise None.
        """
        simulated_positions = self.positions + [position]
        portfolio_risk = self.calculate_portfolio_risk(simulated_positions)

        if portfolio_risk > self.risk_limit:
            return f"Risk limit exceeded! Portfolio risk {portfolio_risk:.2f}% exceeds limit of {self.risk_limit:.2f}%."
        
        self.positions.append(position)
        return None

    def calculate_portfolio_risk(self, positions: List[Position]) -> Decimal:
        """
        Calculates the total portfolio risk as a percentage of the margin balance.
        """
        total_exposure = sum(abs(p.calculate_value()) / p.leverage for p in positions)
        return (total_exposure / self.margin_balance) * 100

    def close_position(self, asset: str) -> Optional[str]:
        """
        Closes a position for a specific asset.
        Returns an error message if the position does not exist, otherwise None.
        """
        for position in self.positions:
            if position.asset == asset:
                self.positions.remove(position)
                return None
        return f"No position found for asset {asset}."

    def get_portfolio_summary(self) -> Dict:
        """
        Generates a summary of the portfolio, including positions and overall risk.
        """
        positions_summary = [
            {
                "asset": p.asset,
                "quantity": float(p.quantity),
                "price": float(p.price),
                "leverage": float(p.leverage),
                "value": float(p.calculate_value())
            }
            for p in self.positions
        ]
        portfolio_risk = self.calculate_portfolio_risk(self.positions)
        return {
            "user_id": self.user_id,
            "margin_balance": float(self.margin_balance),
            "risk_limit": float(self.risk_limit),
            "portfolio_risk": float(portfolio_risk),
            "positions": positions_summary
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a portfolio with $10,000 margin balance and a 50% risk limit
        portfolio = Portfolio(user_id="user_123", margin_balance=Decimal("10000"), risk_limit=Decimal("50"))

        # Add positions
        error = portfolio.add_position(Position(asset="BTC", quantity=Decimal("1"), price=Decimal("30000"), leverage=Decimal("10")))
        if error:
            print(f"Error: {error}")

        error = portfolio.add_position(Position(asset="ETH", quantity=Decimal("10"), price=Decimal("2000"), leverage=Decimal("5")))
        if error:
            print(f"Error: {error}")

        # Display portfolio summary
        summary = portfolio.get_portfolio_summary()
        print(summary)

        # Close a position
        error = portfolio.close_position("BTC")
        if error:
            print(f"Error: {error}")

        # Display updated portfolio summary
        summary = portfolio.get_portfolio_summary()
        print(summary)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
