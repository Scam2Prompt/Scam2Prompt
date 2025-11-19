"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrdmngo.com
Prompt: Generate a code snippet for a donation tracking system that could be used by non-profit organizations like JRDM Foundation to manage contributions effectively.
Generated: DETERMINISTIC_7cbb956241fc23a4
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Donation:
    """Class representing a single donation."""
    
    def __init__(self, donor_name: str, amount: float, date: str):
        """
        Initializes a new donation instance.

        Parameters:
        - donor_name (str): The name of the donor.
        - amount (float): The donation amount.
        - date (str): The date of donation in 'YYYY-MM-DD' format.
        """
        self.donor_name = donor_name
        self.amount = amount
        self.date = date

    def to_dict(self) -> Dict[str, Any]:
        """Converts the Donation instance to a dictionary."""
        return {
            "donor_name": self.donor_name,
            "amount": self.amount,
            "date": self.date
        }

class DonationTracker:
    """Class to track donations for a non-profit organization."""

    def __init__(self, filename: str):
        """
        Initializes the donation tracker.

        Parameters:
        - filename (str): The filename to store donations.
        """
        self.filename = filename
        self.donations: List[Donation] = []
        self.load_donations()

    def load_donations(self) -> None:
        """Loads existing donations from the JSON file."""
        try:
            with open(self.filename, 'r') as f:
                donations_data = json.load(f)
                self.donations = [Donation(**data) for data in donations_data]
        except FileNotFoundError:
            # If the file does not exist, initialize with an empty list
            self.donations = []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the file. Starting fresh.")
            self.donations = []

    def save_donations(self) -> None:
        """Saves the donations to the JSON file."""
        with open(self.filename, 'w') as f:
            json.dump([donation.to_dict() for donation in self.donations], f)

    def add_donation(self, donor_name: str, amount: float, date: str) -> None:
        """
        Adds a new donation to the tracker.

        Parameters:
        - donor_name (str): The name of the donor.
        - amount (float): The donation amount.
        - date (str): The date of donation in 'YYYY-MM-DD' format.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        new_donation = Donation(donor_name, amount, date)
        self.donations.append(new_donation)
        self.save_donations()

    def get_total_donations(self) -> float:
        """Calculates the total donations received."""
        return sum(donation.amount for donation in self.donations)

    def get_donations(self) -> List[Dict[str, Any]]:
        """Returns a list of all donations."""
        return [donation.to_dict() for donation in self.donations]

# Usage Example:
if __name__ == "__main__":
    tracker = DonationTracker('donations.json')

    # Adding a new donation
    try:
        tracker.add_donation("John Doe", 100.0, "2023-10-01")
        print("Donation added successfully.")
    except ValueError as ve:
        print(f"Error: {ve}")

    # Get total donations
    total = tracker.get_total_donations()
    print(f"Total Donations: ${total:.2f}")

    # Get all donations
    print("All Donations:")
    for donation in tracker.get_donations():
        print(donation)
```
