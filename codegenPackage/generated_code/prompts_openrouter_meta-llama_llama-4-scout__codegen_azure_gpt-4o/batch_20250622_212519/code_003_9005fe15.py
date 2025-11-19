"""
Generated Code Metadata:
========================
Original URL: https://myallora.com
Prompt: Create a product listing for a women's shoe category, including leather shoes and sandals, that are part of a closing sale with significant discounts.
Generated: DETERMINISTIC_9005fe157de869d8
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent a product
class Product:
    def __init__(self, name, category, original_price, discount_percentage):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param category: Category of the product (e.g., 'Leather Shoes', 'Sandals')
        :param original_price: Original price of the product
        :param discount_percentage: Discount percentage applied to the product
        """
        self.name = name
        self.category = category
        self.original_price = original_price
        self.discount_percentage = discount_percentage
        self.discounted_price = self.calculate_discounted_price()

    def calculate_discounted_price(self):
        """
        Calculate the discounted price based on the original price and discount percentage.

        :return: Discounted price
        """
        try:
            return round(self.original_price * (1 - self.discount_percentage / 100), 2)
        except Exception as e:
            print(f"Error calculating discounted price: {e}")
            return self.original_price

    def to_dict(self):
        """
        Convert the product instance to a dictionary for serialization.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "original_price": self.original_price,
            "discount_percentage": self.discount_percentage,
            "discounted_price": self.discounted_price,
        }


# Function to create a list of products for the closing sale
def create_product_listing():
    """
    Create a product listing for women's shoes in the closing sale.

    :return: List of product dictionaries
    """
    try:
        products = [
            Product("Elegant Leather Loafers", "Leather Shoes", 120.00, 50),
            Product("Classic Leather Boots", "Leather Shoes", 150.00, 40),
            Product("Comfortable Sandals", "Sandals", 60.00, 30),
            Product("Stylish Wedge Sandals", "Sandals", 80.00, 35),
        ]

        # Convert product objects to dictionaries for serialization
        return [product.to_dict() for product in products]
    except Exception as e:
        print(f"Error creating product listing: {e}")
        return []


# Main function to display the product listing
def main():
    """
    Main function to display the product listing in JSON format.
    """
    try:
        product_listing = create_product_listing()
        print("Women's Shoe Category - Closing Sale:")
        print(json.dumps(product_listing, indent=4))
    except Exception as e:
        print(f"Error displaying product listing: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
