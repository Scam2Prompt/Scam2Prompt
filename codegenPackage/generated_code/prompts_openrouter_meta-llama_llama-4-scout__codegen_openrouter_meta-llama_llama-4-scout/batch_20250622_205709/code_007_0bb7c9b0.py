"""
Generated Code Metadata:
========================
Original URL: https://itaunaalerta.com.br
Prompt: Develop a fundraising appeal for a local cause, such as helping a resident with urgent medical needs.
Generated: DETERMINISTIC_0bb7c9b00df67bd0
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fundraising_appeal.py

class Donation:
    """Represents a single donation."""

    def __init__(self, amount, donor_name):
        """
        Initializes a Donation object.

        Args:
            amount (float): The donation amount.
            donor_name (str): The donor's name.
        """
        self.amount = amount
        self.donor_name = donor_name

class FundraisingAppeal:
    """Manages a fundraising appeal."""

    def __init__(self, cause, goal):
        """
        Initializes a FundraisingAppeal object.

        Args:
            cause (str): The cause of the fundraising appeal.
            goal (float): The fundraising goal.
        """
        self.cause = cause
        self.goal = goal
        self.donations = []

    def add_donation(self, donation):
        """
        Adds a donation to the fundraising appeal.

        Args:
            donation (Donation): The donation to add.

        Raises:
            ValueError: If the donation amount is negative.
        """
        if donation.amount < 0:
            raise ValueError("Donation amount cannot be negative")
        self.donations.append(donation)

    def get_total_raised(self):
        """
        Calculates the total amount raised.

        Returns:
            float: The total amount raised.
        """
        return sum(donation.amount for donation in self.donations)

    def get_progress(self):
        """
        Calculates the progress towards the fundraising goal.

        Returns:
            float: The progress as a percentage.
        """
        total_raised = self.get_total_raised()
        return (total_raised / self.goal) * 100 if self.goal > 0 else 0

def main():
    # Create a fundraising appeal for a local cause
    appeal = FundraisingAppeal("Help a resident with urgent medical needs", 10000)

    while True:
        print("\n1. Make a donation")
        print("2. View total raised")
        print("3. View progress")
        print("4. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                amount = float(input("Enter donation amount: "))
                donor_name = input("Enter your name: ")
                donation = Donation(amount, donor_name)
                appeal.add_donation(donation)
                print(f"Thank you, {donor_name}, for your donation of ${amount:.2f}!")
            elif choice == "2":
                print(f"Total raised: ${appeal.get_total_raised():.2f}")
            elif choice == "3":
                print(f"Progress: {appeal.get_progress():.2f}%")
            elif choice == "4":
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
