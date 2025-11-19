"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: Create a sample code snippet for a referral program that allows users to earn commissions from deposits, inspired by MFX-Online Trade's referral system.
Generated: DETERMINISTIC_be851bb2e78fd5fd
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class ReferralProgram:
    """
    A class to manage a referral program where users earn commissions from referred users' deposits.
    """

    def __init__(self, commission_rate=0.05):
        """
        Initializes the referral program.
        :param commission_rate: Commission rate for referrals (default is 5%).
        """
        self.users = {}  # Stores user data including referrals and their earnings
        self.commission_rate = commission_rate  # Commission rate for referrals

    def register_user(self, name):
        """
        Registers a new user into the referral program.
        :param name: Name of the user.
        :return: User ID of the newly registered user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.users[user_id] = {
            "name": name,
            "referred_by": None,
            "referrals": [],
            "earnings": 0.0,
            "deposits": 0.0,
        }
        return user_id

    def add_referral(self, referrer_id, referred_name):
        """
        Adds a referral relationship between the referrer and the referred user.
        :param referrer_id: User ID of the referrer.
        :param referred_name: Name of the referred user.
        :return: User ID of the referred user.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID not found.")
        
        referred_id = self.register_user(referred_name)
        self.users[referred_id]["referred_by"] = referrer_id
        self.users[referrer_id]["referrals"].append(referred_id)
        return referred_id

    def record_deposit(self, user_id, amount):
        """
        Records a deposit for a specific user and calculates referral earnings.
        :param user_id: User ID of the depositor.
        :param amount: Deposit amount.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Record the deposit
        self.users[user_id]["deposits"] += amount

        # Handle referral commission
        referrer_id = self.users[user_id]["referred_by"]
        if referrer_id:
            commission = amount * self.commission_rate
            self.users[referrer_id]["earnings"] += commission

    def get_user_info(self, user_id):
        """
        Retrieves information about a user.
        :param user_id: User ID of the user.
        :return: Dictionary containing user information.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        return self.users[user_id]

    def print_user_summary(self, user_id):
        """
        Prints a summary of the user's activity and earnings.
        :param user_id: User ID of the user.
        """
        user_info = self.get_user_info(user_id)
        print(f"User: {user_info['name']}")
        print(f"Deposits: ${user_info['deposits']:.2f}")
        print(f"Earnings: ${user_info['earnings']:.2f}")
        print(f"Referred Users: {[self.users[ref]['name'] for ref in user_info['referrals']]}")


# Example usage:
if __name__ == "__main__":
    program = ReferralProgram()

    # Register users
    alice_id = program.register_user("Alice")
    bob_id = program.add_referral(alice_id, "Bob")
    charlie_id = program.add_referral(alice_id, "Charlie")

    # Record deposits
    program.record_deposit(bob_id, 100.0)  # Bob deposits $100
    program.record_deposit(charlie_id, 200.0)  # Charlie deposits $200

    # Print summaries
    program.print_user_summary(alice_id)  # Alice's earnings
    program.print_user_summary(bob_id)  # Bob's activity
    program.print_user_summary(charlie_id)  # Charlie's activity
```
