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
from datetime import datetime

class DonationManager:
    """
    A class to manage donations for a non-profit organization.
    Tracks donors, donation amounts, and program allocations.
    """

    def __init__(self, data_file="donations.json"):
        """
        Initializes the DonationManager with a data file.
        :param data_file: Path to the JSON file for storing donation data.
        """
        self.data_file = data_file
        self.donations = self._load_data()

    def _load_data(self):
        """
        Loads donation data from the JSON file.
        :return: A dictionary containing donation data.
        """
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty data structure
            return {"donors": {}, "programs": {}}
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Unable to decode donation data file. Starting fresh.")
            return {"donors": {}, "programs": {}}

    def _save_data(self):
        """
        Saves donation data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.donations, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save donation data. {e}")

    def add_donor(self, name, email):
        """
        Adds a new donor to the system.
        :param name: Name of the donor.
        :param email: Email address of the donor.
        """
        if email in self.donations["donors"]:
            print("Error: Donor with this email already exists.")
            return

        self.donations["donors"][email] = {
            "name": name,
            "total_donated": 0,
            "donations": []
        }
        self._save_data()
        print(f"Donor '{name}' added successfully.")

    def add_program(self, program_name):
        """
        Adds a new program to the system.
        :param program_name: Name of the program.
        """
        if program_name in self.donations["programs"]:
            print("Error: Program already exists.")
            return

        self.donations["programs"][program_name] = {
            "total_received": 0,
            "donations": []
        }
        self._save_data()
        print(f"Program '{program_name}' added successfully.")

    def record_donation(self, email, amount, program_name):
        """
        Records a donation from a donor to a specific program.
        :param email: Email address of the donor.
        :param amount: Donation amount.
        :param program_name: Name of the program receiving the donation.
        """
        if email not in self.donations["donors"]:
            print("Error: Donor not found.")
            return

        if program_name not in self.donations["programs"]:
            print("Error: Program not found.")
            return

        if amount <= 0:
            print("Error: Donation amount must be positive.")
            return

        # Record donation for the donor
        donation_record = {
            "amount": amount,
            "program": program_name,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.donations["donors"][email]["donations"].append(donation_record)
        self.donations["donors"][email]["total_donated"] += amount

        # Record donation for the program
        self.donations["programs"][program_name]["donations"].append(donation_record)
        self.donations["programs"][program_name]["total_received"] += amount

        self._save_data()
        print(f"Donation of ${amount} recorded successfully.")

    def generate_report(self):
        """
        Generates a summary report of all donations.
        """
        print("\n--- Donation Report ---")
        print("Donors:")
        for email, donor in self.donations["donors"].items():
            print(f"  {donor['name']} ({email}) - Total Donated: ${donor['total_donated']}")
        
        print("\nPrograms:")
        for program_name, program in self.donations["programs"].items():
            print(f"  {program_name} - Total Received: ${program['total_received']}")
        print("-----------------------\n")

# Example usage
if __name__ == "__main__":
    manager = DonationManager()

    # Add donors
    manager.add_donor("Alice Johnson", "alice@example.com")
    manager.add_donor("Bob Smith", "bob@example.com")

    # Add programs
    manager.add_program("Education Fund")
    manager.add_program("Health Initiative")

    # Record donations
    manager.record_donation("alice@example.com", 100, "Education Fund")
    manager.record_donation("bob@example.com", 200, "Health Initiative")

    # Generate report
    manager.generate_report()
```
