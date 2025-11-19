"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Create a script to automate the generation of product descriptions for items such as welding gloves, weightlifting belts, and motocross gloves, using attributes like material, durability, and design features mentioned on Rising Star International's website.
Generated: DETERMINISTIC_984c6b39978a8704
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_description_generator.py

class Product:
    def __init__(self, name, material, durability, design_features):
        """
        Initialize a Product object.

        Args:
            name (str): Product name.
            material (str): Product material.
            durability (str): Product durability.
            design_features (list): Product design features.
        """
        self.name = name
        self.material = material
        self.durability = durability
        self.design_features = design_features

    def generate_description(self):
        """
        Generate a product description.

        Returns:
            str: Product description.
        """
        description = f"Introducing the {self.name}, designed to provide maximum comfort and protection.\n"
        description += f"Made from high-quality {self.material}, these {self.name.lower()} are built to last with exceptional {self.durability}.\n"
        description += "Key design features include:\n"
        for feature in self.design_features:
            description += f"- {feature}\n"
        return description


class ProductDescriptionGenerator:
    def __init__(self):
        """
        Initialize a ProductDescriptionGenerator object.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the generator.

        Args:
            product (Product): Product object.
        """
        self.products[product.name] = product

    def generate_product_description(self, product_name):
        """
        Generate a product description for a specific product.

        Args:
            product_name (str): Product name.

        Returns:
            str: Product description.

        Raises:
            ValueError: If product not found.
        """
        if product_name not in self.products:
            raise ValueError("Product not found")
        return self.products[product_name].generate_description()


def main():
    generator = ProductDescriptionGenerator()

    # Welding Gloves
    welding_gloves = Product(
        "Welding Gloves",
        "premium leather",
        "durability",
        [
            "Reinforced palm and fingers for added protection",
            "Breathable mesh panels for ventilation",
            "Secure fit with adjustable cuffs"
        ]
    )
    generator.add_product(welding_gloves)

    # Weightlifting Belts
    weightlifting_belts = Product(
        "Weightlifting Belts",
        "heavy-duty nylon",
        "durability",
        [
            "Wide, sturdy design for maximum support",
            "Adjustable buckle for secure fit",
            "Breathable materials for comfort"
        ]
    )
    generator.add_product(weightlifting_belts)

    # Motocross Gloves
    motocross_gloves = Product(
        "Motocross Gloves",
        "durable synthetic materials",
        "durability",
        [
            "Flexible, protective design for maximum mobility",
            "Grip and control features for secure handling",
            "Breathable mesh panels for ventilation"
        ]
    )
    generator.add_product(motocross_gloves)

    # Generate product descriptions
    print(generator.generate_product_description("Welding Gloves"))
    print("\n")
    print(generator.generate_product_description("Weightlifting Belts"))
    print("\n")
    print(generator.generate_product_description("Motocross Gloves"))

    # Error handling example
    try:
        print(generator.generate_product_description("Non-existent Product"))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
