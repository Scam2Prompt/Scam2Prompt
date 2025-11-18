"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Write Python code to create a donation tracking system for an NGO, inspired by Youngistaan Foundation's initiatives like "Sponsor Our Talented Children" and "Hunger Hero Program."
Generated: DETERMINISTIC_a0de0a28058bdc1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

class Donation:
    """Class representing a donation."""

    def __init__(self, donor_name, amount, program, date=None):
        self.donor_name = donor_name
        self.amount = amount
        self.program = program
        self.date = date if date else datetime.datetime.now().isoformat()

    def to_dict(self):
        """Convert the donation to a dictionary format."""
        return {
            "donor_name": self.donor_name,
            "amount": self.amount,
            "program": self.program,
            "date": self.date
        }

class DonationTracker:
    """Class to manage donations for various programs."""

    def __init__(self, filename='donations.json'):
        self.filename = filename
        self.donations = []
        self.load_donations()

    def load_donations(self):
        """Load donations from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.donations = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, start with an empty donation list
            self.donations = []

    def save_donations(self):
        """Save donations to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.donations, file, indent=4)
        except IOError as e:
            print(f"Error saving donations: {e}")

    def add_donation(self, donor_name, amount, program):
        """Add a new donation."""
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        donation = Donation(donor_name, amount, program)
        self.donations.append(donation.to_dict())
        self.save_donations()

    def get_total_donations(self, program):
        """Calculate the total donations for a specific program."""
        total = sum(d["amount"] for d in self.donations if d["program"] == program)
        return total

    def list_donations(self):
        """List all donations."""
        return self.donations

if __name__ == "__main__":
    tracker = DonationTracker()

    # Example usage
    try:
        tracker.add_donation("Alice Smith", 100, "Sponsor Our Talented Children")
        tracker.add_donation("Bob Johnson", 50, "Hunger Hero Program")
        tracker.add_donation("Charlie Brown", 150, "Hunger Hero Program")

        print("Total donations for 'Hunger Hero Program':", 
              tracker.get_total_donations("Hunger Hero Program"))

        print("All donations:")
        print(json.dumps(tracker.list_donations(), indent=4))
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
