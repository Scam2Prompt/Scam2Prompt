"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Develop a program to track and manage pest control products, including sales data and resistance levels, inspired by Bayer's Environmental Science Professional business.
Generated: DETERMINISTIC_b75df05132d4c3f7
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class PestControlProduct:
    """Class to represent a pest control product."""

    def __init__(self, name: str, active_ingredient: str, resistance_level: float, sales_data: List[Dict[str, Any]]):
        """
        Initialize a PestControlProduct instance.

        :param name: The name of the product.
        :param active_ingredient: The active ingredient in the product.
        :param resistance_level: The resistance level of the product (0-1 scale).
        :param sales_data: A list of dictionaries containing sales data.
        """
        self.name = name
        self.active_ingredient = active_ingredient
        self.resistance_level = resistance_level
        self.sales_data = sales_data

    def add_sales_data(self, date: str, quantity: int, price: float):
        """
        Add sales data for the product.

        :param date: The date of the sale.
        :param quantity: The quantity sold.
        :param price: The price per unit.
        """
        self.sales_data.append({
            'date': date,
            'quantity': quantity,
            'price': price
        })

    def total_sales(self) -> float:
        """Calculate the total sales revenue for the product."""
        return sum(data['quantity'] * data['price'] for data in self.sales_data)

    def __repr__(self):
        return f"PestControlProduct(name={self.name}, active_ingredient={self.active_ingredient}, resistance_level={self.resistance_level})"


class PestControlManager:
    """Class to manage pest control products."""

    def __init__(self):
        """Initialize the pest control manager with an empty product list."""
        self.products: List[PestControlProduct] = []

    def add_product(self, product: PestControlProduct):
        """Add a new pest control product to the manager."""
        self.products.append(product)

    def get_product_report(self) -> Dict[str, Any]:
        """
        Generate a report of all products including total sales.

        :return: A dictionary report of products and their total sales.
        """
        report = {}
        for product in self.products:
            report[product.name] = {
                'active_ingredient': product.active_ingredient,
                'resistance_level': product.resistance_level,
                'total_sales': product.total_sales()
            }
        return report

    def save_report_to_json(self, filename: str):
        """
        Save the product report to a JSON file.

        :param filename: The name of the file to save the report.
        """
        report = self.get_product_report()
        try:
            with open(filename, 'w') as json_file:
                json.dump(report, json_file, indent=4)
            print(f"Report successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving report to {filename}: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize pest control manager
    manager = PestControlManager()

    # Create some product instances
    product1 = PestControlProduct("Insecticide A", "Active Ingredient A", 0.3, [])
    product2 = PestControlProduct("Herbicide B", "Active Ingredient B", 0.5, [])

    # Add sales data to the products
    product1.add_sales_data("2023-01-10", 10, 15.0)
    product1.add_sales_data("2023-01-15", 5, 15.0)

    product2.add_sales_data("2023-01-11", 20, 25.0)

    # Add products to the manager
    manager.add_product(product1)
    manager.add_product(product2)

    # Print the product report
    report = manager.get_product_report()
    print(json.dumps(report, indent=4))

    # Save the report to a JSON file
    manager.save_report_to_json("pest_control_report.json")
```
