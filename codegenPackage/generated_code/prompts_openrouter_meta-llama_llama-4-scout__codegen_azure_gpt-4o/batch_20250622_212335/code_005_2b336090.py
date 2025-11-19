"""
Generated Code Metadata:
========================
Original URL: https://theaflac.com
Prompt: Design a system to manage Aflac's group insurance products (e.g., QN81000) for large employers in New York, considering the state's specific regulations and policy forms (e.g., NYQN81100M).
Generated: DETERMINISTIC_2b33609076709fe8
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
System to manage Aflac's group insurance products for large employers in New York.
This code is designed to handle insurance products, considering New York's specific regulations and policy forms.
"""

import json
from typing import List, Dict, Optional


class InsuranceProduct:
    """
    Represents an insurance product with specific policy forms and regulations.
    """

    def __init__(self, product_code: str, policy_form: str, description: str):
        """
        Initialize an insurance product.

        :param product_code: Unique code for the insurance product (e.g., QN81000).
        :param policy_form: Policy form specific to New York regulations (e.g., NYQN81100M).
        :param description: Description of the insurance product.
        """
        self.product_code = product_code
        self.policy_form = policy_form
        self.description = description

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the insurance product to a dictionary format.

        :return: Dictionary representation of the insurance product.
        """
        return {
            "product_code": self.product_code,
            "policy_form": self.policy_form,
            "description": self.description,
        }


class InsuranceManager:
    """
    Manages insurance products for large employers in New York.
    """

    def __init__(self):
        """
        Initialize the insurance manager with an empty list of products.
        """
        self.products: List[InsuranceProduct] = []

    def add_product(self, product: InsuranceProduct) -> None:
        """
        Add a new insurance product to the system.

        :param product: InsuranceProduct instance to be added.
        """
        # Check for duplicate product codes
        if any(p.product_code == product.product_code for p in self.products):
            raise ValueError(f"Product with code {product.product_code} already exists.")
        self.products.append(product)

    def remove_product(self, product_code: str) -> None:
        """
        Remove an insurance product by its product code.

        :param product_code: Unique code of the product to be removed.
        """
        self.products = [p for p in self.products if p.product_code != product_code]

    def get_product(self, product_code: str) -> Optional[InsuranceProduct]:
        """
        Retrieve an insurance product by its product code.

        :param product_code: Unique code of the product to retrieve.
        :return: InsuranceProduct instance if found, otherwise None.
        """
        for product in self.products:
            if product.product_code == product_code:
                return product
        return None

    def list_products(self) -> List[Dict[str, str]]:
        """
        List all insurance products in the system.

        :return: List of dictionaries representing all insurance products.
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, file_path: str) -> None:
        """
        Save the list of insurance products to a JSON file.

        :param file_path: Path to the file where products will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save products to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Load insurance products from a JSON file.

        :param file_path: Path to the file containing products data.
        """
        try:
            with open(file_path, "r") as file:
                products_data = json.load(file)
                self.products = [
                    InsuranceProduct(
                        product_code=data["product_code"],
                        policy_form=data["policy_form"],
                        description=data["description"],
                    )
                    for data in products_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load products from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InsuranceManager()

    # Add products
    try:
        manager.add_product(InsuranceProduct("QN81000", "NYQN81100M", "Group insurance for large employers"))
        manager.add_product(InsuranceProduct("QN82000", "NYQN82100M", "Supplemental insurance for employees"))
    except ValueError as e:
        print(f"Error: {e}")

    # List products
    print("Current products:")
    print(manager.list_products())

    # Save products to file
    try:
        manager.save_to_file("insurance_products.json")
        print("Products saved to file.")
    except RuntimeError as e:
        print(f"Error: {e}")

    # Load products from file
    try:
        manager.load_from_file("insurance_products.json")
        print("Products loaded from file:")
        print(manager.list_products())
    except RuntimeError as e:
        print(f"Error: {e}")
```
