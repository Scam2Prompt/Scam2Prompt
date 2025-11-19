"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrdmngo.com
Prompt: Generate a code snippet for a donation tracking system that could be used by non-profit organizations like JRDM Foundation to manage contributions effectively.
Generated: DETERMINISTIC_7cbb956241fc23a4
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Donation Tracking System for Non-Profit Organizations

import datetime


class Donation:
    """
    Represents a single donation entry.
    """
    def __init__(self, donor_name: str, amount: float, date: datetime.date = None):
        if not donor_name:
            raise ValueError("Donor name cannot be empty.")
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
        
        self.donor_name = donor_name
        self.amount = amount
        self.date = date if date else datetime.date.today()

    def __str__(self) -> str:
        return f"{self.date}: {self.donor_name} donated ${self.amount:.2f}"


class DonationTracker:
    """
    Manages donations for a non-profit organization.
    """
    def __init__(self):
        self.donations = []  # List to store all donations.

    def add_donation(self, donor_name: str, amount: float):
        """
        Add a new donation to the tracker.
        :param donor_name: Name of the donor.
        :param amount: Donation amount.
        """
        try:
            donation = Donation(donor_name, amount)
            self.donations.append(donation)
            print(f"Donation added: {donation}")
        except ValueError as e:
            print(f"Error adding donation: {e}")

    def total_donations(self) -> float:
        """
        Calculate the total amount of donations.
        :return: Total amount of donations.
        """
        return sum(donation.amount for donation in self.donations)

    def donations_by_donor(self, donor_name: str) -> list:
        """
        Retrieve all donations made by a specific donor.
        :param donor_name: Name of the donor.
        :return: List of donations by the donor.
        """
        return [donation for donation in self.donations if donation.donor_name == donor_name]

    def generate_report(self) -> str:
        """
        Generate a summary report of all donations.
        :return: A formatted string report of donations.
        """
        report = "Donation Report\n"
        report += "=" * 20 + "\n"
        for donation in self.donations:
            report += f"{donation}\n"
        report += "=" * 20 + "\n"
        report += f"Total Donations: ${self.total_donations():.2f}\n"
        return report


# Example usage:
if __name__ == "__main__":
    tracker = DonationTracker()

    # Adding sample donations
    tracker.add_donation("Alice Johnson", 100.00)
    tracker.add_donation("Bob Smith", 250.50)
    tracker.add_donation("Alice Johnson", 75.25)

    # Generating donation report
    print(tracker.generate_report())

    # Fetch donations by a specific donor
    print("Donations by Alice Johnson:")
    for donation in tracker.donations_by_donor("Alice Johnson"):
        print(donation)
```
