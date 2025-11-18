"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swarpx.com
Prompt: Develop a Python program to simulate cryptocurrency transactions using SwapX's features, including quick swaps and detailed portfolio management.
Generated: DETERMINISTIC_9c7f4c937bc6d96d
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from decimal import Decimal, InvalidOperation
from typing import Dict, List


class SwapX:
    """A class to simulate cryptocurrency transactions using SwapX's features."""
    
    def __init__(self):
        # Initialize user portfolio and exchange rates
        self.portfolio: Dict[str, Decimal] = {}
        self.exchange_rates: Dict[str, Decimal] = {  # Example rates (USD equivalent)
            "BTC": Decimal("25000.0"),
            "ETH": Decimal("1600.0"),
            "LTC": Decimal("65.0"),
            "USDT": Decimal("1.0")
        }

    def add_to_portfolio(self, currency: str, amount: Decimal):
        """Add cryptocurrency to the user's portfolio."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if currency not in self.exchange_rates:
            raise ValueError(f"Currency {currency} not supported.")
        
        # Update portfolio
        self.portfolio[currency] = self.portfolio.get(currency, Decimal("0")) + amount

    def quick_swap(self, from_currency: str, to_currency: str, amount: Decimal):
        """
        Perform a quick swap between two cryptocurrencies.
        Args:
            from_currency: The currency to swap from.
            to_currency: The currency to swap to.
            amount: The amount of 'from_currency' to swap.
        """
        if from_currency == to_currency:
            raise ValueError("Cannot swap the same currency.")
        if from_currency not in self.portfolio or self.portfolio[from_currency] < amount:
            raise ValueError(f"Insufficient balance for {from_currency}.")
        if to_currency not in self.exchange_rates:
            raise ValueError(f"Currency {to_currency} not supported.")
        
        # Calculate the value of 'from_currency' in USD
        from_usd_value = amount * self.exchange_rates[from_currency]
        # Convert USD value to 'to_currency'
        to_amount = from_usd_value / self.exchange_rates[to_currency]

        # Perform the swap
        self.portfolio[from_currency] -= amount
        self.portfolio[to_currency] = self.portfolio.get(to_currency, Decimal("0")) + to_amount

    def get_portfolio(self) -> Dict[str, Decimal]:
        """Retrieve the user's portfolio."""
        return self.portfolio

    def get_portfolio_value_in_usd(self) -> Decimal:
        """Calculate the total portfolio value in USD."""
        total_value = Decimal("0")
        for currency, amount in self.portfolio.items():
            total_value += amount * self.exchange_rates[currency]
        return total_value

    def display_portfolio(self):
        """Display the user's portfolio in a human-readable format."""
        print("---- Portfolio ----")
        for currency, amount in self.portfolio.items():
            print(f"{currency}: {amount} (USD value: {amount * self.exchange_rates[currency]:.2f})")
        print(f"Total USD Value: {self.get_portfolio_value_in_usd():.2f}")
        print("-------------------")


# Example usage
if __name__ == "__main__":
    swapx = SwapX()
    
    try:
        # Add funds to the portfolio
        swapx.add_to_portfolio("BTC", Decimal("0.5"))
        swapx.add_to_portfolio("ETH", Decimal("2"))
        swapx.display_portfolio()

        # Perform a quick swap
        swapx.quick_swap("BTC", "ETH", Decimal("0.1"))
        swapx.display_portfolio()

        # Show total portfolio value in USD
        print(f"Total Portfolio Value (USD): {swapx.get_portfolio_value_in_usd():.2f}")
    
    except (ValueError, InvalidOperation) as e:
        # Handle errors such as invalid input
        print(f"Error: {e}")
```
