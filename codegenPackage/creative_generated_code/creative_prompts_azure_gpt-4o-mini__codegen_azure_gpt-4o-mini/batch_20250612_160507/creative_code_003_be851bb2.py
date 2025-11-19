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
class User:
    """Class representing a user in the referral program."""
    
    def __init__(self, username, balance=0.0):
        """
        Initialize a new user.

        :param username: Name of the user
        :param balance: Initial balance of the user, defaults to 0.0
        """
        self.username = username
        self.balance = balance
        self.referrals = []  # Store user's referrals

    def add_referral(self, referral):
        """
        Add a referral to the user's referrals list.

        :param referral: User object representing the referral
        """
        self.referrals.append(referral)

    def deposit(self, amount):
        """
        Deposit an amount to the user's balance.

        :param amount: Amount to deposit
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.earn_commission(amount)

    def earn_commission(self, deposit_amount):
        """
        Calculate and distribute commission for the user's referrals.

        :param deposit_amount: The amount deposited by the referred user
        """
        commission_rate = 0.1  # 10% commission rate for referrals
        for referral in self.referrals:
            commission = deposit_amount * commission_rate
            referral.balance += commission
            print(f"{referral.username} earned a commission of {commission:.2f} from {self.username}'s deposit.")


def main():
    """Main function to demonstrate the referral program."""
    try:
        # Create users
        alice = User("Alice")
        bob = User("Bob")
        charlie = User("Charlie")

        # Setting up referrals
        alice.add_referral(bob)
        alice.add_referral(charlie)

        # Simulate a deposit
        print(f"Initial balance for {alice.username}: {alice.balance:.2f}")
        print(f"Initial balance for {bob.username}: {bob.balance:.2f}")
        print(f"Initial balance for {charlie.username}: {charlie.balance:.2f}")

        alice.deposit(100)  # Alice deposits $100
        
        # Display updated balances
        print(f"Updated balance for {alice.username}: {alice.balance:.2f}")
        print(f"Updated balance for {bob.username}: {bob.balance:.2f}")
        print(f"Updated balance for {charlie.username}: {charlie.balance:.2f}")

    except ValueError as ve:
        print(f"Error occurred: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
