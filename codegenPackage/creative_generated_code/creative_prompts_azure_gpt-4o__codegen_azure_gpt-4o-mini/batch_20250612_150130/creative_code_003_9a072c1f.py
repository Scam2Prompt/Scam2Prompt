"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Generate a Python script that simulates instant withdrawals and calculates referral bonuses based on the 10% referral program described on epiccoin-miners.ltd.
Generated: DETERMINISTIC_9a072c1fce118dd7
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """Class to represent a user in the system."""
    
    def __init__(self, user_id, balance=0):
        self.user_id = user_id
        self.balance = balance
        self.referrals = []
    
    def add_referral(self, referral_user):
        """Add a referral user."""
        self.referrals.append(referral_user)
        logging.info(f"User {self.user_id} referred user {referral_user.user_id}")

    def withdraw(self, amount):
        """Simulate instant withdrawal of funds."""
        if amount <= 0:
            logging.error("Withdrawal amount must be greater than zero.")
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if amount > self.balance:
            logging.error("Insufficient balance for withdrawal.")
            raise ValueError("Insufficient balance for withdrawal.")

        self.balance -= amount
        logging.info(f"User {self.user_id} withdrew {amount}. New balance: {self.balance}")

    def calculate_referral_bonus(self):
        """Calculate total referral bonuses earned from referrals."""
        bonus = sum(referral.balance * 0.1 for referral in self.referrals)
        logging.info(f"User {self.user_id} has earned a referral bonus of {bonus}")
        return bonus


def simulate_withdrawals_and_referrals(users):
    """Simulate withdrawals and calculate referral bonuses for a list of users."""
    for user in users:
        # Simulate a random withdrawal amount
        withdrawal_amount = random.randint(1, 100)  # Random withdrawal between 1 and 100
        try:
            user.withdraw(withdrawal_amount)
        except ValueError as e:
            logging.warning(f"Withdrawal failed for user {user.user_id}: {e}")

        # Calculate referral bonuses
        referral_bonus = user.calculate_referral_bonus()
        logging.info(f"User {user.user_id} has a total referral bonus of: {referral_bonus}")


def main():
    """Main function to run the simulation."""
    # Create users
    user1 = User(user_id=1, balance=500)
    user2 = User(user_id=2, balance=300)
    user3 = User(user_id=3, balance=700)

    # Set up referrals
    user1.add_referral(user2)
    user1.add_referral(user3)

    # List of users to simulate
    users = [user1, user2, user3]

    # Run the simulation
    simulate_withdrawals_and_referrals(users)


if __name__ == "__main__":
    main()
```
