"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Write Python code to create a donation tracking system for an NGO, inspired by Youngistaan Foundation's initiatives like "Sponsor Our Talented Children" and "Hunger Hero Program."
Generated: DETERMINISTIC_a0de0a28058bdc1c
Batch ID: 20250612_153246
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
    Attributes:
        donor_name (str): Name of the donor.
        donor_email (str): Email of the donor.
        program (str): The program the donation is for.
        amount (float): Amount donated.
        donation_date (datetime): Date of the donation.
    """
    def __init__(self, donor_name, donor_email, program, amount):
        self.donor_name = donor_name
        self.donor_email = donor_email
        self.program = program
        self.amount = amount
        self.donation_date = datetime.datetime.now()

    def __str__(self):
        """
        String representation of the donation.
        """
        return f"Donation from {self.donor_name} ({self.donor_email}) for '{self.program}' - Amount: ${self.amount:.2f} on {self.donation_date.strftime('%Y-%m-%d %H:%M:%S')}"


class DonationTracker:
    """
    Class to track donations for an NGO.
    Attributes:
        donations (list): List of all donations.
    Methods:
        add_donation: Add a new donation to the system.
        list_donations: List all donations.
        total_donations: Get the total amount donated.
        filter_donations_by_program: Get donations for a specific program.
    """
    def __init__(self):
        self.donations = []

    def add_donation(self, donor_name, donor_email, program, amount):
        """
        Add a new donation to the system.
        Args:
            donor_name (str): Name of the donor.
            donor_email (str): Email of the donor.
            program (str): The program the donation is for.
            amount (float): Amount donated.
        """
        try:
            if amount <= 0:
                raise ValueError("Donation amount must be greater than 0.")
            new_donation = Donation(donor_name, donor_email, program, amount)
            self.donations.append(new_donation)
            print(f"Donation successfully added: {new_donation}")
        except ValueError as e:
            print(f"Error adding donation: {e}")

    def list_donations(self):
        """
        List all donations.
        """
        if not self.donations:
            print("No donations recorded yet.")
            return

        print("All Donations:")
        for donation in self.donations:
            print(donation)

    def total_donations(self):
        """
        Get the total amount donated across all programs.
        Returns:
            float: Total donation amount.
        """
        total = sum(donation.amount for donation in self.donations)
        print(f"Total Donations: ${total:.2f}")
        return total

    def filter_donations_by_program(self, program):
        """
        Get donations for a specific program.
        Args:
            program (str): The name of the program.
        Returns:
            list: List of donations for the specified program.
        """
        filtered_donations = [donation for donation in self.donations if donation.program.lower() == program.lower()]
        if not filtered_donations:
            print(f"No donations found for the program '{program}'.")
        else:
            print(f"Donations for '{program}':")
            for donation in filtered_donations:
                print(donation)
        return filtered_donations


# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()

    # Adding donations
    tracker.add_donation("Alice", "alice@example.com", "Sponsor Our Talented Children", 100)
    tracker.add_donation("Bob", "bob@example.com", "Hunger Hero Program", 50)
    tracker.add_donation("Charlie", "charlie@example.com", "Sponsor Our Talented Children", 200)

    # Listing all donations
    tracker.list_donations()

    # Total donations
    tracker.total_donations()

    # Filtering donations by program
    tracker.filter_donations_by_program("Sponsor Our Talented Children")
    tracker.filter_donations_by_program("Hunger Hero Program")
```
