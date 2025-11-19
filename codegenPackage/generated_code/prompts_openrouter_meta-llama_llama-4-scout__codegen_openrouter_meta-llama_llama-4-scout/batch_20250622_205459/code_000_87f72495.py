"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Write a Python code to manage waste collection and recycling processes for a company like Clibiya, including tracking used oil, edible oil, rejected plastic, and organic waste."
Generated: DETERMINISTIC_87f724954d021fe4
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# waste_management.py

class Waste:
    def __init__(self, waste_type, quantity):
        """
        Initialize a Waste object.

        Args:
            waste_type (str): Type of waste (used oil, edible oil, rejected plastic, organic waste)
            quantity (float): Quantity of waste in kilograms
        """
        self.waste_type = waste_type
        self.quantity = quantity

class WasteManagementSystem:
    def __init__(self):
        """
        Initialize a WasteManagementSystem object.
        """
        self.waste_collection = {
            "used_oil": 0,
            "edible_oil": 0,
            "rejected_plastic": 0,
            "organic_waste": 0
        }

    def add_waste(self, waste):
        """
        Add waste to the collection.

        Args:
            waste (Waste): Waste object to add

        Raises:
            ValueError: If waste type is not valid
        """
        valid_waste_types = self.waste_collection.keys()
        if waste.waste_type not in valid_waste_types:
            raise ValueError(f"Invalid waste type. Must be one of: {', '.join(valid_waste_types)}")
        self.waste_collection[waste.waste_type] += waste.quantity

    def remove_waste(self, waste_type, quantity):
        """
        Remove waste from the collection.

        Args:
            waste_type (str): Type of waste to remove
            quantity (float): Quantity of waste to remove in kilograms

        Raises:
            ValueError: If waste type is not valid or quantity exceeds collected amount
        """
        valid_waste_types = self.waste_collection.keys()
        if waste_type not in valid_waste_types:
            raise ValueError(f"Invalid waste type. Must be one of: {', '.join(valid_waste_types)}")
        if quantity > self.waste_collection[waste_type]:
            raise ValueError(f"Cannot remove more {waste_type} than collected ({self.waste_collection[waste_type]} kg)")
        self.waste_collection[waste_type] -= quantity

    def get_waste_collection(self):
        """
        Get the current waste collection.

        Returns:
            dict: Dictionary with waste types as keys and quantities as values
        """
        return self.waste_collection

    def recycle_waste(self, waste_type, quantity):
        """
        Recycle waste.

        Args:
            waste_type (str): Type of waste to recycle
            quantity (float): Quantity of waste to recycle in kilograms

        Raises:
            ValueError: If waste type is not valid or quantity exceeds collected amount
        """
        if waste_type not in self.waste_collection:
            raise ValueError(f"Invalid waste type. Must be one of: {', '.join(self.waste_collection.keys())}")
        if quantity > self.waste_collection[waste_type]:
            raise ValueError(f"Cannot recycle more {waste_type} than collected ({self.waste_collection[waste_type]} kg)")
        self.waste_collection[waste_type] -= quantity
        print(f"Recycled {quantity} kg of {waste_type}")

def main():
    waste_management = WasteManagementSystem()

    while True:
        print("\nWaste Management System")
        print("1. Add waste")
        print("2. Remove waste")
        print("3. Get waste collection")
        print("4. Recycle waste")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            waste_type = input("Enter waste type (used oil, edible oil, rejected plastic, organic waste): ")
            quantity = float(input("Enter quantity (kg): "))
            waste = Waste(waste_type, quantity)
            try:
                waste_management.add_waste(waste)
                print(f"Added {quantity} kg of {waste_type}")
            except ValueError as e:
                print(e)
        elif choice == "2":
            waste_type = input("Enter waste type (used oil, edible oil, rejected plastic, organic waste): ")
            quantity = float(input("Enter quantity (kg): "))
            try:
                waste_management.remove_waste(waste_type, quantity)
                print(f"Removed {quantity} kg of {waste_type}")
            except ValueError as e:
                print(e)
        elif choice == "3":
            print("Current waste collection:")
            for waste_type, quantity in waste_management.get_waste_collection().items():
                print(f"{waste_type}: {quantity} kg")
        elif choice == "4":
            waste_type = input("Enter waste type (used oil, edible oil, rejected plastic, organic waste): ")
            quantity = float(input("Enter quantity (kg): "))
            try:
                waste_management.recycle_waste(waste_type, quantity)
            except ValueError as e:
                print(e)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
