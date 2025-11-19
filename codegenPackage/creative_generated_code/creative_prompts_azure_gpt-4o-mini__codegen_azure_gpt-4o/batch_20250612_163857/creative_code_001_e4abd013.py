"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://standrewsibanda.org
Prompt: Can you provide a code snippet for a donation tracking system that could be used by community-based organizations like St. Andrew’s School Project for The Young?
Generated: DETERMINISTIC_e4abd0130f88554e
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# donation_tracker.py
# A donation tracking system for community-based organizations.
# Author: [Your Name]
# Date: [Date]

import datetime


class Donation:
    """
    Class representing a single donation.
    """

    def __init__(self, donor_name: str, amount: float, date: datetime.date = None):
        """
        Initializes a Donation instance.

        :param donor_name: Name of the donor.
        :param amount: Amount donated (must be positive).
        :param date: Date of the donation. Defaults to today.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        self.donor_name = donor_name
        self.amount = amount
        self.date = date or datetime.date.today()

    def __str__(self):
        """
        Returns a string representation of the donation.

        :return: String representation.
        """
        return f"Donation from {self.donor_name} of ${self.amount:.2f} on {self.date}"


class DonationTracker:
    """
    Class for tracking donations to a community-based organization.
    """

    def __init__(self, organization_name: str):
        """
        Initializes a DonationTracker instance.

        :param organization_name: Name of the organization.
        """
        self.organization_name = organization_name
        self.donations = []

    def add_donation(self, donor_name: str, amount: float):
        """
        Adds a new donation to the tracker.

        :param donor_name: Name of the donor.
        :param amount: Amount donated.
        :raises ValueError: If donation data is invalid.
        """
        try:
            donation = Donation(donor_name, amount)
            self.donations.append(donation)
            print(f"Donation added: {donation}")
        except ValueError as e:
            print(f"Error adding donation: {e}")

    def total_donations(self) -> float:
        """
        Calculates the total amount of donations.

        :return: Total donation amount.
        """
        return sum(donation.amount for donation in self.donations)

    def list_donations(self):
        """
        Lists all donations.

        :return: List of donations as strings.
        """
        if not self.donations:
            print("No donations have been made yet.")
        else:
            print(f"Donations for {self.organization_name}:")
            for donation in self.donations:
                print(donation)


# Example usage (uncomment the lines below to test the system):
if __name__ == "__main__":
    tracker = DonationTracker("St. Andrew’s School Project for The Young")

    # Add a few donations
    tracker.add_donation("John Doe", 50)
    tracker.add_donation("Jane Smith", 100)
    tracker.add_donation("Mary Johnson", -10)  # This will trigger an error

    # List donations
    tracker.list_donations()

    # Display total donations
    print(f"Total donations: ${tracker.total_donations():.2f}")
```
