"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passiveinvestincome.com
Prompt: Create a Python script that calculates referral commissions based on PassiveInvestIncome's 5% referral program. Include functionality to track referrals and calculate earnings for multiple users.
Generated: DETERMINISTIC_e0d0b2f8a45b6f31
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    """
    A class to represent a referral program for calculating commissions.
    """

    def __init__(self):
        """
        Initializes the ReferralProgram with an empty dictionary for tracking users and their referrals.
        """
        self.users = {}  # Dictionary to store user data

    def add_user(self, username):
        """
        Adds a new user to the referral program.

        Args:
            username (str): The username of the user.

        Raises:
            ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        
        self.users[username] = {"referrals": [], "earnings": 0.0}

    def add_referral(self, referrer, referral):
        """
        Adds a referral under the specified referrer.

        Args:
            referrer (str): The username of the referrer.
            referral (str): The username of the referral to be added.

        Raises:
            ValueError: If the referrer or referral does not exist.
        """
        if referrer not in self.users:
            raise ValueError(f"Referrer '{referrer}' does not exist.")
        if referral not in self.users:
            raise ValueError(f"Referral '{referral}' does not exist.")
        
        self.users[referrer]["referrals"].append(referral)

    def calculate_earnings(self, username, amount_invested):
        """
        Calculates and updates the earnings for the specified user based on the amount invested.

        Args:
            username (str): The username of the user to calculate earnings for.
            amount_invested (float): The amount invested by the referral.

        Raises:
            ValueError: If the user does not exist.
        
        Returns:
            float: The commission earned from the referral.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")

        commission_rate = 0.05  # 5% commission
        earnings = amount_invested * commission_rate
        self.users[username]["earnings"] += earnings
        
        return earnings

    def get_user_info(self, username):
        """
        Retrieves the information for the specified user.

        Args:
            username (str): The username of the user.

        Raises:
            ValueError: If the user does not exist.
        
        Returns:
            dict: A dictionary containing the user's referrals and earnings.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        
        return self.users[username]

    def display_all_users(self):
        """
        Displays the information of all users in the referral program.
        """
        for user, data in self.users.items():
            print(f"User: {user}, Referrals: {data['referrals']}, Earnings: ${data['earnings']:.2f}")


# Example usage:
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Adding users
    referral_program.add_user("Alice")
    referral_program.add_user("Bob")
    
    # Adding a referral
    referral_program.add_referral("Alice", "Bob")

    # Calculating earnings
    earnings_bob = referral_program.calculate_earnings("Alice", 1000)
    print(f"Alice earned: ${earnings_bob:.2f}")

    # Displaying user information
    referral_program.display_all_users()
```
