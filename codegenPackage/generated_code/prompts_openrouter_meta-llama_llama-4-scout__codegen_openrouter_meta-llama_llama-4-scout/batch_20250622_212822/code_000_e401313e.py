"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: "Generate a Python script to manage tire inventory for different vehicle types, including trucks, with specifications like 175/45R13."
Generated: DETERMINISTIC_e401313e0026fde1
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tire_inventory.py

class Tire:
    def __init__(self, size, vehicle_type, quantity):
        """
        Initialize a Tire object.

        Args:
            size (str): Tire size (e.g., 175/45R13)
            vehicle_type (str): Vehicle type (e.g., truck, car, motorcycle)
            quantity (int): Number of tires in stock
        """
        self.size = size
        self.vehicle_type = vehicle_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.size} - {self.vehicle_type}: {self.quantity} in stock"


class TireInventory:
    def __init__(self):
        """
        Initialize an empty tire inventory.
        """
        self.tires = {}

    def add_tire(self, tire):
        """
        Add a tire to the inventory.

        Args:
            tire (Tire): Tire object to add
        """
        key = (tire.size, tire.vehicle_type)
        if key in self.tires:
            self.tires[key].quantity += tire.quantity
        else:
            self.tires[key] = tire

    def remove_tire(self, size, vehicle_type, quantity):
        """
        Remove a specified quantity of tires from the inventory.

        Args:
            size (str): Tire size
            vehicle_type (str): Vehicle type
            quantity (int): Quantity to remove

        Raises:
            ValueError: If quantity to remove exceeds available stock
        """
        key = (size, vehicle_type)
        if key not in self.tires:
            raise ValueError("Tire not found in inventory")
        if self.tires[key].quantity < quantity:
            raise ValueError("Not enough tires in stock")
        self.tires[key].quantity -= quantity
        if self.tires[key].quantity == 0:
            del self.tires[key]

    def get_tire(self, size, vehicle_type):
        """
        Get a tire object from the inventory.

        Args:
            size (str): Tire size
            vehicle_type (str): Vehicle type

        Returns:
            Tire: Tire object if found, None otherwise
        """
        key = (size, vehicle_type)
        return self.tires.get(key)

    def list_tires(self):
        """
        List all tires in the inventory.
        """
        for tire in self.tires.values():
            print(tire)


def main():
    inventory = TireInventory()

    while True:
        print("\nTire Inventory Management")
        print("1. Add tire")
        print("2. Remove tire")
        print("3. List tires")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            size = input("Enter tire size (e.g., 175/45R13): ")
            vehicle_type = input("Enter vehicle type (e.g., truck, car): ")
            quantity = int(input("Enter quantity: "))
            tire = Tire(size, vehicle_type, quantity)
            inventory.add_tire(tire)
            print(f"Added {quantity} {size} tires for {vehicle_type}")
        elif choice == "2":
            size = input("Enter tire size (e.g., 175/45R13): ")
            vehicle_type = input("Enter vehicle type (e.g., truck, car): ")
            quantity = int(input("Enter quantity to remove: "))
            try:
                inventory.remove_tire(size, vehicle_type, quantity)
                print(f"Removed {quantity} {size} tires for {vehicle_type}")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            inventory.list_tires()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
