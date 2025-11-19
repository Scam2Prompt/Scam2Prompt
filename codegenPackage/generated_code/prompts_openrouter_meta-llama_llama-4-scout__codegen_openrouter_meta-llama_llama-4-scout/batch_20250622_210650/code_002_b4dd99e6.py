"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Generate a list of door hardware products, including finishes in satin nickel and bronze, that can be used for a construction project in Alabama, Mississippi, or Florida.
Generated: DETERMINISTIC_b4dd99e643d4aab4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# door_hardware.py

class DoorHardware:
    def __init__(self, name, finish, state):
        """
        Initialize a DoorHardware object.

        Args:
            name (str): Name of the door hardware product.
            finish (str): Finish of the door hardware product.
            state (list): List of states where the product can be used.
        """
        self.name = name
        self.finish = finish
        self.state = state

class DoorHardwareCatalog:
    def __init__(self):
        """
        Initialize a DoorHardwareCatalog object.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a door hardware product to the catalog.

        Args:
            product (DoorHardware): DoorHardware object to add.
        """
        self.products.append(product)

    def get_products_by_finish_and_state(self, finish, states):
        """
        Get a list of door hardware products with a specific finish that can be used in a list of states.

        Args:
            finish (str): Finish of the door hardware products to retrieve.
            states (list): List of states where the products can be used.

        Returns:
            list: List of DoorHardware objects matching the criteria.
        """
        return [product for product in self.products if product.finish == finish and any(state in product.state for state in states)]

def main():
    # Create a catalog of door hardware products
    catalog = DoorHardwareCatalog()

    # Add products to the catalog
    catalog.add_product(DoorHardware("Door Handle", "Satin Nickel", ["Alabama", "Mississippi", "Florida"]))
    catalog.add_product(DoorHardware("Door Lock", "Satin Nickel", ["Alabama", "Mississippi", "Florida"]))
    catalog.add_product(DoorHardware("Door Hinge", "Bronze", ["Alabama", "Mississippi", "Florida"]))
    catalog.add_product(DoorHardware("Door Handle", "Bronze", ["Alabama", "Mississippi", "Georgia"]))
    catalog.add_product(DoorHardware("Door Lock", "Bronze", ["Alabama", "Mississippi", "Florida"]))

    # Define the states and finishes of interest
    states = ["Alabama", "Mississippi", "Florida"]
    finishes = ["Satin Nickel", "Bronze"]

    # Get the products with the specified finishes that can be used in the specified states
    for finish in finishes:
        products = catalog.get_products_by_finish_and_state(finish, states)
        print(f"Products with {finish} finish that can be used in {', '.join(states)}:")
        for product in products:
            print(f"- {product.name}")

if __name__ == "__main__":
    main()
```
