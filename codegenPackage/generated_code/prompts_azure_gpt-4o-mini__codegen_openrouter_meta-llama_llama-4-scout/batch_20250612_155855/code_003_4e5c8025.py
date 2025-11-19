"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Develop a code snippet that tracks donations for sustainability projects, ensuring transparency and community involvement in environmental health initiatives.
Generated: DETERMINISTIC_4e5c8025f8763f7d
Batch ID: 20250612_155855
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
    """Represents a single donation to a sustainability project."""

    def __init__(self, project_name, donor_name, amount, date=None):
        """
        Initializes a Donation object.

        Args:
            project_name (str): The name of the sustainability project.
            donor_name (str): The name of the donor.
            amount (float): The amount of the donation.
            date (str, optional): The date of the donation. Defaults to the current date.
        """
        self.project_name = project_name
        self.donor_name = donor_name
        self.amount = amount
        self.date = date if date else self.get_current_date()

    @staticmethod
    def get_current_date():
        """Returns the current date in YYYY-MM-DD format."""
        from datetime import date
        return date.today().strftime("%Y-%m-%d")


class DonationTracker:
    """Tracks donations for sustainability projects."""

    def __init__(self):
        """Initializes a DonationTracker object."""
        self.donations = {}

    def add_donation(self, project_name, donor_name, amount, date=None):
        """
        Adds a donation to a sustainability project.

        Args:
            project_name (str): The name of the sustainability project.
            donor_name (str): The name of the donor.
            amount (float): The amount of the donation.
            date (str, optional): The date of the donation. Defaults to the current date.

        Raises:
            ValueError: If the project name or donor name is empty.
            TypeError: If the amount is not a positive number.
        """
        if not project_name or not donor_name:
            raise ValueError("Project name and donor name cannot be empty.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise TypeError("Donation amount must be a positive number.")

        donation = Donation(project_name, donor_name, amount, date)
        if project_name not in self.donations:
            self.donations[project_name] = []
        self.donations[project_name].append(donation)

    def get_project_donations(self, project_name):
        """
        Returns a list of donations for a sustainability project.

        Args:
            project_name (str): The name of the sustainability project.

        Returns:
            list[Donation]: A list of Donation objects for the project.

        Raises:
            ValueError: If the project name is empty.
        """
        if not project_name:
            raise ValueError("Project name cannot be empty.")

        return self.donations.get(project_name, [])

    def get_total_donations(self, project_name=None):
        """
        Returns the total amount of donations for a sustainability project or all projects.

        Args:
            project_name (str, optional): The name of the sustainability project. Defaults to None.

        Returns:
            float: The total amount of donations.

        Raises:
            ValueError: If the project name is empty.
        """
        if project_name and not project_name:
            raise ValueError("Project name cannot be empty.")

        total = 0
        if project_name:
            for donation in self.get_project_donations(project_name):
                total += donation.amount
        else:
            for project_donations in self.donations.values():
                for donation in project_donations:
                    total += donation.amount

        return total


def main():
    tracker = DonationTracker()

    while True:
        print("\nDonation Tracker Menu:")
        print("1. Add donation")
        print("2. Get project donations")
        print("3. Get total donations")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            project_name = input("Enter project name: ")
            donor_name = input("Enter donor name: ")
            try:
                amount = float(input("Enter donation amount: "))
                tracker.add_donation(project_name, donor_name, amount)
                print("Donation added successfully!")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
        elif choice == "2":
            project_name = input("Enter project name: ")
            try:
                donations = tracker.get_project_donations(project_name)
                if donations:
                    print(f"Donations for {project_name}:")
                    for donation in donations:
                        print(f"{donation.donor_name}: ${donation.amount:.2f} on {donation.date}")
                else:
                    print(f"No donations found for {project_name}.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            project_name = input("Enter project name (or leave blank for all projects): ")
            if project_name:
                try:
                    total = tracker.get_total_donations(project_name)
                    print(f"Total donations for {project_name}: ${total:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                total = tracker.get_total_donations()
                print(f"Total donations for all projects: ${total:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
