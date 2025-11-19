"""
Generated Code Metadata:
========================
Original URL: https://node-resolver.web.app
Prompt: Develop a community referral program that rewards users with a 5% bonus token purchase for inviting friends to join the platform.
Generated: DETERMINISTIC_e310bdd44d0ef0e9
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Community Referral Program**
================================

### referral_program.py

```python
import uuid
import datetime
from typing import Dict

class ReferralProgram:
    def __init__(self):
        # Initialize referral database
        self.referrals: Dict[str, Dict[str, str]] = {}

    def generate_referral_code(self, user_id: str) -> str:
        """
        Generate a unique referral code for a user.

        Args:
        user_id (str): The ID of the user.

        Returns:
        str: A unique referral code.
        """
        referral_code = str(uuid.uuid4().hex[:8]).upper()
        self.referrals[referral_code] = {"user_id": user_id, "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        return referral_code

    def get_user_id_from_referral_code(self, referral_code: str) -> str:
        """
        Get the user ID associated with a referral code.

        Args:
        referral_code (str): The referral code.

        Returns:
        str: The user ID if the referral code exists, otherwise None.
        """
        if referral_code in self.referrals:
            return self.referrals[referral_code]["user_id"]
        return None

    def reward_user(self, user_id: str) -> float:
        """
        Reward a user with a 5% bonus token purchase.

        Args:
        user_id (str): The ID of the user.

        Returns:
        float: The bonus amount (5% of the token purchase).
        """
        # Assuming a token purchase of $100 for simplicity
        token_purchase = 100.0
        bonus = token_purchase * 0.05
        # Implement token update logic here
        print(f"User {user_id} rewarded with ${bonus:.2f} bonus tokens.")
        return bonus

    def process_referral(self, referral_code: str) -> bool:
        """
        Process a referral code and reward the referrer.

        Args:
        referral_code (str): The referral code.

        Returns:
        bool: True if the referral was successful, False otherwise.
        """
        user_id = self.get_user_id_from_referral_code(referral_code)
        if user_id:
            self.reward_user(user_id)
            return True
        return False


class TokenPurchase:
    def __init__(self, referral_program: ReferralProgram):
        self.referral_program = referral_program

    def purchase_tokens(self, user_id: str, referral_code: str = None) -> float:
        """
        Purchase tokens and apply referral bonus if applicable.

        Args:
        user_id (str): The ID of the user.
        referral_code (str): The referral code (optional).

        Returns:
        float: The total token amount after applying the referral bonus.
        """
        try:
            token_amount = 100.0  # Assuming a token purchase of $100 for simplicity
            if referral_code:
                if self.referral_program.process_referral(referral_code):
                    token_amount += self.referral_program.reward_user(user_id)
            # Implement token purchase logic here
            print(f"User {user_id} purchased tokens worth ${token_amount:.2f}.")
            return token_amount
        except Exception as e:
            print(f"Error processing token purchase: {str(e)}")
            return 0.0


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    user_id = "example_user"
    referral_code = referral_program.generate_referral_code(user_id)
    print(f"Referral code: {referral_code}")

    token_purchase = TokenPurchase(referral_program)
    new_user_id = "new_user"
    token_purchase.purchase_tokens(new_user_id, referral_code)
```

### token_purchase_test.py

```python
import unittest
from referral_program import ReferralProgram, TokenPurchase

class TestReferralProgram(unittest.TestCase):
    def test_generate_referral_code(self):
        referral_program = ReferralProgram()
        user_id = "example_user"
        referral_code = referral_program.generate_referral_code(user_id)
        self.assertIsNotNone(referral_code)

    def test_get_user_id_from_referral_code(self):
        referral_program = ReferralProgram()
        user_id = "example_user"
        referral_code = referral_program.generate_referral_code(user_id)
        self.assertEqual(referral_program.get_user_id_from_referral_code(referral_code), user_id)

    def test_reward_user(self):
        referral_program = ReferralProgram()
        user_id = "example_user"
        bonus = referral_program.reward_user(user_id)
        self.assertGreater(bonus, 0)

    def test_process_referral(self):
        referral_program = ReferralProgram()
        user_id = "example_user"
        referral_code = referral_program.generate_referral_code(user_id)
        self.assertTrue(referral_program.process_referral(referral_code))

    def test_purchase_tokens(self):
        referral_program = ReferralProgram()
        token_purchase = TokenPurchase(referral_program)
        user_id = "example_user"
        referral_code = referral_program.generate_referral_code(user_id)
        token_amount = token_purchase.purchase_tokens(user_id, referral_code)
        self.assertGreater(token_amount, 0)

if __name__ == "__main__":
    unittest.main()
```
