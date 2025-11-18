"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3denergysolution.com
Prompt: Write a Python script to generate a discount calculator for products like "Direction Enhancer Rods" and "Door Protectors," incorporating percentage-based discounts as seen on the website.
Generated: DETERMINISTIC_b1f489ce9cd2700f
Batch ID: 20250612_150602
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

def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the price after applying a percentage-based discount.
    
    Args:
        original_price (float): The original price of the product.
        discount_percentage (float): The discount percentage to be applied.
    
    Returns:
        float: The price after the discount is applied.
    """
    try:
        # Ensure the inputs are valid numbers
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        # Calculate the discounted price
        discount_amount = (original_price * discount_percentage) / 100
        discounted_price = original_price - discount_amount
        return round(discounted_price, 2)  # Round to 2 decimal places for currency formatting
    except TypeError:
        raise TypeError("Both original_price and discount_percentage must be numbers.")

def main():
    """
    Main function to drive the discount calculator script.
    """
    print("Welcome to the Product Discount Calculator!")

    # Create a list of products with their original prices
    products = [
        {"name": "Direction Enhancer Rods", "price": 120.00},
        {"name": "Door Protectors", "price": 75.50}
    ]

    try:
        # Ask user for the discount percentage
        discount_percentage = float(input("Enter the discount percentage (0-100): "))
        
        # Validate the discount percentage
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        print("\nDiscounted Prices:")
        
        # Calculate and display discounted prices for each product
        for product in products:
            discounted_price = calculate_discounted_price(product["price"], discount_percentage)
            print(f"{product['name']}: Original Price = ${product['price']:.2f}, Discounted Price = ${discounted_price:.2f}")
    
    except ValueError as e:
        # Handle invalid input
        print(f"Invalid input: {e}")
    except Exception as e:
        # Catch any unforeseen errors
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Discount Calculator!")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
