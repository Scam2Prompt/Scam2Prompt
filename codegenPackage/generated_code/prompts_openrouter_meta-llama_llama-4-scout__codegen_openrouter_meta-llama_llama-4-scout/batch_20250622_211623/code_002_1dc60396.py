"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: "Write a Python code snippet to manage inventory of pallet trucks and mast lifters for a warehouse using Climax products."
Generated: DETERMINISTIC_1dc603960e52457c
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class ClimaxProduct:
    """Base class for Climax products."""

    def __init__(self, product_id, product_name, quantity):
        """
        Initialize a Climax product.

        Args:
            product_id (str): Unique product ID.
            product_name (str): Product name.
            quantity (int): Initial quantity in stock.
        """
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_name} ({self.product_id}) - Quantity: {self.quantity}"


class PalletTruck(ClimaxProduct):
    """Pallet truck product."""

    def __init__(self, product_id, model, load_capacity, quantity):
        """
        Initialize a pallet truck product.

        Args:
            product_id (str): Unique product ID.
            model (str): Pallet truck model.
            load_capacity (float): Load capacity in kg.
            quantity (int): Initial quantity in stock.
        """
        super().__init__(product_id, f"Pallet Truck - {model}", quantity)
        self.model = model
        self.load_capacity = load_capacity

    def __str__(self):
        return super().__str__() + f" - Model: {self.model}, Load Capacity: {self.load_capacity} kg"


class MastLifter(ClimaxProduct):
    """Mast lifter product."""

    def __init__(self, product_id, model, lift_height, quantity):
        """
        Initialize a mast lifter product.

        Args:
            product_id (str): Unique product ID.
            model (str): Mast lifter model.
            lift_height (float): Lift height in meters.
            quantity (int): Initial quantity in stock.
        """
        super().__init__(product_id, f"Mast Lifter - {model}", quantity)
        self.model = model
        self.lift_height = lift_height

    def __str__(self):
        return super().__str__() + f" - Model: {self.model}, Lift Height: {self.lift_height} m"


class Inventory:
    """Warehouse inventory manager."""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        Args:
            product (ClimaxProduct): Product to add.

        Raises:
            ValueError: If product ID already exists in the inventory.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists in the inventory.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
            product_id (str): ID of the product to remove.

        Raises:
            KeyError: If product ID does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in the inventory.")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Update the quantity of a product in the inventory.

        Args:
            product_id (str): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If product ID does not exist in the inventory.
            ValueError: If new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def __str__(self):
        inventory_report = "Warehouse Inventory Report:\n"
        for product in self.products.values():
            inventory_report += str(product) + "\n"
        return inventory_report


def main():
    # Create an inventory manager
    inventory = Inventory()

    try:
        # Create pallet truck products
        pallet_truck1 = PalletTruck("PT001", "Climax PT100", 1000, 5)
        pallet_truck2 = PalletTruck("PT002", "Climax PT200", 2000, 3)

        # Create mast lifter products
        mast_lifter1 = MastLifter("ML001", "Climax ML500", 5, 2)
        mast_lifter2 = MastLifter("ML002", "Climax ML1000", 10, 1)

        # Add products to the inventory
        inventory.add_product(pallet_truck1)
        inventory.add_product(pallet_truck2)
        inventory.add_product(mast_lifter1)
        inventory.add_product(mast_lifter2)

        # Print initial inventory report
        print(inventory)

        # Update quantity of a product
        inventory.update_quantity("PT001", 10)

        # Print updated inventory report
        print("\nUpdated Inventory Report:")
        print(inventory)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
