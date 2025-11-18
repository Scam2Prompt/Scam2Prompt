"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Write a program to automate dispatch scheduling for a fragrance supplier with a centralized warehouse, similar to Karnataka Aromas' infrastructure.
Generated: DETERMINISTIC_0ad6c3ff72d2ea06
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Union


# Define classes to encapsulate dispatch-related information
class Product:
    """Represents a product in the fragrance supplier's inventory."""
    def __init__(self, product_id: str, name: str, quantity: int):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity


class Dispatch:
    """Represents a dispatch schedule including products and destination."""
    def __init__(self, dispatch_id: str, destination: str, products: List[Product], dispatch_date: datetime.date):
        self.dispatch_id = dispatch_id
        self.destination = destination
        self.products = products
        self.dispatch_date = dispatch_date


class Warehouse:
    """Represents the centralized warehouse."""
    def __init__(self):
        self.inventory = {}  # Inventory: {product_id: quantity}

    def add_product(self, product_id: str, name: str, quantity: int):
        """Add or update products in the warehouse inventory."""
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def check_availability(self, product_id: str, quantity: int) -> bool:
        """Check if the requested quantity is available in the inventory."""
        return product_id in self.inventory and self.inventory[product_id]['quantity'] >= quantity

    def deduct_inventory(self, product_id: str, quantity: int) -> None:
        """Deduct the specified quantity of a product from inventory."""
        if self.check_availability(product_id, quantity):
            self.inventory[product_id]['quantity'] -= quantity
        else:
            raise ValueError(f"Insufficient stock for product ID: {product_id}")


class DispatchScheduler:
    """Handles the scheduling of dispatches."""
    def __init__(self, warehouse: Warehouse):
        self.warehouse = warehouse
        self.dispatches = []  # List of Dispatch instances

    def schedule_dispatch(self, destination: str, products: List[Dict[str, Union[str, int]]], dispatch_date: str) -> str:
        """
        Schedule a dispatch.

        :param destination: Destination of delivery.
        :param products: List of products with product_id and quantity.
        :param dispatch_date: Dispatch date (YYYY-MM-DD).
        :return: Dispatch ID if successful.
        """
        try:
            # Generate unique dispatch ID
            dispatch_id = f"DISPATCH-{len(self.dispatches) + 1}"
            dispatch_date = datetime.datetime.strptime(dispatch_date, "%Y-%m-%d").date()

            # Validate and prepare product list
            product_list = []
            for item in products:
                product_id = item['product_id']
                quantity = item['quantity']

                if self.warehouse.check_availability(product_id, quantity):
                    self.warehouse.deduct_inventory(product_id, quantity)
                    product_name = self.warehouse.inventory[product_id]['name']
                    product_list.append(Product(product_id, product_name, quantity))
                else:
                    raise ValueError(f"Product ID {product_id} is unavailable or insufficient stock.")

            # Create and store the dispatch
            dispatch = Dispatch(dispatch_id, destination, product_list, dispatch_date)
            self.dispatches.append(dispatch)

            return dispatch_id

        except Exception as e:
            # Handle errors gracefully
            print(f"Error scheduling dispatch: {e}")
            return str(e)

    def list_dispatches(self) -> List[Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]]:
        """List all scheduled dispatches."""
        dispatch_list = []
        for dispatch in self.dispatches:
            dispatch_list.append({
                "dispatch_id": dispatch.dispatch_id,
                "destination": dispatch.destination,
                "dispatch_date": str(dispatch.dispatch_date),
                "products": [
                    {"product_id": product.product_id, "name": product.name, "quantity": product.quantity}
                    for product in dispatch.products
                ]
            })
        return dispatch_list


# Main function to simulate the program
def main():
    # Initialize the warehouse and scheduler
    warehouse = Warehouse()
    scheduler = DispatchScheduler(warehouse)

    # Add products to inventory
    warehouse.add_product("P001", "Lavender Oil", 100)
    warehouse.add_product("P002", "Rose Oil", 50)
    warehouse.add_product("P003", "Sandalwood Oil", 75)

    # Schedule a dispatch
    dispatch_id = scheduler.schedule_dispatch(
        destination="Bangalore",
        products=[
            {"product_id": "P001", "quantity": 30},
            {"product_id": "P002", "quantity": 10}
        ],
        dispatch_date="2023-11-01"
    )
    print(f"Scheduled Dispatch ID: {dispatch_id}")

    # List all dispatches
    print("List of Dispatches:")
    print(json.dumps(scheduler.list_dispatches(), indent=4))


if __name__ == "__main__":
    main()
```
