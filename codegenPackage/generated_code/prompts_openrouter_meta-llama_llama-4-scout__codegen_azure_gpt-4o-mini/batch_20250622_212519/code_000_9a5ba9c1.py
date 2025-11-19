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
    """
    A class to represent a product in a clothing store.
    """

    def __init__(self, name, description, original_price, discount_percentage):
        """
        Initializes a new product with the given attributes.

        :param name: str - The name of the product
        :param description: str - A description of the product
        :param original_price: float - The original price of the product
        :param discount_percentage: float - The discount percentage applied to the product
        """
        self.name = name
        self.description = description
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self):
        """
        Calculates the discounted price of the product.

        :return: float - The price after applying the discount
        """
        if not (0 <= self.discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = (self.discount_percentage / 100) * self.original_price
        discounted_price = self.original_price - discount_amount
        return round(discounted_price, 2)

    def display_product_info(self):
        """
        Displays the product information including the discounted price.

        :return: str - Formatted string with product details
        """
        try:
            discounted_price = self.calculate_discounted_price()
            return (f"Product Name: {self.name}\n"
                    f"Description: {self.description}\n"
                    f"Original Price: ${self.original_price:.2f}\n"
                    f"Discount: {self.discount_percentage}% off\n"
                    f"Sale Price: ${discounted_price:.2f}")
        except ValueError as e:
            return str(e)


# Example usage
if __name__ == "__main__":
    # Create a maxi dress product
    maxi_dress = Product(
        name="Elegant Maxi Dress",
        description=("This stunning maxi dress features a flowing silhouette, "
                     "perfect for any occasion. Made from lightweight fabric, "
                     "it offers both comfort and style."),
        original_price=100.00,
        discount_percentage=80
    )

    # Display the product information
    print(maxi_dress.display_product_info())
```
