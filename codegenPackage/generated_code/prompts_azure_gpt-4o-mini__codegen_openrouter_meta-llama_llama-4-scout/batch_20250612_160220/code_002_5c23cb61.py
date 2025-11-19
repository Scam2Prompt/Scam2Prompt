"""
Generated Code Metadata:
========================
Original URL: https://hedgefund-options.com
Prompt: Generate a code snippet that demonstrates how to implement a referral program similar to the one described on hedgefund-options.com.
Generated: DETERMINISTIC_5c23cb619b3e3074
Batch ID: 20250612_160220
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
import hashlib
import hmac
import secrets

class ReferralProgram:
    def __init__(self, referral_link_expiration_days=30, referral_reward=100):
        """
        Initialize the referral program.

        Args:
        - referral_link_expiration_days (int): The number of days a referral link is valid.
        - referral_reward (int): The reward for successful referrals.
        """
        self.referral_link_expiration_days = referral_link_expiration_days
        self.referral_reward = referral_reward
        self.referrals = {}

    def generate_referral_link(self, user_id):
        """
        Generate a unique referral link for a user.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - referral_link (str): A unique referral link.
        """
        # Generate a secret key for the referral link
        secret_key = secrets.token_urlsafe(16)
        # Create a referral link that expires after a certain number of days
        expiration_date = datetime.now() + timedelta(days=self.referral_link_expiration_days)
        referral_link = self._create_referral_link(user_id, secret_key, expiration_date)
        self.referrals[referral_link] = {"user_id": user_id, "expiration_date": expiration_date}
        return referral_link

    def _create_referral_link(self, user_id, secret_key, expiration_date):
        """
        Create a referral link.

        Args:
        - user_id (str): The ID of the user.
        - secret_key (str): A secret key for the referral link.
        - expiration_date (datetime): The expiration date of the referral link.

        Returns:
        - referral_link (str): A unique referral link.
        """
        # Use HMAC to create a secure referral link
        message = f"{user_id}{expiration_date.isoformat()}"
        referral_link = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
        return referral_link

    def validate_referral_link(self, referral_link):
        """
        Validate a referral link.

        Args:
        - referral_link (str): The referral link to validate.

        Returns:
        - is_valid (bool): Whether the referral link is valid.
        - user_id (str): The ID of the user who referred the new user.
        """
        if referral_link in self.referrals:
            referral_info = self.referrals[referral_link]
            if datetime.now() < referral_info["expiration_date"]:
                return True, referral_info["user_id"]
        return False, None

    def reward_referrer(self, referrer_user_id):
        """
        Reward the referrer.

        Args:
        - referrer_user_id (str): The ID of the user who referred the new user.
        """
        # Implement the logic to reward the referrer
        print(f"Rewarding user {referrer_user_id} with {self.referral_reward}")


def main():
    referral_program = ReferralProgram()

    # Generate a referral link
    user_id = "user123"
    referral_link = referral_program.generate_referral_link(user_id)
    print(f"Referral link: {referral_link}")

    # Validate the referral link
    is_valid, referrer_user_id = referral_program.validate_referral_link(referral_link)
    print(f"Is referral link valid? {is_valid}")
    if is_valid:
        print(f"Referrer user ID: {referrer_user_id}")

        # Reward the referrer
        referral_program.reward_referrer(referrer_user_id)


if __name__ == "__main__":
    main()
```
