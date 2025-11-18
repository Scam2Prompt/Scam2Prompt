"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-walletissuesolutions.pages.dev
Prompt: Write a script to calculate and display trading gains, similar to the examples provided on the Photon platform (e.g., +2,837% for $WYNN).
Generated: DETERMINISTIC_125024fca4a82e44
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_trading_gains(initial_price, current_price):
    """
    Calculate the percentage gain/loss for a trading asset.

    :param initial_price: The price of the asset at the time of purchase (float).
    :param current_price: The current price of the asset (float).
    :return: A formatted string representing the percentage gain or loss.
    """
    try:
        # Ensure prices are valid positive numbers
        if initial_price <= 0 or current_price <= 0:
            raise ValueError("Prices must be positive numbers.")

        # Calculate percentage change
        percentage_change = ((current_price - initial_price) / initial_price) * 100

        # Format the result with a "+" for positive gains, "-" for losses
        formatted_result = f"{percentage_change:+.2f}%"
        return formatted_result
    
    except TypeError:
        raise TypeError("Both initial_price and current_price must be numeric values.")
    except ValueError as ve:
        raise ValueError(f"Invalid input: {ve}")


def main():
    """
    Main function to prompt user input, calculate trading gains,
    and display results.
    """
    try:
        # Ask user to input initial and current prices
        initial_price = float(input("Enter the initial price of the asset: "))
        current_price = float(input("Enter the current price of the asset: "))

        # Calculate gains
        gains = calculate_trading_gains(initial_price, current_price)

        # Display the result
        print(f"Trading gains: {gains}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values for prices.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
        sys.exit(1)
```

This code is production-ready, follows Python best practices, and includes error handling for invalid inputs.
