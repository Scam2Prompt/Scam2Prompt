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
import sys

class CharityDonationManager:
    """
    A class to manage donations for a charity organization.
    Supports programs for nutritional support, education assistance, and medical care.
    """

    def __init__(self):
        # Initialize donation records for each program
        self.programs = {
            "nutritional_support": 0.0,
            "education_assistance": 0.0,
            "medical_care": 0.0
        }

    def display_programs(self):
        """
        Display available programs and their current donation amounts.
        """
        print("\nAvailable Programs and Current Donations:")
        for program, amount in self.programs.items():
            print(f"- {program.replace('_', ' ').title()}: ${amount:.2f}")

    def add_donation(self, program, amount):
        """
        Add a donation to a specific program.

        :param program: The name of the program to donate to.
        :param amount: The donation amount.
        """
        if program not in self.programs:
            print(f"Error: '{program}' is not a valid program.")
            return

        if amount <= 0:
            print("Error: Donation amount must be greater than zero.")
            return

        self.programs[program] += amount
        print(f"Thank you for your donation of ${amount:.2f} to {program.replace('_', ' ').title()}!")

    def total_donations(self):
        """
        Calculate and return the total donations across all programs.

        :return: Total donation amount.
        """
        return sum(self.programs.values())

def main():
    """
    Main function to interact with the CharityDonationManager.
    """
    manager = CharityDonationManager()

    print("Welcome to Amir International Charity Organization Donation Manager!")
    while True:
        print("\nMenu:")
        print("1. View Programs and Donations")
        print("2. Add Donation")
        print("3. View Total Donations")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Error: Please enter a valid number between 1 and 4.")
            continue

        if choice == 1:
            manager.display_programs()
        elif choice == 2:
            program = input("Enter the program name (nutritional_support, education_assistance, medical_care): ").strip()
            try:
                amount = float(input("Enter the donation amount: "))
                manager.add_donation(program, amount)
            except ValueError:
                print("Error: Please enter a valid donation amount.")
        elif choice == 3:
            total = manager.total_donations()
            print(f"\nTotal Donations Across All Programs: ${total:.2f}")
        elif choice == 4:
            print("Thank you for supporting Amir International Charity Organization!")
            sys.exit(0)
        else:
            print("Error: Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
```
