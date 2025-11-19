"""
Generated Code Metadata:
========================
Original URL: https://mfxhk.com
Prompt: Create a sample code snippet for a referral program that allows users to earn commissions from deposits, inspired by MFX-Online Trade's referral system.
Generated: DETERMINISTIC_be851bb2e78fd5fd
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    Represents a user in the referral program.
    Each user has a unique ID, a balance, and a list of referrals.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0.0
        self.referrals = []

    def add_referral(self, referral):
        """
        Adds a referral to the user's list of referrals.
        
        :param referral: User object representing the referred user
        """
        self.referrals.append(referral)

    def deposit(self, amount):
        """
        Processes a deposit for the user and updates the balance.
        
        :param amount: Amount to deposit
        :raises ValueError: If the deposit amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"User {self.user_id} deposited {amount}. New balance: {self.balance}")

    def calculate_commission(self, referral_amount, commission_rate):
        """
        Calculates the commission earned from referrals based on their deposits.
        
        :param referral_amount: Total amount deposited by referrals
        :param commission_rate: Commission rate as a decimal (e.g., 0.1 for 10%)
        :return: Commission earned
        """
        return referral_amount * commission_rate


class ReferralProgram:
    """
    Manages the referral program, including user registrations and commission calculations.
    """
    def __init__(self, commission_rate):
        self.users = {}
        self.commission_rate = commission_rate

    def register_user(self, user_id):
        """
        Registers a new user in the referral program.
        
        :param user_id: Unique identifier for the user
        :raises ValueError: If the user ID already exists
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id)
        print(f"User {user_id} registered successfully.")

    def add_referral(self, referrer_id, referred_id):
        """
        Adds a referral relationship between two users.
        
        :param referrer_id: User ID of the referrer
        :param referred_id: User ID of the referred user
        :raises ValueError: If either user ID does not exist
        """
        if referrer_id not in self.users or referred_id not in self.users:
            raise ValueError("Both users must be registered.")
        self.users[referrer_id].add_referral(self.users[referred_id])
        print(f"User {referred_id} referred by {referrer_id}.")

    def process_deposit(self, user_id, amount):
        """
        Processes a deposit for a user and calculates commissions for their referrals.
        
        :param user_id: User ID of the depositing user
        :param amount: Amount to deposit
        :raises ValueError: If the user ID does not exist
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        user = self.users[user_id]
        user.deposit(amount)

        # Calculate commissions for the referrer
        for referral in user.referrals:
            commission = referral.calculate_commission(amount, self.commission_rate)
            user.balance += commission
            print(f"User {user.user_id} earned commission of {commission} from referral {referral.user_id}.")


# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram(commission_rate=0.1)  # 10% commission
        referral_program.register_user("user1")
        referral_program.register_user("user2")
        referral_program.add_referral("user1", "user2")
        referral_program.process_deposit("user2", 1000)  # user2 deposits $1000
    except ValueError as e:
        print(f"Error: {e}")
```
