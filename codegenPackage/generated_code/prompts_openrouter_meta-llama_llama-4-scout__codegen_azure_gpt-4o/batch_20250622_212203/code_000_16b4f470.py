"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Write a Python script to manage donations for a non-profit organization like Indological India, which has focus areas including Swasth Bharat and education.
Generated: DETERMINISTIC_16b4f4708b6713fe
Batch ID: 20250622_212203
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
    A class to manage donations for a non-profit organization.
    """

    def __init__(self, data_file="donations.json"):
        """
        Initialize the DonationManager with a data file to store donation records.

        :param data_file: Path to the JSON file where donation data will be stored.
        """
        self.data_file = data_file
        self.donations = self._load_donations()

    def _load_donations(self):
        """
        Load donation records from the JSON file.

        :return: A dictionary containing donation records.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading donation data. Starting with an empty record.")
                return {}
        return {}

    def _save_donations(self):
        """
        Save donation records to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.donations, file, indent=4)
        except IOError as e:
            print(f"Error saving donation data: {e}")

    def add_donation(self, donor_name, amount, focus_area):
        """
        Add a new donation record.

        :param donor_name: Name of the donor.
        :param amount: Donation amount (must be positive).
        :param focus_area: Focus area for the donation (e.g., "Swasth Bharat", "Education").
        """
        if amount <= 0:
            print("Donation amount must be positive.")
            return

        if focus_area not in ["Swasth Bharat", "Education"]:
            print("Invalid focus area. Please choose 'Swasth Bharat' or 'Education'.")
            return

        donation_id = len(self.donations) + 1
        self.donations[donation_id] = {
            "donor_name": donor_name,
            "amount": amount,
            "focus_area": focus_area
        }
        self._save_donations()
        print(f"Donation added successfully! Donation ID: {donation_id}")

    def view_donations(self):
        """
        View all donation records.
        """
        if not self.donations:
            print("No donations found.")
            return

        print("Donation Records:")
        for donation_id, details in self.donations.items():
            print(f"ID: {donation_id}, Donor: {details['donor_name']}, "
                  f"Amount: {details['amount']}, Focus Area: {details['focus_area']}")

    def delete_donation(self, donation_id):
        """
        Delete a donation record by its ID.

        :param donation_id: ID of the donation to delete.
        """
        if donation_id in self.donations:
            del self.donations[donation_id]
            self._save_donations()
            print(f"Donation ID {donation_id} deleted successfully.")
        else:
            print(f"Donation ID {donation_id} not found.")

def main():
    """
    Main function to interact with the DonationManager.
    """
    manager = DonationManager()

    while True:
        print("\nDonation Management System")
        print("1. Add Donation")
        print("2. View Donations")
        print("3. Delete Donation")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            donor_name = input("Enter donor name: ")
            try:
                amount = float(input("Enter donation amount: "))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            focus_area = input("Enter focus area (Swasth Bharat/Education): ")
            manager.add_donation(donor_name, amount, focus_area)
        elif choice == 2:
            manager.view_donations()
        elif choice == 3:
            try:
                donation_id = int(input("Enter donation ID to delete: "))
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
                continue
            manager.delete_donation(donation_id)
        elif choice == 4:
            print("Exiting Donation Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
```
