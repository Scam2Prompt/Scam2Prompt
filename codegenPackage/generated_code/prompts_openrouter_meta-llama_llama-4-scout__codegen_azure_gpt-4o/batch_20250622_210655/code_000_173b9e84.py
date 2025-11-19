"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Write a Python script to manage donations for a social organization like CEFOR, including tracking and reporting features.
Generated: DETERMINISTIC_173b9e8421f254a3
Batch ID: 20250622_210655
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

class DonationManager:
    """
    A class to manage donations for a social organization.
    Includes functionality to add donations, view all donations, and generate reports.
    """

    def __init__(self, data_file="donations.json"):
        """
        Initializes the DonationManager with a data file to store donation records.
        :param data_file: Path to the JSON file where donation data will be stored.
        """
        self.data_file = data_file
        self.donations = self._load_donations()

    def _load_donations(self):
        """
        Loads donation data from the JSON file.
        If the file does not exist, initializes an empty list.
        :return: List of donation records.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading donation data. Starting with an empty record.")
                return []
        return []

    def _save_donations(self):
        """
        Saves the current donation data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.donations, file, indent=4)
        except IOError as e:
            print(f"Error saving donation data: {e}")

    def add_donation(self, donor_name, amount, date=None):
        """
        Adds a new donation record.
        :param donor_name: Name of the donor.
        :param amount: Donation amount (must be positive).
        :param date: Date of the donation (defaults to today if not provided).
        """
        if amount <= 0:
            print("Donation amount must be positive.")
            return

        if date is None:
            date = datetime.date.today().isoformat()

        donation = {
            "donor_name": donor_name,
            "amount": amount,
            "date": date
        }
        self.donations.append(donation)
        self._save_donations()
        print(f"Donation added successfully: {donation}")

    def view_donations(self):
        """
        Displays all donation records.
        """
        if not self.donations:
            print("No donations found.")
            return

        print("Donation Records:")
        for idx, donation in enumerate(self.donations, start=1):
            print(f"{idx}. Donor: {donation['donor_name']}, Amount: ${donation['amount']:.2f}, Date: {donation['date']}")

    def generate_report(self):
        """
        Generates a summary report of all donations.
        Includes total donations, number of donations, and average donation amount.
        """
        if not self.donations:
            print("No donations available to generate a report.")
            return

        total_amount = sum(donation["amount"] for donation in self.donations)
        num_donations = len(self.donations)
        average_donation = total_amount / num_donations

        print("Donation Report:")
        print(f"Total Donations: ${total_amount:.2f}")
        print(f"Number of Donations: {num_donations}")
        print(f"Average Donation Amount: ${average_donation:.2f}")

def main():
    """
    Main function to interact with the DonationManager.
    Provides a simple menu for managing donations.
    """
    manager = DonationManager()

    while True:
        print("\nDonation Management System")
        print("1. Add Donation")
        print("2. View Donations")
        print("3. Generate Report")
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
            date = input("Enter donation date (YYYY-MM-DD) or press Enter for today: ")
            manager.add_donation(donor_name, amount, date if date else None)
        elif choice == 2:
            manager.view_donations()
        elif choice == 3:
            manager.generate_report()
        elif choice == 4:
            print("Exiting the Donation Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
