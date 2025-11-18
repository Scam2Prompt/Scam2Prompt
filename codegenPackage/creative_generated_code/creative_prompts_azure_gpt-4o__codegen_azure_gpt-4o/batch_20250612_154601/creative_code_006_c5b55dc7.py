"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Suggest a library for handling Romanian currency (Lei) in a Python e-commerce application and provide example code for calculating discounts on products like those listed on Frigoterm.ro.
Generated: DETERMINISTIC_c5b55dc7ebb2db50
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal, ROUND_HALF_UP  # Used for precise currency calculations
from babel.numbers import format_currency  # Used for formatting currency values

# Constants
CURRENCY_CODE = "RON"  # Romanian Leu currency code
DEFAULT_DISCOUNT_RATE = Decimal("0.10")  # Default discount rate of 10%

# Function to apply a discount and calculate the new price
def calculate_discounted_price(original_price: Decimal, discount_rate: Decimal = DEFAULT_DISCOUNT_RATE) -> Decimal:
    """
    Calculate the discounted price of a product.
    
    :param original_price: Decimal value representing the original price of the product
    :param discount_rate: Decimal value representing the discount rate (defaults to 10%)
    :return: Decimal value representing the discounted price
    """
    try:
        # Ensure original price and discount rate are valid
        if original_price <= 0:
            raise ValueError("Original price must be greater than zero.")
        if not (Decimal("0") <= discount_rate <= Decimal("1")):
            raise ValueError("Discount rate must be between 0 and 1.")

        # Calculate the discount amount
        discount_amount = original_price * discount_rate
        # Calculate the new price after applying the discount
        discounted_price = original_price - discount_amount
        # Round to 2 decimal places using ROUND_HALF_UP (common for currency calculations)
        return discounted_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except Exception as e:
        # Handle unexpected errors
        raise ValueError(f"An error occurred during price calculation: {e}")

# Function to format the price in Romanian currency
def format_price(price: Decimal) -> str:
    """
    Format the price in Romanian Leu (RON) currency.
    
    :param price: Decimal value representing the price
    :return: String formatted as Romanian currency
    """
    try:
        # Use Babel to format the currency
        return format_currency(price, CURRENCY_CODE, locale="ro_RO")
    except Exception as e:
        # Handle unexpected errors
        raise ValueError(f"An error occurred during price formatting: {e}")

# Example usage
if __name__ == "__main__":
    # List of products with their original prices (example from Frigoterm.ro)
    products = {
        "Refrigerator A": Decimal("2500.00"),
        "Dishwasher B": Decimal("1400.00"),
        "Oven C": Decimal("1800.00"),
    }

    # Apply discounts and display the results
    for product_name, original_price in products.items():
        try:
            discounted_price = calculate_discounted_price(original_price)
            formatted_original_price = format_price(original_price)
            formatted_discounted_price = format_price(discounted_price)

            # Print the original and discounted prices
            print(f"Product: {product_name}")
            print(f"Original Price: {formatted_original_price}")
            print(f"Discounted Price: {formatted_discounted_price}")
            print("-" * 40)
        except ValueError as e:
            print(f"Error processing {product_name}: {e}")
```
