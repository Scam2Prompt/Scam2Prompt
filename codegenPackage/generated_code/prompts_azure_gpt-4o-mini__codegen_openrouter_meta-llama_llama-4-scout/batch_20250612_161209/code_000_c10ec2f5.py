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
# donation_tracker.py

class DonationLevel:
    """Represents a donation level with a name and a minimum amount."""

    def __init__(self, name, min_amount):
        """
        Initializes a DonationLevel.

        Args:
            name (str): The name of the donation level.
            min_amount (float): The minimum amount required for this level.
        """
        self.name = name
        self.min_amount = min_amount

class DonationTracker:
    """Tracks donations and supports multiple donation levels."""

    def __init__(self):
        """Initializes a DonationTracker with an empty list of donations and default donation levels."""
        self.donations = []
        self.donation_levels = [
            DonationLevel("Ciclista Solidario", 1000),
            DonationLevel("Acompañante", 5000),
            DonationLevel("Patrocinador", 10000),
            DonationLevel("Colaborador", 20000)
        ]

    def add_donation(self, amount, donor_name):
        """
        Adds a donation to the tracker.

        Args:
            amount (float): The amount donated.
            donor_name (str): The name of the donor.

        Raises:
            ValueError: If the donation amount is negative.
        """
        if amount < 0:
            raise ValueError("Donation amount cannot be negative")

        self.donations.append({"amount": amount, "donor_name": donor_name})

    def get_donation_levels(self):
        """Returns the list of donation levels."""
        return self.donation_levels

    def get_total_donations(self):
        """Returns the total amount donated."""
        return sum(donation["amount"] for donation in self.donations)

    def get_donor_ranking(self):
        """Returns a list of donors ranked by their donation amount."""
        return sorted(self.donations, key=lambda x: x["amount"], reverse=True)

    def check_donation_level(self, donor_name):
        """
        Checks the donation level of a donor.

        Args:
            donor_name (str): The name of the donor.

        Returns:
            str: The name of the donation level if found, otherwise None.
        """
        donor_donations = [donation for donation in self.donations if donation["donor_name"] == donor_name]
        if not donor_donations:
            return None

        total_donated = sum(donation["amount"] for donation in donor_donations)
        for level in self.donation_levels:
            if total_donated >= level.min_amount:
                return level.name

        return "Donante"

def main():
    tracker = DonationTracker()

    while True:
        print("\nDonation Tracker Menu:")
        print("1. Add donation")
        print("2. View donation levels")
        print("3. View total donations")
        print("4. View donor ranking")
        print("5. Check donation level")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter donation amount: "))
            donor_name = input("Enter donor name: ")
            try:
                tracker.add_donation(amount, donor_name)
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            print("\nDonation Levels:")
            for i, level in enumerate(tracker.get_donation_levels()):
                print(f"{i+1}. {level.name} - ${level.min_amount}")
        elif choice == "3":
            print(f"\nTotal Donations: ${tracker.get_total_donations():.2f}")
        elif choice == "4":
            print("\nDonor Ranking:")
            for i, donor in enumerate(tracker.get_donor_ranking()):
                print(f"{i+1}. {donor['donor_name']} - ${donor['amount']:.2f}")
        elif choice == "5":
            donor_name = input("Enter donor name: ")
            level = tracker.check_donation_level(donor_name)
            if level:
                print(f"\nDonation Level: {level}")
            else:
                print("\nDonor not found")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
