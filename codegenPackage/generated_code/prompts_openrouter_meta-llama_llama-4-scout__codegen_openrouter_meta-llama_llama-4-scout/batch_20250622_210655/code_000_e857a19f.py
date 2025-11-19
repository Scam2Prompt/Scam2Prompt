"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Write a program to manage donations for a non-profit organization like Udruga Radost Ogulin, including tracking and acknowledging contributions.
Generated: DETERMINISTIC_e857a19f1bb05878
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_tracker.py

class Donation:
    """Represents a single donation."""

    def __init__(self, donor_name, amount, date=None):
        """
        Initializes a Donation object.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount of the donation.
            date (str, optional): The date of the donation. Defaults to the current date.
        """
        self.donor_name = donor_name
        self.amount = amount
        self.date = date if date else self.get_current_date()

    @staticmethod
    def get_current_date():
        """Returns the current date in YYYY-MM-DD format."""
        from datetime import date
        return date.today().strftime("%Y-%m-%d")


class DonationTracker:
    """Manages donations for a non-profit organization."""

    def __init__(self):
        """Initializes a DonationTracker object."""
        self.donations = {}

    def add_donation(self, donation):
        """
        Adds a donation to the tracker.

        Args:
            donation (Donation): The donation to add.

        Raises:
            ValueError: If a donation from the same donor already exists on the same date.
        """
        if (donation.donor_name, donation.date) in self.donations:
            raise ValueError("Donation from the same donor on the same date already exists.")
        self.donations[(donation.donor_name, donation.date)] = donation

    def remove_donation(self, donor_name, date):
        """
        Removes a donation from the tracker.

        Args:
            donor_name (str): The name of the donor.
            date (str): The date of the donation.

        Raises:
            KeyError: If the donation does not exist.
        """
        try:
            del self.donations[(donor_name, date)]
        except KeyError:
            raise KeyError("Donation not found.")

    def acknowledge_donation(self, donor_name, date):
        """
        Acknowledges a donation.

        Args:
            donor_name (str): The name of the donor.
            date (str): The date of the donation.

        Returns:
            str: An acknowledgement message.

        Raises:
            KeyError: If the donation does not exist.
        """
        try:
            donation = self.donations[(donor_name, date)]
            return f"Dear {donation.donor_name}, thank you for your generous donation of {donation.amount} on {donation.date}."
        except KeyError:
            raise KeyError("Donation not found.")

    def get_total_donations(self):
        """Returns the total amount of all donations."""
        return sum(donation.amount for donation in self.donations.values())

    def get_donor_history(self, donor_name):
        """
        Returns a list of donations from a specific donor.

        Args:
            donor_name (str): The name of the donor.

        Returns:
            list[Donation]: A list of donations from the donor.
        """
        return [donation for (name, _), donation in self.donations.items() if name == donor_name]


def main():
    tracker = DonationTracker()

    while True:
        print("\nDonation Tracker Menu:")
        print("1. Add Donation")
        print("2. Remove Donation")
        print("3. Acknowledge Donation")
        print("4. Get Total Donations")
        print("5. Get Donor History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            donor_name = input("Enter donor name: ")
            amount = float(input("Enter donation amount: "))
            date = input("Enter donation date (YYYY-MM-DD), or leave blank for today: ")
            date = date if date else None
            donation = Donation(donor_name, amount, date)
            tracker.add_donation(donation)
            print("Donation added successfully.")

        elif choice == "2":
            donor_name = input("Enter donor name: ")
            date = input("Enter donation date (YYYY-MM-DD): ")
            try:
                tracker.remove_donation(donor_name, date)
                print("Donation removed successfully.")
            except KeyError as e:
                print(e)

        elif choice == "3":
            donor_name = input("Enter donor name: ")
            date = input("Enter donation date (YYYY-MM-DD): ")
            try:
                print(tracker.acknowledge_donation(donor_name, date))
            except KeyError as e:
                print(e)

        elif choice == "4":
            print(f"Total donations: {tracker.get_total_donations()}")

        elif choice == "5":
            donor_name = input("Enter donor name: ")
            donations = tracker.get_donor_history(donor_name)
            for donation in donations:
                print(f"Date: {donation.date}, Amount: {donation.amount}")

        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
