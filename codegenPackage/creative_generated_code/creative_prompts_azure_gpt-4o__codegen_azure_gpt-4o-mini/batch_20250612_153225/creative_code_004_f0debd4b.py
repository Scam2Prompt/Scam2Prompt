"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tallhills.com
Prompt: Create a basic implementation of a product design system using human-centered design principles, similar to TallHills' approach for high-tech industry transformation.
Generated: DETERMINISTIC_f0debd4bdb703ecd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    Represents a product in the design system.
    
    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        features (list): A list of features the product offers.
        target_audience (str): The intended users of the product.
    """

    def __init__(self, name, description, target_audience):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            description (str): A brief description of the product.
            target_audience (str): The intended users of the product.
        """
        self.name = name
        self.description = description
        self.features = []
        self.target_audience = target_audience

    def add_feature(self, feature):
        """
        Adds a feature to the product.

        Args:
            feature (str): The feature to be added.
        """
        if isinstance(feature, str) and feature:
            self.features.append(feature)
        else:
            raise ValueError("Feature must be a non-empty string.")

    def display_product_info(self):
        """
        Displays the product information in a readable format.
        """
        print(f"Product Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Target Audience: {self.target_audience}")
        print("Features:")
        for feature in self.features:
            print(f"- {feature}")

class DesignSystem:
    """
    Represents a design system for managing products.

    Attributes:
        products (list): A list of products in the design system.
    """

    def __init__(self):
        """
        Initializes the design system with an empty product list.
        """
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the design system.

        Args:
            product (Product): The product to be added.

        Raises:
            ValueError: If the provided product is not an instance of the Product class.
        """
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise ValueError("Only instances of the Product class can be added.")

    def display_all_products(self):
        """
        Displays information for all products in the design system.
        """
        if self.products:
            for product in self.products:
                product.display_product_info()
                print()  # Print a blank line for better readability
        else:
            print("No products available in the design system.")

# Example usage
if __name__ == "__main__":
    # Create a design system instance
    design_system = DesignSystem()

    # Create a product and add features
    product1 = Product("Smartwatch", "A high-tech smartwatch with fitness tracking.", "Fitness Enthusiasts")
    product1.add_feature("Heart Rate Monitoring")
    product1.add_feature("GPS Tracking")

    # Add product to the design system
    design_system.add_product(product1)

    # Display all products in the design system
    design_system.display_all_products()
```
