"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gcapmarkets.com
Prompt: Create an example of a financial product that could be introduced in a trading application, reflecting the innovative approach of GCap Markets.
Generated: DETERMINISTIC_eb74b1997791fca9
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python module for managing a hypothetical financial product called 'FlexiOption'.
FlexiOption is an innovative financial instrument that combines characteristics 
of options and structured products, offering dynamic strike prices and flexible 
expiration times based on market conditions.

This code reflects a production-ready implementation for integration into 
a trading application.
"""

import datetime
from typing import Callable


class FlexiOption:
    """
    Class representing the FlexiOption financial product.
    """

    def __init__(self, symbol: str, strike_price: float, premium: float, 
                 expiration_date: datetime.date, market_condition_fn: Callable[[float], float]):
        """
        Initializes a FlexiOption instance.

        :param symbol: The asset symbol (e.g., 'AAPL' for Apple stock).
        :param strike_price: Initial strike price of the option.
        :param premium: The cost to purchase the option.
        :param expiration_date: The expiration date of the option.
        :param market_condition_fn: A callable function that dynamically adjusts the strike price 
                                    based on market conditions. Accepts current market price and 
                                    returns updated strike price.
        """
        self.symbol = symbol
        self.strike_price = strike_price
        self.premium = premium
        self.expiration_date = expiration_date
        self.market_condition_fn = market_condition_fn
        self.creation_date = datetime.date.today()

    def is_expired(self) -> bool:
        """
        Checks if the option has expired.

        :return: True if expired, False otherwise.
        """
        return datetime.date.today() > self.expiration_date

    def update_strike_price(self, current_market_price: float) -> None:
        """
        Updates the strike price based on the market condition function.

        :param current_market_price: The current market price of the underlying asset.
        """
        try:
            self.strike_price = self.market_condition_fn(current_market_price)
        except Exception as e:
            raise ValueError(f"Error updating strike price: {e}")

    def __str__(self) -> str:
        """
        Returns a string representation of the FlexiOption.

        :return: A string describing the option.
        """
        status = "Expired" if self.is_expired() else "Active"
        return (f"FlexiOption(symbol={self.symbol}, strike_price={self.strike_price}, "
                f"premium={self.premium}, expiration_date={self.expiration_date}, "
                f"status={status})")


# Example usage:

def dynamic_strike_price_adjustment(current_market_price: float) -> float:
    """
    Example market adjustment function for strike price.

    :param current_market_price: Current market price of the underlying asset.
    :return: Adjusted strike price (e.g., 10% above current market price).
    """
    return current_market_price * 1.1


def main():
    """
    Demonstrates creating and managing a FlexiOption instance.
    """
    try:
        # Create a FlexiOption with example parameters
        option = FlexiOption(
            symbol="AAPL",
            strike_price=150.0,
            premium=5.0,
            expiration_date=datetime.date(2024, 1, 1),
            market_condition_fn=dynamic_strike_price_adjustment
        )

        print(option)

        # Simulate market price change
        current_market_price = 160.0
        option.update_strike_price(current_market_price)

        print("After market adjustment:")
        print(option)

        # Check expiration status after updating
        print("Is the option expired?", option.is_expired())

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```
