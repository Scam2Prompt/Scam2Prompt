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

class FishingBaitManager:
    """
    A class to manage and store fishing bait information.
    Supports natural baits like bloodworm and casters.
    """

    def __init__(self, data_file="fishing_baits.json"):
        """
        Initialize the fishing bait manager with a data file.

        :param data_file: Path to the JSON file to store bait data.
        """
        self.data_file = data_file
        self.baits = self.load_baits()

    def load_baits(self):
        """
        Load bait data from the JSON file.

        :return: A dictionary of bait data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading bait data. Starting with an empty database.")
                return {}
        return {}

    def save_baits(self):
        """
        Save bait data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.baits, file, indent=4)
        except IOError as e:
            print(f"Error saving bait data: {e}")

    def add_bait(self, bait_name, bait_type, quantity):
        """
        Add a new bait to the database.

        :param bait_name: Name of the bait (e.g., "Bloodworm").
        :param bait_type: Type of bait (e.g., "Natural").
        :param quantity: Quantity of bait in stock.
        """
        if bait_name in self.baits:
            print(f"Bait '{bait_name}' already exists. Updating quantity.")
            self.baits[bait_name]["quantity"] += quantity
        else:
            self.baits[bait_name] = {
                "type": bait_type,
                "quantity": quantity
            }
        self.save_baits()
        print(f"Bait '{bait_name}' added/updated successfully.")

    def remove_bait(self, bait_name):
        """
        Remove a bait from the database.

        :param bait_name: Name of the bait to remove.
        """
        if bait_name in self.baits:
            del self.baits[bait_name]
            self.save_baits()
            print(f"Bait '{bait_name}' removed successfully.")
        else:
            print(f"Bait '{bait_name}' does not exist.")

    def update_quantity(self, bait_name, quantity):
        """
        Update the quantity of a specific bait.

        :param bait_name: Name of the bait.
        :param quantity: New quantity value.
        """
        if bait_name in self.baits:
            self.baits[bait_name]["quantity"] = quantity
            self.save_baits()
            print(f"Quantity for '{bait_name}' updated to {quantity}.")
        else:
            print(f"Bait '{bait_name}' does not exist.")

    def list_baits(self):
        """
        List all available baits in the database.
        """
        if self.baits:
            print("Available Baits:")
            for bait_name, details in self.baits.items():
                print(f" - {bait_name}: Type={details['type']}, Quantity={details['quantity']}")
        else:
            print("No baits available.")

if __name__ == "__main__":
    # Example usage of the FishingBaitManager class
    manager = FishingBaitManager()

    # Add some baits
    manager.add_bait("Bloodworm", "Natural", 50)
    manager.add_bait("Casters", "Natural", 30)

    # List all baits
    manager.list_baits()

    # Update quantity for a bait
    manager.update_quantity("Bloodworm", 40)

    # Remove a bait
    manager.remove_bait("Casters")

    # List all baits again
    manager.list_baits()
```
