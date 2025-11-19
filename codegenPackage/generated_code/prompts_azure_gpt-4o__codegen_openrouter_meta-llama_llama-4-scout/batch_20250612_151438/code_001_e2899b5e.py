"""
Generated Code Metadata:
========================
Original URL: https://elon-crypto.online
Prompt: Generate a script that simulates the referral bonus system for OctaFx VIP plans, ensuring it adheres to the zero-level referral bonus structure mentioned on the webpage.
Generated: DETERMINISTIC_e2899b5ef169c58b
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_bonus_system.py

class OctaFxVIPReferralSystem:
    """
    Simulates the referral bonus system for OctaFx VIP plans.

    The zero-level referral bonus structure is as follows:
    - The referrer and referee both receive a bonus when the referee signs up and meets certain conditions.
    """

    def __init__(self):
        # Initialize an empty dictionary to store users and their referral information
        self.users = {}

    def add_user(self, user_id, referrer_id=None):
        """
        Adds a new user to the system.

        Args:
            user_id (str): The unique ID of the user.
            referrer_id (str, optional): The ID of the user who referred this user. Defaults to None.

        Returns:
            bool: True if the user was added successfully, False otherwise.
        """
        if user_id in self.users:
            print(f"User {user_id} already exists in the system.")
            return False

        # Initialize the user's referral information
        self.users[user_id] = {"referrer_id": referrer_id, "has_signed_up": False}

        # If the user has a referrer, update the referrer's information
        if referrer_id and referrer_id in self.users:
            pass  # No immediate action needed

        print(f"User {user_id} added to the system.")
        return True

    def sign_up(self, user_id):
        """
        Simulates a user signing up and meeting the conditions for the referral bonus.

        Args:
            user_id (str): The ID of the user who signed up.

        Returns:
            bool: True if the user signed up successfully, False otherwise.
        """
        if user_id not in self.users:
            print(f"User {user_id} does not exist in the system.")
            return False

        # Update the user's sign-up status
        self.users[user_id]["has_signed_up"] = True

        # Award the referral bonus to the referrer and referee
        self.award_referral_bonus(user_id)

        print(f"User {user_id} has signed up.")
        return True

    def award_referral_bonus(self, user_id):
        """
        Awards the referral bonus to the referrer and referee.

        Args:
            user_id (str): The ID of the user who signed up.

        Returns:
            None
        """
        referrer_id = self.users[user_id]["referrer_id"]
        if referrer_id and self.users[referrer_id]["has_signed_up"]:
            print(f"Awarding referral bonus to user {referrer_id} and {user_id}.")
            # Implement the actual bonus award logic here (e.g., update account balances)
            pass

def main():
    referral_system = OctaFxVIPReferralSystem()

    # Example usage:
    referral_system.add_user("user1")
    referral_system.add_user("user2", "user1")
    referral_system.sign_up("user2")

if __name__ == "__main__":
    main()
```
