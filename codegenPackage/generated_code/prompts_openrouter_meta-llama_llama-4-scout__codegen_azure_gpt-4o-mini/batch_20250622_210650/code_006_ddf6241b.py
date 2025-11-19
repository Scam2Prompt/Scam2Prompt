"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Create a referral program in Python that rewards customers for referring new clients to a digital marketing agency in New Zealand.
Generated: DETERMINISTIC_ddf6241b1dd42173
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta

class ReferralProgram:
    def __init__(self):
        # Initialize the referral program with an empty list of referrals
        self.referrals = {}
        self.rewards = {}
        self.reward_amount = 50  # Reward amount in NZD for each successful referral

    def add_referral(self, referrer_email, new_client_email):
        """
        Add a new referral to the program.

        :param referrer_email: Email of the referrer
        :param new_client_email: Email of the new client being referred
        :raises ValueError: If the referrer or new client email is invalid
        """
        if not self._is_valid_email(referrer_email) or not self._is_valid_email(new_client_email):
            raise ValueError("Invalid email address provided.")

        referral_id = str(uuid.uuid4())
        self.referrals[referral_id] = {
            'referrer': referrer_email,
            'new_client': new_client_email,
            'date': datetime.now(),
            'rewarded': False
        }
        print(f"Referral added: {referral_id}")

    def reward_referral(self, referral_id):
        """
        Reward the referrer for a successful referral.

        :param referral_id: Unique ID of the referral
        :raises KeyError: If the referral ID does not exist
        :raises ValueError: If the referral has already been rewarded
        """
        if referral_id not in self.referrals:
            raise KeyError("Referral ID does not exist.")

        referral = self.referrals[referral_id]
        if referral['rewarded']:
            raise ValueError("This referral has already been rewarded.")

        # Mark the referral as rewarded
        referral['rewarded'] = True
        self.rewards[referral['referrer']] = self.rewards.get(referral['referrer'], 0) + self.reward_amount
        print(f"Rewarded {referral['referrer']} with {self.reward_amount} NZD for referral ID: {referral_id}")

    def get_referral_status(self, referral_id):
        """
        Get the status of a referral.

        :param referral_id: Unique ID of the referral
        :return: Dictionary containing referral details
        :raises KeyError: If the referral ID does not exist
        """
        if referral_id not in self.referrals:
            raise KeyError("Referral ID does not exist.")
        return self.referrals[referral_id]

    def get_total_rewards(self, email):
        """
        Get the total rewards earned by a referrer.

        :param email: Email of the referrer
        :return: Total rewards earned
        """
        return self.rewards.get(email, 0)

    @staticmethod
    def _is_valid_email(email):
        """
        Validate the email format.

        :param email: Email address to validate
        :return: True if valid, False otherwise
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Adding referrals
    try:
        referral_program.add_referral("referrer@example.com", "newclient@example.com")
        referral_program.add_referral("referrer@example.com", "anotherclient@example.com")
        
        # Rewarding a referral
        referral_id = list(referral_program.referrals.keys())[0]
        referral_program.reward_referral(referral_id)
        
        # Checking total rewards
        total_rewards = referral_program.get_total_rewards("referrer@example.com")
        print(f"Total rewards for referrer@example.com: {total_rewards} NZD")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
