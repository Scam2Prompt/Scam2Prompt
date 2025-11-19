"""
Generated Code Metadata:
========================
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Generate a code snippet to create an e-commerce product listing for "Creatina Hardcore" from Integralmédica, including price and payment options.
Generated: DETERMINISTIC_42bc2ab0a93ae7e0
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define the Product class
class Product:
    """
    A class to represent an e-commerce product.
    """
    def __init__(self, name, brand, price, payment_options):
        """
        Initialize the product with name, brand, price, and payment options.

        :param name: str - Name of the product
        :param brand: str - Brand of the product
        :param price: float - Price of the product
        :param payment_options: list - List of payment options
        """
        self.name = name
        self.brand = brand
        self.price = price
        self.payment_options = payment_options

    def to_dict(self):
        """
        Convert the product details to a dictionary.

        :return: dict - Product details as a dictionary
        """
        return {
            "name": self.name,
            "brand": self.brand,
            "price": self.price,
            "payment_options": self.payment_options
        }

# Function to create a product listing
def create_product_listing():
    """
    Create a product listing for 'Creatina Hardcore' from Integralmédica.

    :return: str - JSON representation of the product listing
    """
    try:
        # Product details
        product_name = "Creatina Hardcore"
        product_brand = "Integralmédica"
        product_price = 99.99  # Price in USD
        product_payment_options = [
            "Credit Card",
            "PayPal",
            "Bank Transfer",
            "Cash on Delivery"
        ]

        # Create a Product instance
        product = Product(
            name=product_name,
            brand=product_brand,
            price=product_price,
            payment_options=product_payment_options
        )

        # Convert product details to JSON
        product_json = json.dumps(product.to_dict(), indent=4)
        return product_json

    except Exception as e:
        # Handle any unexpected errors
        return json.dumps({"error": str(e)})

# Main execution
if __name__ == "__main__":
    # Generate the product listing
    product_listing = create_product_listing()
    print(product_listing)
```
