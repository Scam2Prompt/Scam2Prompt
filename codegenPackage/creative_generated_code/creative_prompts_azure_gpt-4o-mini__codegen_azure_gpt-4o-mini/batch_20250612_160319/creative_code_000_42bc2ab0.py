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
class Product:
    """
    A class to represent an e-commerce product listing.
    """

    def __init__(self, name, brand, price, payment_options):
        """
        Initializes a new product instance.

        :param name: str - The name of the product.
        :param brand: str - The brand of the product.
        :param price: float - The price of the product.
        :param payment_options: list - A list of available payment options.
        """
        self.name = name
        self.brand = brand
        self.price = price
        self.payment_options = payment_options

    def display_product_info(self):
        """
        Displays detailed information about the product.
        """
        try:
            print(f"Product Name: {self.name}")
            print(f"Brand: {self.brand}")
            print(f"Price: ${self.price:.2f}")
            print("Payment Options:")
            for option in self.payment_options:
                print(f" - {option}")
        except Exception as e:
            print("An error occurred while displaying product information:", str(e))


def main():
    """
    Main function to create and display an e-commerce product listing.
    """
    # Product details
    product_name = "Creatina Hardcore"
    product_brand = "Integralmédica"
    product_price = 89.90  # Price in local currency (e.g., BRL)
    payment_methods = ["Credit Card", "PayPal", "Bank Transfer"]

    # Create a product instance
    product = Product(product_name, product_brand, product_price, payment_methods)

    # Display product information
    product.display_product_info()


if __name__ == "__main__":
    main()
```
