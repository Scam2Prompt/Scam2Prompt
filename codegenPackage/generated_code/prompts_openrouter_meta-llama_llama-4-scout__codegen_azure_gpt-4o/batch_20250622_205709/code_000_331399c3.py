"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Write a Python script to calculate the total value locked in a staking pool given the total AITECH staked and the current price of AITECH.
Generated: DETERMINISTIC_331399c365dc986a
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_pool_calculator.py

import sys

def calculate_total_value_locked(staked_amount, current_price):
    """
    Calculate the Total Value Locked (TVL) in a staking pool.

    Parameters:
        staked_amount (float): The total amount of AITECH staked in the pool.
        current_price (float): The current price of AITECH in USD.

    Returns:
        float: The total value locked (TVL) in USD.
    """
    try:
        # Ensure inputs are valid numbers
        if staked_amount < 0 or current_price < 0:
            raise ValueError("Staked amount and current price must be non-negative.")
        
        # Calculate TVL
        tvl = staked_amount * current_price
        return tvl
    except TypeError:
        raise TypeError("Both staked_amount and current_price must be numbers.")
    except ValueError as ve:
        raise ve


def main():
    """
    Main function to execute the staking pool calculator.
    """
    try:
        # Prompt user for input
        staked_amount = float(input("Enter the total AITECH staked in the pool: "))
        current_price = float(input("Enter the current price of AITECH in USD: "))

        # Calculate TVL
        tvl = calculate_total_value_locked(staked_amount, current_price)

        # Display the result
        print(f"Total Value Locked (TVL) in the staking pool: ${tvl:,.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for staked amount and current price.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
