"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Develop a program to track and visualize the supply chain for critical forgings and fabrication items for Indian Railways, leveraging the manufacturing expertise of Lalbaba Industrial Corporation Pvt. Ltd.
Generated: DETERMINISTIC_46b0a3f4e14fb42d
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_tracker.py

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class SupplyChainTracker:
    def __init__(self):
        """
        Initialize the supply chain tracker with an empty inventory.
        """
        self.inventory = []
        self.manufacturing_partners = ["Lalbaba Industrial Corporation Pvt. Ltd."]
        self.railway_departments = ["Indian Railways"]

    def add_item(self, item_name, item_type, quantity, partner):
        """
        Add a new item to the inventory.

        Args:
            item_name (str): Name of the item.
            item_type (str): Type of the item (forging or fabrication).
            quantity (int): Quantity of the item.
            partner (str): Manufacturing partner.

        Raises:
            ValueError: If the partner is not a recognized manufacturing partner.
        """
        if partner not in self.manufacturing_partners:
            raise ValueError("Invalid manufacturing partner")

        item = {
            "item_name": item_name,
            "item_type": item_type,
            "quantity": quantity,
            "partner": partner,
            "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.inventory.append(item)

    def update_item(self, item_name, quantity):
        """
        Update the quantity of an existing item in the inventory.

        Args:
            item_name (str): Name of the item.
            quantity (int): New quantity of the item.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for item in self.inventory:
            if item["item_name"] == item_name:
                item["quantity"] = quantity
                item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return
        raise ValueError("Item not found in inventory")

    def remove_item(self, item_name):
        """
        Remove an item from the inventory.

        Args:
            item_name (str): Name of the item.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for item in self.inventory:
            if item["item_name"] == item_name:
                self.inventory.remove(item)
                return
        raise ValueError("Item not found in inventory")

    def get_inventory(self):
        """
        Get the current inventory.

        Returns:
            list: List of items in the inventory.
        """
        return self.inventory

    def visualize_inventory(self):
        """
        Visualize the current inventory using a bar chart.
        """
        item_names = [item["item_name"] for item in self.inventory]
        quantities = [item["quantity"] for item in self.inventory]

        plt.bar(item_names, quantities)
        plt.xlabel("Item Name")
        plt.ylabel("Quantity")
        plt.title("Current Inventory")
        plt.show()


def main():
    tracker = SupplyChainTracker()

    while True:
        print("1. Add item to inventory")
        print("2. Update item quantity")
        print("3. Remove item from inventory")
        print("4. Get current inventory")
        print("5. Visualize current inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            item_type = input("Enter item type (forging/fabrication): ")
            quantity = int(input("Enter quantity: "))
            partner = input("Enter manufacturing partner: ")
            tracker.add_item(item_name, item_type, quantity, partner)
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            tracker.update_item(item_name, quantity)
        elif choice == "3":
            item_name = input("Enter item name: ")
            tracker.remove_item(item_name)
        elif choice == "4":
            inventory = tracker.get_inventory()
            df = pd.DataFrame(inventory)
            print(df)
        elif choice == "5":
            tracker.visualize_inventory()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
