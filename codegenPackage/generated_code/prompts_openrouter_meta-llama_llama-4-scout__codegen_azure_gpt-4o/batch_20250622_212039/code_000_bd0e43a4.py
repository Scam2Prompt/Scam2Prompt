"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Write a Python script to track and manage donations of sanitary pads and dignity care packages for a non-profit organization like My Flow Foundation.
Generated: DETERMINISTIC_bd0e43a40eb8cc4c
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class DonationManager:
    """
    A class to manage donations of sanitary pads and dignity care packages
    for a non-profit organization.
    """

    def __init__(self, data_file="donations.json"):
        """
        Initializes the DonationManager with a data file to store donation records.

        :param data_file: Path to the JSON file where donation data is stored.
        """
        self.data_file = data_file
        self.donations = self._load_data()

    def _load_data(self):
        """
        Loads donation data from the JSON file. If the file does not exist,
        initializes an empty donation record.

        :return: A dictionary containing donation records.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading donation data. Initializing empty records.")
                return {}
        return {}

    def _save_data(self):
        """
        Saves the current donation data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.donations, file, indent=4)
        except IOError as e:
            print(f"Error saving donation data: {e}")

    def add_donation(self, donor_name, item_type, quantity):
        """
        Adds a donation record.

        :param donor_name: Name of the donor.
        :param item_type: Type of item donated (e.g., "Sanitary Pads", "Dignity Care Packages").
        :param quantity: Quantity of items donated.
        """
        if item_type not in ["Sanitary Pads", "Dignity Care Packages"]:
            print("Invalid item type. Please use 'Sanitary Pads' or 'Dignity Care Packages'.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if donor_name not in self.donations:
            self.donations[donor_name] = {}

        if item_type in self.donations[donor_name]:
            self.donations[donor_name][item_type] += quantity
        else:
            self.donations[donor_name][item_type] = quantity

        print(f"Donation added: {donor_name} donated {quantity} {item_type}.")
        self._save_data()

    def view_donations(self):
        """
        Displays all donation records.
        """
        if not self.donations:
            print("No donations recorded yet.")
            return

        print("Donation Records:")
        for donor, items in self.donations.items():
            print(f"Donor: {donor}")
            for item_type, quantity in items.items():
                print(f"  {item_type}: {quantity}")

    def total_donations(self):
        """
        Calculates and displays the total quantity of each item type donated.

        :return: A dictionary with total quantities of each item type.
        """
        totals = {"Sanitary Pads": 0, "Dignity Care Packages": 0}
        for items in self.donations.values():
            for item_type, quantity in items.items():
                if item_type in totals:
                    totals[item_type] += quantity

        print("Total Donations:")
        for item_type, total in totals.items():
            print(f"  {item_type}: {total}")

        return totals


# Main script
if __name__ == "__main__":
    manager = DonationManager()

    while True:
        print("\nDonation Management System")
        print("1. Add Donation")
        print("2. View Donations")
        print("3. View Total Donations")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            donor_name = input("Enter donor name: ").strip()
            item_type = input("Enter item type (Sanitary Pads/Dignity Care Packages): ").strip()
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
                continue

            manager.add_donation(donor_name, item_type, quantity)

        elif choice == 2:
            manager.view_donations()

        elif choice == 3:
            manager.total_donations()

        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
```
