"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-c5i.pages.dev
Prompt: Write a script to calculate slippage fees for token swaps on Aerodrome Finance, ensuring minimal slippage for traders.
Generated: DETERMINISTIC_b70eb52cd450b229
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_slippage_fee(amount_in, market_price, acceptable_slippage):
    """
    Calculate slippage fee for token swaps.

    Parameters:
        amount_in (float): Amount of tokens to swap.
        market_price (float): Current market price of the token.
        acceptable_slippage (float): Maximum acceptable slippage percentage allowed by the trader (e.g., 0.01 for 1%).

    Returns:
        float: Slippage fee incurred for the swap.
    """
    try:
        # Ensure valid input values
        if amount_in <= 0:
            raise ValueError("Amount to swap must be greater than zero.")
        if market_price <= 0:
            raise ValueError("Market price must be greater than zero.")
        if acceptable_slippage < 0 or acceptable_slippage > 1:
            raise ValueError("Acceptable slippage must be between 0 and 1.")

        # Calculate slippage fee
        slippage_fee = amount_in * market_price * acceptable_slippage
        return slippage_fee

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interactively calculate slippage fee based on user input.
    """
    try:
        print("Welcome to Aerodrome Token Swap Slippage Fee Calculator")

        # Get user input for token swap details
        amount_in = float(input("Enter the amount of tokens to swap: "))
        market_price = float(input("Enter the current market price of the token: "))
        acceptable_slippage = float(input("Enter the acceptable slippage percentage (e.g., 0.01 for 1%): "))

        # Calculate slippage fee
        slippage_fee = calculate_slippage_fee(amount_in, market_price, acceptable_slippage)

        if slippage_fee is not None:
            print(f"Slippage Fee: {slippage_fee:.6f}")
        else:
            print("Could not calculate slippage fee due to input error.")

    except ValueError:
        print("Invalid input. Please provide numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
