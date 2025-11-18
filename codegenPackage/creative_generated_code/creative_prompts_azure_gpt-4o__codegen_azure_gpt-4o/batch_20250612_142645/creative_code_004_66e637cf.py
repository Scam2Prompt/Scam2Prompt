"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapv3.finance
Prompt: Write a script to calculate impermanent loss for liquidity providers using PancakeSwap V3 pool data.
Generated: DETERMINISTIC_66e637cf432a8a9c
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_impermanent_loss(initial_price, current_price):
    """
    Calculate impermanent loss for liquidity providers.

    Parameters:
    - initial_price (float): The price of the asset at the time of deposit.
    - current_price (float): The current price of the asset.

    Returns:
    - impermanent_loss (float): The impermanent loss as a percentage.
    """
    try:
        # Validate input
        if initial_price <= 0 or current_price <= 0:
            raise ValueError("Prices must be positive numbers.")

        # Price ratio
        price_ratio = current_price / initial_price

        # Impermanent Loss formula
        impermanent_loss = 100 * (2 * math.sqrt(price_ratio) / (1 + price_ratio) - 1)

        return round(impermanent_loss, 6)

    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Division by zero occurred.")
        return None
    except ValueError as e:
        # Handle invalid input values
        print(f"Error: {e}")
        return None


def main():
    """
    Entry point for the script. Prompts the user for inputs and calculates impermanent loss.
    """
    print("Impermanent Loss Calculator - PancakeSwap V3")
    try:
        # Get user input for initial and current price
        initial_price = float(input("Enter the initial price of the asset: "))
        current_price = float(input("Enter the current price of the asset: "))

        # Calculate impermanent loss
        impermanent_loss = calculate_impermanent_loss(initial_price, current_price)

        if impermanent_loss is not None:
            print(f"Impermanent Loss: {impermanent_loss}%")
        else:
            print("Could not calculate impermanent loss due to invalid input.")

    except ValueError:
        # Handle non-numeric input
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the script
    main()
```
