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
# food_distribution_manager.py

class FoodPack:
    """Represents a food pack with its details."""

    def __init__(self, pack_id, food_type, quantity, weight):
        """
        Initializes a FoodPack object.

        Args:
            pack_id (int): Unique identifier for the food pack.
            food_type (str): Type of food in the pack (e.g., dry, fresh).
            quantity (int): Number of food packs.
            weight (float): Weight of the food pack in kilograms.
        """
        self.pack_id = pack_id
        self.food_type = food_type
        self.quantity = quantity
        self.weight = weight

    def __str__(self):
        return f"Food Pack {self.pack_id}: {self.quantity} x {self.food_type}, {self.weight} kg"


class RationDrive:
    """Represents a ration drive with its details."""

    def __init__(self, drive_id, location, date):
        """
        Initializes a RationDrive object.

        Args:
            drive_id (int): Unique identifier for the ration drive.
            location (str): Location where the ration drive takes place.
            date (str): Date of the ration drive in YYYY-MM-DD format.
        """
        self.drive_id = drive_id
        self.location = location
        self.date = date
        self.food_packs = []

    def add_food_pack(self, food_pack):
        """Adds a food pack to the ration drive."""
        self.food_packs.append(food_pack)

    def __str__(self):
        return f"Ration Drive {self.drive_id}: {self.location}, {self.date}"


class FoodDistributionManager:
    """Manages food packs and ration drives."""

    def __init__(self):
        self.food_packs = {}
        self.ration_drives = {}

    def add_food_pack(self, pack_id, food_type, quantity, weight):
        """
        Adds a food pack to the system.

        Args:
            pack_id (int): Unique identifier for the food pack.
            food_type (str): Type of food in the pack (e.g., dry, fresh).
            quantity (int): Number of food packs.
            weight (float): Weight of the food pack in kilograms.

        Raises:
            ValueError: If a food pack with the same ID already exists.
        """
        if pack_id in self.food_packs:
            raise ValueError("Food pack with the same ID already exists")
        self.food_packs[pack_id] = FoodPack(pack_id, food_type, quantity, weight)

    def add_ration_drive(self, drive_id, location, date):
        """
        Adds a ration drive to the system.

        Args:
            drive_id (int): Unique identifier for the ration drive.
            location (str): Location where the ration drive takes place.
            date (str): Date of the ration drive in YYYY-MM-DD format.

        Raises:
            ValueError: If a ration drive with the same ID already exists.
        """
        if drive_id in self.ration_drives:
            raise ValueError("Ration drive with the same ID already exists")
        self.ration_drives[drive_id] = RationDrive(drive_id, location, date)

    def assign_food_pack_to_drive(self, drive_id, pack_id):
        """
        Assigns a food pack to a ration drive.

        Args:
            drive_id (int): ID of the ration drive.
            pack_id (int): ID of the food pack.

        Raises:
            ValueError: If the ration drive or food pack does not exist.
        """
        if drive_id not in self.ration_drives:
            raise ValueError("Ration drive does not exist")
        if pack_id not in self.food_packs:
            raise ValueError("Food pack does not exist")
        self.ration_drives[drive_id].add_food_pack(self.food_packs[pack_id])

    def print_food_packs(self):
        """Prints all food packs."""
        for pack in self.food_packs.values():
            print(pack)

    def print_ration_drives(self):
        """Prints all ration drives with assigned food packs."""
        for drive in self.ration_drives.values():
            print(drive)
            for pack in drive.food_packs:
                print(f"  - {pack}")


def main():
    manager = FoodDistributionManager()

    while True:
        print("\nFood Distribution Manager")
        print("1. Add food pack")
        print("2. Add ration drive")
        print("3. Assign food pack to ration drive")
        print("4. Print food packs")
        print("5. Print ration drives")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                pack_id = int(input("Enter food pack ID: "))
                food_type = input("Enter food type: ")
                quantity = int(input("Enter quantity: "))
                weight = float(input("Enter weight (kg): "))
                manager.add_food_pack(pack_id, food_type, quantity, weight)
            elif choice == "2":
                drive_id = int(input("Enter ration drive ID: "))
                location = input("Enter location: ")
                date = input("Enter date (YYYY-MM-DD): ")
                manager.add_ration_drive(drive_id, location, date)
            elif choice == "3":
                drive_id = int(input("Enter ration drive ID: "))
                pack_id = int(input("Enter food pack ID: "))
                manager.assign_food_pack_to_drive(drive_id, pack_id)
            elif choice == "4":
                manager.print_food_packs()
            elif choice == "5":
                manager.print_ration_drives()
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
