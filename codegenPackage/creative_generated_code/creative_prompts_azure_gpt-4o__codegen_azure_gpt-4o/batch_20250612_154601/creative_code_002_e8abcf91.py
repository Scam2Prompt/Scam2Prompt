"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarlado.com
Prompt: Generate code to calculate swap fees for Forex trading, referencing the concept of swap fees mentioned on Emarlado's website.
Generated: DETERMINISTIC_e8abcf91cd1e2af4
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import Union


class ForexSwapCalculator:
    """
    A class to calculate swap fees for Forex trading.

    Swap fees are calculated based on the overnight interest rate differential between the currencies in a pair,
    the leverage used, and the number of days the position is held.
    """

    def __init__(self, base_currency_rate: float, quote_currency_rate: float, leverage: int):
        """
        Initializes the ForexSwapCalculator.

        Parameters:
        - base_currency_rate (float): Interest rate of the base currency.
        - quote_currency_rate (float): Interest rate of the quote currency.
        - leverage (int): Leverage applied to the trading account.
        """
        self.base_currency_rate = base_currency_rate
        self.quote_currency_rate = quote_currency_rate
        self.leverage = leverage

    def calculate_swap_fee(
        self, position_size: Union[int, float], swap_type: str, days_held: int
    ) -> Union[float, None]:
        """
        Calculates the swap fee.

        Parameters:
        - position_size (int | float): The size of the trading position (in units).
        - swap_type (str): Type of position ('long' or 'short').
        - days_held (int): Number of days the position is held.

        Returns:
        - float | None: The calculated swap fee or None if input is invalid.
        """

        # Validate swap type
        if swap_type not in ["long", "short"]:
            print("Error: swap_type must be 'long' or 'short'.")
            return None

        # Calculate interest rate differential
        if swap_type == "long":
            interest_rate_diff = self.base_currency_rate - self.quote_currency_rate
        elif swap_type == "short":
            interest_rate_diff = self.quote_currency_rate - self.base_currency_rate

        # Calculate swap fee
        try:
            swap_fee = (
                position_size * interest_rate_diff * self.leverage * days_held / 365
            )
            return swap_fee
        except Exception as e:
            print(f"Error calculating swap fee: {e}")
            return None


# Example usage
if __name__ == "__main__":
    try:
        # Define parameters
        base_currency_rate = 2.5  # Interest rate of base currency
        quote_currency_rate = 1.75  # Interest rate of quote currency
        leverage = 30  # Leverage applied
        position_size = 100_000  # Position size in units
        swap_type = "long"  # Position type ('long' or 'short')
        days_held = 7  # Number of days held

        # Create an instance of ForexSwapCalculator
        calculator = ForexSwapCalculator(base_currency_rate, quote_currency_rate, leverage)

        # Calculate swap fee
        swap_fee = calculator.calculate_swap_fee(position_size, swap_type, days_held)

        # Output result
        if swap_fee is not None:
            print(f"Swap fee for a {swap_type} position held for {days_held} days: {swap_fee:.2f}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
