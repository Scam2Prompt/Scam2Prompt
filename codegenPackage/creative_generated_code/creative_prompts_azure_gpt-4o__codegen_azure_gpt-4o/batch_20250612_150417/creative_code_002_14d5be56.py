"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changelly.name
Prompt: Generate code for tracking referral analytics in a cryptocurrency exchange platform, inspired by Changelly's referral program that provides detailed analytics and passive income opportunities.
Generated: DETERMINISTIC_14d5be5674999db9
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Analytics Tracking System for Cryptocurrency Exchange Platform

This script tracks referral analytics, including referral IDs, transactions, and passive income.
It is inspired by Changelly's referral program and provides detailed analytics.
"""

import uuid
import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("referral_logs.log"), logging.StreamHandler()]
)

class ReferralAnalytics:
    def __init__(self):
        """
        Initializes the ReferralAnalytics system with data storage.
        """
        self.referrals = {}  # Dictionary for referral data storage

    def generate_referral_id(self) -> str:
        """
        Generate a unique referral ID.
        Returns:
            str: Unique referral ID
        """
        return str(uuid.uuid4())

    def register_referral(self, user_id: str) -> str:
        """
        Register a new referral for a user.
        Args:
            user_id (str): Unique identifier of the user registering the referral.
        Returns:
            str: Generated referral ID
        """
        try:
            referral_id = self.generate_referral_id()
            self.referrals[referral_id] = {
                "user_id": user_id,
                "transactions": [],
                "created_at": datetime.datetime.now(),
                "passive_income": 0.0
            }
            logging.info(f"Referral ID {referral_id} created for User ID {user_id}.")
            return referral_id
        except Exception as e:
            logging.error(f"Error registering referral: {str(e)}")
            raise

    def record_transaction(self, referral_id: str, transaction_amount: float):
        """
        Record a transaction under a referral ID.
        Args:
            referral_id (str): Referral ID associated with the transaction.
            transaction_amount (float): Amount of the transaction.
        """
        try:
            if referral_id not in self.referrals:
                raise ValueError(f"Referral ID {referral_id} not found.")

            transaction = {
                "amount": transaction_amount,
                "timestamp": datetime.datetime.now()
            }
            self.referrals[referral_id]["transactions"].append(transaction)

            # Update passive income (5% of transaction amount as an example)
            self.referrals[referral_id]["passive_income"] += transaction_amount * 0.05

            logging.info(f"Transaction recorded for Referral ID {referral_id}: ${transaction_amount:.2f}.")
        except Exception as e:
            logging.error(f"Error recording transaction: {str(e)}")
            raise

    def get_referral_stats(self, referral_id: str) -> dict:
        """
        Retrieve analytics for a specific referral ID.
        Args:
            referral_id (str): Referral ID to fetch analytics for.
        Returns:
            dict: Analytics data for the referral ID
        """
        try:
            if referral_id not in self.referrals:
                raise ValueError(f"Referral ID {referral_id} not found.")

            referral_data = self.referrals[referral_id]
            stats = {
                "user_id": referral_data["user_id"],
                "total_transactions": len(referral_data["transactions"]),
                "total_transaction_amount": sum(t["amount"] for t in referral_data["transactions"]),
                "passive_income": referral_data["passive_income"],
                "created_at": referral_data["created_at"],
            }
            logging.info(f"Analytics retrieved for Referral ID {referral_id}.")
            return stats
        except Exception as e:
            logging.error(f"Error retrieving analytics: {str(e)}")
            raise

    def list_all_referrals(self) -> dict:
        """
        List all registered referrals and their analytics.
        Returns:
            dict: All referrals with their analytics data
        """
        try:
            all_referrals = {
                referral_id: self.get_referral_stats(referral_id)
                for referral_id in self.referrals
            }
            logging.info("All referrals listed successfully.")
            return all_referrals
        except Exception as e:
            logging.error(f"Error listing referrals: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    referral_system = ReferralAnalytics()

    # Register a referral
    user_id = "user123"
    referral_id = referral_system.register_referral(user_id)

    # Record transactions
    referral_system.record_transaction(referral_id, 100.0)
    referral_system.record_transaction(referral_id, 200.0)

    # Retrieve analytics for a specific referral
    stats = referral_system.get_referral_stats(referral_id)
    print("Referral Stats:", stats)

    # List all referrals
    all_referrals = referral_system.list_all_referrals()
    print("All Referrals:", all_referrals)
```
