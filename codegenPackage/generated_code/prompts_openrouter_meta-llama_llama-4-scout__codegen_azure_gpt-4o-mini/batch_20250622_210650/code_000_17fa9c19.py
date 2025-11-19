"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Write a code for a donation tracking system that can be used by a non-profit organization like Viajeras, which supports women who have experienced sexual aggression.
Generated: DETERMINISTIC_17fa9c1938b27158
Batch ID: 20250622_210650
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
        :param date: Date of the donation (defaults to current date)
        """
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


class DonationTracker:
    """Class to track donations for a non-profit organization."""
    
    def __init__(self, filename='donations.json'):
        """
        Initialize the donation tracker.

        :param filename: The file where donations will be stored
        """
        self.filename = filename
        self.donations = self.load_donations()

    def load_donations(self):
        """Load donations from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return [Donation(**donation) for donation in json.load(file)]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the donation file.")
            return []

    def save_donations(self):
        """Save donations to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([donation.to_dict() for donation in self.donations], file, indent=4)

    def add_donation(self, donor_name, amount):
        """
        Add a new donation.

        :param donor_name: Name of the donor
        :param amount: Amount donated
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        new_donation = Donation(donor_name, amount)
        self.donations.append(new_donation)
        self.save_donations()

    def total_donations(self):
        """Calculate the total amount of donations."""
        return sum(donation.amount for donation in self.donations)

    def list_donations(self):
        """List all donations."""
        return [donation.to_dict() for donation in self.donations]


if __name__ == "__main__":
    # Example usage of the DonationTracker
    tracker = DonationTracker()

    # Adding donations
    try:
        tracker.add_donation("Alice Smith", 100.0)
        tracker.add_donation("Bob Johnson", 50.0)
    except ValueError as e:
        print(f"Error adding donation: {e}")

    # Display total donations
    print(f"Total Donations: ${tracker.total_donations():.2f}")

    # List all donations
    print("Donations List:")
    for donation in tracker.list_donations():
        print(donation)
```
