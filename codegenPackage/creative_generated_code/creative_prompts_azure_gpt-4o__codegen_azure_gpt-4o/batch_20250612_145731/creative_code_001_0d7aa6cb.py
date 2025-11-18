"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pass-vee.com
Prompt: Generate code to calculate margin level and free margin for a trading account based on the definitions provided on the Changexcapital website.
Generated: DETERMINISTIC_0d7aa6cb7e6404a0
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Margin Level and Free Margin Calculator for Trading Accounts
# Author: [Your Name]
# Date: [Today's Date]

# Import necessary module for exception handling
import sys

def calculate_margin_level_and_free_margin(equity, used_margin):
    """
    Calculates the margin level and free margin for a trading account.

    Args:
        equity (float): The total equity of the trading account.
        used_margin (float): The margin that is currently being used in trades.

    Returns:
        dict: A dictionary containing 'margin_level' (percentage) and 'free_margin' (float).

    Raises:
        ValueError: If equity or used_margin is negative.
        ZeroDivisionError: If used_margin is zero when calculating margin level.
    """
    # Validate input
    if equity < 0:
        raise ValueError("Equity cannot be negative.")
    if used_margin < 0:
        raise ValueError("Used margin cannot be negative.")
    
    # Calculate free margin
    free_margin = equity - used_margin

    # Calculate margin level (represented as a percentage)
    if used_margin == 0:
        margin_level = float('inf')  # Infinite margin level when used margin is zero
    else:
        margin_level = (equity / used_margin) * 100

    # Return results as a dictionary
    return {
        "margin_level": margin_level,
        "free_margin": free_margin
    }

def main():
    """
    Main function to interact with the user for calculating margin level and free margin.
    """
    try:
        # Take user inputs
        equity = float(input("Enter account equity (e.g., 10000): "))
        used_margin = float(input("Enter used margin (e.g., 2000): "))

        # Perform calculations
        results = calculate_margin_level_and_free_margin(equity, used_margin)

        # Display results
        print("\n--- Calculation Results ---")
        print(f"Margin Level: {results['margin_level']:.2f}%")
        print(f"Free Margin: {results['free_margin']:.2f}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except ZeroDivisionError:
        print("Error: Used margin cannot be zero when calculating margin level.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
