"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Construct a code example that integrates a referral program for hot tub purchases, similar to the one offered by Country Leisure, into an existing e-commerce platform.
Generated: DETERMINISTIC_18830af9fcc907be
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/referral/{user_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

class ReferralProgram:
    """
    Class to manage the referral program for hot tub purchases.
    """

    def __init__(self):
        self.referrals = {}  # Store referral links and associated users
        self.purchases = {}  # Store purchases made by users

    def create_referral(self, user_id):
        """
        Create a referral link for a given user.

        :param user_id: Unique identifier for the user
        :return: Referral link
        """
        referral_link = f"https://example.com/referral/{user_id}"
        self.referrals[user_id] = referral_link
        return referral_link

    def record_purchase(self, user_id, referred_by=None):
        """
        Record a purchase made by a user and handle referral bonus.

        :param user_id: Unique identifier for the user making the purchase
        :param referred_by: Unique identifier for the user who referred them
        """
        if user_id in self.purchases:
            raise ValueError(f"User {user_id} has already made a purchase.")

        # Record the purchase
        self.purchases[user_id] = {
            'referred_by': referred_by,
            'purchase_amount': 5000  # Assuming a fixed purchase amount for simplicity
        }

        if referred_by and referred_by in self.referrals:
            self._apply_referral_bonus(referred_by)

    def _apply_referral_bonus(self, referred_by):
        """
        Apply a referral bonus to the referring user.

        :param referred_by: Unique identifier for the user who referred
        """
        # Simulate applying a bonus, e.g., store in a database or credit account
        print(f"Bonus applied to user {referred_by} for referring a new purchase.")

    def get_user_referrals(self, user_id):
        """
        Retrieve the referral link for a user.

        :param user_id: Unique identifier for the user
        :return: Referral link or None if not found
        """
        return self.referrals.get(user_id, None)

# Example usage of the ReferralProgram class
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Create a referral for a user
    user_id = "user123"
    referral_link = referral_program.create_referral(user_id)
    print(f"Referral link for {user_id}: {referral_link}")

    # Record a purchase with referral
    try:
        referral_program.record_purchase("user456", referred_by=user_id)
        print(f"Purchase recorded for user456 referred by {user_id}.")
    except ValueError as e:
        print(e)

    # Retrieve referral link
    link = referral_program.get_user_referrals(user_id)
    print(f"Retrieved referral link: {link}")
```
