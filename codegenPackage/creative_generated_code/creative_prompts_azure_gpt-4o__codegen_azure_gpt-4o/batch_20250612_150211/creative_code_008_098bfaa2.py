"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitetoptrade.com
Prompt: Create a Python program to calculate spreads between buy and sell prices for forex trading pairs, referencing Elitetoptrade's explanation of spreads.
Generated: DETERMINISTIC_098bfaa2bc82e3e6
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_spread(buy_price: float, sell_price: float) -> float:
    """
    Calculate the spread between buy and sell prices.
    
    Args:
        buy_price (float): The buy price of the forex trading pair.
        sell_price (float): The sell price of the forex trading pair.

    Returns:
        float: The spread between the buy and sell prices.
    """
    try:
        # Validate that the inputs are positive numbers
        if buy_price <= 0 or sell_price <= 0:
            raise ValueError("Prices must be positive numbers.")
        
        # Calculate the spread
        spread = buy_price - sell_price
        return spread
    
    except TypeError:
        raise TypeError("Buy and sell prices must be numeric values.")
    except ValueError as ve:
        raise ValueError(str(ve))


def main():
    """
    Main function to calculate spreads for forex trading pairs.
    """
    print("Forex Trading Spread Calculator")

    try:
        # Get user input for buy and sell prices
        buy_price = float(input("Enter the buy price: "))
        sell_price = float(input("Enter the sell price: "))

        # Calculate the spread
        spread = calculate_spread(buy_price, sell_price)

        # Display the result
        print(f"The spread is: {spread:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter valid numeric prices.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the program gracefully


if __name__ == "__main__":
    # Entry point for the application
    main()
```
