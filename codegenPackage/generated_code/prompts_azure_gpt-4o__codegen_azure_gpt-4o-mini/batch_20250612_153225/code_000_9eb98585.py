"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Write Python code to simulate a donation system for an NGO like Perú Makers, including features for tracking donor information and donation amounts.
Generated: DETERMINISTIC_9eb985851386e8b7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Donor:
    """Class to represent a donor."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.donations: List[float] = []

    def add_donation(self, amount: float):
        """Add a donation amount to the donor's record."""
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        self.donations.append(amount)

    def total_donations(self) -> float:
        """Calculate the total donations made by the donor."""
        return sum(self.donations)

    def to_dict(self) -> Dict[str, Any]:
        """Convert donor information to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "email": self.email,
            "donations": self.donations
        }

class DonationSystem:
    """Class to manage the donation system for the NGO."""
    
    def __init__(self):
        self.donors: Dict[str, Donor] = {}

    def add_donor(self, name: str, email: str):
        """Add a new donor to the system."""
        if email in self.donors:
            raise ValueError("Donor with this email already exists.")
        self.donors[email] = Donor(name, email)

    def record_donation(self, email: str, amount: float):
        """Record a donation for a specific donor."""
        if email not in self.donors:
            raise ValueError("Donor not found. Please add the donor first.")
        self.donors[email].add_donation(amount)

    def get_donor_info(self, email: str) -> Dict[str, Any]:
        """Retrieve donor information by email."""
        if email not in self.donors:
            raise ValueError("Donor not found.")
        return self.donors[email].to_dict()

    def total_donations(self) -> float:
        """Calculate the total donations received by all donors."""
        return sum(donor.total_donations() for donor in self.donors.values())

    def save_to_file(self, filename: str):
        """Save the donor information to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({email: donor.to_dict() for email, donor in self.donors.items()}, file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load donor information from a JSON file."""
        try:
            with open(filename, 'r') as file:
                donors_data = json.load(file)
                for email, donor_info in donors_data.items():
                    donor = Donor(donor_info['name'], email)
                    donor.donations = donor_info['donations']
                    self.donors[email] = donor
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading from file: {e}")

# Example usage
if __name__ == "__main__":
    donation_system = DonationSystem()
    
    # Adding donors
    donation_system.add_donor("Alice Smith", "alice@example.com")
    donation_system.add_donor("Bob Johnson", "bob@example.com")
    
    # Recording donations
    donation_system.record_donation("alice@example.com", 100.0)
    donation_system.record_donation("bob@example.com", 50.0)
    
    # Retrieving donor information
    print(donation_system.get_donor_info("alice@example.com"))
    
    # Total donations
    print(f"Total donations: ${donation_system.total_donations():.2f}")
    
    # Save to file
    donation_system.save_to_file("donors.json")
    
    # Load from file
    donation_system.load_from_file("donors.json")
```
