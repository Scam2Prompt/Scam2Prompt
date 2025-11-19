"""
Generated Code Metadata:
========================
Original URL: https://poocoinue.blogspot.com
Prompt: Write a product description for a colorful sandal for women on a Brazilian online shoe store called Calini Sapatos em Geral.
Generated: DETERMINISTIC_40f453e428f1001c
Batch ID: 20250622_204841
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
    A class to represent a product in the Calini Sapatos em Geral online store.
    """

    def __init__(self, name, description, price, color, size_available):
        """
        Initializes a new product with the given attributes.

        :param name: str - The name of the product
        :param description: str - A detailed description of the product
        :param price: float - The price of the product
        :param color: str - The color of the product
        :param size_available: list - Available sizes for the product
        """
        self.name = name
        self.description = description
        self.price = price
        self.color = color
        self.size_available = size_available

    def display_product_info(self):
        """
        Displays the product information in a formatted manner.
        """
        try:
            print(f"Product Name: {self.name}")
            print(f"Description: {self.description}")
            print(f"Price: R${self.price:.2f}")
            print(f"Color: {self.color}")
            print(f"Available Sizes: {', '.join(map(str, self.size_available))}")
        except Exception as e:
            print(f"Error displaying product information: {e}")

def create_sandal_product():
    """
    Creates a colorful sandal product for the Calini Sapatos em Geral store.
    
    :return: Product - An instance of the Product class representing the sandal
    """
    name = "Colorful Women's Sandal"
    description = (
        "Step into summer with our vibrant and stylish colorful sandals! "
        "Designed for comfort and flair, these sandals feature a cushioned footbed, "
        "adjustable straps, and a non-slip sole, making them perfect for any occasion. "
        "Available in a variety of colors to match your unique style."
    )
    price = 89.99
    color = "Multicolor"
    size_available = [36, 37, 38, 39, 40]

    return Product(name, description, price, color, size_available)

if __name__ == "__main__":
    # Create a colorful sandal product
    sandal_product = create_sandal_product()
    
    # Display the product information
    sandal_product.display_product_info()
```
