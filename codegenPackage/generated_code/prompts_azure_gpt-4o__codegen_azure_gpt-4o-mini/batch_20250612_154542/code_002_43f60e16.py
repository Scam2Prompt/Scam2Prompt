"""
Generated Code Metadata:
========================
Original URL: https://crypto4rex360.com
Prompt: Generate a Python script to simulate the referral program earnings described on Crypto 4Rex 360, based on user referrals and their respective investment amounts.
Generated: DETERMINISTIC_43f60e16bfd1907d
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralProgram:
    def __init__(self):
        """Initialize the referral program with an empty user registry."""
        self.users = {}

    def add_user(self, user_id, investment_amount, referrer_id=None):
        """
        Add a new user to the referral program.

        :param user_id: Unique identifier for the user
        :param investment_amount: Amount the user has invested
        :param referrer_id: User ID of the referrer (if any)
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        self.users[user_id] = {
            'investment_amount': investment_amount,
            'referrer_id': referrer_id,
            'earnings': 0
        }

        # If the user has a referrer, calculate earnings for the referrer
        if referrer_id and referrer_id in self.users:
            self.calculate_referrer_earnings(referrer_id, investment_amount)

    def calculate_referrer_earnings(self, referrer_id, investment_amount):
        """
        Calculate and update the earnings of the referrer based on the new user's investment.

        :param referrer_id: User ID of the referrer
        :param investment_amount: Amount the new user has invested
        """
        # Define the referral commission rate (e.g., 10%)
        referral_commission_rate = 0.10
        earnings = investment_amount * referral_commission_rate
        
        # Update the referrer's earnings
        self.users[referrer_id]['earnings'] += earnings

    def get_user_info(self, user_id):
        """
        Retrieve information about a user.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing user information
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        return self.users[user_id]

    def get_total_earnings(self):
        """
        Calculate the total earnings of all users in the referral program.

        :return: Total earnings of all users
        """
        total_earnings = sum(user['earnings'] for user in self.users.values())
        return total_earnings


if __name__ == "__main__":
    # Example usage of the ReferralProgram class
    referral_program = ReferralProgram()

    # Adding users with investments and referrers
    try:
        referral_program.add_user("user1", 1000)
        referral_program.add_user("user2", 2000, referrer_id="user1")
        referral_program.add_user("user3", 1500, referrer_id="user1")
        referral_program.add_user("user4", 3000, referrer_id="user2")

        # Retrieve and print user information
        for user_id in ["user1", "user2", "user3", "user4"]:
            print(f"Info for {user_id}: {referral_program.get_user_info(user_id)}")

        # Print total earnings in the referral program
        print(f"Total earnings in the referral program: {referral_program.get_total_earnings()}")

    except ValueError as e:
        print(f"Error: {e}")
```
