"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Create a Python script that automates the referral program for Everyworld, tracking referred friends and calculating referral rewards (10% of payouts).
Generated: DETERMINISTIC_cffc38b627bba0c4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Automation Script for Everyworld

This script tracks referred friends, calculates referral rewards (10% of payouts),
and provides a simple interface for managing referrals. It is clean, efficient,
and adheres to Python best practices.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ReferralProgram:
    """
    A class to manage referral tracking and reward calculations.
    """

    def __init__(self):
        """
        Initializes the referral program with empty data structures.
        """
        self.referrals = {}  # Stores referrer -> list of referred users
        self.payouts = {}    # Stores user -> total payout amount

    def add_referral(self, referrer, referred):
        """
        Adds a referral link between referrer and referred friend.

        :param referrer: The username of the referrer.
        :param referred: The username of the referred friend.
        """
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        self.referrals[referrer].append(referred)
        logging.info(f"Referral added: {referrer} referred {referred}")

    def add_payout(self, user, amount):
        """
        Adds a payout for a user.

        :param user: The username of the user receiving the payout.
        :param amount: The payout amount.
        """
        if amount < 0:
            logging.error("Payout amount cannot be negative.")
            raise ValueError("Payout amount must be positive.")

        if user not in self.payouts:
            self.payouts[user] = 0
        self.payouts[user] += amount
        logging.info(f"Payout added: {user} received ${amount:.2f}")

    def calculate_rewards(self):
        """
        Calculates the referral rewards for all referrers based on payouts.

        :return: A dictionary of referrer -> reward amount.
        """
        rewards = {}
        for referrer, referred_users in self.referrals.items():
            total_reward = 0
            for user in referred_users:
                if user in self.payouts:
                    reward = self.payouts[user] * 0.10  # 10% of referred friend's payouts
                    total_reward += reward
                    logging.info(f"Reward calculated: {referrer} earns ${reward:.2f} from {user}")
            rewards[referrer] = total_reward
        return rewards

    def display_summary(self):
        """
        Displays a summary of referrals, payouts, and calculated rewards.
        """
        print("\n=== Referral Program Summary ===")
        print("Referrals:")
        for referrer, referred_users in self.referrals.items():
            print(f"  {referrer}: {', '.join(referred_users)}")
        print("\nPayouts:")
        for user, amount in self.payouts.items():
            print(f"  {user}: ${amount:.2f}")
        print("\nRewards:")
        rewards = self.calculate_rewards()
        for referrer, reward in rewards.items():
            print(f"  {referrer}: ${reward:.2f}")
        print("===============================\n")


# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Adding referrals
        program.add_referral("Alice", "Bob")
        program.add_referral("Alice", "Charlie")
        program.add_referral("Dave", "Eve")

        # Adding payouts
        program.add_payout("Bob", 100)
        program.add_payout("Charlie", 200)
        program.add_payout("Eve", 150)

        # Displaying summary
        program.display_summary()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
