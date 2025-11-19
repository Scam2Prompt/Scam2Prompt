"""
Generated Code Metadata:
========================
Original URL: https://cakco.com
Prompt: "Write a product specification for a braided design one-shoulder underarm lunch box bag made of genuine leather."
Generated: DETERMINISTIC_8ddc021cb628b0f5
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProductSpecification:
    def __init__(self, product_name, material, description):
        """
        Initialize a ProductSpecification object.

        Args:
            product_name (str): The name of the product.
            material (str): The material used to make the product.
            description (str): A brief description of the product.
        """
        self.product_name = product_name
        self.material = material
        self.description = description
        self.features = []
        self.dimensions = {}
        self.specifications = {}

    def add_feature(self, feature):
        """
        Add a feature to the product.

        Args:
            feature (str): A feature of the product.
        """
        self.features.append(feature)

    def add_dimension(self, dimension, value):
        """
        Add a dimension to the product.

        Args:
            dimension (str): The dimension (e.g., length, width, height).
            value (str): The value of the dimension.
        """
        self.dimensions[dimension] = value

    def add_specification(self, specification, value):
        """
        Add a specification to the product.

        Args:
            specification (str): The specification (e.g., color, weight).
            value (str): The value of the specification.
        """
        self.specifications[specification] = value

    def __str__(self):
        """
        Return a string representation of the ProductSpecification object.
        """
        product_info = f"Product Name: {self.product_name}\n"
        product_info += f"Material: {self.material}\n"
        product_info += f"Description: {self.description}\n\n"

        product_info += "Features:\n"
        for feature in self.features:
            product_info += f"- {feature}\n"

        product_info += "\nDimensions:\n"
        for dimension, value in self.dimensions.items():
            product_info += f"- {dimension.capitalize()}: {value}\n"

        product_info += "\nSpecifications:\n"
        for specification, value in self.specifications.items():
            product_info += f"- {specification.capitalize().replace('_', ' ')}: {value}\n"

        return product_info


def main():
    try:
        # Create a ProductSpecification object
        lunch_bag = ProductSpecification(
            product_name="Braided Design One-Shoulder Underarm Lunch Box Bag",
            material="Genuine Leather",
            description="A stylish and functional lunch box bag made of genuine leather with a braided design."
        )

        # Add features
        lunch_bag.add_feature("One-shoulder design")
        lunch_bag.add_feature("Underarm carry")
        lunch_bag.add_feature("Braided design")

        # Add dimensions
        lunch_bag.add_dimension("length", "10 inches")
        lunch_bag.add_dimension("width", "7 inches")
        lunch_bag.add_dimension("height", "4 inches")

        # Add specifications
        lunch_bag.add_specification("color", "Brown")
        lunch_bag.add_specification("weight", "1.5 pounds")
        lunch_bag.add_specification("closure_type", "Magnetic snap")

        # Print the product specification
        print(lunch_bag)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
