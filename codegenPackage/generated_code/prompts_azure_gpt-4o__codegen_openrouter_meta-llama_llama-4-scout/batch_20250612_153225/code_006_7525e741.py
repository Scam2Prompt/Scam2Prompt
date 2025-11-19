"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Generate code for tracking customer referrals and rewards, inspired by referral programs offered by digital marketing agencies.
Generated: DETERMINISTIC_7525e7411df711c1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

from datetime import datetime, timedelta
import uuid
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Customer:
    def __init__(self, customer_id, name, email):
        """
        Initialize a Customer object.

        Args:
        - customer_id (str): Unique identifier for the customer.
        - name (str): Customer name.
        - email (str): Customer email.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.referrals = []
        self.rewards = []

class ReferralProgram:
    def __init__(self):
        """
        Initialize a ReferralProgram object.
        """
        self.customers = {}
        self.referral_rewards = {
            "referrer": 10,
            "referree": 10
        }
        self.referral_expiration_days = 30

    def add_customer(self, customer_id, name, email):
        """
        Add a new customer to the referral program.

        Args:
        - customer_id (str): Unique identifier for the customer.
        - name (str): Customer name.
        - email (str): Customer email.

        Returns:
        - Customer: The added Customer object.
        """
        if customer_id in self.customers:
            logger.error(f"Customer with ID {customer_id} already exists.")
            return None

        customer = Customer(customer_id, name, email)
        self.customers[customer_id] = customer
        return customer

    def create_referral(self, referrer_id, referree_id):
        """
        Create a new referral.

        Args:
        - referrer_id (str): Unique identifier for the referrer.
        - referree_id (str): Unique identifier for the referree.

        Returns:
        - bool: True if the referral was created successfully, False otherwise.
        """
        if referrer_id not in self.customers or referree_id not in self.customers:
            logger.error("One or both customers do not exist.")
            return False

        referrer = self.customers[referrer_id]
        referree = self.customers[referree_id]

        # Generate a unique referral code
        referral_code = str(uuid.uuid4())

        # Set referral expiration date
        expiration_date = datetime.now() + timedelta(days=self.referral_expiration_days)

        # Add referral to referrer's and referree's records
        referrer.referrals.append({"referree_id": referree_id, "referral_code": referral_code, "expiration_date": expiration_date})
        referree.referrals.append({"referrer_id": referrer_id, "referral_code": referral_code, "expiration_date": expiration_date})

        # Award referral rewards
        referrer.rewards.append({"reward_type": "referrer", "points": self.referral_rewards["referrer"]})
        referree.rewards.append({"reward_type": "referree", "points": self.referral_rewards["referree"]})

        logger.info(f"Referral created: {referrer_id} -> {referree_id} (Referral Code: {referral_code})")
        return True

    def get_customer_rewards(self, customer_id):
        """
        Get a customer's rewards.

        Args:
        - customer_id (str): Unique identifier for the customer.

        Returns:
        - list: A list of rewards for the customer.
        """
        if customer_id not in self.customers:
            logger.error(f"Customer with ID {customer_id} does not exist.")
            return []

        customer = self.customers[customer_id]
        return customer.rewards

def main():
    referral_program = ReferralProgram()

    # Add customers
    customer1 = referral_program.add_customer("C001", "John Doe", "john.doe@example.com")
    customer2 = referral_program.add_customer("C002", "Jane Doe", "jane.doe@example.com")

    # Create referral
    referral_program.create_referral("C001", "C002")

    # Get customer rewards
    rewards = referral_program.get_customer_rewards("C001")
    logger.info(f"Rewards for C001: {rewards}")

if __name__ == "__main__":
    main()
```
