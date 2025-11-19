"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Write a product description for the Eva Chair and Beach House Armchair, highlighting their design inspiration, materials, and suitability for outdoor spaces in hotels, restaurants, or private residences."
Generated: DETERMINISTIC_09c17f1e086e9cbd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Furniture:
    def __init__(self, name, description, materials, suitable_for):
        """
        Initialize a Furniture object.

        Args:
            name (str): The name of the furniture.
            description (str): A brief description of the furniture.
            materials (list): A list of materials used to make the furniture.
            suitable_for (list): A list of spaces where the furniture is suitable for.
        """
        self.name = name
        self.description = description
        self.materials = materials
        self.suitable_for = suitable_for

    def get_description(self):
        """
        Returns a formatted description of the furniture.

        Returns:
            str: A formatted description of the furniture.
        """
        return f"{self.name}: {self.description}"

    def get_details(self):
        """
        Returns a formatted string of the furniture's details.

        Returns:
            str: A formatted string of the furniture's details.
        """
        materials_str = ", ".join(self.materials)
        suitable_for_str = ", ".join(self.suitable_for)
        return f"Design Inspiration: Modern and sleek design inspired by nature.\nMaterials: {materials_str}\nSuitable for: {suitable_for_str}"


class ProductDescriptionGenerator:
    def __init__(self):
        """
        Initialize a ProductDescriptionGenerator object.
        """
        self.furniture_products = {
            "Eva Chair": Furniture(
                "Eva Chair",
                "A stylish and comfortable chair perfect for outdoor spaces.",
                ["Durable synthetic wicker", "Weather-resistant cushions"],
                ["Hotels", "Restaurants", "Private Residences"]
            ),
            "Beach House Armchair": Furniture(
                "Beach House Armchair",
                "A cozy and inviting armchair ideal for beach-inspired outdoor spaces.",
                ["Recycled plastic", "Soft-touch cushions"],
                ["Hotels", "Restaurants", "Private Residences"]
            )
        }

    def generate_description(self, product_name):
        """
        Generates a product description for the given product name.

        Args:
            product_name (str): The name of the product.

        Returns:
            str: A formatted product description.

        Raises:
            ValueError: If the product name is not found.
        """
        if product_name not in self.furniture_products:
            raise ValueError("Product not found")

        product = self.furniture_products[product_name]
        description = product.get_description()
        details = product.get_details()

        return f"{description}\n\n{details}"


def main():
    generator = ProductDescriptionGenerator()

    try:
        eva_chair_description = generator.generate_description("Eva Chair")
        beach_house_armchair_description = generator.generate_description("Beach House Armchair")

        print("Eva Chair:")
        print(eva_chair_description)
        print("\nBeach House Armchair:")
        print(beach_house_armchair_description)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
