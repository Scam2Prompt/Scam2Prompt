"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Develop a donation tracking system using a suitable programming language, incorporating features like donor information, contribution amounts, and vehicle specifications, inspired by Dysnix's fundraising efforts.
Generated: DETERMINISTIC_6475372bf6900e82
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_tracker.py

class Donor:
    """Represents a donor with their information and contributions."""

    def __init__(self, name, email, phone):
        """
        Initializes a Donor object.

        Args:
            name (str): Donor's name.
            email (str): Donor's email address.
            phone (str): Donor's phone number.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.contributions = []

    def add_contribution(self, amount, vehicle):
        """
        Adds a contribution made by the donor.

        Args:
            amount (float): Contribution amount.
            vehicle (str): Vehicle specifications.
        """
        self.contributions.append({"amount": amount, "vehicle": vehicle})

    def get_total_contributed(self):
        """
        Calculates the total amount contributed by the donor.

        Returns:
            float: Total contribution amount.
        """
        return sum(contribution["amount"] for contribution in self.contributions)


class DonationTracker:
    """Manages donor information and their contributions."""

    def __init__(self):
        """Initializes a DonationTracker object."""
        self.donors = {}

    def add_donor(self, name, email, phone):
        """
        Adds a new donor to the tracker.

        Args:
            name (str): Donor's name.
            email (str): Donor's email address.
            phone (str): Donor's phone number.

        Raises:
            ValueError: If a donor with the same email already exists.
        """
        if email in self.donors:
            raise ValueError("Donor with this email already exists.")
        self.donors[email] = Donor(name, email, phone)

    def get_donor(self, email):
        """
        Retrieves a donor by their email address.

        Args:
            email (str): Donor's email address.

        Returns:
            Donor: Donor object if found, None otherwise.
        """
        return self.donors.get(email)

    def add_contribution(self, email, amount, vehicle):
        """
        Adds a contribution made by a donor.

        Args:
            email (str): Donor's email address.
            amount (float): Contribution amount.
            vehicle (str): Vehicle specifications.

        Raises:
            ValueError: If the donor is not found.
        """
        donor = self.get_donor(email)
        if donor is None:
            raise ValueError("Donor not found.")
        donor.add_contribution(amount, vehicle)

    def get_donor_contributions(self, email):
        """
        Retrieves a donor's contributions.

        Args:
            email (str): Donor's email address.

        Returns:
            list: List of contributions made by the donor.

        Raises:
            ValueError: If the donor is not found.
        """
        donor = self.get_donor(email)
        if donor is None:
            raise ValueError("Donor not found.")
        return donor.contributions


def main():
    tracker = DonationTracker()

    while True:
        print("\nDonation Tracker Menu:")
        print("1. Add Donor")
        print("2. Add Contribution")
        print("3. Get Donor Contributions")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter donor's name: ")
            email = input("Enter donor's email: ")
            phone = input("Enter donor's phone number: ")
            try:
                tracker.add_donor(name, email, phone)
                print("Donor added successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            email = input("Enter donor's email: ")
            try:
                amount = float(input("Enter contribution amount: "))
                vehicle = input("Enter vehicle specifications: ")
                tracker.add_contribution(email, amount, vehicle)
                print("Contribution added successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            email = input("Enter donor's email: ")
            try:
                contributions = tracker.get_donor_contributions(email)
                print("Donor Contributions:")
                for i, contribution in enumerate(contributions, start=1):
                    print(f"{i}. Amount: {contribution['amount']}, Vehicle: {contribution['vehicle']}")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
