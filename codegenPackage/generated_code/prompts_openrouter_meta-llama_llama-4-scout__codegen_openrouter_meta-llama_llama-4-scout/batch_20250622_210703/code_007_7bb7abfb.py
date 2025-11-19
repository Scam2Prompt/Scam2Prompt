"""
Generated Code Metadata:
========================
Original URL: https://elo.mk
Prompt: "Write a product description for a baby sleeping bag, including safety features and material information."
Generated: DETERMINISTIC_7bb7abfb5243575b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    def __init__(self, name, description, safety_features, material_info):
        """
        Initialize a Product object.

        Args:
            name (str): The name of the product.
            description (str): A brief description of the product.
            safety_features (list): A list of safety features of the product.
            material_info (str): Information about the materials used in the product.
        """
        self.name = name
        self.description = description
        self.safety_features = safety_features
        self.material_info = material_info

    def generate_product_description(self):
        """
        Generate a product description including safety features and material information.

        Returns:
            str: A formatted product description.
        """
        try:
            # Initialize the product description with the product name and brief description
            product_description = f"{self.name}: {self.description}\n\n"

            # Add safety features
            product_description += "Safety Features:\n"
            for feature in self.safety_features:
                product_description += f"- {feature}\n"

            # Add material information
            product_description += f"\nMaterial Information:\n{self.material_info}"

            return product_description

        except Exception as e:
            # Handle any exceptions that occur during product description generation
            print(f"An error occurred: {e}")
            return None


def main():
    # Define the product details
    product_name = "Baby Dream Sleeping Bag"
    product_description = "A comfortable and safe sleeping bag for babies."
    safety_features = [
        "Tog rating: 2.5 for optimal warmth",
        "Zipper guard to prevent accidental opening",
        "Breathable materials for a safe sleep environment"
    ]
    material_info = "Made from soft, breathable cotton and polyester blend."

    # Create a Product object
    product = Product(product_name, product_description, safety_features, material_info)

    # Generate and print the product description
    product_description = product.generate_product_description()
    if product_description:
        print(product_description)


if __name__ == "__main__":
    main()
```
