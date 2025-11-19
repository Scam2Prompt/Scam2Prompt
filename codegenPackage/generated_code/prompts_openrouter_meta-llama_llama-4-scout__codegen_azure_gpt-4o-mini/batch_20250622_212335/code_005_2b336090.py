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
import json
from typing import List, Dict, Optional

class InsuranceProduct:
    """
    Class to represent an insurance product.
    """
    def __init__(self, product_code: str, product_name: str, policy_form: str):
        self.product_code = product_code
        self.product_name = product_name
        self.policy_form = policy_form

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the insurance product to a dictionary.
        """
        return {
            "product_code": self.product_code,
            "product_name": self.product_name,
            "policy_form": self.policy_form
        }

class InsuranceProductManager:
    """
    Class to manage a collection of insurance products.
    """
    def __init__(self):
        self.products: List[InsuranceProduct] = []

    def add_product(self, product: InsuranceProduct) -> None:
        """
        Add a new insurance product to the manager.
        """
        if self.get_product(product.product_code):
            raise ValueError(f"Product with code {product.product_code} already exists.")
        self.products.append(product)

    def get_product(self, product_code: str) -> Optional[InsuranceProduct]:
        """
        Retrieve an insurance product by its code.
        """
        for product in self.products:
            if product.product_code == product_code:
                return product
        return None

    def remove_product(self, product_code: str) -> None:
        """
        Remove an insurance product from the manager.
        """
        product = self.get_product(product_code)
        if product is None:
            raise ValueError(f"Product with code {product_code} does not exist.")
        self.products.remove(product)

    def list_products(self) -> List[Dict[str, str]]:
        """
        List all insurance products in a dictionary format.
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str) -> None:
        """
        Save the list of insurance products to a JSON file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save products to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load insurance products from a JSON file.
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = InsuranceProduct(
                        product_code=product_data['product_code'],
                        product_name=product_data['product_name'],
                        policy_form=product_data['policy_form']
                    )
                    self.add_product(product)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load products from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = InsuranceProductManager()
    
    # Adding products
    try:
        manager.add_product(InsuranceProduct("QN81000", "Group Accident Insurance", "NYQN81100M"))
        manager.add_product(InsuranceProduct("QN82000", "Group Critical Illness Insurance", "NYQN82100M"))
    except ValueError as e:
        print(e)

    # Listing products
    print(manager.list_products())

    # Saving to file
    manager.save_to_file("insurance_products.json")

    # Loading from file
    new_manager = InsuranceProductManager()
    new_manager.load_from_file("insurance_products.json")
    print(new_manager.list_products())
```
