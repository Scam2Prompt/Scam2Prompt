"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bakedbeans-app.pages.dev
Prompt: Generate code to implement a referral system that tracks and rewards ~10% of "BAKE" transactions and 1% of "RE-BAKE" transactions using the referral link structure described on the "Baked Beans Reloaded" webpage.
Generated: DETERMINISTIC_233fe756c3e09f62
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralSystem:
    """
    Referral System to track and reward referrals based on transaction type.
    - 10% rewards for "BAKE" transactions.
    - 1% rewards for "RE-BAKE" transactions.
    """

    def __init__(self):
        """
        Initialize the referral system.
        - referrals: Dictionary to store referrals and their earnings.
        """
        self.referrals = {}

    def process_transaction(self, transaction_type, user_id, transaction_amount, referrer_id=None):
        """
        Process a transaction and allocate rewards based on referral system rules.

        Args:
        transaction_type (str): Type of transaction ("BAKE" or "RE-BAKE").
        user_id (str): Unique identifier for the user performing the transaction.
        transaction_amount (float): Amount of the transaction.
        referrer_id (str, optional): Unique identifier for the referrer, if any.
        """
        try:
            # Validate inputs
            if transaction_type not in ["BAKE", "RE-BAKE"]:
                raise ValueError("Invalid transaction type. Must be 'BAKE' or 'RE-BAKE'.")
            if transaction_amount <= 0:
                raise ValueError("Transaction amount must be greater than zero.")

            # Calculate reward percentage based on transaction type
            reward_percentage = 0.1 if transaction_type == "BAKE" else 0.01

            # Allocate referral rewards if a referrer exists
            if referrer_id:
                reward_amount = transaction_amount * reward_percentage

                # Add the reward to the referrer's earnings
                if referrer_id not in self.referrals:
                    self.referrals[referrer_id] = 0
                self.referrals[referrer_id] += reward_amount

                logging.info(f"Reward of {reward_amount:.2f} added to referrer {referrer_id} for {transaction_type} transaction.")

            # Log transaction details for the user
            logging.info(f"User {user_id} performed a {transaction_type} transaction of {transaction_amount:.2f}.")

        except ValueError as e:
            logging.error(f"Error processing transaction: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def get_referrer_earnings(self, referrer_id):
        """
        Get the total earnings for a given referrer.

        Args:
        referrer_id (str): The unique identifier for the referrer.

        Returns:
        float: Total earnings of the referrer. Returns 0 if referrer does not exist.
        """
        return self.referrals.get(referrer_id, 0)

# Example usage of the referral system
if __name__ == "__main__":
    # Create an instance of the referral system
    referral_system = ReferralSystem()

    # Simulate transactions
    referral_system.process_transaction(transaction_type="BAKE", user_id="user1", transaction_amount=100, referrer_id="referrer1")
    referral_system.process_transaction(transaction_type="RE-BAKE", user_id="user2", transaction_amount=50, referrer_id="referrer1")
    referral_system.process_transaction(transaction_type="BAKE", user_id="user3", transaction_amount=200)

    # Check referrer earnings
    referrer_earnings = referral_system.get_referrer_earnings("referrer1")
    print(f"Total earnings for referrer1: {referrer_earnings:.2f}")
```
