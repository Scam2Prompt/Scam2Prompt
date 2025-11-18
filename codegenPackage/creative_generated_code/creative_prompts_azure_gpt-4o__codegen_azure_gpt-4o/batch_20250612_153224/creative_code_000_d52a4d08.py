"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Write Python code to create an online donation system for a non-profit organization, including features for tracking donations and generating financial reports, inspired by the "موقع جمع التبرعات" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_d52a4d089c2e0514
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict

class DonationSystem:
    """
    A class to represent an online donation system for a non-profit organization.
    """
    
    def __init__(self):
        """
        Initialize the donation system with an empty list of donations and donors.
        """
        self.donations = []  # List to store donation records
        self.donors = {}  # Dictionary to store donor information
    
    def add_donor(self, donor_id: str, name: str, email: str):
        """
        Adds a new donor to the system.
        
        :param donor_id: Unique identifier for the donor
        :param name: Name of the donor
        :param email: Email address of the donor
        """
        if donor_id in self.donors:
            raise ValueError("Donor ID already exists.")
        
        self.donors[donor_id] = {
            "name": name,
            "email": email,
            "total_donated": 0.0
        }
    
    def record_donation(self, donor_id: str, amount: float):
        """
        Records a donation made by a donor.
        
        :param donor_id: Unique identifier for the donor
        :param amount: Amount of the donation
        """
        if donor_id not in self.donors:
            raise ValueError("Donor ID does not exist.")
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        # Create a donation record
        donation = {
            "donor_id": donor_id,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.donations.append(donation)
        
        # Update donor's total donated amount
        self.donors[donor_id]["total_donated"] += amount
    
    def generate_financial_report(self) -> Dict[str, float]:
        """
        Generates a financial report summarizing donations.
        
        :return: A dictionary with total donations and donations by individual donors
        """
        total_donations = sum(donation["amount"] for donation in self.donations)
        donations_by_donor = {
            donor_id: donor_info["total_donated"]
            for donor_id, donor_info in self.donors.items()
        }
        
        return {
            "total_donations": total_donations,
            "donations_by_donor": donations_by_donor
        }
    
    def save_data_to_file(self, file_path: str):
        """
        Saves donation and donor data to a file in JSON format.
        
        :param file_path: Path to the file where data will be saved
        """
        try:
            data = {
                "donors": self.donors,
                "donations": self.donations
            }
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save data to file: {e}")
    
    def load_data_from_file(self, file_path: str):
        """
        Loads donation and donor data from a JSON file.
        
        :param file_path: Path to the file where data is stored
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.donors = data.get("donors", {})
                self.donations = data.get("donations", [])
        except Exception as e:
            raise IOError(f"Failed to load data from file: {e}")


# Example usage of the DonationSystem class
if __name__ == "__main__":
    system = DonationSystem()
    
    # Add donors
    system.add_donor("D001", "Alice Smith", "alice@example.com")
    system.add_donor("D002", "Bob Johnson", "bob@example.com")
    
    # Record donations
    system.record_donation("D001", 100.0)
    system.record_donation("D002", 50.0)
    system.record_donation("D001", 75.0)
    
    # Generate financial report
    report = system.generate_financial_report()
    print("Financial Report:")
    print(report)
    
    # Save data to file
    system.save_data_to_file("donation_data.json")
    
    # Load data from file
    new_system = DonationSystem()
    new_system.load_data_from_file("donation_data.json")
    print("Loaded Data:")
    print(new_system.generate_financial_report())
```
