"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Write code to manage referrals for a training program, including tracking enrollments and rewards, similar to the referral system described on SMART Training Resources' website.
Generated: DETERMINISTIC_944bbb8ce05baa02
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Referral:
    """
    Class to represent a referral for the training program.
    """
    def __init__(self, referrer_id: str, referred_email: str):
        self.referral_id = str(uuid.uuid4())  # Unique identifier for the referral
        self.referrer_id = referrer_id        # ID of the referrer
        self.referred_email = referred_email    # Email of the referred person
        self.enrollment_date: Optional[datetime] = None  # Date of enrollment
        self.rewarded: bool = False            # Reward status for the referral

    def enroll(self):
        """
        Method to mark the referred person as enrolled.
        """
        self.enrollment_date = datetime.now()

    def reward_referrer(self):
        """
        Method to mark the referral as rewarded.
        """
        if self.enrollment_date:
            self.rewarded = True
        else:
            raise ValueError("Referral must be enrolled before rewarding.")


class ReferralManager:
    """
    Class to manage referrals and enrollments in the training program.
    """
    def __init__(self):
        self.referrals: Dict[str, Referral] = {}  # Store referrals by ID

    def create_referral(self, referrer_id: str, referred_email: str) -> Referral:
        """
        Create a new referral.
        
        Args:
            referrer_id (str): The ID of the referrer.
            referred_email (str): The email of the referred person.
        
        Returns:
            Referral: The created referral object.
        """
        referral = Referral(referrer_id, referred_email)
        self.referrals[referral.referral_id] = referral
        return referral

    def enroll_referral(self, referral_id: str):
        """
        Enroll a referred person using their referral ID.
        
        Args:
            referral_id (str): The ID of the referral to enroll.
        
        Raises:
            KeyError: If the referral ID does not exist.
        """
        try:
            referral = self.referrals[referral_id]
            referral.enroll()
        except KeyError:
            raise KeyError(f"Referral ID {referral_id} does not exist.")

    def reward_referral(self, referral_id: str):
        """
        Reward the referrer for a successful enrollment.
        
        Args:
            referral_id (str): The ID of the referral to reward.
        
        Raises:
            KeyError: If the referral ID does not exist.
        """
        try:
            referral = self.referrals[referral_id]
            referral.reward_referrer()
        except KeyError:
            raise KeyError(f"Referral ID {referral_id} does not exist.")
        except ValueError as e:
            raise ValueError(f"Cannot reward referral: {e}")

    def get_referral_status(self, referral_id: str) -> Dict:
        """
        Get the status of a referral.
        
        Args:
            referral_id (str): The ID of the referral to check.
        
        Returns:
            Dict: A dictionary containing referral details.
        
        Raises:
            KeyError: If the referral ID does not exist.
        """
        try:
            referral = self.referrals[referral_id]
            return {
                "referral_id": referral.referral_id,
                "referrer_id": referral.referrer_id,
                "referred_email": referral.referred_email,
                "enrollment_date": referral.enrollment_date,
                "rewarded": referral.rewarded,
            }
        except KeyError:
            raise KeyError(f"Referral ID {referral_id} does not exist.")
```
