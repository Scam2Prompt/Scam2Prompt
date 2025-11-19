"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Design a system to manage donations and financial support for a humanitarian organization, ensuring transparency and accountability in fund allocation.
Generated: DETERMINISTIC_f1ba3ece01d43813
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
from typing import List, Dict, Optional

class Donation:
    """Class to represent a donation."""
    
    def __init__(self, donor_name: str, amount: float, date: Optional[datetime] = None):
        self.donor_name = donor_name
        self.amount = amount
        self.date = date if date else datetime.now()

    def to_dict(self) -> Dict:
        """Convert the donation to a dictionary for easy serialization."""
        return {
            "donor_name": self.donor_name,
            "amount": self.amount,
            "date": self.date.isoformat()
        }

class FundAllocation:
    """Class to represent fund allocation for specific projects."""
    
    def __init__(self, project_name: str, allocated_amount: float):
        self.project_name = project_name
        self.allocated_amount = allocated_amount
        self.date_allocated = datetime.now()

    def to_dict(self) -> Dict:
        """Convert the fund allocation to a dictionary for easy serialization."""
        return {
            "project_name": self.project_name,
            "allocated_amount": self.allocated_amount,
            "date_allocated": self.date_allocated.isoformat()
        }

class DonationManager:
    """Class to manage donations and fund allocations."""
    
    def __init__(self):
        self.donations: List[Donation] = []
        self.allocations: List[FundAllocation] = []

    def add_donation(self, donor_name: str, amount: float) -> None:
        """Add a new donation to the system."""
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        donation = Donation(donor_name, amount)
        self.donations.append(donation)

    def allocate_funds(self, project_name: str, amount: float) -> None:
        """Allocate funds to a specific project."""
        if amount <= 0:
            raise ValueError("Allocated amount must be greater than zero.")
        allocation = FundAllocation(project_name, amount)
        self.allocations.append(allocation)

    def get_donations(self) -> List[Dict]:
        """Retrieve all donations as a list of dictionaries."""
        return [donation.to_dict() for donation in self.donations]

    def get_allocations(self) -> List[Dict]:
        """Retrieve all fund allocations as a list of dictionaries."""
        return [allocation.to_dict() for allocation in self.allocations]

    def save_to_file(self, filename: str) -> None:
        """Save donations and allocations to a JSON file."""
        data = {
            "donations": self.get_donations(),
            "allocations": self.get_allocations()
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save data to {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load donations and allocations from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.donations = [Donation(**donation) for donation in data.get("donations", [])]
                self.allocations = [FundAllocation(**allocation) for allocation in data.get("allocations", [])]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load data from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = DonationManager()
    try:
        manager.add_donation("Alice", 100.0)
        manager.add_donation("Bob", 200.0)
        manager.allocate_funds("Food Relief", 150.0)
        
        # Save to file
        manager.save_to_file("donations.json")
        
        # Load from file
        manager.load_from_file("donations.json")
        
        print("Donations:", manager.get_donations())
        print("Allocations:", manager.get_allocations())
    except Exception as e:
        print(f"An error occurred: {e}")
```
