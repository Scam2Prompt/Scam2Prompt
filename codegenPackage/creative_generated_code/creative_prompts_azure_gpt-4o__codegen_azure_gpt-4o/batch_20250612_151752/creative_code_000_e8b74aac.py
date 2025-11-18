"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Write a Python script to calculate inventory levels for an automotive parts store, including categories like "plaquettes de freins," "embrayage," and "batteries," as described on the Distribution Pièces Service website.
Generated: DETERMINISTIC_e8b74aac1fd06c48
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Inventory:
    """
    A class to manage inventory levels for an automotive parts store.
    """

    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.inventory = {
            "plaquettes de freins": 0,
            "embrayage": 0,
            "batteries": 0
        }

    def display_inventory(self):
        """
        Displays the current inventory levels.
        """
        print("Current Inventory Levels:")
        for part, quantity in self.inventory.items():
            print(f"{part}: {quantity}")
        print()

    def update_inventory(self, part_name, quantity):
        """
        Updates the inventory with the given part and quantity.

        Parameters:
        part_name (str): The name of the part to update.
        quantity (int): The quantity to add (can be negative to subtract).
        """
        if part_name not in self.inventory:
            print(f"Error: '{part_name}' is not a valid part.")
            return

        new_quantity = self.inventory[part_name] + quantity
        if new_quantity < 0:
            print(f"Error: Not enough stock to subtract {quantity} from '{part_name}'.")
            return

        self.inventory[part_name] = new_quantity
        print(f"Inventory updated: {part_name} now has {new_quantity} units.")
        print()

    def run(self):
        """
        Runs the inventory management system.
        """
        print("Welcome to the Automotive Parts Inventory Management System!")
        print("Available parts: 'plaquettes de freins', 'embrayage', 'batteries'")
        print("Type 'exit' to quit the program.")
        print()

        while True:
            try:
                command = input("Enter a command (display/update/exit): ").strip().lower()
                
                if command == 'exit':
                    print("Exiting the program. Goodbye!")
                    break
                elif command == 'display':
                    self.display_inventory()
                elif command == 'update':
                    part_name = input("Enter the part name: ").strip().lower()
                    if part_name not in self.inventory:
                        print("Error: Invalid part name. Please try again.")
                        continue

                    try:
                        quantity = int(input("Enter the quantity to add/subtract: ").strip())
                        self.update_inventory(part_name, quantity)
                    except ValueError:
                        print("Error: Quantity must be an integer. Please try again.")
                else:
                    print("Error: Invalid command. Please try again.")
                    
            except KeyboardInterrupt:
                print("\nProgram interrupted. Exiting...")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break


if __name__ == "__main__":
    try:
        inventory_manager = Inventory()
        inventory_manager.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
```
