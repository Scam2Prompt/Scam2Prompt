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
import json
import os
from datetime import datetime

class Donation:
    """Class to represent a donation."""
    
    def __init__(self, donor_name, amount, date=None):
        self.donor_name = donor_name
        self.amount = amount
        self.date = date if date else datetime.now().isoformat()

    def to_dict(self):
        """Convert the donation to a dictionary."""
        return {
            'donor_name': self.donor_name,
            'amount': self.amount,
            'date': self.date
        }

class DonationManager:
    """Class to manage donations."""
    
    def __init__(self, filename='donations.json'):
        self.filename = filename
        self.donations = []
        self.load_donations()

    def load_donations(self):
        """Load donations from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.donations = json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON from the file.")
                    self.donations = []
        else:
            print("No donation file found. Starting fresh.")

    def save_donations(self):
        """Save donations to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.donations, file, indent=4)

    def add_donation(self, donor_name, amount):
        """Add a new donation."""
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        donation = Donation(donor_name, amount)
        self.donations.append(donation.to_dict())
        self.save_donations()
        print(f"Donation of {amount} from {donor_name} added successfully.")

    def get_total_donations(self):
        """Calculate the total amount of donations."""
        return sum(donation['amount'] for donation in self.donations)

    def generate_report(self):
        """Generate a report of all donations."""
        report = {
            'total_donations': self.get_total_donations(),
            'donations': self.donations
        }
        return report

    def print_report(self):
        """Print the donation report."""
        report = self.generate_report()
        print("Donation Report:")
        print(f"Total Donations: {report['total_donations']}")
        for donation in report['donations']:
            print(f"Donor: {donation['donor_name']}, Amount: {donation['amount']}, Date: {donation['date']}")

def main():
    """Main function to run the donation manager."""
    manager = DonationManager()
    
    while True:
        print("\nDonation Manager")
        print("1. Add Donation")
        print("2. View Report")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            donor_name = input("Enter donor name: ")
            try:
                amount = float(input("Enter donation amount: "))
                manager.add_donation(donor_name, amount)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            manager.print_report()
        elif choice == '3':
            print("Exiting the Donation Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
