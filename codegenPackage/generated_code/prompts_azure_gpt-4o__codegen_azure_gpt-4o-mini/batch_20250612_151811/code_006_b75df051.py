"""
Generated Code Metadata:
========================
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Develop a program to track and manage pest control products, including sales data and resistance levels, inspired by Bayer's Environmental Science Professional business.
Generated: DETERMINISTIC_b75df05132d4c3f7
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class PestControlProduct:
    """
    Class to represent a pest control product.
    """
    def __init__(self, name: str, resistance_level: str, sales_data: List[Dict[str, Any]]):
        """
        Initialize a PestControlProduct instance.

        :param name: Name of the pest control product.
        :param resistance_level: Resistance level of the product.
        :param sales_data: List of sales data dictionaries.
        """
        self.name = name
        self.resistance_level = resistance_level
        self.sales_data = sales_data

    def add_sales_data(self, data: Dict[str, Any]):
        """
        Add sales data to the product.

        :param data: A dictionary containing sales data.
        """
        self.sales_data.append(data)

    def get_total_sales(self) -> float:
        """
        Calculate the total sales for the product.

        :return: Total sales amount.
        """
        return sum(sale.get('amount', 0) for sale in self.sales_data)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the product information to a dictionary.

        :return: Dictionary representation of the product.
        """
        return {
            'name': self.name,
            'resistance_level': self.resistance_level,
            'sales_data': self.sales_data
        }


class PestControlManager:
    """
    Class to manage pest control products.
    """
    def __init__(self):
        """
        Initialize the PestControlManager with an empty product list.
        """
        self.products: List[PestControlProduct] = []

    def add_product(self, product: PestControlProduct):
        """
        Add a new pest control product to the manager.

        :param product: An instance of PestControlProduct.
        """
        self.products.append(product)

    def get_product(self, name: str) -> PestControlProduct:
        """
        Retrieve a product by its name.

        :param name: Name of the product to retrieve.
        :return: PestControlProduct instance.
        :raises ValueError: If the product is not found.
        """
        for product in self.products:
            if product.name == name:
                return product
        raise ValueError(f"Product '{name}' not found.")

    def save_to_file(self, filename: str):
        """
        Save the product data to a JSON file.

        :param filename: The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load product data from a JSON file.

        :param filename: The name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = PestControlProduct(
                        name=product_data['name'],
                        resistance_level=product_data['resistance_level'],
                        sales_data=product_data['sales_data']
                    )
                    self.add_product(product)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = PestControlManager()

    # Create a new product
    product1 = PestControlProduct(
        name="Insecticide A",
        resistance_level="Low",
        sales_data=[{"date": "2023-01-01", "amount": 150.0}, {"date": "2023-01-15", "amount": 200.0}]
    )

    # Add product to manager
    manager.add_product(product1)

    # Add more sales data
    product1.add_sales_data({"date": "2023-02-01", "amount": 300.0})

    # Save products to file
    manager.save_to_file("pest_control_products.json")

    # Load products from file
    manager.load_from_file("pest_control_products.json")

    # Retrieve total sales for a product
    total_sales = product1.get_total_sales()
    print(f"Total sales for {product1.name}: ${total_sales:.2f}")
```
