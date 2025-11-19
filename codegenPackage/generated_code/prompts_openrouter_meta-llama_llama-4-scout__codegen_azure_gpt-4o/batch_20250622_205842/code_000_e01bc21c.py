"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write a Python script to manage food distribution for a non-profit organization like Rakhshanda Memorial, including tracking food packs and ration drives.
Generated: DETERMINISTIC_e01bc21c4f3dd792
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os


class FoodDistributionManager:
    """
    A class to manage food distribution for a non-profit organization.
    Tracks food packs and ration drives.
    """

    def __init__(self, data_file="food_distribution_data.json"):
        """
        Initialize the FoodDistributionManager with a data file.
        :param data_file: Path to the JSON file for storing data.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Load data from the JSON file. If the file doesn't exist, initialize with empty data.
        :return: Dictionary containing food packs and ration drives.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading data file. Initializing with empty data.")
        return {"food_packs": {}, "ration_drives": []}

    def _save_data(self):
        """
        Save the current data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_food_pack(self, pack_id, description, quantity):
        """
        Add a new food pack to the inventory.
        :param pack_id: Unique identifier for the food pack.
        :param description: Description of the food pack.
        :param quantity: Quantity of the food pack.
        """
        if pack_id in self.data["food_packs"]:
            print(f"Food pack with ID {pack_id} already exists.")
            return
        self.data["food_packs"][pack_id] = {
            "description": description,
            "quantity": quantity,
        }
        self._save_data()
        print(f"Food pack {pack_id} added successfully.")

    def update_food_pack_quantity(self, pack_id, quantity):
        """
        Update the quantity of an existing food pack.
        :param pack_id: Unique identifier for the food pack.
        :param quantity: New quantity of the food pack.
        """
        if pack_id not in self.data["food_packs"]:
            print(f"Food pack with ID {pack_id} does not exist.")
            return
        self.data["food_packs"][pack_id]["quantity"] = quantity
        self._save_data()
        print(f"Food pack {pack_id} updated successfully.")

    def add_ration_drive(self, drive_name, date, food_packs):
        """
        Add a new ration drive.
        :param drive_name: Name of the ration drive.
        :param date: Date of the ration drive (YYYY-MM-DD).
        :param food_packs: List of food pack IDs to be distributed.
        """
        try:
            drive_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        for pack_id in food_packs:
            if pack_id not in self.data["food_packs"]:
                print(f"Food pack with ID {pack_id} does not exist. Skipping.")
                food_packs.remove(pack_id)

        self.data["ration_drives"].append({
            "drive_name": drive_name,
            "date": str(drive_date),
            "food_packs": food_packs,
        })
        self._save_data()
        print(f"Ration drive '{drive_name}' added successfully.")

    def view_food_packs(self):
        """
        View all food packs in the inventory.
        """
        print("Food Packs:")
        for pack_id, details in self.data["food_packs"].items():
            print(f"ID: {pack_id}, Description: {details['description']}, Quantity: {details['quantity']}")

    def view_ration_drives(self):
        """
        View all ration drives.
        """
        print("Ration Drives:")
        for drive in self.data["ration_drives"]:
            print(f"Name: {drive['drive_name']}, Date: {drive['date']}, Food Packs: {', '.join(drive['food_packs'])}")


if __name__ == "__main__":
    # Example usage of the FoodDistributionManager
    manager = FoodDistributionManager()

    # Add food packs
    manager.add_food_pack("FP001", "Rice Pack", 100)
    manager.add_food_pack("FP002", "Wheat Pack", 50)

    # Update food pack quantity
    manager.update_food_pack_quantity("FP001", 120)

    # Add ration drive
    manager.add_ration_drive("Drive 1", "2023-10-01", ["FP001", "FP002"])

    # View food packs and ration drives
    manager.view_food_packs()
    manager.view_ration_drives()
```
