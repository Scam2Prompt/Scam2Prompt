"""
Generated Code Metadata:
========================
Original URL: https://waldoenruta.com
Prompt: Generate a code snippet for a donation tracking system that supports multiple donation levels, inspired by Waldo en Ruta's fundraising for his cycling journey across Chile.
Generated: DETERMINISTIC_c10ec2f5c20a6661
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Donation:
    """
    Represents a single donation.
    """
    def __init__(self, donor_name, amount, level):
        """
        Initializes a Donation instance.

        :param donor_name: Name of the donor
        :param amount: Donation amount
        :param level: Donation level (e.g., Bronze, Silver, Gold)
        """
        self.donor_name = donor_name
        self.amount = amount
        self.level = level
        self.date = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the donation.
        """
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.donor_name} donated ${self.amount:.2f} ({self.level})"


class DonationTracker:
    """
    Tracks donations and categorizes them by levels.
    """
    def __init__(self):
        """
        Initializes the DonationTracker instance.
        """
        self.donations = []  # List to store all donations
        self.levels = {
            "Bronze": (0, 50),
            "Silver": (51, 100),
            "Gold": (101, float('inf'))
        }

    def determine_level(self, amount):
        """
        Determines the donation level based on the amount.

        :param amount: Donation amount
        :return: Donation level as a string
        """
        for level, (min_amount, max_amount) in self.levels.items():
            if min_amount <= amount <= max_amount:
                return level
        return "Unknown"

    def add_donation(self, donor_name, amount):
        """
        Adds a new donation to the tracker.

        :param donor_name: Name of the donor
        :param amount: Donation amount
        :raises ValueError: If the donation amount is invalid
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        level = self.determine_level(amount)
        donation = Donation(donor_name, amount, level)
        self.donations.append(donation)

    def get_donations_by_level(self, level):
        """
        Retrieves all donations for a specific level.

        :param level: Donation level (e.g., Bronze, Silver, Gold)
        :return: List of donations for the specified level
        """
        return [donation for donation in self.donations if donation.level == level]

    def display_all_donations(self):
        """
        Displays all donations in the tracker.
        """
        if not self.donations:
            print("No donations have been made yet.")
            return

        print("All Donations:")
        for donation in self.donations:
            print(donation)


# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()

    try:
        tracker.add_donation("Alice", 25)
        tracker.add_donation("Bob", 75)
        tracker.add_donation("Charlie", 150)
    except ValueError as e:
        print(f"Error: {e}")

    tracker.display_all_donations()

    print("\nGold Level Donations:")
    gold_donations = tracker.get_donations_by_level("Gold")
    for donation in gold_donations:
        print(donation)
```
