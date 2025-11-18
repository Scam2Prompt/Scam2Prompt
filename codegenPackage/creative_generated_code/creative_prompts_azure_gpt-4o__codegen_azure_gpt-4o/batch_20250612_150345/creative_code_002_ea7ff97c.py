"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: Generate code for a referral program system that tracks user referrals and calculates referral bonuses, as described on Zadepositslot's referral program page.
Generated: DETERMINISTIC_ea7ff97c2b7864aa
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for a referral program system that tracks user referrals and calculates referral bonuses:

```python
from typing import Dict, List
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralProgram:
    def __init__(self):
        # Dictionary to store user data
        # Example structure: {'user_id': {'referrer': 'referrer_id', 'bonus': 0.0}}
        self.users = {}
        # Bonus amount for each referral
        self.referral_bonus = 10.0

    def register_user(self, user_id: str, referrer_id: str = None) -> bool:
        """
        Registers a new user in the system. If a referrer is provided, it tracks the referral.

        :param user_id: Unique ID for the new user.
        :param referrer_id: Unique ID of the referrer (if any).
        :return: True if registration is successful, False if user_id already exists.
        """
        if user_id in self.users:
            logging.warning(f"User {user_id} already exists. Registration skipped.")
            return False  # User already exists

        # Register the user with optional referrer
        self.users[user_id] = {'referrer': referrer_id, 'bonus': 0.0}
        logging.info(f"User {user_id} registered successfully.")
        
        # If there is a valid referrer, award the referrer a bonus
        if referrer_id and referrer_id in self.users:
            self._award_bonus(referrer_id)

        return True

    def _award_bonus(self, referrer_id: str):
        """
        Private method to award a bonus to the referrer.

        :param referrer_id: The user ID of the referrer to award.
        """
        if referrer_id in self.users:
            self.users[referrer_id]['bonus'] += self.referral_bonus
            logging.info(f"Referrer {referrer_id} awarded ${self.referral_bonus} bonus.")
        else:
            logging.error(f"Referrer ID {referrer_id} not found. Bonus not awarded.")

    def get_user_info(self, user_id: str) -> Dict[str, str]:
        """
        Retrieves user information including the referrer and current bonus.

        :param user_id: The user ID to retrieve information for.
        :return: A dictionary containing the user's referrer and bonus. Empty dictionary if user not found.
        """
        if user_id in self.users:
            return self.users[user_id]
        else:
            logging.warning(f"User {user_id} not found.")
            return {}

    def calculate_total_bonus(self) -> float:
        """
        Calculates the total bonus distributed across all users.

        :return: Total bonus amount.
        """
        total_bonus = sum(user['bonus'] for user in self.users.values())
        logging.info(f"Total bonus distributed: ${total_bonus}")
        return total_bonus

    def list_users(self) -> List[str]:
        """
        Returns a list of all registered user IDs.

        :return: List of user IDs.
        """
        return list(self.users.keys())


# Example usage:
if __name__ == "__main__":
    program = ReferralProgram()
    
    # Register users with and without referrers
    program.register_user("user1")  # No referrer
    program.register_user("user2", "user1")  # user2 was referred by user1
    program.register_user("user3", "user1")  # user3 was referred by user1
    program.register_user("user4", "user2")  # user4 was referred by user2
    
    # Print user details
    print("User Details:")
    for user_id in program.list_users():
        print(f"{user_id}: {program.get_user_info(user_id)}")
    
    # Calculate total bonus distributed
    print(f"Total Bonus Distributed: ${program.calculate_total_bonus()}")
```

This Python code is a clean, production-ready implementation of a referral program system with proper comments, error handling, and logging for debugging purposes.
