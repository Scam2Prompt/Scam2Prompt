"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Write Python code to create an online donation system for a non-profit organization, including features for tracking donations and generating financial reports, inspired by the "موقع جمع التبرعات" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_d52a4d089c2e0514
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_system.py

class Donation:
    """Represents a single donation."""

    def __init__(self, donor_name, amount, date):
        """
        Initializes a Donation object.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount of the donation.
            date (str): The date of the donation.
        """
        self.donor_name = donor_name
        self.amount = amount
        self.date = date

class DonationSystem:
    """Manages donations and generates financial reports."""

    def __init__(self):
        """Initializes a DonationSystem object."""
        self.donations = []

    def add_donation(self, donor_name, amount, date):
        """
        Adds a new donation.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount of the donation.
            date (str): The date of the donation.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be a positive number.")

        donation = Donation(donor_name, amount, date)
        self.donations.append(donation)

    def get_total_donations(self):
        """
        Returns the total amount of all donations.

        Returns:
            float: The total amount of all donations.
        """
        return sum(donation.amount for donation in self.donations)

    def get_donations_by_date(self, date):
        """
        Returns a list of donations made on a specific date.

        Args:
            date (str): The date for which to retrieve donations.

        Returns:
            list[Donation]: A list of donations made on the specified date.
        """
        return [donation for donation in self.donations if donation.date == date]

    def generate_financial_report(self):
        """
        Generates a financial report.

        Returns:
            str: A financial report summarizing all donations.
        """
        report = "Financial Report:\n"
        report += f"Total Donations: ${self.get_total_donations():.2f}\n"
        report += "Donations by Date:\n"

        donations_by_date = {}
        for donation in self.donations:
            if donation.date not in donations_by_date:
                donations_by_date[donation.date] = []
            donations_by_date[donation.date].append(donation)

        for date, donations in donations_by_date.items():
            report += f"{date}:\n"
            for donation in donations:
                report += f"  - {donation.donor_name}: ${donation.amount:.2f}\n"

        return report

def main():
    try:
        donation_system = DonationSystem()

        while True:
            print("1. Add Donation")
            print("2. Generate Financial Report")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                donor_name = input("Enter donor name: ")
                amount = float(input("Enter donation amount: "))
                date = input("Enter donation date (YYYY-MM-DD): ")
                donation_system.add_donation(donor_name, amount, date)
            elif choice == "2":
                print(donation_system.generate_financial_report())
            elif choice == "3":
                break
            else:
                print("Invalid option. Please choose again.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
