"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com
Prompt: Generate a code snippet for a referral program that tracks user referrals and calculates additional income for an investment platform like Safe Wealth Haven.
Generated: DETERMINISTIC_baa1dd3fad1c23a5
Batch ID: 20250612_160156
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
    A class to manage a referral program for users on an investment platform.
    Tracks user referrals and calculates additional income based on referrals.
    """

    def __init__(self):
        # Dictionary to hold user earnings and their referrals
        self.user_data = {}

    def add_user(self, user_id):
        """
        Adds a new user to the program with no referrals or earnings.

        :param user_id: Unique identifier for the user
        """
        if user_id in self.user_data:
            raise ValueError(f"User {user_id} already exists.")
        self.user_data[user_id] = {'referrals': [], 'earnings': 0.0}

    def refer_user(self, referrer_id, referred_id):
        """
        Tracks a referral from one user to another.

        :param referrer_id: The user ID of the referrer
        :param referred_id: The user ID of the referred user
        """
        if referrer_id not in self.user_data:
            raise ValueError(f"Referrer {referrer_id} does not exist.")
        if referred_id in self.user_data:
            raise ValueError(f"User {referred_id} already exists.")

        # Add the referred user to the referrer's list of referrals
        self.user_data[referrer_id]['referrals'].append(referred_id)
        self.add_user(referred_id)  # Add referred user automatically

    def calculate_earnings(self, user_id, amount_per_referral=50):
        """
        Calculates income for a user based on their referrals.

        :param user_id: Unique identifier for the user
        :param amount_per_referral: Amount earned per successful referral
        :return: The total earnings for the user
        """
        if user_id not in self.user_data:
            raise ValueError(f"User {user_id} does not exist.")

        referral_count = len(self.user_data[user_id]['referrals'])
        total_earnings = referral_count * amount_per_referral
        self.user_data[user_id]['earnings'] = total_earnings
        return total_earnings

    def get_user_data(self, user_id):
        """
        Retrieves the user data including referrals and earnings.

        :param user_id: Unique identifier for the user
        :return: A dictionary containing user referrals and earnings
        """
        if user_id not in self.user_data:
            raise ValueError(f"User {user_id} does not exist.")
        
        return self.user_data[user_id]


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Adding users
    try:
        referral_program.add_user('user1')
        referral_program.add_user('user2')

        # Referring users
        referral_program.refer_user('user1', 'user2')

        # Calculate earnings for user1
        earnings = referral_program.calculate_earnings('user1')
        print(f"User1 Earnings: ${earnings}")

        # Retrieve user data
        user_data = referral_program.get_user_data('user1')
        print(f"User1 Data: {user_data}")

    except ValueError as e:
        print(f"Error: {e}")
```
