"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Generate a Python script to calculate the number of JESSE tokens that can be bought with a given amount of BASE, assuming a rate of 0.1 BASE ~ 99,500 JESSE.
Generated: DETERMINISTIC_01d43781f7d9f06c
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
JESSE Token Calculator Script

Calculates the number of JESSE tokens that can be bought with a given amount of BASE.

Usage:
    python jesse_calculator.py <base_amount>

Assumptions:
    - Exchange rate: 0.1 BASE ~ 99,500 JESSE
"""

import sys

def calculate_jesse_tokens(base_amount: float, exchange_rate_base: float = 0.1, exchange_rate_jesse: float = 99500) -> float:
    """
    Calculate the number of JESSE tokens that can be bought with a given amount of BASE.

    Args:
        base_amount (float): The amount of BASE to exchange.
        exchange_rate_base (float, optional): The amount of BASE in the exchange rate. Defaults to 0.1.
        exchange_rate_jesse (float, optional): The amount of JESSE in the exchange rate. Defaults to 99500.

    Returns:
        float: The number of JESSE tokens that can be bought.

    Raises:
        ValueError: If the base amount or exchange rates are not positive numbers.
    """
    if base_amount <= 0 or exchange_rate_base <= 0 or exchange_rate_jesse <= 0:
        raise ValueError("Base amount and exchange rates must be positive numbers.")

    jesse_tokens = (base_amount / exchange_rate_base) * exchange_rate_jesse
    return jesse_tokens

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python jesse_calculator.py <base_amount>")
            sys.exit(1)

        base_amount = float(sys.argv[1])
        jesse_tokens = calculate_jesse_tokens(base_amount)

        print(f"With {base_amount} BASE, you can buy {jesse_tokens:.2f} JESSE tokens.")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
