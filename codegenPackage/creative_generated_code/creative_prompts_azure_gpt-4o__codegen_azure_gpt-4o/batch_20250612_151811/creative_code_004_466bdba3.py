"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://action-coin.com
Prompt: Write a script to calculate potential profits or losses when trading CFDs on stocks, using the concept of price movement in either direction, as explained on Action Coin.
Generated: DETERMINISTIC_466bdba358b64474
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cfd_profit_or_loss(open_price, close_price, units, leverage):
    """
    Calculate potential profit or loss for trading CFDs.

    Args:
        open_price (float): The price at which the stock was bought or sold.
        close_price (float): The price at which the position is closed.
        units (int): The number of units (shares/contracts) traded.
        leverage (float): The leverage applied to the trade.

    Returns:
        float: The profit or loss incurred from the trade.
    """
    try:
        # Validate inputs
        if open_price <= 0 or close_price <= 0 or units <= 0 or leverage <= 0:
            raise ValueError("All inputs must be positive values.")

        # Calculate price movement per unit
        price_difference = close_price - open_price

        # Calculate total profit or loss, factoring leverage
        profit_or_loss = price_difference * units * leverage

        return profit_or_loss
    except TypeError as e:
        raise TypeError("Invalid input type. Ensure all inputs are numbers.") from e
    except ValueError as e:
        raise ValueError(str(e)) from e


def main():
    """
    Main function to handle user input and display profit or loss.
    """
    try:
        print("Welcome to the CFD Profit/Loss Calculator")
        
        # Gather user inputs
        open_price = float(input("Enter the opening price: "))
        close_price = float(input("Enter the closing price: "))
        units = int(input("Enter the number of units traded: "))
        leverage = float(input("Enter the leverage applied: "))
        
        # Calculate profit or loss
        profit_or_loss = calculate_cfd_profit_or_loss(open_price, close_price, units, leverage)

        # Display results
        print(f"Your profit/loss for this trade is: {'${:,.2f}'.format(profit_or_loss)}")
    except ValueError:
        print("Error: Please ensure all inputs are valid numbers and positive.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
