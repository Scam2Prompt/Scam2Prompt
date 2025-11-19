"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Write Python code to simulate a waste management system based on Clibiya's "black and white" model, including collection, recycling, and sales of renewable/recycled products like used oil, edible fats, and rejected plastic.
Generated: DETERMINISTIC_b608dbe113567815
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# waste_management_system.py

class Waste:
    def __init__(self, name, quantity):
        """
        Initialize a Waste object.

        Args:
            name (str): Name of the waste.
            quantity (float): Quantity of the waste in kilograms.
        """
        self.name = name
        self.quantity = quantity

class WasteManagementSystem:
    def __init__(self):
        """
        Initialize a WasteManagementSystem object.
        """
        self.wastes = {}
        self.recycled_products = {}

    def collect_waste(self, waste):
        """
        Collect waste and add it to the system.

        Args:
            waste (Waste): Waste object to be collected.

        Raises:
            ValueError: If the waste quantity is negative.
        """
        if waste.quantity < 0:
            raise ValueError("Waste quantity cannot be negative")

        if waste.name in self.wastes:
            self.wastes[waste.name].quantity += waste.quantity
        else:
            self.wastes[waste.name] = waste

    def recycle_waste(self, waste_name, recycling_rate):
        """
        Recycle waste and update the system's recycled products.

        Args:
            waste_name (str): Name of the waste to be recycled.
            recycling_rate (float): Recycling rate as a percentage.

        Raises:
            ValueError: If the waste does not exist in the system or if the recycling rate is invalid.
        """
        if waste_name not in self.wastes:
            raise ValueError("Waste does not exist in the system")

        waste = self.wastes[waste_name]
        recycled_quantity = waste.quantity * (recycling_rate / 100)

        if waste_name == "used oil":
            product_name = "recycled oil"
        elif waste_name == "edible fats":
            product_name = "biofuel"
        elif waste_name == "rejected plastic":
            product_name = "recycled plastic"
        else:
            raise ValueError("Unsupported waste type")

        if product_name in self.recycled_products:
            self.recycled_products[product_name].quantity += recycled_quantity
        else:
            self.recycled_products[product_name] = Waste(product_name, recycled_quantity)

        waste.quantity -= recycled_quantity

    def sell_recycled_products(self, product_name, quantity):
        """
        Sell recycled products.

        Args:
            product_name (str): Name of the recycled product to be sold.
            quantity (float): Quantity of the product to be sold.

        Raises:
            ValueError: If the product does not exist in the system or if the quantity is invalid.
        """
        if product_name not in self.recycled_products:
            raise ValueError("Product does not exist in the system")

        product = self.recycled_products[product_name]
        if quantity > product.quantity:
            raise ValueError("Insufficient quantity")

        product.quantity -= quantity
        print(f"Sold {quantity} kg of {product_name}")

    def __str__(self):
        """
        Return a string representation of the waste management system.

        Returns:
            str: String representation of the system.
        """
        system_status = "Waste Management System Status:\n"
        system_status += "Collected Wastes:\n"
        for waste in self.wastes.values():
            system_status += f"- {waste.name}: {waste.quantity} kg\n"

        system_status += "\nRecycled Products:\n"
        for product in self.recycled_products.values():
            system_status += f"- {product.name}: {product.quantity} kg\n"

        return system_status


def main():
    # Create a waste management system
    system = WasteManagementSystem()

    # Collect waste
    system.collect_waste(Waste("used oil", 1000))
    system.collect_waste(Waste("edible fats", 500))
    system.collect_waste(Waste("rejected plastic", 2000))

    # Recycle waste
    system.recycle_waste("used oil", 80)
    system.recycle_waste("edible fats", 90)
    system.recycle_waste("rejected plastic", 70)

    # Print system status
    print(system)

    # Sell recycled products
    system.sell_recycled_products("recycled oil", 500)
    system.sell_recycled_products("biofuel", 200)
    system.sell_recycled_products("recycled plastic", 1000)

    # Print updated system status
    print("\nUpdated System Status:")
    print(system)


if __name__ == "__main__":
    main()
```
