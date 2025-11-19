"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Write Python code to create a donation tracking system for an NGO, inspired by Youngistaan Foundation's initiatives like "Sponsor Our Talented Children" and "Hunger Hero Program."
Generated: DETERMINISTIC_a0de0a28058bdc1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_tracking_system.py

class Donor:
    """Represents a donor in the system."""

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

    def add_donation(self, donation):
        """
        Adds a donation to the donor's record.

        Args:
            donation (Donation): The donation to add.
        """
        self.donations.append(donation)


class Donation:
    """Represents a donation in the system."""

    def __init__(self, amount, program, date):
        """
        Initializes a Donation object.

        Args:
            amount (float): The donation amount.
            program (str): The program the donation is for (e.g., "Sponsor Our Talented Children").
            date (str): The date of the donation.
        """
        self.amount = amount
        self.program = program
        self.date = date


class Program:
    """Represents a program in the system."""

    def __init__(self, name, goal):
        """
        Initializes a Program object.

        Args:
            name (str): The program's name.
            goal (float): The program's fundraising goal.
        """
        self.name = name
        self.goal = goal
        self.collected = 0

    def add_donation(self, donation):
        """
        Adds a donation to the program's total.

        Args:
            donation (Donation): The donation to add.
        """
        if donation.program == self.name:
            self.collected += donation.amount
        else:
            raise ValueError("Donation is not for this program")

    def __str__(self):
        return f"{self.name}: ${self.collected:.2f} / ${self.goal:.2f}"


class DonationTrackingSystem:
    """Represents the donation tracking system."""

    def __init__(self):
        self.donors = {}
        self.programs = {}

    def add_donor(self, donor):
        """
        Adds a donor to the system.

        Args:
            donor (Donor): The donor to add.
        """
        self.donors[donor.email] = donor

    def add_program(self, program):
        """
        Adds a program to the system.

        Args:
            program (Program): The program to add.
        """
        self.programs[program.name] = program

    def make_donation(self, donor_email, amount, program_name, date):
        """
        Records a donation in the system.

        Args:
            donor_email (str): The email of the donor making the donation.
            amount (float): The donation amount.
            program_name (str): The name of the program the donation is for.
            date (str): The date of the donation.

        Raises:
            ValueError: If the donor or program is not found.
        """
        if donor_email not in self.donors:
            raise ValueError("Donor not found")
        if program_name not in self.programs:
            raise ValueError("Program not found")

        donor = self.donors[donor_email]
        program = self.programs[program_name]
        donation = Donation(amount, program_name, date)
        donor.add_donation(donation)
        program.add_donation(donation)

    def get_program_status(self, program_name):
        """
        Gets the status of a program.

        Args:
            program_name (str): The name of the program.

        Returns:
            str: The program's status.

        Raises:
            ValueError: If the program is not found.
        """
        if program_name not in self.programs:
            raise ValueError("Program not found")
        return str(self.programs[program_name])

    def get_donor_history(self, donor_email):
        """
        Gets a donor's donation history.

        Args:
            donor_email (str): The email of the donor.

        Returns:
            list: The donor's donations.

        Raises:
            ValueError: If the donor is not found.
        """
        if donor_email not in self.donors:
            raise ValueError("Donor not found")
        return self.donors[donor_email].donations


def main():
    system = DonationTrackingSystem()

    # Create programs
    program1 = Program("Sponsor Our Talented Children", 10000)
    program2 = Program("Hunger Hero Program", 5000)
    system.add_program(program1)
    system.add_program(program2)

    # Create donors
    donor1 = Donor("John Doe", "john@example.com")
    donor2 = Donor("Jane Doe", "jane@example.com")
    system.add_donor(donor1)
    system.add_donor(donor2)

    # Make donations
    system.make_donation("john@example.com", 1000, "Sponsor Our Talented Children", "2022-01-01")
    system.make_donation("jane@example.com", 500, "Hunger Hero Program", "2022-01-15")
    system.make_donation("john@example.com", 2000, "Sponsor Our Talented Children", "2022-02-01")

    # Print program status
    print(system.get_program_status("Sponsor Our Talented Children"))
    print(system.get_program_status("Hunger Hero Program"))

    # Print donor history
    donations = system.get_donor_history("john@example.com")
    for donation in donations:
        print(f"Donation to {donation.program} on {donation.date}: ${donation.amount:.2f}")


if __name__ == "__main__":
    main()
```
