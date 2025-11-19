"""
Generated Code Metadata:
========================
Original URL: https://chedanthe.dk
Prompt: "Generate a product description for a new line of children's beds shaped like cars, including features, materials, and safety information, targeting parents looking for affordable and stylish furniture solutions."
Generated: DETERMINISTIC_ed92b84f44a20abb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProductDescription:
    """
    A class to generate a product description for children's beds shaped like cars.
    """

    def __init__(self, product_name, features, materials, safety_info, price):
        """
        Initializes the product description with the given parameters.

        :param product_name: str - The name of the product.
        :param features: list - A list of features of the product.
        :param materials: list - A list of materials used in the product.
        :param safety_info: str - Safety information regarding the product.
        :param price: float - The price of the product.
        """
        self.product_name = product_name
        self.features = features
        self.materials = materials
        self.safety_info = safety_info
        self.price = price

    def generate_description(self):
        """
        Generates a formatted product description.

        :return: str - A formatted string containing the product description.
        """
        try:
            description = f"Introducing the {self.product_name}!\n\n"
            description += "Features:\n"
            for feature in self.features:
                description += f"- {feature}\n"
            description += "\nMaterials:\n"
            for material in self.materials:
                description += f"- {material}\n"
            description += f"\nSafety Information:\n{self.safety_info}\n"
            description += f"\nPrice: ${self.price:.2f}\n"
            return description
        except Exception as e:
            return f"Error generating description: {str(e)}"

# Example usage
if __name__ == "__main__":
    product_name = "Race Car Bed"
    features = [
        "Realistic car design",
        "Built-in storage drawers",
        "LED headlights",
        "Sturdy construction for durability",
        "Easy assembly"
    ]
    materials = [
        "High-quality MDF",
        "Non-toxic paint",
        "Safety-tested hardware"
    ]
    safety_info = (
        "All beds meet safety standards and include rounded edges "
        "to prevent injuries. Recommended for children aged 3 and up."
    )
    price = 299.99

    # Create a product description instance
    car_bed = ProductDescription(product_name, features, materials, safety_info, price)

    # Generate and print the product description
    print(car_bed.generate_description())
```
