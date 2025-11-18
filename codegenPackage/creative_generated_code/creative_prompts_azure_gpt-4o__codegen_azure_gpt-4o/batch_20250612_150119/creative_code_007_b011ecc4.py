"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Write a program to calculate commission fees for Bitcoin mixing transactions, using the range of 4-5% mentioned on mixtum.me.
Generated: DETERMINISTIC_b011ecc48424c6ef
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_commission(amount_in_btc):
    """
    Calculate the commission fee for a Bitcoin transaction.

    Args:
        amount_in_btc (float): The amount in Bitcoin for the transaction.

    Returns:
        tuple: A tuple containing the minimum and maximum commission fees.
    """
    try:
        # Validate the input
        if amount_in_btc <= 0:
            raise ValueError("Transaction amount must be greater than 0.")

        # Define commission rate range (4% to 5%)
        min_rate = 0.04
        max_rate = 0.05

        # Calculate commission fees
        min_commission = amount_in_btc * min_rate
        max_commission = amount_in_btc * max_rate

        return min_commission, max_commission

    except TypeError:
        raise TypeError("Invalid input: amount_in_btc must be a number.")
    except ValueError as ve:
        raise ValueError(str(ve))


def main():
    """
    Main entry point for the program. Prompts the user for input
    and calculates the Bitcoin transaction commission fees.
    """
    try:
        # Prompt the user for the transaction amount in BTC
        user_input = input("Enter the transaction amount in Bitcoin: ").strip()

        # Convert input to float
        amount_in_btc = float(user_input)

        # Calculate commission range
        min_fee, max_fee = calculate_commission(amount_in_btc)

        # Display the result
        print(f"For a Bitcoin transaction of {amount_in_btc} BTC:")
        print(f"  Minimum commission fee (4%): {min_fee:.8f} BTC")
        print(f"  Maximum commission fee (5%): {max_fee:.8f} BTC")

    except ValueError as ve:
        # Handle invalid numeric input
        print(f"Error: {ve}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
