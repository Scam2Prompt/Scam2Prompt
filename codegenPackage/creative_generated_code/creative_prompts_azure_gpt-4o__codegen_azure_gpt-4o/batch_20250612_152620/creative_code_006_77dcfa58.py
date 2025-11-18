"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkabridge.pages.dev
Prompt: Develop a program to calculate the percentage difference between the limit price and market price for a specific ad on PolkaBridge.
Generated: DETERMINISTIC_77dcfa5841e52d29
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_percentage_difference(limit_price, market_price):
    """
    Calculate the percentage difference between the limit price and market price.

    Args:
        limit_price (float): The limit price of the ad.
        market_price (float): The market price for the ad.

    Returns:
        float: The percentage difference as a positive value.
    """
    try:
        # Ensure inputs are positive numbers
        if limit_price <= 0 or market_price <= 0:
            raise ValueError("Prices must be positive numbers.")
        
        # Calculate the percentage difference
        difference = abs(limit_price - market_price)
        percentage_difference = (difference / market_price) * 100
        return percentage_difference
    except TypeError:
        raise TypeError("Both limit_price and market_price must be numeric values.")
    except Exception as e:
        # Catch any other unforeseen errors
        raise RuntimeError(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to handle user input and output the percentage difference calculation.
    """
    try:
        # Prompt user for limit price and market price inputs
        print("Enter the limit price and market price for the PolkaBridge ad.")
        limit_price = float(input("Limit Price: "))
        market_price = float(input("Market Price: "))

        # Perform calculation
        percentage_difference = calculate_percentage_difference(limit_price, market_price)

        # Display the result
        print(f"Percentage Difference: {percentage_difference:.2f}%")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point for the program
    main()
```
