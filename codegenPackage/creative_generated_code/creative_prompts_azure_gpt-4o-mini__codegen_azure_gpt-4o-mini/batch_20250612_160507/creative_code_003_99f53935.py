"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Describe how to set up a referral program for freight factoring using Summar Financial's guidelines and provide sample code for tracking referrals.
Generated: DETERMINISTIC_99f5393512e93196
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

import uuid
from datetime import datetime

class ReferralProgram:
    def __init__(self):
        # Dictionary to hold referral data
        self.referrals = {}

    def generate_referral_code(self, user_id):
        """
        Generate a unique referral code for a user.

        Args:
            user_id (str): The ID of the user generating the referral code.

        Returns:
            str: A unique referral code.
        """
        referral_code = f"REF-{user_id}-{uuid.uuid4().hex[:6]}"
        return referral_code

    def add_referral(self, referral_code, referred_user_id):
        """
        Add a referral to the system.

        Args:
            referral_code (str): The unique code associated with the referrer.
            referred_user_id (str): The ID of the user being referred.

        Raises:
            ValueError: If the referral code is invalid or already used.
        """
        if referral_code in self.referrals:
            raise ValueError("Referral code has already been used.")

        self.referrals[referral_code] = {
            "referred_user_id": referred_user_id,
            "date": datetime.now()
        }

    def get_referral_info(self, referral_code):
        """
        Retrieve information about a specific referral.

        Args:
            referral_code (str): The unique code associated with the referral.

        Returns:
            dict: Information about the referral, or None if not found.
        """
        return self.referrals.get(referral_code, None)

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Generate a referral code for a user
    user_id = "user123"
    referral_code = referral_program.generate_referral_code(user_id)
    print(f"Generated referral code: {referral_code}")

    # Add a referral
    try:
        referred_user_id = "user456"
        referral_program.add_referral(referral_code, referred_user_id)
        print(f"Referral added for {referred_user_id} with code {referral_code}.")
    except ValueError as e:
        print(f"Error adding referral: {e}")

    # Retrieve referral information
    referral_info = referral_program.get_referral_info(referral_code)
    if referral_info:
        print(f"Referral info: {referral_info}")
    else:
        print("Referral code not found.")
```
