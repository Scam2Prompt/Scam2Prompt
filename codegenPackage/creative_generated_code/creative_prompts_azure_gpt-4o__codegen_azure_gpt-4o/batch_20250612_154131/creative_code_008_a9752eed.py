"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-axiomtrade.com
Prompt: Write a script to calculate the spread between bid and ask prices for a given financial instrument, as described in Ultronikclio's trading basics.
Generated: DETERMINISTIC_a9752eed75d914e3
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_spread(bid_price: float, ask_price: float) -> float:
    """
    Calculate the spread between bid and ask prices.

    Args:
        bid_price (float): The bid price of the financial instrument.
        ask_price (float): The ask price of the financial instrument.

    Returns:
        float: The spread between the bid and ask prices.

    Raises:
        ValueError: If bid_price or ask_price is negative.
    """
    if bid_price < 0 or ask_price < 0:
        raise ValueError("Bid and Ask prices must be non-negative values.")

    return ask_price - bid_price


def main():
    """
    Main function to prompt the user for bid and ask prices,
    calculate the spread, and display the result.
    """
    try:
        # Prompt user for input prices
        bid_price = float(input("Enter the bid price: "))
        ask_price = float(input("Enter the ask price: "))

        # Calculate the spread
        spread = calculate_spread(bid_price, ask_price)

        # Display the result
        print(f"The spread between the bid and ask prices is: {spread:.2f}")
    except ValueError as ve:
        # Handle invalid input or calculation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
