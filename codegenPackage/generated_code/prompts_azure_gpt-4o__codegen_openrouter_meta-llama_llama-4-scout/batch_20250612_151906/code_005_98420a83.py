"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Write code to calculate lead times and minimize delays in the supply chain for products such as turbines, instrumentation equipment, and plumbing materials, inspired by Cedar International Inc.'s logistics approach.
Generated: DETERMINISTIC_98420a83f4979637
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class SupplyChainOptimizer:
    def __init__(self):
        """
        Initialize the SupplyChainOptimizer class.
        
        Attributes:
        - products (Dict): A dictionary to store product information.
        """
        self.products = {}

    def add_product(self, product_name: str, order_date: datetime, delivery_date: datetime, 
                    production_time: timedelta, transportation_time: timedelta):
        """
        Add a product to the supply chain.

        Args:
        - product_name (str): The name of the product.
        - order_date (datetime): The date the product was ordered.
        - delivery_date (datetime): The expected delivery date of the product.
        - production_time (timedelta): The time required to produce the product.
        - transportation_time (timedelta): The time required to transport the product.
        """
        self.products[product_name] = {
            "order_date": order_date,
            "delivery_date": delivery_date,
            "production_time": production_time,
            "transportation_time": transportation_time
        }

    def calculate_lead_time(self, product_name: str) -> timedelta:
        """
        Calculate the lead time for a product.

        Args:
        - product_name (str): The name of the product.

        Returns:
        - timedelta: The lead time for the product.

        Raises:
        - KeyError: If the product does not exist in the supply chain.
        """
        if product_name not in self.products:
            raise KeyError("Product not found in the supply chain")

        product = self.products[product_name]
        lead_time = product["production_time"] + product["transportation_time"]
        return lead_time

    def minimize_delays(self) -> Dict:
        """
        Identify products with potential delays in the supply chain.

        Returns:
        - Dict: A dictionary containing products with potential delays.
        """
        delayed_products = {}
        for product, info in self.products.items():
            lead_time = self.calculate_lead_time(product)
            if info["delivery_date"] < info["order_date"] + lead_time:
                delayed_products[product] = {
                    "order_date": info["order_date"],
                    "delivery_date": info["delivery_date"],
                    "lead_time": lead_time
                }
        return delayed_products


def main():
    optimizer = SupplyChainOptimizer()

    # Add products to the supply chain
    optimizer.add_product(
        "Turbine",
        datetime(2024, 9, 1),
        datetime(2024, 10, 15),
        timedelta(days=20),
        timedelta(days=15)
    )

    optimizer.add_product(
        "Instrumentation Equipment",
        datetime(2024, 9, 5),
        datetime(2024, 11, 1),
        timedelta(days=30),
        timedelta(days=10)
    )

    optimizer.add_product(
        "Plumbing Materials",
        datetime(2024, 9, 10),
        datetime(2024, 10, 20),
        timedelta(days=10),
        timedelta(days=5)
    )

    # Calculate lead times
    print("Lead Times:")
    for product in optimizer.products:
        lead_time = optimizer.calculate_lead_time(product)
        print(f"{product}: {lead_time}")

    # Identify potential delays
    delayed_products = optimizer.minimize_delays()
    if delayed_products:
        print("\nPotential Delays:")
        for product, info in delayed_products.items():
            print(f"Product: {product}")
            print(f"Order Date: {info['order_date']}")
            print(f"Delivery Date: {info['delivery_date']}")
            print(f"Lead Time: {info['lead_time']}")
            print("------------------------")
    else:
        print("\nNo potential delays found.")

if __name__ == "__main__":
    main()
```
