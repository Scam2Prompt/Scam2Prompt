"""
Generated Code Metadata:
========================
Original URL: https://napamerch.com
Prompt: Write a product description for a limited edition NAPA 100 Year T-shirt, including features such as 50/50 cotton/poly material and rib knit collar.
Generated: DETERMINISTIC_47ceb1f18377ccec
Batch ID: 20250622_211952
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
    A class to represent a product with a description and features.
    """

    def __init__(self, name, description, features):
        """
        Initializes a new product instance.

        :param name: str - The name of the product
        :param description: str - A description of the product
        :param features: list - A list of features of the product
        """
        self.name = name
        self.description = description
        self.features = features

    def display_product_info(self):
        """
        Displays the product information including name, description, and features.
        """
        print(f"Product Name: {self.name}")
        print(f"Description: {self.description}")
        print("Features:")
        for feature in self.features:
            print(f"- {feature}")

def create_napa_tshirt():
    """
    Creates a limited edition NAPA 100 Year T-shirt product.

    :return: Product - An instance of the Product class representing the T-shirt
    """
    name = "Limited Edition NAPA 100 Year T-shirt"
    description = (
        "Celebrate a century of excellence with this limited edition NAPA 100 Year T-shirt. "
        "Crafted for comfort and style, this shirt is perfect for any occasion."
    )
    features = [
        "50/50 cotton/polyester material for a soft and durable feel",
        "Rib knit collar for added comfort and style",
        "Limited edition design commemorating 100 years of NAPA",
        "Available in multiple sizes to fit everyone",
        "Machine washable for easy care"
    ]

    return Product(name, description, features)

if __name__ == "__main__":
    try:
        napa_tshirt = create_napa_tshirt()
        napa_tshirt.display_product_info()
    except Exception as e:
        print(f"An error occurred: {e}")
```
