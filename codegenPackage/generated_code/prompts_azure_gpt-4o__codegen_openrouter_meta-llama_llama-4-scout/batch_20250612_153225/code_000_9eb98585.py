"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Write Python code to simulate a donation system for an NGO like Perú Makers, including features for tracking donor information and donation amounts.
Generated: DETERMINISTIC_9eb985851386e8b7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_system.py

class Donor:
    """Represents a donor with their information and donation history."""

    def __init__(self, name, email):
        """
        Initializes a Donor object.

        Args:
            name (str): The donor's name.
            email (str): The donor's email address.
        """
        self.name = name
        self.email = email
        self.donations = []

    def add_donation(self, amount, date=None):
        """
        Adds a new donation to the donor's history.

        Args:
            amount (float): The donation amount.
            date (str, optional): The donation date. Defaults to None.

        Raises:
            ValueError: If the donation amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive")

        self.donations.append({"amount": amount, "date": date})

    def get_total_donations(self):
        """
        Calculates the total amount donated by the donor.

        Returns:
            float: The total donation amount.
        """
        return sum(donation["amount"] for donation in self.donations)

    def get_donation_history(self):
        """
        Retrieves the donor's donation history.

        Returns:
            list: A list of dictionaries containing donation information.
        """
        return self.donations


class DonationSystem:
    """Manages donor information and donation tracking."""

    def __init__(self):
        """
        Initializes a DonationSystem object.
        """
        self.donors = {}

    def add_donor(self, name, email):
        """
        Adds a new donor to the system.

        Args:
            name (str): The donor's name.
            email (str): The donor's email address.

        Raises:
            ValueError: If a donor with the same email already exists.
        """
        if email in self.donors:
            raise ValueError("Donor with this email already exists")

        self.donors[email] = Donor(name, email)

    def get_donor(self, email):
        """
        Retrieves a donor by their email address.

        Args:
            email (str): The donor's email address.

        Returns:
            Donor: The Donor object associated with the email.

        Raises:
            ValueError: If no donor with the given email exists.
        """
        try:
            return self.donors[email]
        except KeyError:
            raise ValueError("Donor not found")

    def record_donation(self, email, amount, date=None):
        """
        Records a new donation from a donor.

        Args:
            email (str): The donor's email address.
            amount (float): The donation amount.
            date (str, optional): The donation date. Defaults to None.

        Raises:
            ValueError: If the donor does not exist or the donation amount is invalid.
        """
        donor = self.get_donor(email)
        donor.add_donation(amount, date)


def main():
    # Example usage
    system = DonationSystem()

    system.add_donor("John Doe", "john@example.com")
    system.record_donation("john@example.com", 100.0, "2022-01-01")
    system.record_donation("john@example.com", 50.0, "2022-02-01")

    donor = system.get_donor("john@example.com")
    print(f"Donor: {donor.name} ({donor.email})")
    print("Donation History:")
    for donation in donor.get_donation_history():
        print(f"  - {donation['date']}: ${donation['amount']:.2f}")
    print(f"Total Donations: ${donor.get_total_donations():.2f}")


if __name__ == "__main__":
    main()
```
