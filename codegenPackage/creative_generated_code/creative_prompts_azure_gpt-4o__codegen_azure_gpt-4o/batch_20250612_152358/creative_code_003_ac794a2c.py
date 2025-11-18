"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Develop a Python program to track referral earnings and calculate the 70% referral commission mentioned in the AUTOBUX system.
Generated: DETERMINISTIC_ac794a2cb4c65dc5
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to track referral earnings and calculate a 70% referral commission.

# Import necessary modules
import sys

class ReferralEarningsTracker:
    """
    A class to track referral earnings and calculate referral commission.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty dictionary to store user earnings.
        """
        self.earnings = {}  # Dictionary to store user earnings {username: total_earnings}

    def add_earning(self, username, amount):
        """
        Adds earnings for a given user.

        :param username: str - The username of the referrer.
        :param amount: float - The earning amount to be added.
        """
        try:
            if amount < 0:
                raise ValueError("Earning amount cannot be negative.")

            if username in self.earnings:
                self.earnings[username] += amount
            else:
                self.earnings[username] = amount

            print(f"Added earning of ${amount:.2f} for user '{username}'.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def calculate_commission(self, username):
        """
        Calculates the 70% referral commission for a given user.

        :param username: str - The username of the referrer.
        :return: float - The calculated commission amount.
        """
        try:
            if username not in self.earnings:
                raise KeyError(f"User '{username}' does not exist in the records.")

            total_earnings = self.earnings[username]
            commission = total_earnings * 0.7
            return commission
        except KeyError as ke:
            print(f"Error: {ke}")
            return 0.0

    def display_user_earnings(self):
        """
        Displays all users and their total earnings.
        """
        if not self.earnings:
            print("No earnings recorded yet.")
            return

        print("\nUser Earnings:")
        for username, earning in self.earnings.items():
            print(f"  {username}: ${earning:.2f}")

    def display_user_commission(self):
        """
        Displays all users and their calculated commissions.
        """
        if not self.earnings:
            print("No earnings recorded yet.")
            return

        print("\nUser Commissions (70%):")
        for username, earning in self.earnings.items():
            commission = earning * 0.7
            print(f"  {username}: ${commission:.2f}")


# Main function to interact with the program
def main():
    """
    Main function to provide a menu-driven interface for the user.
    """
    tracker = ReferralEarningsTracker()

    while True:
        print("\n--- Referral Earnings Tracker ---")
        print("1. Add Earning")
        print("2. Calculate Commission for a User")
        print("3. Display All Earnings")
        print("4. Display All Commissions")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            username = input("Enter username: ")
            try:
                amount = float(input("Enter earning amount: "))
                tracker.add_earning(username, amount)
            except ValueError:
                print("Invalid input. Amount must be a number.")

        elif choice == "2":
            username = input("Enter username: ")
            commission = tracker.calculate_commission(username)
            if commission > 0:
                print(f"The 70% referral commission for '{username}' is: ${commission:.2f}")

        elif choice == "3":
            tracker.display_user_earnings()

        elif choice == "4":
            tracker.display_user_commission()

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Entry point of the program
if __name__ == "__main__":
    main()
```
