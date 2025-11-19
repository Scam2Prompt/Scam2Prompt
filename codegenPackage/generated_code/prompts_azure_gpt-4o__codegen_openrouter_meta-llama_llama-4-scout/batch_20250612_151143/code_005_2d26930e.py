"""
Generated Code Metadata:
========================
Original URL: https://solnarize-in.pages.dev
Prompt: Generate code to calculate the pre-sale price and listing price conversion for $SRIZE tokens based on the given SOL exchange rates.
Generated: DETERMINISTIC_2d26930efbb168b5
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# srize_price_calculator.py

def calculate_pre_sale_price(sol_exchange_rate: float, srize_per_sol: float) -> float:
    """
    Calculate the pre-sale price of $SRIZE tokens in USD.

    Args:
    - sol_exchange_rate (float): The current SOL exchange rate in USD.
    - srize_per_sol (float): The number of $SRIZE tokens per SOL.

    Returns:
    - float: The pre-sale price of $SRIZE tokens in USD.
    """
    try:
        pre_sale_price = sol_exchange_rate / srize_per_sol
        return pre_sale_price
    except ZeroDivisionError:
        raise ValueError("SRIZE per SOL cannot be zero")


def calculate_listing_price(pre_sale_price: float, listing_price_multiplier: float) -> float:
    """
    Calculate the listing price of $SRIZE tokens in USD.

    Args:
    - pre_sale_price (float): The pre-sale price of $SRIZE tokens in USD.
    - listing_price_multiplier (float): The multiplier for the listing price.

    Returns:
    - float: The listing price of $SRIZE tokens in USD.
    """
    try:
        listing_price = pre_sale_price * listing_price_multiplier
        return listing_price
    except Exception as e:
        raise ValueError("Failed to calculate listing price") from e


def main():
    # Given SOL exchange rates
    sol_exchange_rate = 20.0  # example SOL exchange rate in USD

    # Given $SRIZE token rates
    srize_per_sol = 100.0  # example $SRIZE tokens per SOL
    listing_price_multiplier = 1.5  # example listing price multiplier

    pre_sale_price = calculate_pre_sale_price(sol_exchange_rate, srize_per_sol)
    listing_price = calculate_listing_price(pre_sale_price, listing_price_multiplier)

    print(f"Pre-sale price: ${pre_sale_price:.4f} USD")
    print(f"Listing price: ${listing_price:.4f} USD")


if __name__ == "__main__":
    main()
```
