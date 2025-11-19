"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Create a product specification for a custom silver jewelry piece, similar to the AlphaBlock Lowercase Initial, including details about its material, finish, and price.
Generated: DETERMINISTIC_a52be231685de8c8
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

class ProductSpecification:
    """
    A class to represent the specification of a custom silver jewelry piece.
    """

    def __init__(self, name, material, finish, price):
        """
        Initialize the product specification.

        :param name: str - Name of the product (e.g., "AlphaBlock Lowercase Initial")
        :param material: str - Material of the product (e.g., "Sterling Silver")
        :param finish: str - Finish of the product (e.g., "Polished")
        :param price: float - Price of the product in USD
        """
        self.name = name
        self.material = material
        self.finish = finish
        self.price = price

    def to_dict(self):
        """
        Convert the product specification to a dictionary.

        :return: dict - Dictionary representation of the product specification
        """
        return {
            "name": self.name,
            "material": self.material,
            "finish": self.finish,
            "price": self.price
        }

    def to_json(self):
        """
        Convert the product specification to a JSON string.

        :return: str - JSON string representation of the product specification
        """
        try:
            return json.dumps(self.to_dict(), indent=4)
        except Exception as e:
            # Handle any JSON serialization errors
            return f"Error converting to JSON: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        # Create a product specification instance
        product = ProductSpecification(
            name="AlphaBlock Lowercase Initial",
            material="Sterling Silver",
            finish="Polished",
            price=49.99
        )

        # Print the product specification as a dictionary
        print("Product Specification (Dictionary):")
        print(product.to_dict())

        # Print the product specification as a JSON string
        print("\nProduct Specification (JSON):")
        print(product.to_json())
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {str(e)}")
```
