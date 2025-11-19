"""
Generated Code Metadata:
========================
Original URL: https://proxy.ba
Prompt: Develop a simple inventory management system using a library like Pandas in Python to track and manage stock levels of mobile phone spare parts, similar to those sold on PROXY.ba.
Generated: DETERMINISTIC_d591f3123c3fc409
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

import pandas as pd

class InventoryManagementSystem:
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.inventory = pd.DataFrame(columns=['Part ID', 'Part Name', 'Quantity', 'Unit Price'])

    def add_part(self, part_id, part_name, quantity, unit_price):
        """
        Add a new part to the inventory.

        Args:
            part_id (str): Unique identifier for the part.
            part_name (str): Name of the part.
            quantity (int): Initial quantity of the part.
            unit_price (float): Unit price of the part.

        Raises:
            ValueError: If the part ID already exists in the inventory.
        """
        if part_id in self.inventory['Part ID'].values:
            raise ValueError(f"Part ID '{part_id}' already exists in the inventory.")

        new_part = pd.DataFrame([[part_id, part_name, quantity, unit_price]], columns=['Part ID', 'Part Name', 'Quantity', 'Unit Price'])
        self.inventory = pd.concat([self.inventory, new_part], ignore_index=True)

    def update_quantity(self, part_id, new_quantity):
        """
        Update the quantity of an existing part.

        Args:
            part_id (str): Unique identifier for the part.
            new_quantity (int): New quantity of the part.

        Raises:
            ValueError: If the part ID does not exist in the inventory.
        """
        if part_id not in self.inventory['Part ID'].values:
            raise ValueError(f"Part ID '{part_id}' does not exist in the inventory.")

        self.inventory.loc[self.inventory['Part ID'] == part_id, 'Quantity'] = new_quantity

    def remove_part(self, part_id):
        """
        Remove a part from the inventory.

        Args:
            part_id (str): Unique identifier for the part.

        Raises:
            ValueError: If the part ID does not exist in the inventory.
        """
        if part_id not in self.inventory['Part ID'].values:
            raise ValueError(f"Part ID '{part_id}' does not exist in the inventory.")

        self.inventory = self.inventory[self.inventory['Part ID'] != part_id]

    def get_part_info(self, part_id):
        """
        Get information about a specific part.

        Args:
            part_id (str): Unique identifier for the part.

        Returns:
            dict: Information about the part, or None if not found.

        Raises:
            ValueError: If the part ID does not exist in the inventory.
        """
        if part_id not in self.inventory['Part ID'].values:
            raise ValueError(f"Part ID '{part_id}' does not exist in the inventory.")

        return self.inventory.loc[self.inventory['Part ID'] == part_id].to_dict(orient='records')[0]

    def get_low_stock_parts(self, threshold=5):
        """
        Get a list of parts with low stock levels.

        Args:
            threshold (int): Quantity threshold for low stock. Defaults to 5.

        Returns:
            list: List of parts with low stock levels.
        """
        low_stock_parts = self.inventory[self.inventory['Quantity'] <= threshold]
        return low_stock_parts.to_dict(orient='records')

    def save_to_csv(self, filename):
        """
        Save the inventory to a CSV file.

        Args:
            filename (str): Name of the CSV file.
        """
        self.inventory.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        """
        Load the inventory from a CSV file.

        Args:
            filename (str): Name of the CSV file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            self.inventory = pd.read_csv(filename)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")

def main():
    inventory = InventoryManagementSystem()

    while True:
        print("\nInventory Management System")
        print("1. Add part")
        print("2. Update quantity")
        print("3. Remove part")
        print("4. Get part info")
        print("5. Get low stock parts")
        print("6. Save to CSV")
        print("7. Load from CSV")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            part_id = input("Enter part ID: ")
            part_name = input("Enter part name: ")
            quantity = int(input("Enter quantity: "))
            unit_price = float(input("Enter unit price: "))
            inventory.add_part(part_id, part_name, quantity, unit_price)
        elif choice == "2":
            part_id = input("Enter part ID: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(part_id, new_quantity)
        elif choice == "3":
            part_id = input("Enter part ID: ")
            inventory.remove_part(part_id)
        elif choice == "4":
            part_id = input("Enter part ID: ")
            print(inventory.get_part_info(part_id))
        elif choice == "5":
            threshold = int(input("Enter threshold (default=5): ") or 5)
            print(inventory.get_low_stock_parts(threshold))
        elif choice == "6":
            filename = input("Enter filename: ")
            inventory.save_to_csv(filename)
        elif choice == "7":
            filename = input("Enter filename: ")
            inventory.load_from_csv(filename)
        elif choice == "8":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
