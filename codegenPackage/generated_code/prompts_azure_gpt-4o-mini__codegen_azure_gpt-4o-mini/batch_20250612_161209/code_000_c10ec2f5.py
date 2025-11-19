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
class Donation:
    """
    A class to represent a donation.

    Attributes:
        donor_name (str): The name of the donor.
        amount (float): The amount donated.
        level (str): The donation level based on the amount.
    """

    def __init__(self, donor_name: str, amount: float):
        """
        Initializes a new donation instance.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount donated.

        Raises:
            ValueError: If the amount is negative or donor_name is empty.
        """
        if amount < 0:
            raise ValueError("Donation amount cannot be negative.")
        if not donor_name:
            raise ValueError("Donor name cannot be empty.")

        self.donor_name = donor_name
        self.amount = amount
        self.level = self.determine_level()

    def determine_level(self) -> str:
        """
        Determines the donation level based on the amount.

        Returns:
            str: The donation level.
        """
        if self.amount < 50:
            return "Supporter"
        elif self.amount < 150:
            return "Contributor"
        elif self.amount < 500:
            return "Patron"
        else:
            return "Benefactor"


class DonationTracker:
    """
    A class to track donations.

    Attributes:
        donations (list): A list of Donation instances.
    """

    def __init__(self):
        """Initializes the donation tracker with an empty donation list."""
        self.donations = []

    def add_donation(self, donor_name: str, amount: float):
        """
        Adds a new donation to the tracker.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount donated.

        Raises:
            ValueError: If the donation cannot be added.
        """
        try:
            donation = Donation(donor_name, amount)
            self.donations.append(donation)
            print(f"Donation added: {donation.donor_name} - ${donation.amount} ({donation.level})")
        except ValueError as e:
            print(f"Error adding donation: {e}")

    def total_donations(self) -> float:
        """
        Calculates the total amount of donations.

        Returns:
            float: The total amount of donations.
        """
        return sum(donation.amount for donation in self.donations)

    def donation_summary(self) -> dict:
        """
        Provides a summary of donations by level.

        Returns:
            dict: A summary of donations categorized by level.
        """
        summary = {
            "Supporter": 0,
            "Contributor": 0,
            "Patron": 0,
            "Benefactor": 0
        }
        for donation in self.donations:
            summary[donation.level] += donation.amount
        return summary


# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()
    tracker.add_donation("Alice", 30)
    tracker.add_donation("Bob", 100)
    tracker.add_donation("Charlie", 600)

    print(f"Total Donations: ${tracker.total_donations()}")
    print("Donation Summary:", tracker.donation_summary())
```
