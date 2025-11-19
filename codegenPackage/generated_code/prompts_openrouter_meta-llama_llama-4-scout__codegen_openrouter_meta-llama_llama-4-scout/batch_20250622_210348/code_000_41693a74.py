"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Write a Python script to manage donations for a charity organization like Amir International Charity Organization, which has programs for nutritional support, education assistance, and medical care.
Generated: DETERMINISTIC_41693a74a32c3a49
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_manager.py

class Donation:
    """Represents a single donation."""

    def __init__(self, donor_name, amount, program):
        """
        Initializes a Donation object.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount donated.
            program (str): The program the donation is for (e.g., nutritional support, education assistance, medical care).
        """
        self.donor_name = donor_name
        self.amount = amount
        self.program = program

class CharityOrganization:
    """Represents a charity organization with multiple programs."""

    def __init__(self, name):
        """
        Initializes a CharityOrganization object.

        Args:
            name (str): The name of the charity organization.
        """
        self.name = name
        self.programs = {}
        self.donations = []

    def add_program(self, program_name):
        """
        Adds a new program to the charity organization.

        Args:
            program_name (str): The name of the program.

        Raises:
            ValueError: If the program already exists.
        """
        if program_name in self.programs:
            raise ValueError(f"Program '{program_name}' already exists.")
        self.programs[program_name] = 0.0

    def remove_program(self, program_name):
        """
        Removes a program from the charity organization.

        Args:
            program_name (str): The name of the program.

        Raises:
            ValueError: If the program does not exist.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program '{program_name}' does not exist.")
        del self.programs[program_name]

    def make_donation(self, donor_name, amount, program):
        """
        Records a new donation.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount donated.
            program (str): The program the donation is for.

        Raises:
            ValueError: If the program does not exist or the amount is invalid.
        """
        if program not in self.programs:
            raise ValueError(f"Program '{program}' does not exist.")
        if amount <= 0:
            raise ValueError("Invalid donation amount.")

        self.programs[program] += amount
        self.donations.append(Donation(donor_name, amount, program))

    def get_program_balance(self, program_name):
        """
        Gets the current balance for a program.

        Args:
            program_name (str): The name of the program.

        Returns:
            float: The current balance for the program.

        Raises:
            ValueError: If the program does not exist.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program '{program_name}' does not exist.")
        return self.programs[program_name]

    def get_all_donations(self):
        """
        Gets a list of all donations.

        Returns:
            list[Donation]: A list of all donations.
        """
        return self.donations

def main():
    # Create a charity organization
    charity = CharityOrganization("Amir International Charity Organization")

    # Add programs
    charity.add_program("Nutritional Support")
    charity.add_program("Education Assistance")
    charity.add_program("Medical Care")

    try:
        # Make donations
        charity.make_donation("John Doe", 100.0, "Nutritional Support")
        charity.make_donation("Jane Doe", 50.0, "Education Assistance")
        charity.make_donation("Bob Smith", 200.0, "Medical Care")

        # Get program balances
        print("Program Balances:")
        for program, balance in charity.programs.items():
            print(f"{program}: ${balance:.2f}")

        # Get all donations
        print("\nAll Donations:")
        for donation in charity.get_all_donations():
            print(f"Donor: {donation.donor_name}, Amount: ${donation.amount:.2f}, Program: {donation.program}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
