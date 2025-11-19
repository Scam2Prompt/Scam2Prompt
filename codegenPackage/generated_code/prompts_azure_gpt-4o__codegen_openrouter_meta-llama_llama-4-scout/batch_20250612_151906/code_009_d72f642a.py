"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Write a program to model and simulate supply chain scenarios for oil and gas industry products, incorporating Cedar International Inc.'s expertise in procurement and logistics.
Generated: DETERMINISTIC_d72f642a75ae39ec
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_simulator.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ProductType(Enum):
    """ Enum for oil and gas industry products """
    CRUDE_OIL = 1
    REFINED_OIL = 2
    NATURAL_GAS = 3

@dataclass
class Product:
    """ Data class to represent a product """
    product_type: ProductType
    quantity: float  # in barrels or units
    unit_price: float  # in USD

@dataclass
class Supplier:
    """ Data class to represent a supplier """
    name: str
    product: Product
    lead_time: int  # in days
    cost: float  # in USD

@dataclass
class Logistics:
    """ Data class to represent logistics information """
    transportation_mode: str  # e.g., truck, ship, pipeline
    transportation_cost: float  # in USD
    delivery_time: int  # in days

class SupplyChainSimulator:
    """ Class to simulate supply chain scenarios """

    def __init__(self):
        self.suppliers = []
        self.logistics = []
        self.products = []

    def add_supplier(self, supplier: Supplier):
        """ Add a supplier to the supply chain """
        self.suppliers.append(supplier)

    def add_logistics(self, logistics: Logistics):
        """ Add logistics information to the supply chain """
        self.logistics.append(logistics)

    def add_product(self, product: Product):
        """ Add a product to the supply chain """
        self.products.append(product)

    def simulate_supply_chain(self):
        """ Simulate the supply chain and calculate total cost """
        total_cost = 0
        for supplier in self.suppliers:
            total_cost += supplier.cost
            print(f"Supplier: {supplier.name}, Cost: ${supplier.cost:.2f}")
        
        for logistics_info in self.logistics:
            total_cost += logistics_info.transportation_cost
            print(f"Logistics: {logistics_info.transportation_mode}, Cost: ${logistics_info.transportation_cost:.2f}")
        
        for product in self.products:
            print(f"Product: {product.product_type.name}, Quantity: {product.quantity}, Unit Price: ${product.unit_price:.2f}")
        
        return total_cost

    def calculate_delivery_time(self):
        """ Calculate the total delivery time """
        total_delivery_time = 0
        for supplier in self.suppliers:
            total_delivery_time += supplier.lead_time
        for logistics_info in self.logistics:
            total_delivery_time += logistics_info.delivery_time
        return total_delivery_time

def main():
    simulator = SupplyChainSimulator()

    # Create products
    crude_oil = Product(ProductType.CRUDE_OIL, 1000, 50)
    refined_oil = Product(ProductType.REFINED_OIL, 500, 60)

    # Create suppliers
    supplier1 = Supplier("Cedar International Inc.", crude_oil, 10, 10000)
    supplier2 = Supplier("Supplier 2", refined_oil, 15, 15000)

    # Create logistics information
    logistics1 = Logistics("ship", 5000, 20)
    logistics2 = Logistics("pipeline", 2000, 5)

    # Add suppliers, logistics, and products to the simulator
    simulator.add_supplier(supplier1)
    simulator.add_supplier(supplier2)
    simulator.add_logistics(logistics1)
    simulator.add_logistics(logistics2)
    simulator.add_product(crude_oil)
    simulator.add_product(refined_oil)

    try:
        # Simulate the supply chain
        total_cost = simulator.simulate_supply_chain()
        delivery_time = simulator.calculate_delivery_time()
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Total Delivery Time: {delivery_time} days")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
