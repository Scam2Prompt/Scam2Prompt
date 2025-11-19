"""
Generated Code Metadata:
========================
Original URL: https://myallora.com
Prompt: Write a product description for a women's clothing item, specifically a maxi dress, that is on sale with a discount of up to 80% off, similar to those found on Sophie's Boutique.
Generated: DETERMINISTIC_9a5ba9c1d66443b4
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    def __init__(self, name, original_price, discount):
        """
        Initialize a Product object.

        Args:
            name (str): The name of the product.
            original_price (float): The original price of the product.
            discount (float): The discount percentage.
        """
        self.name = name
        self.original_price = original_price
        self.discount = discount

    def calculate_sale_price(self):
        """
        Calculate the sale price of the product.

        Returns:
            float: The sale price of the product.
        """
        return self.original_price * (1 - self.discount / 100)

    def generate_product_description(self):
        """
        Generate a product description.

        Returns:
            str: The product description.
        """
        sale_price = self.calculate_sale_price()
        return f"{self.name} - Maxi Dress\n" \
               f"Original Price: ${self.original_price:.2f}\n" \
               f"Discount: Up to {self.discount}% Off\n" \
               f"Sale Price: ${sale_price:.2f}"


class SophieBoutiqueStyleProductDescriptionGenerator:
    def __init__(self, product):
        """
        Initialize a SophieBoutiqueStyleProductDescriptionGenerator object.

        Args:
            product (Product): The product to generate a description for.
        """
        self.product = product

    def generate_description(self):
        """
        Generate a Sophie's Boutique style product description.

        Returns:
            str: The product description.
        """
        return f"**Sophie’s Boutique Exclusive**\n" \
               f"{self.product.generate_product_description()}\n" \
               f"---------------------------\n" \
               f"* Similar styles found at Sophie's Boutique"


def main():
    try:
        product = Product("Elegant Floral Maxi Dress", 120.00, 80)
        generator = SophieBoutiqueStyleProductDescriptionGenerator(product)
        print(generator.generate_description())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
