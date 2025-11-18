"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Write Python code to simulate a donation system for an NGO like Perú Makers, including features for tracking donor information and donation amounts.
Generated: DETERMINISTIC_9eb985851386e8b7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class DonationSystem:
    """A class to manage donations for an NGO."""

    def __init__(self, data_file='donations.json'):
        """Initialize the donation system with a specified data file."""
        self.data_file = data_file
        self.donors = self.load_donors()

    def load_donors(self):
        """Load donor information from a JSON file."""
        if not os.path.exists(self.data_file):
            return {}
        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: Could not decode JSON. Starting with an empty donor list.")
                return {}

    def save_donors(self):
        """Save donor information to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.donors, file, indent=4)

    def add_donation(self, donor_name, amount):
        """Add a donation for a specific donor.
        
        Args:
            donor_name (str): The name of the donor.
            amount (float): The donation amount.
        """
        if amount <= 0:
            print("Error: Donation amount must be greater than zero.")
            return

        if donor_name in self.donors:
            self.donors[donor_name] += amount
        else:
            self.donors[donor_name] = amount
        
        self.save_donors()
        print(f"Donation of {amount} from {donor_name} added successfully.")

    def get_donor_info(self, donor_name):
        """Retrieve the donation amount for a specific donor.
        
        Args:
            donor_name (str): The name of the donor.
        
        Returns:
            float: Total donation amount for the donor or None if not found.
        """
        return self.donors.get(donor_name, None)

    def get_total_donations(self):
        """Calculate the total amount of donations received."""
        return sum(self.donors.values())

    def display_all_donors(self):
        """Display all donor information."""
        if not self.donors:
            print("No donations recorded.")
            return
        
        print("Donor Information:")
        for donor, amount in self.donors.items():
            print(f"{donor}: {amount}")

if __name__ == "__main__":
    donation_system = DonationSystem()

    # Example usage
    donation_system.add_donation("Alice", 100.0)
    donation_system.add_donation("Bob", 150.5)
    donation_system.add_donation("Alice", 50.0)

    print(f"Total Donations: {donation_system.get_total_donations()}")
    donation_system.display_all_donors()
    print(f"Alice's Donations: {donation_system.get_donor_info('Alice')}")
```
