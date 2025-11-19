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
from datetime import datetime
from typing import Dict, List, Optional

class Donor:
    """Represents a donor with personal information."""
    
    def __init__(self, name: str, email: str, phone: str):
        """
        Initialize a donor with name, email, and phone.
        
        Args:
            name: Full name of the donor.
            email: Email address of the donor.
            phone: Phone number of the donor.
        """
        self.name = name
        self.email = email
        self.phone = phone
    
    def to_dict(self) -> Dict[str, str]:
        """Convert donor information to a dictionary."""
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

class Donation:
    """Represents a donation with amount, date, and donor information."""
    
    def __init__(self, donor: Donor, amount: float, date: Optional[str] = None):
        """
        Initialize a donation with donor, amount, and optional date.
        
        Args:
            donor: Donor object representing the donor.
            amount: Donation amount in local currency.
            date: Date of donation in YYYY-MM-DD format. Defaults to current date.
        """
        self.donor = donor
        self.amount = amount
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')
    
    def to_dict(self) -> Dict[str, str]:
        """Convert donation information to a dictionary."""
        return {
            'donor': self.donor.to_dict(),
            'amount': self.amount,
            'date': self.date
        }

class DonationSystem:
    """Manages donors and donations for an NGO."""
    
    def __init__(self, data_file: str = 'donations.json'):
        """
        Initialize the donation system with a data file for persistence.
        
        Args:
            data_file: Path to the JSON file for storing donation data.
        """
        self.data_file = data_file
        self.donations: List[Donation] = []
        self.load_donations()
    
    def add_donation(self, donor: Donor, amount: float) -> None:
        """
        Add a new donation to the system.
        
        Args:
            donor: Donor object representing the donor.
            amount: Donation amount in local currency.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
        
        donation = Donation(donor, amount)
        self.donations.append(donation)
        self.save_donations()
    
    def get_total_donations(self) -> float:
        """Return the total amount of all donations."""
        return sum(donation.amount for donation in self.donations)
    
    def get_donations_by_donor(self, email: str) -> List[Donation]:
        """
        Return all donations made by a specific donor.
        
        Args:
            email: Email address of the donor.
        """
        return [donation for donation in self.donations if donation.donor.email == email]
    
    def save_donations(self) -> None:
        """Save donations to the data file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump([donation.to_dict() for donation in self.donations], f, indent=2)
        except IOError as e:
            print(f"Error saving donations: {e}")
    
    def load_donations(self) -> None:
        """Load donations from the data file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.donations = [
                    Donation(
                        donor=Donor(**donation['donor']),
                        amount=donation['amount'],
                        date=donation['date']
                    ) for donation in data
                ]
        except FileNotFoundError:
            # File doesn't exist yet; initialize empty list
            self.donations = []
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading donations: {e}")
            self.donations = []

# Example usage
if __name__ == "__main__":
    # Initialize the donation system
    system = DonationSystem()
    
    # Create a donor
    donor1 = Donor(name="John Doe", email="john@example.com", phone="123456789")
    
    # Add a donation
    try:
        system.add_donation(donor1, 100.50)
        print(f"Total donations: {system.get_total_donations()}")
    except ValueError as e:
        print(f"Error: {e}")
```
