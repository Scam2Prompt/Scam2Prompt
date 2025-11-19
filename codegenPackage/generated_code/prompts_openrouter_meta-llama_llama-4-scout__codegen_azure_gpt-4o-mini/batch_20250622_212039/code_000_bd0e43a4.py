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
from datetime import datetime

class DonationManager:
    """Class to manage donations for sanitary pads and dignity care packages."""

    def __init__(self, data_file='donations.json'):
        """Initialize the DonationManager with a data file."""
        self.data_file = data_file
        self.donations = self.load_donations()

    def load_donations(self):
        """Load donations from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON from the file. Starting with an empty donation list.")
                    return []
        return []

    def save_donations(self):
        """Save donations to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.donations, file, indent=4)

    def add_donation(self, donor_name, item_type, quantity):
        """Add a new donation to the list."""
        donation = {
            'donor_name': donor_name,
            'item_type': item_type,
            'quantity': quantity,
            'date': datetime.now().isoformat()
        }
        self.donations.append(donation)
        self.save_donations()
        print(f"Donation added: {donation}")

    def view_donations(self):
        """View all donations."""
        if not self.donations:
            print("No donations found.")
            return
        for donation in self.donations:
            print(donation)

    def total_donations(self):
        """Calculate the total number of items donated."""
        total = sum(donation['quantity'] for donation in self.donations)
        print(f"Total donations: {total}")

def main():
    """Main function to run the donation manager."""
    manager = DonationManager()

    while True:
        print("\nDonation Manager")
        print("1. Add Donation")
        print("2. View Donations")
        print("3. Total Donations")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            donor_name = input("Enter donor name: ")
            item_type = input("Enter item type (sanitary pads/dignity care package): ")
            try:
                quantity = int(input("Enter quantity: "))
                if quantity < 1:
                    raise ValueError("Quantity must be a positive integer.")
                manager.add_donation(donor_name, item_type, quantity)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            manager.view_donations()
        elif choice == '3':
            manager.total_donations()
        elif choice == '4':
            print("Exiting the Donation Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
