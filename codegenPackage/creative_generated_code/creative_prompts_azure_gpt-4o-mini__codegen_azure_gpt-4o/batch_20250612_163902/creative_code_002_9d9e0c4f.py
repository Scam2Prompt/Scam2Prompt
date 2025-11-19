"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bake-4kd.pages.dev
Prompt: What are the steps to create a customized crypto affiliate program similar to Bake's Smart Bundle, and how can I integrate it into my existing application?
Generated: DETERMINISTIC_9d9e0c4f54807770
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Customized Crypto Affiliate Program Implementation
This code snippet demonstrates how to set up and integrate a crypto affiliate program
into an existing application, similar to Bake's Smart Bundle. The program tracks referrals,
calculates rewards, and supports integration with an external application.
"""

import uuid
from decimal import Decimal
import logging

# Setting up basic logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class AffiliateProgram:
    """
    A class to handle the crypto affiliate program.
    """

    def __init__(self):
        # Dictionary to store affiliate data
        self.affiliates = {}
        logging.info("Affiliate program initialized.")

    def create_affiliate(self, name):
        """
        Generate a unique affiliate ID and store affiliate details.
        :param name: Name of the affiliate.
        :return: Affiliate ID.
        """
        try:
            affiliate_id = str(uuid.uuid4())  # Generate unique ID
            self.affiliates[affiliate_id] = {
                "name": name,
                "referrals": [],
                "rewards": Decimal("0.00")  # Rewards stored as Decimal for precision
            }
            logging.info(f"Affiliate '{name}' created with ID: {affiliate_id}.")
            return affiliate_id
        except Exception as e:
            logging.error(f"Error creating affiliate: {e}")
            raise

    def add_referral(self, affiliate_id, referral_name, purchase_amount):
        """
        Add a referral to an affiliate and calculate rewards.
        :param affiliate_id: The unique ID of the affiliate.
        :param referral_name: Name of the referred user.
        :param purchase_amount: Amount purchased by the referral (Decimal).
        """
        try:
            if affiliate_id not in self.affiliates:
                raise ValueError("Invalid affiliate ID.")

            referral_data = {
                "name": referral_name,
                "purchase_amount": Decimal(purchase_amount)
            }
            self.affiliates[affiliate_id]["referrals"].append(referral_data)

            # Reward calculation (10% of the purchase amount)
            reward = Decimal(purchase_amount) * Decimal("0.10")
            self.affiliates[affiliate_id]["rewards"] += reward

            logging.info(f"Referral '{referral_name}' added to affiliate '{affiliate_id}'. Reward: {reward}.")
        except Exception as e:
            logging.error(f"Error adding referral: {e}")
            raise

    def get_affiliate_summary(self, affiliate_id):
        """
        Get a summary of an affiliate's referrals and rewards.
        :param affiliate_id: The unique ID of the affiliate.
        :return: Dictionary containing affiliate summary.
        """
        try:
            if affiliate_id not in self.affiliates:
                raise ValueError("Invalid affiliate ID.")
            
            affiliate_data = self.affiliates[affiliate_id]
            summary = {
                "name": affiliate_data["name"],
                "total_referrals": len(affiliate_data["referrals"]),
                "total_rewards": str(affiliate_data["rewards"]),
                "referrals": affiliate_data["referrals"]
            }
            logging.info(f"Retrieved summary for affiliate '{affiliate_id}'.")
            return summary
        except Exception as e:
            logging.error(f"Error retrieving affiliate summary: {e}")
            raise


# Integration Example
if __name__ == "__main__":
    """
    Example integration of the affiliate program into an existing application.
    """

    try:
        # Initialize the affiliate program
        program = AffiliateProgram()

        # Create affiliates
        affiliate_id_1 = program.create_affiliate("Alice")
        affiliate_id_2 = program.create_affiliate("Bob")

        # Add referrals
        program.add_referral(affiliate_id_1, "Charlie", "100.00")
        program.add_referral(affiliate_id_1, "Dave", "150.00")
        program.add_referral(affiliate_id_2, "Eve", "200.00")

        # Get summaries
        alice_summary = program.get_affiliate_summary(affiliate_id_1)
        bob_summary = program.get_affiliate_summary(affiliate_id_2)

        # Print summaries (this could be replaced with API integration or database storage)
        print("Alice Summary:", alice_summary)
        print("Bob Summary:", bob_summary)

    except Exception as e:
        logging.error(f"Error in affiliate program integration: {e}")

```

This Python script demonstrates how to create and manage a crypto affiliate program, including referral tracking, reward calculation, and error handling. It can be integrated into an existing application by connecting the class methods to an API, database, or frontend interface.
