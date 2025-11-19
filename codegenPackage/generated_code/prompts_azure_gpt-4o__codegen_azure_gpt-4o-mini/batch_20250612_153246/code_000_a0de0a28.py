"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Write Python code to create a donation tracking system for an NGO, inspired by Youngistaan Foundation's initiatives like "Sponsor Our Talented Children" and "Hunger Hero Program."
Generated: DETERMINISTIC_a0de0a28058bdc1c
Batch ID: 20250612_153246
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
    
    def __init__(self, donor_name, amount, program, date=None):
        self.donor_name = donor_name
        self.amount = amount
        self.program = program
        self.date = date if date else datetime.now().isoformat()

    def to_dict(self):
        """Convert the donation to a dictionary for easy serialization."""
        return {
            "donor_name": self.donor_name,
            "amount": self.amount,
            "program": self.program,
            "date": self.date
        }

class DonationTracker:
    """Class to track donations for various programs."""
    
    def __init__(self, filename='donations.json'):
        self.filename = filename
        self.donations = []
        self.load_donations()

    def load_donations(self):
        """Load donations from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.donations = [Donation(**donation) for donation in json.load(file)]
        except FileNotFoundError:
            # If the file does not exist, we start with an empty donation list
            self.donations = []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the donation file.")
            self.donations = []

    def save_donations(self):
        """Save donations to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([donation.to_dict() for donation in self.donations], file, indent=4)
        except IOError as e:
            print(f"Error: Could not write to file {self.filename}. {e}")

    def add_donation(self, donor_name, amount, program):
        """Add a new donation to the tracker."""
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        donation = Donation(donor_name, amount, program)
        self.donations.append(donation)
        self.save_donations()

    def get_total_donations(self, program):
        """Get the total donations for a specific program."""
        total = sum(donation.amount for donation in self.donations if donation.program == program)
        return total

    def list_donations(self):
        """List all donations."""
        return [donation.to_dict() for donation in self.donations]

def main():
    """Main function to run the donation tracking system."""
    tracker = DonationTracker()

    # Example usage
    try:
        tracker.add_donation("Alice Smith", 100.0, "Sponsor Our Talented Children")
        tracker.add_donation("Bob Johnson", 50.0, "Hunger Hero Program")
        
        print("Total donations for 'Sponsor Our Talented Children':", tracker.get_total_donations("Sponsor Our Talented Children"))
        print("Total donations for 'Hunger Hero Program':", tracker.get_total_donations("Hunger Hero Program"))
        
        print("All donations:", tracker.list_donations())
    except ValueError as e:
        print(f"ValueError: {e}")

if __name__ == "__main__":
    main()
```
