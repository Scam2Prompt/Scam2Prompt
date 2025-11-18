"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Write a program to model and simulate supply chain scenarios for oil and gas industry products, incorporating Cedar International Inc.'s expertise in procurement and logistics.
Generated: DETERMINISTIC_d72f642a75ae39ec
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Supplier:
    """Represents a supplier in the supply chain."""
    
    def __init__(self, name: str, reliability: float):
        self.name = name
        self.reliability = reliability

    def supply(self, quantity: int) -> bool:
        """Simulate the supply of a given quantity based on supplier reliability."""
        success = random.random() <= self.reliability
        logging.info(f'Supplier {self.name} supplying {quantity}: {"Success" if success else "Failed"}')
        return success

class Warehouse:
    """Represents a warehouse that stores products."""
    
    def __init__(self, name: str):
        self.name = name
        self.inventory: Dict[str, int] = {}

    def receive(self, product: str, quantity: int):
        """Receive products into the warehouse inventory."""
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        logging.info(f'Warehouse {self.name} received {quantity} of {product}.')

    def dispatch(self, product: str, quantity: int) -> bool:
        """Dispatch products from the warehouse inventory."""
        if self.inventory.get(product, 0) >= quantity:
            self.inventory[product] -= quantity
            logging.info(f'Warehouse {self.name} dispatched {quantity} of {product}.')
            return True
        logging.warning(f'Warehouse {self.name} insufficient inventory for {product}.')
        return False

class Retailer:
    """Represents a retailer in the supply chain."""
    
    def __init__(self, name: str):
        self.name = name

    def order(self, warehouse: Warehouse, product: str, quantity: int) -> bool:
        """Order a product from a warehouse."""
        logging.info(f'Retailer {self.name} attempting to order {quantity} of {product}.')
        return warehouse.dispatch(product, quantity)

class SupplyChainSimulation:
    """Simulates a supply chain scenario for oil and gas products."""
    
    def __init__(self, suppliers: List[Supplier], warehouse: Warehouse, retailer: Retailer):
        self.suppliers = suppliers
        self.warehouse = warehouse
        self.retailer = retailer

    def run_simulation(self, product: str, quantity: int):
        """Run the supply chain simulation."""
        logging.info(f'Starting simulation for product {product} with quantity {quantity}.')
        
        # Step 1: Supply from suppliers
        total_supplied = 0
        for supplier in self.suppliers:
            if supplier.supply(quantity):
                total_supplied += quantity
                
                # Receive the supplied product into the warehouse
                self.warehouse.receive(product, quantity)

        # Step 2: Retailer orders the product
        if total_supplied > 0:
            ordered = self.retailer.order(self.warehouse, product, quantity)
            if ordered:
                logging.info(f'Retailer {self.retailer.name} successfully ordered {quantity} of {product}.')
            else:
                logging.warning(f'Retailer {self.retailer.name} failed to order {quantity} of {product}.')
        else:
            logging.warning('No product supplied from any supplier.')

if __name__ == "__main__":
    # Create suppliers with varying reliability
    suppliers = [
        Supplier(name='Supplier A', reliability=0.9),
        Supplier(name='Supplier B', reliability=0.8),
        Supplier(name='Supplier C', reliability=0.7)
    ]

    # Create a warehouse
    warehouse = Warehouse(name='Main Warehouse')

    # Create a retailer
    retailer = Retailer(name='Retailer 1')

    # Initialize and run the supply chain simulation
    simulation = SupplyChainSimulation(suppliers=suppliers, warehouse=warehouse, retailer=retailer)
    simulation.run_simulation(product='Crude Oil', quantity=100)
```
