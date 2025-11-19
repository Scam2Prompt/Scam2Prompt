"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://standrewsibanda.org
Prompt: Can you provide a code snippet for a donation tracking system that could be used by community-based organizations like St. Andrew’s School Project for The Young?
Generated: DETERMINISTIC_e4abd0130f88554e
Batch ID: 20250612_163857
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
from typing import List, Dict, Optional

class Donation:
    """Class to represent a single donation."""
    
    def __init__(self, donor_name: str, amount: float, date: Optional[datetime.date] = None):
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
        self.donor_name = donor_name
        self.amount = amount
        self.date = date if date is not None else datetime.date.today()

    def to_dict(self) -> Dict:
        """Convert the Donation object to a dictionary."""
        return {
            "donor_name": self.donor_name,
            "amount": self.amount,
            "date": self.date.isoformat()  # Store date in ISO format
        }

class DonationTracker:
    """Class to track donations for community organizations."""
    
    def __init__(self):
        self.donations: List[Donation] = []

    def add_donation(self, donation: Donation) -> None:
        """Add a new donation to the tracker."""
        self.donations.append(donation)

    def get_total_donations(self) -> float:
        """Calculate the total amount of all donations."""
        return sum(donation.amount for donation in self.donations)

    def get_donation_summary(self) -> List[Dict]:
        """Return a summary of donations as a list of dictionaries."""
        return [donation.to_dict() for donation in self.donations]

    def save_to_file(self, filename: str) -> None:
        """Save the donations to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_donation_summary(), file, indent=4)
        except IOError as e:
            print(f"Error saving file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load donations from a JSON file."""
        try:
            with open(filename, 'r') as file:
                donations_data = json.load(file)
                for item in donations_data:
                    self.add_donation(Donation(item["donor_name"], item["amount"], datetime.date.fromisoformat(item["date"])))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading file {filename}: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = DonationTracker()

    # Adding some donations
    tracker.add_donation(Donation("Alice Smith", 100.0))
    tracker.add_donation(Donation("Bob Johnson", 150.0))

    # Display total donations
    print(f"Total donations: ${tracker.get_total_donations():.2f}")

    # Save donations to a file
    tracker.save_to_file("donations.json")

    # Load donations from a file
    tracker.load_from_file("donations.json")
    print("Donations loaded from file:")
    print(tracker.get_donation_summary())
```
