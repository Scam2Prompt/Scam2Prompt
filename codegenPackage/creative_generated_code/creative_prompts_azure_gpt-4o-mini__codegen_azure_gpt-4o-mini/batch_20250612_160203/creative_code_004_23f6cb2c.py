"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Write a code example demonstrating how to implement a referral program feature in a trading platform similar to BitBullMiningPro.
Generated: DETERMINISTIC_23f6cb2c93b15233
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the trading platform.
    Each user can have a referral code and can refer other users.
    """
    def __init__(self, username, referral_code=None):
        self.username = username
        self.referral_code = referral_code or self.generate_referral_code()
        self.referrals = []

    def generate_referral_code(self):
        """
        Generate a unique referral code for the user.
        The code is based on the username for simplicity.
        """
        return f"REF-{self.username}"

    def refer_user(self, new_user):
        """
        Adds a new user to the list of referrals.
        A user can only refer a user if they provide a valid referral code.
        """
        if new_user.referral_code == self.referral_code:
            self.referrals.append(new_user)
            return True
        return False


class ReferralProgram:
    """
    Manages the referral program functionality.
    Handles user registrations and tracks referrals.
    """
    def __init__(self):
        self.users = {}

    def register_user(self, username, referral_code=None):
        """
        Register a new user with an optional referral code.
        If the referral code is valid, associate the new user with the referrer.
        """
        try:
            if username in self.users:
                raise ValueError("Username already exists.")

            new_user = User(username, referral_code)

            # If referral code is provided, find the referrer
            if referral_code and referral_code in self.users:
                referrer = self.users[referral_code]
                if not referrer.refer_user(new_user):
                    raise ValueError("Invalid referral code.")

            # Store the new user
            self.users[new_user.referral_code] = new_user
            print(f"User {username} registered successfully with referral code: {new_user.referral_code}")
            return new_user

        except Exception as e:
            print(f"Error registering user: {e}")
            return None

    def get_referrals(self, referral_code):
        """
        Return the list of referrals for a given referral code.
        """
        if referral_code in self.users:
            return self.users[referral_code].referrals
        else:
            print("Referral code not found.")
            return []


# Example usage
def main():
    referral_program = ReferralProgram()

    # Register a user without a referral
    user1 = referral_program.register_user("Alice")

    # Register a user with a referral
    user2 = referral_program.register_user("Bob", referral_code=user1.referral_code)

    # Attempt to register a user with an invalid referral code
    user3 = referral_program.register_user("Charlie", referral_code="INVALID-CODE")

    # Retrieve referrals for user1
    referrals_for_user1 = referral_program.get_referrals(user1.referral_code)
    print(f"Referrals for {user1.username}: {[user.username for user in referrals_for_user1]}")

if __name__ == "__main__":
    main()
```
