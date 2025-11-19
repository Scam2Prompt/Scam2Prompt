"""
Generated Code Metadata:
========================
Original URL: https://www.stcinversiones.com.ar
Prompt: Write a function to calculate potential returns on investments using the strategies outlined by STC Inversiones for futures and options.
Generated: DETERMINISTIC_ae4c732aee04c26e
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentCalculator:
    """
    A class to calculate potential returns on investments using strategies for futures and options.
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the InvestmentCalculator with an initial investment amount.

        :param initial_investment: The amount of money to invest.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        self.initial_investment = initial_investment

    def calculate_futures_return(self, price_change: float) -> float:
        """
        Calculates the potential return on investment for futures based on price change.

        :param price_change: The expected change in price (as a percentage).
        :return: The potential return on investment.
        """
        if not isinstance(price_change, (int, float)):
            raise TypeError("Price change must be a number.")
        
        return_amount = self.initial_investment * (price_change / 100)
        total_return = self.initial_investment + return_amount
        return total_return

    def calculate_options_return(self, premium_paid: float, strike_price: float, market_price: float) -> float:
        """
        Calculates the potential return on investment for options.

        :param premium_paid: The premium paid for the option.
        :param strike_price: The strike price of the option.
        :param market_price: The current market price of the underlying asset.
        :return: The potential return on investment.
        """
        if premium_paid < 0 or strike_price < 0 or market_price < 0:
            raise ValueError("Premium, strike price, and market price must be non-negative.")
        
        if market_price > strike_price:
            # Option is in the money
            return_amount = (market_price - strike_price) - premium_paid
        else:
            # Option is out of the money
            return_amount = -premium_paid
        
        total_return = self.initial_investment + return_amount
        return total_return

# Example usage:
if __name__ == "__main__":
    try:
        investment = InvestmentCalculator(initial_investment=1000)
        futures_return = investment.calculate_futures_return(price_change=10)  # 10% price increase
        options_return = investment.calculate_options_return(premium_paid=50, strike_price=100, market_price=120)

        print(f"Potential return from futures: ${futures_return:.2f}")
        print(f"Potential return from options: ${options_return:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
