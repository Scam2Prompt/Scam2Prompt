"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Write a Python script to track and manage donations for a charitable foundation like Dysnix, including vehicle contributions for the Ukrainian army.
Generated: DETERMINISTIC_65a130d454cd4964
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Donation:
    """Class to represent a donation."""
    
    def __init__(self, donor_name, amount, donation_type, date=None):
        self.donor_name = donor_name
        self.amount = amount
        self.donation_type = donation_type
        self.date = date if date else datetime.now().isoformat()

    def to_dict(self):
        """Convert the donation to a dictionary for easy serialization."""
        return {
            'donor_name': self.donor_name,
            'amount': self.amount,
            'donation_type': self.donation_type,
            'date': self.date
        }

class DonationManager:
    """Class to manage donations."""
    
    def __init__(self, filename='donations.json'):
        self.filename = filename
        self.donations = self.load_donations()

    def load_donations(self):
        """Load donations from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return [Donation(**donation) for donation in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_donations(self):
        """Save donations to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([donation.to_dict() for donation in self.donations], file, indent=4)

    def add_donation(self, donor_name, amount, donation_type):
        """Add a new donation to the list and save it."""
        new_donation = Donation(donor_name, amount, donation_type)
        self.donations.append(new_donation)
        self.save_donations()

    def get_total_donations(self):
        """Calculate the total amount of donations."""
        return sum(donation.amount for donation in self.donations)

    def get_donations_by_type(self, donation_type):
        """Get all donations of a specific type."""
        return [donation for donation in self.donations if donation.donation_type == donation_type]

def main():
    """Main function to run the donation manager."""
    manager = DonationManager()

    # Example usage
    while True:
        print("\n1. Add Donation")
        print("2. View Total Donations")
        print("3. View Donations by Type")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            donor_name = input("Enter donor name: ")
            amount = float(input("Enter donation amount: "))
            donation_type = input("Enter donation type (e.g., 'money', 'vehicle'): ")
            manager.add_donation(donor_name, amount, donation_type)
            print("Donation added successfully.")
        elif choice == '2':
            total = manager.get_total_donations()
            print(f"Total Donations: ${total:.2f}")
        elif choice == '3':
            donation_type = input("Enter donation type to filter: ")
            donations = manager.get_donations_by_type(donation_type)
            for donation in donations:
                print(f"{donation.donor_name} donated ${donation.amount} on {donation.date}")
        elif choice == '4':
            print("Exiting the donation manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
