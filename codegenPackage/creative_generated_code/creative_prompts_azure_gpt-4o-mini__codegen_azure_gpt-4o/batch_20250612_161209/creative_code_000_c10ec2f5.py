"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waldoenruta.com
Prompt: Generate a code snippet for a donation tracking system that supports multiple donation levels, inspired by Waldo en Ruta's fundraising for his cycling journey across Chile.
Generated: DETERMINISTIC_c10ec2f5c20a6661
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Donation:
    """
    Class to represent a single donation.
    """
    def __init__(self, donor_name, amount, donation_level):
        """
        Initialize a Donation instance.
        :param donor_name: str - Name of the donor.
        :param amount: float - Donation amount.
        :param donation_level: str - Level of donation (e.g., Bronze, Silver, Gold).
        """
        self.donor_name = donor_name
        self.amount = amount
        self.donation_level = donation_level
        self.date = datetime.datetime.now()

    def __str__(self):
        """
        String representation of the donation.
        """
        return f"Donation from {self.donor_name}: ${self.amount:.2f} ({self.donation_level}) on {self.date.strftime('%Y-%m-%d')}"

class DonationTracker:
    """
    Class to track multiple donations and categorize them by levels.
    """
    def __init__(self):
        """
        Initialize a DonationTracker instance.
        """
        self.donations = []
        self.donation_levels = {
            "Bronze": (0, 49),
            "Silver": (50, 99),
            "Gold": (100, float('inf'))
        }

    def add_donation(self, donor_name, amount):
        """
        Add a donation to the system.
        :param donor_name: str - Name of the donor.
        :param amount: float - Donation amount.
        :raises ValueError: If the donation amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")

        # Determine donation level based on amount
        donation_level = self.get_donation_level(amount)
        donation = Donation(donor_name, amount, donation_level)
        self.donations.append(donation)

    def get_donation_level(self, amount):
        """
        Determine the donation level based on the amount.
        :param amount: float - Donation amount.
        :return: str - Donation level.
        """
        for level, (min_amount, max_amount) in self.donation_levels.items():
            if min_amount <= amount <= max_amount:
                return level
        return "Unknown"

    def get_all_donations(self):
        """
        Retrieve all donations.
        :return: list - List of all donations.
        """
        return self.donations

    def get_total_donations(self):
        """
        Calculate the total amount of donations.
        :return: float - Total donation amount.
        """
        return sum(donation.amount for donation in self.donations)

    def print_donations_summary(self):
        """
        Print a summary of all donations.
        """
        print("Donations Summary:")
        for donation in self.donations:
            print(donation)
        print(f"Total Donations: ${self.get_total_donations():.2f}")


# Example usage:
if __name__ == "__main__":
    tracker = DonationTracker()

    try:
        tracker.add_donation("Alice", 25)
        tracker.add_donation("Bob", 75)
        tracker.add_donation("Charlie", 150)
    except ValueError as e:
        print(f"Error: {e}")

    tracker.print_donations_summary()
```
