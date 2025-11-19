"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Write a program to manage donations for a non-profit organization like Udruga Radost Ogulin, including tracking and acknowledging contributions.
Generated: DETERMINISTIC_e857a19f1bb05878
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
from datetime import datetime

class Donation:
    """Class to represent a donation."""
    
    def __init__(self, donor_name, amount, date=None):
        """
        Initialize a new donation.

        :param donor_name: Name of the donor
        :param amount: Amount donated
        :param date: Date of the donation (defaults to today)
        """
        self.donor_name = donor_name
        self.amount = amount
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """Convert the donation to a dictionary."""
        return {
            "donor_name": self.donor_name,
            "amount": self.amount,
            "date": self.date
        }

class DonationManager:
    """Class to manage donations."""
    
    def __init__(self, filename='donations.json'):
        """
        Initialize the donation manager.

        :param filename: File to store donations
        """
        self.filename = filename
        self.donations = self.load_donations()

    def load_donations(self):
        """Load donations from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_donations(self):
        """Save donations to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.donations, file, indent=4)

    def add_donation(self, donor_name, amount):
        """
        Add a new donation.

        :param donor_name: Name of the donor
        :param amount: Amount donated
        """
        donation = Donation(donor_name, amount)
        self.donations.append(donation.to_dict())
        self.save_donations()
        self.acknowledge_donation(donation)

    def acknowledge_donation(self, donation):
        """Acknowledge the donation to the donor."""
        print(f"Thank you, {donation.donor_name}, for your generous donation of ${donation.amount:.2f} on {donation.date}!")

    def get_total_donations(self):
        """Calculate the total amount of donations."""
        return sum(donation['amount'] for donation in self.donations)

    def list_donations(self):
        """List all donations."""
        return self.donations

if __name__ == "__main__":
    # Example usage of the DonationManager
    donation_manager = DonationManager()

    # Adding donations
    donation_manager.add_donation("Alice Smith", 100.00)
    donation_manager.add_donation("Bob Johnson", 250.50)

    # Listing all donations
    print("All Donations:")
    for donation in donation_manager.list_donations():
        print(donation)

    # Total donations
    total = donation_manager.get_total_donations()
    print(f"Total Donations: ${total:.2f}")
```
