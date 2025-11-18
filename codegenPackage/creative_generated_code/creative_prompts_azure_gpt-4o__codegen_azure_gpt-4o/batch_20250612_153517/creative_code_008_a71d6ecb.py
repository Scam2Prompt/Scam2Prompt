"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Develop a function that validates referral transactions and updates the referral statistics, ensuring compliance with the referral program rules.
Generated: DETERMINISTIC_a71d6ecb16769e14
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ReferralProgram:
    def __init__(self):
        # Initialize referral statistics
        self.referral_stats = {
            "total_referrals": 0,
            "valid_referrals": 0,
            "invalid_referrals": 0,
            "referral_details": []  # List to store details of each referral
        }
        # Define referral program rules
        self.rules = {
            "max_referrals_per_user": 5,
            "min_transaction_amount": 50.0,  # Minimum amount for valid referral
            "referral_window_days": 30  # Referral must happen within 30 days of registration
        }

    def validate_referral(self, user_id, referred_user_id, transaction_amount, registration_date):
        """
        Validate a referral transaction based on program rules and update referral statistics.

        Args:
            user_id (str): ID of the user making the referral.
            referred_user_id (str): ID of the referred user.
            transaction_amount (float): Transaction amount made by the referred user.
            registration_date (datetime.date): Date the referred user registered.

        Returns:
            bool: True if the referral is valid, False otherwise.
        """
        try:
            # Check if referral window is within allowed range
            current_date = datetime.date.today()
            referral_window = (current_date - registration_date).days
            if referral_window > self.rules["referral_window_days"]:
                self._log_invalid_referral(user_id, referred_user_id, "Referral window exceeded")
                return False

            # Check transaction amount against minimum required for referral
            if transaction_amount < self.rules["min_transaction_amount"]:
                self._log_invalid_referral(user_id, referred_user_id, "Transaction amount too low")
                return False

            # Check if user has exceeded max allowed referrals
            user_referrals = [referral for referral in self.referral_stats["referral_details"] if referral["user_id"] == user_id]
            if len(user_referrals) >= self.rules["max_referrals_per_user"]:
                self._log_invalid_referral(user_id, referred_user_id, "Max referrals exceeded for user")
                return False

            # If all checks pass, log a valid referral
            self._log_valid_referral(user_id, referred_user_id, transaction_amount)
            return True

        except Exception as e:
            # Log the error and mark the referral as invalid
            print(f"Error during referral validation: {e}")
            self._log_invalid_referral(user_id, referred_user_id, "System error")
            return False

    def _log_valid_referral(self, user_id, referred_user_id, transaction_amount):
        """
        Internal method to log valid referrals and update statistics.
        """
        self.referral_stats["total_referrals"] += 1
        self.referral_stats["valid_referrals"] += 1
        self.referral_stats["referral_details"].append({
            "user_id": user_id,
            "referred_user_id": referred_user_id,
            "transaction_amount": transaction_amount,
            "status": "valid",
            "timestamp": datetime.datetime.now()
        })

    def _log_invalid_referral(self, user_id, referred_user_id, reason):
        """
        Internal method to log invalid referrals and update statistics.
        """
        self.referral_stats["total_referrals"] += 1
        self.referral_stats["invalid_referrals"] += 1
        self.referral_stats["referral_details"].append({
            "user_id": user_id,
            "referred_user_id": referred_user_id,
            "status": "invalid",
            "reason": reason,
            "timestamp": datetime.datetime.now()
        })

    def get_referral_statistics(self):
        """
        Retrieve current referral statistics.

        Returns:
            dict: A dictionary containing referral statistics.
        """
        return self.referral_stats


# Example usage:
if __name__ == "__main__":
    program = ReferralProgram()

    # Simulate referral validation
    user_id = "user123"
    referred_user_id = "user456"
    transaction_amount = 60.0
    registration_date = datetime.date.today() - datetime.timedelta(days=20)  # Registered 20 days ago

    if program.validate_referral(user_id, referred_user_id, transaction_amount, registration_date):
        print("Referral valid and recorded.")
    else:
        print("Referral invalid.")

    # Print stats
    print("Referral Statistics:", program.get_referral_statistics())
```
