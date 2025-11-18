"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Write Python code to simulate a donation system for an NGO like Perú Makers, including features for tracking donor information and donation amounts.
Generated: DETERMINISTIC_9eb985851386e8b7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class DonationSystem:
    """
    A class to simulate a donation system for an NGO,
    allowing the tracking of donor information and donation amounts.
    """

    def __init__(self):
        # Initialize an empty list to store donor information
        self.donors = []

    def add_donor(self, name, email, amount):
        """
        Add a new donor to the system.

        :param name: The name of the donor.
        :param email: The email address of the donor.
        :param amount: The donation amount.
        """
        try:
            if amount <= 0:
                raise ValueError("Donation amount must be greater than zero.")
            donor = {
                "name": name,
                "email": email,
                "amount": amount
            }
            self.donors.append(donor)
            print(f"Thank you, {name}, for your donation of ${amount:.2f}!")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_donors(self):
        """
        List all donors and their donations.
        """
        if not self.donors:
            print("No donors found.")
            return
        print("List of donors:")
        for i, donor in enumerate(self.donors, start=1):
            print(f"{i}. {donor['name']} ({donor['email']}) - ${donor['amount']:.2f}")

    def total_donations(self):
        """
        Calculate and display the total donations received.
        """
        total = sum(donor['amount'] for donor in self.donors)
        print(f"Total donations received: ${total:.2f}")


def main():
    """
    Main function to interact with the donation system.
    """
    system = DonationSystem()

    while True:
        print("\nDonation System")
        print("1. Add a donor")
        print("2. List all donors")
        print("3. Show total donations")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter donor's name: ")
                email = input("Enter donor's email: ")
                try:
                    amount = float(input("Enter donation amount: "))
                except ValueError:
                    print("Invalid input. Donation amount must be a number.")
                    continue
                system.add_donor(name, email, amount)
            elif choice == 2:
                system.list_donors()
            elif choice == 3:
                system.total_donations()
            elif choice == 4:
                print("Thank you for using the donation system. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
