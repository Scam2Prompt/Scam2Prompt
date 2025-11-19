"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Write a Python script to manage donations for a non-profit organization like NICER Foundation, including tracking donors, amounts, and program allocations.
Generated: DETERMINISTIC_149f27fd97cd752c
Batch ID: 20250622_205459
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

class DonationManager:
    def __init__(self, data_file: str):
        """
        Initializes the DonationManager with a specified data file.
        
        :param data_file: Path to the JSON file where donation data will be stored.
        """
        self.data_file = data_file
        self.donations = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Loads donation data from the JSON file.
        
        :return: A list of donations.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted or invalid.")
            return []

    def save_data(self) -> None:
        """
        Saves the current donations data to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.donations, file, indent=4)

    def add_donation(self, donor_name: str, amount: float, program: str) -> None:
        """
        Adds a new donation to the list and saves it to the file.
        
        :param donor_name: Name of the donor.
        :param amount: Amount donated.
        :param program: Program to which the donation is allocated.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        donation = {
            "donor_name": donor_name,
            "amount": amount,
            "program": program
        }
        self.donations.append(donation)
        self.save_data()

    def get_donations(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of all donations.
        
        :return: A list of donations.
        """
        return self.donations

    def get_total_donations(self) -> float:
        """
        Calculates the total amount of donations received.
        
        :return: Total donation amount.
        """
        return sum(donation['amount'] for donation in self.donations)

    def get_donations_by_program(self, program: str) -> List[Dict[str, Any]]:
        """
        Retrieves donations allocated to a specific program.
        
        :param program: The program to filter donations by.
        :return: A list of donations for the specified program.
        """
        return [donation for donation in self.donations if donation['program'] == program]

def main():
    # Initialize the DonationManager with the path to the data file
    donation_manager = DonationManager('donations.json')

    # Example usage
    try:
        donation_manager.add_donation("Alice Smith", 100.0, "Education")
        donation_manager.add_donation("Bob Johnson", 50.0, "Health")
        
        print("Total Donations:", donation_manager.get_total_donations())
        print("All Donations:", donation_manager.get_donations())
        print("Education Donations:", donation_manager.get_donations_by_program("Education"))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
