"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.stcinversiones.com.ar
Prompt: Write a function to calculate potential returns on investments using the strategies outlined by STC Inversiones for futures and options.
Generated: DETERMINISTIC_ae4c732aee04c26e
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentCalculator:
    """
    A class to calculate potential returns on investments using strategies for futures and options.
    """

    def __init__(self):
        pass

    def calculate_futures_return(self, initial_investment: float, price_change: float) -> float:
        """
        Calculate the potential return on a futures investment.

        Args:
            initial_investment (float): The amount initially invested.
            price_change (float): The expected change in price (positive or negative).

        Returns:
            float: The potential return on investment.

        Raises:
            ValueError: If initial_investment or price_change is negative.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be non-negative.")
        if price_change < -initial_investment:
            raise ValueError("Price change cannot result in negative total value.")

        return initial_investment + price_change

    def calculate_options_return(self, initial_investment: float, strike_price: float, market_price: float) -> float:
        """
        Calculate the potential return on an options investment.

        Args:
            initial_investment (float): The amount initially invested in the options.
            strike_price (float): The price at which the option can be exercised.
            market_price (float): The current market price of the underlying asset.

        Returns:
            float: The potential return on investment.

        Raises:
            ValueError: If initial_investment, strike_price, or market_price is negative.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be non-negative.")
        if strike_price < 0:
            raise ValueError("Strike price must be non-negative.")
        if market_price < 0:
            raise ValueError("Market price must be non-negative.")

        # Calculate potential profit from exercising the option
        potential_profit = max(0, market_price - strike_price)

        # Calculate total value considering the initial investment
        return potential_profit - initial_investment

# Sample usage:
if __name__ == "__main__":
    calculator = InvestmentCalculator()

    try:
        futures_return = calculator.calculate_futures_return(1000, 200)
        print(f"Potential return on futures investment: ${futures_return:.2f}")

        options_return = calculator.calculate_options_return(100, 50, 80)
        print(f"Potential return on options investment: ${options_return:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
