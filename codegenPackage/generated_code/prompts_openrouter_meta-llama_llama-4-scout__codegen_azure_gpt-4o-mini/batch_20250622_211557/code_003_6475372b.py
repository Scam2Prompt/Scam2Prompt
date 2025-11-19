"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Develop a donation tracking system using a suitable programming language, incorporating features like donor information, contribution amounts, and vehicle specifications, inspired by Dysnix's fundraising efforts.
Generated: DETERMINISTIC_6475372bf6900e82
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
from typing import List, Dict, Optional

class Donor:
    """Class to represent a donor."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, str]:
        """Convert donor information to a dictionary."""
        return {"name": self.name, "email": self.email}

class Contribution:
    """Class to represent a contribution."""
    
    def __init__(self, donor: Donor, amount: float, vehicle_spec: str):
        self.donor = donor
        self.amount = amount
        self.vehicle_spec = vehicle_spec

    def to_dict(self) -> Dict[str, str]:
        """Convert contribution information to a dictionary."""
        return {
            "donor": self.donor.to_dict(),
            "amount": self.amount,
            "vehicle_spec": self.vehicle_spec
        }

class DonationTracker:
    """Class to track donations."""
    
    def __init__(self):
        self.contributions: List[Contribution] = []

    def add_contribution(self, donor: Donor, amount: float, vehicle_spec: str) -> None:
        """Add a new contribution to the tracker."""
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")
        contribution = Contribution(donor, amount, vehicle_spec)
        self.contributions.append(contribution)

    def get_total_donations(self) -> float:
        """Calculate the total amount of donations."""
        return sum(contribution.amount for contribution in self.contributions)

    def save_to_file(self, filename: str) -> None:
        """Save contributions to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([contribution.to_dict() for contribution in self.contributions], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load contributions from a JSON file."""
        try:
            with open(filename, 'r') as file:
                contributions_data = json.load(file)
                for data in contributions_data:
                    donor_data = data['donor']
                    donor = Donor(donor_data['name'], donor_data['email'])
                    self.add_contribution(donor, data['amount'], data['vehicle_spec'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()
    
    # Adding contributions
    try:
        donor1 = Donor("Alice Smith", "alice@example.com")
        tracker.add_contribution(donor1, 100.0, "2015 Honda Civic")
        
        donor2 = Donor("Bob Johnson", "bob@example.com")
        tracker.add_contribution(donor2, 250.0, "2018 Toyota Corolla")
        
        print(f"Total Donations: ${tracker.get_total_donations():.2f}")
        
        # Save contributions to a file
        tracker.save_to_file("donations.json")
        
        # Load contributions from a file
        new_tracker = DonationTracker()
        new_tracker.load_from_file("donations.json")
        print(f"Total Donations after loading: ${new_tracker.get_total_donations():.2f}")
        
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
