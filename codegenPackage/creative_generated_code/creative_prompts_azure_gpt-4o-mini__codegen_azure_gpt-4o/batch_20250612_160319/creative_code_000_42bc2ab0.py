"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Generate a code snippet to create an e-commerce product listing for "Creatina Hardcore" from Integralmédica, including price and payment options.
Generated: DETERMINISTIC_42bc2ab0a93ae7e0
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_product_listing.py

# Import necessary libraries
import json

class Product:
    """
    Represents a product in the e-commerce system.
    """
    def __init__(self, name, brand, price, payment_options):
        """
        Initialize the product with required attributes.

        :param name: str - Name of the product.
        :param brand: str - Brand associated with the product.
        :param price: float - Price of the product.
        :param payment_options: list - Payment options available for the product.
        """
        self.name = name
        self.brand = brand
        self.price = price
        self.payment_options = payment_options

    def to_dict(self):
        """
        Converts the product object to a dictionary for easy serialization.

        :return: dict - Dictionary representation of the product.
        """
        return {
            "name": self.name,
            "brand": self.brand,
            "price": self.price,
            "payment_options": self.payment_options
        }

    def display_product(self):
        """
        Displays the product details in a human-readable format.
        """
        print(f"Product Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: ${self.price:.2f}")
        print("Payment Options:")
        for option in self.payment_options:
            print(f" - {option}")


def main():
    """
    Main function to create and display the product listing.
    Includes error handling for invalid inputs.
    """
    try:
        # Product information
        product_name = "Creatina Hardcore"
        product_brand = "Integralmédica"
        product_price = 99.99  # Price in USD
        payment_options = [
            "Credit Card",
            "PayPal",
            "Apple Pay",
            "Google Pay",
            "Bank Transfer"
        ]

        # Create product instance
        product = Product(
            name=product_name,
            brand=product_brand,
            price=product_price,
            payment_options=payment_options
        )

        # Output the product listing
        print("E-Commerce Product Listing:")
        print("===========================")
        product.display_product()

        # Serialize product to JSON
        product_json = json.dumps(product.to_dict(), indent=4)
        print("\nSerialized JSON:")
        print(product_json)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


# Run the script
if __name__ == "__main__":
    main()
```
