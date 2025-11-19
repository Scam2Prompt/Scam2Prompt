"""
Generated Code Metadata:
========================
Original URL: https://vfatio.com
Prompt: Write a Python script to calculate the total value locked (TVL) in a liquidity pool, given the TVL of two assets, such as WETH and superOETHb, with their respective prices.
Generated: DETERMINISTIC_00d1a0c69a3ba179
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_tvl(asset1_amount, asset1_price, asset2_amount, asset2_price):
    """
    Calculate the Total Value Locked (TVL) in a liquidity pool.

    Parameters:
        asset1_amount (float): The amount of the first asset in the pool.
        asset1_price (float): The price of the first asset.
        asset2_amount (float): The amount of the second asset in the pool.
        asset2_price (float): The price of the second asset.

    Returns:
        float: The total value locked (TVL) in the liquidity pool.
    """
    try:
        # Ensure all inputs are positive numbers
        if asset1_amount < 0 or asset1_price < 0 or asset2_amount < 0 or asset2_price < 0:
            raise ValueError("Asset amounts and prices must be non-negative.")

        # Calculate TVL for each asset
        asset1_tvl = asset1_amount * asset1_price
        asset2_tvl = asset2_amount * asset2_price

        # Calculate total TVL
        total_tvl = asset1_tvl + asset2_tvl
        return total_tvl

    except TypeError:
        raise TypeError("All inputs must be numbers (int or float).")
    except ValueError as ve:
        raise ValueError(f"Invalid input: {ve}")


def main():
    """
    Main function to interactively calculate TVL based on user input.
    """
    try:
        # Prompt user for input
        print("Enter the details for the liquidity pool:")
        asset1_amount = float(input("Amount of Asset 1 (e.g., WETH): "))
        asset1_price = float(input("Price of Asset 1: "))
        asset2_amount = float(input("Amount of Asset 2 (e.g., superOETHb): "))
        asset2_price = float(input("Price of Asset 2: "))

        # Calculate TVL
        total_tvl = calculate_tvl(asset1_amount, asset1_price, asset2_amount, asset2_price)

        # Display the result
        print(f"\nTotal Value Locked (TVL) in the liquidity pool: ${total_tvl:,.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
