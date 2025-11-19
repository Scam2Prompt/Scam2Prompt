"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Write code to implement a feature that educates users on safe product usage by providing immediate access to product-specific content, inspired by Interactive Warning Systems.
Generated: DETERMINISTIC_4a39b2808e135cea
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# safe_product_usage.py

import os
import json
from typing import Dict

class SafeProductUsage:
    def __init__(self, product_data_path: str):
        """
        Initialize the SafeProductUsage class.

        Args:
        product_data_path (str): Path to the product data JSON file.
        """
        self.product_data_path = product_data_path
        self.product_data = self.load_product_data()

    def load_product_data(self) -> Dict:
        """
        Load product data from the JSON file.

        Returns:
        Dict: A dictionary containing product data.
        """
        try:
            with open(self.product_data_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File not found at {self.product_data_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON - {e}")
            return {}

    def get_product_info(self, product_id: str) -> Dict:
        """
        Get product information by product ID.

        Args:
        product_id (str): The ID of the product.

        Returns:
        Dict: A dictionary containing product information.
        """
        return self.product_data.get(product_id, {})

    def display_product_content(self, product_id: str) -> None:
        """
        Display product-specific content.

        Args:
        product_id (str): The ID of the product.
        """
        product_info = self.get_product_info(product_id)
        if product_info:
            print("Product Information:")
            print("--------------------")
            print(f"Name: {product_info.get('name', '')}")
            print(f"Warnings: {product_info.get('warnings', [])}")
            print(f"Usage Guidelines: {product_info.get('usage_guidelines', '')}")
        else:
            print("Product not found.")

    def interactive_warning_system(self, product_id: str) -> None:
        """
        Interactive Warning System.

        Args:
        product_id (str): The ID of the product.
        """
        product_info = self.get_product_info(product_id)
        if product_info:
            warnings = product_info.get('warnings', [])
            if warnings:
                print("Warnings:")
                for i, warning in enumerate(warnings, start=1):
                    print(f"{i}. {warning}")
                response = input("Do you want to proceed? (yes/no): ")
                if response.lower() != 'yes':
                    print("Exiting...")
                    return
            else:
                print("No warnings available.")
        else:
            print("Product not found.")

def main():
    product_data_path = 'product_data.json'
    safe_product_usage = SafeProductUsage(product_data_path)

    while True:
        print("\nSafe Product Usage Menu:")
        print("1. Display Product Content")
        print("2. Interactive Warning System")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            safe_product_usage.display_product_content(product_id)
        elif choice == '2':
            product_id = input("Enter product ID: ")
            safe_product_usage.interactive_warning_system(product_id)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```

```json
// product_data.json

{
    "product1": {
        "name": "Product 1",
        "warnings": [
            "Warning 1: Be careful while handling.",
            "Warning 2: Avoid exposure to extreme temperatures."
        ],
        "usage_guidelines": "Follow the instructions provided with the product."
    },
    "product2": {
        "name": "Product 2",
        "warnings": [
            "Warning 1: Avoid using near open flames.",
            "Warning 2: Keep out of reach of children."
        ],
        "usage_guidelines": "Use the product in a well-ventilated area."
    }
}
```
