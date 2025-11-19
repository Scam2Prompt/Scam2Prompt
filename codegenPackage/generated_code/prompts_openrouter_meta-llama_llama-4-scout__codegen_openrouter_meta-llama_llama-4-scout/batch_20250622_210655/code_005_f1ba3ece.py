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
# donation_management_system.py

from datetime import datetime
from typing import Dict, List

class Donation:
    """Represents a single donation."""

    def __init__(self, donor_name: str, amount: float, date: datetime):
        """
        Initializes a Donation object.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount donated.
            date (datetime): The date of the donation.
        """
        self.donor_name = donor_name
        self.amount = amount
        self.date = date

class Fund:
    """Represents a fund for a specific cause."""

    def __init__(self, name: str):
        """
        Initializes a Fund object.

        Args:
            name (str): The name of the fund.
        """
        self.name = name
        self.donations: List[Donation] = []
        self.total_amount = 0.0

    def add_donation(self, donation: Donation):
        """
        Adds a donation to the fund.

        Args:
            donation (Donation): The donation to add.
        """
        self.donations.append(donation)
        self.total_amount += donation.amount

    def get_donations(self) -> List[Donation]:
        """
        Returns a list of donations in the fund.

        Returns:
            List[Donation]: A list of donations.
        """
        return self.donations

class DonationManagementSystem:
    """Manages donations and financial support for a humanitarian organization."""

    def __init__(self):
        """
        Initializes a DonationManagementSystem object.
        """
        self.funds: Dict[str, Fund] = {}

    def create_fund(self, name: str):
        """
        Creates a new fund.

        Args:
            name (str): The name of the fund.

        Raises:
            ValueError: If a fund with the same name already exists.
        """
        if name in self.funds:
            raise ValueError("Fund already exists")
        self.funds[name] = Fund(name)

    def add_donation(self, fund_name: str, donor_name: str, amount: float):
        """
        Adds a donation to a fund.

        Args:
            fund_name (str): The name of the fund.
            donor_name (str): The name of the donor.
            amount (float): The amount donated.

        Raises:
            ValueError: If the fund does not exist.
        """
        if fund_name not in self.funds:
            raise ValueError("Fund does not exist")
        fund = self.funds[fund_name]
        donation = Donation(donor_name, amount, datetime.now())
        fund.add_donation(donation)

    def get_fund_info(self, fund_name: str) -> Dict:
        """
        Returns information about a fund.

        Args:
            fund_name (str): The name of the fund.

        Returns:
            Dict: A dictionary containing fund information.

        Raises:
            ValueError: If the fund does not exist.
        """
        if fund_name not in self.funds:
            raise ValueError("Fund does not exist")
        fund = self.funds[fund_name]
        return {
            "name": fund.name,
            "total_amount": fund.total_amount,
            "donations": [
                {"donor_name": donation.donor_name, "amount": donation.amount, "date": donation.date}
                for donation in fund.get_donations()
            ],
        }

def main():
    # Example usage
    system = DonationManagementSystem()

    try:
        system.create_fund("Disaster Relief")
        system.add_donation("Disaster Relief", "John Doe", 100.0)
        system.add_donation("Disaster Relief", "Jane Doe", 50.0)

        fund_info = system.get_fund_info("Disaster Relief")
        print(fund_info)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
