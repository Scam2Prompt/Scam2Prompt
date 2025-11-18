"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdstarfx.com
Prompt: Write a Python script to calculate the required margin for a forex trade using the leverage values (1:500, 1:400, 1:300) provided for the account types on the S D STAR FX LTD platform.
Generated: DETERMINISTIC_1bbbcf6bc8a915aa
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the required margin for a forex trade based on leverage.
This script supports leverage values of 1:500, 1:400, and 1:300, as provided
by the account types on the S D STAR FX LTD platform.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import required module
import sys

# Function to calculate margin
def calculate_margin(trade_size_usd, leverage_ratio):
    """
    Calculates the required margin for a forex trade.

    Args:
        trade_size_usd (float): The size of the trade in USD.
        leverage_ratio (int): The leverage value (e.g., 500 for 1:500).

    Returns:
        float: The required margin in USD.
    """
    try:
        # Margin calculation formula: Margin = Trade Size / Leverage Ratio
        margin = trade_size_usd / leverage_ratio
        return margin
    except ZeroDivisionError:
        raise ValueError("Leverage ratio cannot be zero.")
    except TypeError:
        raise ValueError("Invalid input type. Ensure trade size is a number and leverage is an integer.")

# Supported leverage values
SUPPORTED_LEVERAGES = [500, 400, 300]

def main():
    """
    Main function to interactively calculate margin based on user input.
    """
    try:
        # Get user input for trade size
        trade_size_usd = float(input("Enter the trade size in USD: "))
        if trade_size_usd <= 0:
            raise ValueError("Trade size must be a positive number.")

        # Get user input for leverage ratio
        print("Available leverage ratios: 1:500, 1:400, 1:300")
        leverage_ratio = int(input("Enter the leverage ratio (e.g., 500 for 1:500): "))
        if leverage_ratio not in SUPPORTED_LEVERAGES:
            raise ValueError(f"Invalid leverage ratio. Supported values are {SUPPORTED_LEVERAGES}.")

        # Calculate margin
        margin = calculate_margin(trade_size_usd, leverage_ratio)

        # Display the result
        print(f"Required margin for a trade size of ${trade_size_usd} with 1:{leverage_ratio} leverage is: ${margin:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the margin calculator.")

# Run the script
if __name__ == "__main__":
    main()
```
