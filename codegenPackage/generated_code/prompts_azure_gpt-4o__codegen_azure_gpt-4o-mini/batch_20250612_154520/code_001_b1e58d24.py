"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Generate code to calculate donor compensation based on the Orlando Plasma Centers model, where donors earn between $100-$200 per donation. Include logic for tracking multiple donations per month.
Generated: DETERMINISTIC_b1e58d24fe068ec1
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Donor:
    """
    A class to represent a donor and calculate their compensation based on the number of donations made.
    """

    def __init__(self, name):
        """
        Initializes a new donor with a name and an empty donation history.

        :param name: str - The name of the donor
        """
        self.name = name
        self.donations = []  # List to track donation amounts

    def add_donation(self, amount):
        """
        Adds a donation amount to the donor's donation history.

        :param amount: float - The amount earned from the donation
        :raises ValueError: If the amount is not between 100 and 200
        """
        if amount < 100 or amount > 200:
            raise ValueError("Donation amount must be between $100 and $200.")
        self.donations.append(amount)

    def total_compensation(self):
        """
        Calculates the total compensation earned by the donor from all donations.

        :return: float - The total compensation
        """
        return sum(self.donations)

    def donation_count(self):
        """
        Returns the total number of donations made by the donor.

        :return: int - The number of donations
        """
        return len(self.donations)

    def __str__(self):
        """
        Returns a string representation of the donor's information.

        :return: str - Donor's name and total compensation
        """
        return f"Donor: {self.name}, Total Compensation: ${self.total_compensation():.2f}"


def main():
    """
    Main function to demonstrate the Donor class functionality.
    """
    try:
        # Create a donor instance
        donor = Donor("John Doe")

        # Simulate adding donations
        donor.add_donation(150)
        donor.add_donation(200)
        donor.add_donation(100)

        # Display donor information
        print(donor)
        print(f"Total Donations Made: {donor.donation_count()}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
