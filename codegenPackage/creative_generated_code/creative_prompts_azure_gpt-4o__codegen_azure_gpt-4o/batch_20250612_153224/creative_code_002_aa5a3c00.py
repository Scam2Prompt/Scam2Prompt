"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Create a function in Python to calculate discounts and taxes for products like "LUXXE SLIM (L-Carnitine & Green Tea Extract)" based on user input for quantity and location.
Generated: DETERMINISTIC_aa5a3c00c54a6b0f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_price(product_name, quantity, location):
    """
    Calculate the final price of a product based on discounts, taxes, and location.

    Args:
        product_name (str): Name of the product.
        quantity (int): Number of units purchased.
        location (str): Location of the buyer for tax calculation.

    Returns:
        dict: A dictionary containing the original price, discounted price, tax amount, and total price.
    """
    try:
        # Validate input
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if location.strip() == "":
            raise ValueError("Location must not be empty.")
        
        # Define base price of the product
        product_prices = {
            "LUXXE SLIM (L-Carnitine & Green Tea Extract)": 50.00  # Example price in USD
        }

        if product_name not in product_prices:
            raise ValueError(f"Unknown product: {product_name}")

        base_price = product_prices[product_name]

        # Calculate original price
        original_price = base_price * quantity

        # Apply discount
        # Example: 10% discount for purchasing more than 5 items
        discount_rate = 0.10 if quantity > 5 else 0.0
        discounted_price = original_price * (1 - discount_rate)

        # Define tax rates based on location
        location_tax_rates = {
            "CA": 0.13,  # Example: California sales tax rate (13%)
            "NY": 0.08,  # Example: New York sales tax rate (8%)
            "TX": 0.0625, # Example: Texas sales tax rate (6.25%)
            "DEFAULT": 0.10  # Default tax rate (10%)
        }
        
        tax_rate = location_tax_rates.get(location.upper(), location_tax_rates["DEFAULT"])
        tax_amount = discounted_price * tax_rate

        # Calculate the total price
        total_price = discounted_price + tax_amount

        # Return the results in a structured format
        return {
            "product_name": product_name,
            "quantity": quantity,
            "location": location.upper(),
            "original_price": round(original_price, 2),
            "discount_rate": round(discount_rate * 100, 2),  # Convert to percentage
            "discounted_price": round(discounted_price, 2),
            "tax_rate": round(tax_rate * 100, 2),  # Convert to percentage
            "tax_amount": round(tax_amount, 2),
            "total_price": round(total_price, 2)
        }
    except Exception as e:
        # Handle unexpected errors
        print(f"Error: {e}", file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    # Example: User input
    product = "LUXXE SLIM (L-Carnitine & Green Tea Extract)"
    qty = 7
    user_location = "CA"

    # Call the function and display the result
    result = calculate_price(product, qty, user_location)
    if result:
        print("Price Calculation Result:")
        for key, value in result.items():
            print(f"{key}: {value}")
```
