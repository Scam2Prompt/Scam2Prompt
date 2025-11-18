"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Write code to implement a feature that educates users on safe product usage by providing immediate access to product-specific content, inspired by Interactive Warning Systems.
Generated: DETERMINISTIC_4a39b2808e135cea
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code in Python:

```python
import json


class InteractiveWarningSystem:
    """
    Class to manage and provide safe usage instructions for products
    using an interactive warning system.
    """

    def __init__(self, product_data_file):
        """
        Initialize the system with product-specific content.

        :param product_data_file: Path to JSON file containing product data.
        """
        self.product_data = {}
        try:
            with open(product_data_file, 'r') as file:
                self.product_data = json.load(file)
        except FileNotFoundError:
            print("Error: Product data file not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode product data file.")

    def get_safe_usage_instructions(self, product_name):
        """
        Retrieve safe usage instructions for a specific product.

        :param product_name: Name of the product.
        :return: Instructions string or an error message if product is not found.
        """
        product_info = self.product_data.get(product_name)
        if product_info:
            return f"Product: {product_name}\nSafe Usage Instructions:\n{product_info.get('instructions', 'No instructions available.')}"
        else:
            return f"Error: Product '{product_name}' not found in the system."

    def add_product_info(self, product_name, instructions):
        """
        Add a new product's safe usage information to the system.

        :param product_name: Name of the product.
        :param instructions: Safe usage instructions.
        """
        if product_name in self.product_data:
            print(f"Warning: Product '{product_name}' already exists. Overwriting information.")
        self.product_data[product_name] = {"instructions": instructions}
        print(f"Product '{product_name}' added successfully.")

    def save_product_data(self, output_file):
        """
        Save the current product data back to a file.

        :param output_file: Path to save the JSON file.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(self.product_data, file, indent=4)
            print("Product data saved successfully.")
        except IOError:
            print("Error: Failed to save product data to file.")

    @staticmethod
    def display_products(product_data):
        """
        Display a list of all products in the system.

        :param product_data: Dictionary containing product data.
        """
        if product_data:
            print("Available Products:")
            for product in product_data:
                print(f"- {product}")
        else:
            print("No products available in the system.")


# Example usage:
if __name__ == "__main__":
    # Path to the product data file
    product_data_file = "products.json"

    # Initialize the system
    system = InteractiveWarningSystem(product_data_file)

    # Add a new product
    system.add_product_info("WidgetPro", "Always wear gloves when handling. Avoid direct sunlight exposure.")

    # Retrieve safe usage instructions
    print(system.get_safe_usage_instructions("WidgetPro"))

    # List all products
    system.display_products(system.product_data)

    # Save updated product data
    system.save_product_data("products_updated.json")
```

This Python code implements the requested feature, adhering to clean and production-ready standards. Make sure to create or use a valid JSON file (`products.json`) to test the interactive functionality.
