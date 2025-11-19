"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmask.com
Prompt: Generate a Python script to manage and store fishing bait, including options for natural baits like bloodworm and casters, as mentioned on metmask.com.
Generated: DETERMINISTIC_6348c1f8d64e3c2e
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class BaitManager:
    """A class to manage and store fishing bait."""

    def __init__(self, storage_file='bait_storage.json'):
        """Initialize the BaitManager with a storage file."""
        self.storage_file = storage_file
        self.bait_inventory = self.load_bait_inventory()

    def load_bait_inventory(self):
        """Load bait inventory from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON, starting with empty inventory.")
                    return {}
        return {}

    def save_bait_inventory(self):
        """Save the current bait inventory to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.bait_inventory, file, indent=4)

    def add_bait(self, bait_name, quantity):
        """Add a specified quantity of bait to the inventory."""
        if bait_name in self.bait_inventory:
            self.bait_inventory[bait_name] += quantity
        else:
            self.bait_inventory[bait_name] = quantity
        self.save_bait_inventory()

    def remove_bait(self, bait_name, quantity):
        """Remove a specified quantity of bait from the inventory."""
        if bait_name in self.bait_inventory:
            if self.bait_inventory[bait_name] >= quantity:
                self.bait_inventory[bait_name] -= quantity
                if self.bait_inventory[bait_name] == 0:
                    del self.bait_inventory[bait_name]
                self.save_bait_inventory()
            else:
                print(f"Error: Not enough {bait_name} in inventory to remove.")
        else:
            print(f"Error: {bait_name} not found in inventory.")

    def view_inventory(self):
        """Display the current bait inventory."""
        if self.bait_inventory:
            print("Current Bait Inventory:")
            for bait, quantity in self.bait_inventory.items():
                print(f"{bait}: {quantity}")
        else:
            print("The bait inventory is empty.")

def main():
    """Main function to run the BaitManager."""
    manager = BaitManager()
    
    while True:
        print("\nOptions:")
        print("1. View Inventory")
        print("2. Add Bait")
        print("3. Remove Bait")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            manager.view_inventory()
        elif choice == '2':
            name = input("Enter the bait name: ")
            quantity = int(input("Enter the quantity to add: "))
            manager.add_bait(name, quantity)
        elif choice == '3':
            name = input("Enter the bait name: ")
            quantity = int(input("Enter the quantity to remove: "))
            manager.remove_bait(name, quantity)
        elif choice == '4':
            print("Exiting the Bait Manager.")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
```
