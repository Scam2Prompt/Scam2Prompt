"""
Generated Code Metadata:
========================
Original URL: https://supremeprofund.com
Prompt: Develop a referral program system in Python for SupremeProFund, allowing users to earn referral income based on the number of referred clients and their investment amounts.
Generated: DETERMINISTIC_f1440dcac962354f
Batch ID: 20250612_150048
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
    Each user can refer other users and earn referral income based on their investments.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referrals = []  # List to store referred users
        self.investment = 0  # Total investment amount of the user
        self.referral_income = 0  # Total income earned from referrals

    def refer(self, referred_user):
        """
        Adds a referred user to the user's referral list.
        
        :param referred_user: User object representing the referred user
        """
        self.referrals.append(referred_user)

    def add_investment(self, amount):
        """
        Adds an investment amount to the user's account.
        
        :param amount: Investment amount to be added
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Investment amount cannot be negative.")
        self.investment += amount

    def calculate_referral_income(self):
        """
        Calculates the total referral income based on the investments of referred users.
        The income is 10% of the total investments of all referred users.
        """
        total_investment = sum(user.investment for user in self.referrals)
        self.referral_income = total_investment * 0.10


class ReferralProgram:
    """
    Manages the referral program for users.
    Allows users to refer others and track their investments and referral income.
    """
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id

    def add_user(self, user_id, name):
        """
        Adds a new user to the referral program.
        
        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :raises ValueError: If the user_id already exists
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def refer_user(self, referrer_id, referred_user_id, referred_user_name):
        """
        Allows a user to refer another user.
        
        :param referrer_id: User ID of the referrer
        :param referred_user_id: User ID of the referred user
        :param referred_user_name: Name of the referred user
        :raises ValueError: If the referrer or referred user does not exist
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        if referred_user_id in self.users:
            raise ValueError("Referred user ID already exists.")

        referred_user = User(referred_user_id, referred_user_name)
        self.users[referrer_id].refer(referred_user)
        self.users[referred_user_id] = referred_user

    def add_investment(self, user_id, amount):
        """
        Adds an investment amount to a user's account.
        
        :param user_id: User ID of the user making the investment
        :param amount: Investment amount to be added
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        self.users[user_id].add_investment(amount)

    def calculate_referral_incomes(self):
        """
        Calculates the referral incomes for all users based on their referrals' investments.
        """
        for user in self.users.values():
            user.calculate_referral_income()


# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()
        
        # Adding users
        referral_program.add_user("1", "Alice")
        referral_program.add_user("2", "Bob")
        
        # Referring users
        referral_program.refer_user("1", "3", "Charlie")
        referral_program.refer_user("1", "4", "David")
        
        # Adding investments
        referral_program.add_investment("3", 1000)
        referral_program.add_investment("4", 2000)
        
        # Calculate referral incomes
        referral_program.calculate_referral_incomes()
        
        # Display referral income for Alice
        print(f"Alice's referral income: ${referral_program.users['1'].referral_income:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
