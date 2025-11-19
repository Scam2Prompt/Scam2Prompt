"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shaddow.co
Prompt: Create a function that allows users to specify price ranges for trading on Shadow Exchange, leveraging its concentrated liquidity model.
Generated: DETERMINISTIC_2674b1d5bf2a2383
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShadowExchange:
    def __init__(self):
        # Initialize an empty list to store price ranges
        self.price_ranges = []

    def add_price_range(self, lower_bound: float, upper_bound: float) -> None:
        """
        Adds a new price range for trading.

        :param lower_bound: The lower bound of the price range (inclusive).
        :param upper_bound: The upper bound of the price range (inclusive).
        :raises ValueError: If bounds are invalid (e.g., lower_bound >= upper_bound or negative values).
        """
        # Validate input bounds
        if lower_bound < 0 or upper_bound < 0:
            raise ValueError("Price bounds must be non-negative.")
        if lower_bound >= upper_bound:
            raise ValueError("Lower bound must be less than upper bound.")

        # Append the price range to the list
        self.price_ranges.append((lower_bound, upper_bound))

    def get_price_ranges(self) -> list[tuple]:
        """
        Retrieves all specified price ranges for trading.

        :return: A list of tuples, where each tuple represents a price range (lower_bound, upper_bound).
        """
        return self.price_ranges

    def clear_price_ranges(self) -> None:
        """
        Clears all specified price ranges.

        :return: None.
        """
        self.price_ranges.clear()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Shadow Exchange instance
        shadow_exchange = ShadowExchange()

        # Add price ranges
        shadow_exchange.add_price_range(1.0, 5.0)
        shadow_exchange.add_price_range(10.0, 20.0)

        # Retrieve and print all price ranges
        print("Price Ranges:", shadow_exchange.get_price_ranges())

        # Clear price ranges
        shadow_exchange.clear_price_ranges()
        print("Cleared Price Ranges:", shadow_exchange.get_price_ranges())
    except ValueError as e:
        # Handle invalid price range input
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected exceptions
        print(f"Unexpected error: {e}")
```
