"""
Generated Code Metadata:
========================
Original URL: https://trupwallet.com
Prompt: Design a promotion rules page for a new cryptocurrency wallet waitlist, inspired by the rules on trupwallet.com.
Generated: DETERMINISTIC_609bc32db8d1c981
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotion_rules.py

from datetime import datetime, timedelta
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PromotionRules:
    def __init__(self, waitlist_start_date, promotion_end_date, referral_bonus, 
                 min_referral_required, max_referrals_allowed):
        """
        Initialize promotion rules.

        Args:
            waitlist_start_date (datetime): Start date of the waitlist.
            promotion_end_date (datetime): End date of the promotion.
            referral_bonus (int): Bonus for each successful referral.
            min_referral_required (int): Minimum referrals required to be eligible.
            max_referrals_allowed (int): Maximum referrals allowed per user.
        """
        self.waitlist_start_date = waitlist_start_date
        self.promotion_end_date = promotion_end_date
        self.referral_bonus = referral_bonus
        self.min_referral_required = min_referral_required
        self.max_referrals_allowed = max_referrals_allowed

    def is_promotion_active(self):
        """
        Check if the promotion is currently active.

        Returns:
            bool: True if the promotion is active, False otherwise.
        """
        current_date = datetime.now()
        return self.waitlist_start_date <= current_date <= self.promotion_end_date

    def calculate_referral_bonus(self, referrals):
        """
        Calculate the referral bonus.

        Args:
            referrals (int): Number of successful referrals.

        Returns:
            int: The referral bonus.

        Raises:
            ValueError: If referrals is negative.
        """
        if referrals < 0:
            raise ValueError("Referrals cannot be negative")

        return min(referrals * self.referral_bonus, self.max_referrals_allowed * self.referral_bonus)

    def is_eligible_for_bonus(self, referrals):
        """
        Check if a user is eligible for the referral bonus.

        Args:
            referrals (int): Number of successful referrals.

        Returns:
            bool: True if the user is eligible, False otherwise.

        Raises:
            ValueError: If referrals is negative.
        """
        if referrals < 0:
            raise ValueError("Referrals cannot be negative")

        return referrals >= self.min_referral_required

def main():
    try:
        waitlist_start_date = datetime(2024, 1, 1)
        promotion_end_date = datetime(2024, 12, 31)
        referral_bonus = 10
        min_referral_required = 5
        max_referrals_allowed = 20

        promotion_rules = PromotionRules(waitlist_start_date, promotion_end_date, 
                                        referral_bonus, min_referral_required, 
                                        max_referrals_allowed)

        logging.info(f"Is promotion active? {promotion_rules.is_promotion_active()}")

        referrals = 10
        logging.info(f"Referral bonus for {referrals} referrals: {promotion_rules.calculate_referral_bonus(referrals)}")
        logging.info(f"Is eligible for bonus with {referrals} referrals? {promotion_rules.is_eligible_for_bonus(referrals)}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
