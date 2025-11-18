"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supremeprofund.com
Prompt: Develop a referral program system in Python for SupremeProFund, allowing users to earn referral income based on the number of referred clients and their investment amounts.
Generated: DETERMINISTIC_f1440dcac962354f
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program System for SupremeProFund

This program allows users to earn referral income based on the number of referred 
clients and their respective investment amounts. The referral income is calculated 
using predefined percentages and rules.

Key Features:
1. Referral income is based on investment tiers.
2. Users can view their total referral income.
3. Error handling is implemented for invalid inputs.
"""

# Import necessary modules
import sys

class ReferralProgram:
    """
    A class to manage the referral program for SupremeProFund.
    """
    def __init__(self):
        """
        Initialize referral program data structures.
        """
        self.users = {}  # Dictionary to store user data: {username: {'clients': [], 'income': 0.0}}
        self.investment_tiers = {
            (0, 999): 0.01,       # 1% referral income for investments below $1000
            (1000, 9999): 0.02,   # 2% referral income for investments $1000-$9999
            (10000, float('inf')): 0.03  # 3% referral income for investments $10000 and above
        }

    def add_user(self, username):
        """
        Add a new user to the referral program.

        :param username: Username of the user to be added.
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists in the system.")
        self.users[username] = {'clients': [], 'income': 0.0}

    def add_client(self, referrer_username, client_name, investment_amount):
        """
        Add a referred client to a user's account.

        :param referrer_username: Username of the referrer.
        :param client_name: Name of the referred client.
        :param investment_amount: Investment amount by the client.
        """
        if referrer_username not in self.users:
            raise ValueError(f"Referrer '{referrer_username}' does not exist in the system.")

        if investment_amount < 0:
            raise ValueError("Investment amount must be a positive number.")

        # Calculate referral income based on investment tiers
        referral_percentage = self._get_referral_percentage(investment_amount)
        referral_income = investment_amount * referral_percentage

        # Update user's referral data
        self.users[referrer_username]['clients'].append({'name': client_name, 'investment': investment_amount})
        self.users[referrer_username]['income'] += referral_income

    def _get_referral_percentage(self, investment_amount):
        """
        Get the referral percentage based on the investment amount.

        :param investment_amount: Investment amount.
        :return: Referral percentage.
        """
        for tier, percentage in self.investment_tiers.items():
            if tier[0] <= investment_amount <= tier[1]:
                return percentage
        return 0.0

    def get_user_income(self, username):
        """
        Retrieve the total referral income for a given user.

        :param username: Username of the user.
        :return: Total referral income.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist in the system.")
        return self.users[username]['income']

    def display_user_info(self, username):
        """
        Display user information including referred clients and total income.

        :param username: Username of the user.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist in the system.")

        user_data = self.users[username]
        print(f"User: {username}")
        print("Referred Clients:")
        for client in user_data['clients']:
            print(f"- Name: {client['name']}, Investment: ${client['investment']:.2f}")
        print(f"Total Referral Income: ${user_data['income']:.2f}")

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the referral program
        referral_program = ReferralProgram()

        # Add users
        referral_program.add_user("john_doe")
        referral_program.add_user("jane_smith")

        # Add referred clients
        referral_program.add_client("john_doe", "client_a", 5000)
        referral_program.add_client("john_doe", "client_b", 12000)
        referral_program.add_client("jane_smith", "client_c", 800)

        # Display user information
        referral_program.display_user_info("john_doe")
        referral_program.display_user_info("jane_smith")

        # Get individual user income
        print(f"John Doe's Total Income: ${referral_program.get_user_income('john_doe'):.2f}")
        print(f"Jane Smith's Total Income: ${referral_program.get_user_income('jane_smith'):.2f}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```
