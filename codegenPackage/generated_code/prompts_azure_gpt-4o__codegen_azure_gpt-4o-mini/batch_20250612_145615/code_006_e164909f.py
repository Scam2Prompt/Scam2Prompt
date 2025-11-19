"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Create a function that generates sustainable product designs inspired by Linea 7’s approach, focusing on durability, functionality, and end-user experience.
Generated: DETERMINISTIC_e164909f81acdbe4
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class SustainableProduct:
    """
    A class to represent a sustainable product design.
    """

    def __init__(self, name: str, materials: List[str], functionality: str, durability: str):
        """
        Initializes a new sustainable product design.

        :param name: Name of the product
        :param materials: List of materials used in the product
        :param functionality: Description of the product's functionality
        :param durability: Description of the product's durability
        """
        self.name = name
        self.materials = materials
        self.functionality = functionality
        self.durability = durability

    def __str__(self):
        """
        Returns a string representation of the product design.
        """
        return f"Product Name: {self.name}\nMaterials: {', '.join(self.materials)}\nFunctionality: {self.functionality}\nDurability: {self.durability}"


def generate_sustainable_product_design() -> SustainableProduct:
    """
    Generates a sustainable product design inspired by Linea 7's approach.

    :return: An instance of SustainableProduct
    """
    # Sample data for generating product designs
    product_names = ["Eco-Friendly Chair", "Biodegradable Phone Case", "Recycled Water Bottle"]
    materials_options = [
        ["Bamboo", "Recycled Plastic"],
        ["Biodegradable Plastic", "Natural Rubber"],
        ["Stainless Steel", "Recycled Glass"]
    ]
    functionality_options = [
        "Lightweight and portable for easy transport.",
        "Durable and resistant to wear and tear.",
        "Multi-functional with storage capabilities."
    ]
    durability_options = [
        "Designed to last for over 10 years.",
        "Resistant to extreme weather conditions.",
        "Easily repairable with common tools."
    ]

    try:
        # Randomly select attributes for the product design
        name = random.choice(product_names)
        materials = random.choice(materials_options)
        functionality = random.choice(functionality_options)
        durability = random.choice(durability_options)

        # Create and return a new SustainableProduct instance
        return SustainableProduct(name, materials, functionality, durability)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the product design: {e}")
        return None


if __name__ == "__main__":
    # Generate a sustainable product design and print its details
    product_design = generate_sustainable_product_design()
    if product_design:
        print(product_design)
```
