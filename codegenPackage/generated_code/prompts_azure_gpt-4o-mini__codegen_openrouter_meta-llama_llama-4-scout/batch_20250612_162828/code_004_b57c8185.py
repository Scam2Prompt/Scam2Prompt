"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: Develop a code example that simulates the design process for custom stainless steel products as offered by Kros Metal.
Generated: DETERMINISTIC_b57c8185608d8161
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

# Define an Enum for product types
class ProductType(str, Enum):
    CUSTOM_PIPE = "custom_pipe"
    CUSTOM_FITTING = "custom_fitting"
    CUSTOM_SHEET = "custom_sheet"

# Define a class for Product
class Product:
    def __init__(self, product_type: ProductType, material: str, dimensions: Dict[str, float], quantity: int):
        """
        Initialize a Product object.

        Args:
        - product_type (ProductType): The type of product.
        - material (str): The material of the product.
        - dimensions (Dict[str, float]): The dimensions of the product.
        - quantity (int): The quantity of the product.
        """
        self.product_type = product_type
        self.material = material
        self.dimensions = dimensions
        self.quantity = quantity

    def __str__(self):
        return f"Product Type: {self.product_type.value}, Material: {self.material}, Dimensions: {self.dimensions}, Quantity: {self.quantity}"

# Define a class for DesignProcess
class DesignProcess:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the design process.

        Args:
        - product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product_index: int):
        """
        Remove a product from the design process.

        Args:
        - product_index (int): The index of the product to remove.

        Raises:
        - IndexError: If the product index is out of range.
        """
        try:
            del self.products[product_index]
        except IndexError:
            print("Product index out of range.")

    def get_products(self) -> List[Product]:
        """
        Get the list of products in the design process.

        Returns:
        - List[Product]: The list of products.
        """
        return self.products

    def simulate_design(self):
        """
        Simulate the design process.

        This method will iterate over each product and print its details.
        """
        for i, product in enumerate(self.products):
            print(f"Product {i+1}: {product}")

def main():
    # Create a DesignProcess object
    design_process = DesignProcess()

    # Create products
    product1 = Product(
        ProductType.CUSTOM_PIPE,
        "Stainless Steel",
        {"length": 10.0, "diameter": 2.0},
        5
    )

    product2 = Product(
        ProductType.CUSTOM_FITTING,
        "Stainless Steel",
        {"width": 5.0, "height": 3.0},
        10
    )

    # Add products to the design process
    design_process.add_product(product1)
    design_process.add_product(product2)

    # Simulate the design process
    design_process.simulate_design()

    # Remove a product
    design_process.remove_product(0)

    # Simulate the design process again
    print("\nAfter removing a product:")
    design_process.simulate_design()

if __name__ == "__main__":
    main()
```
