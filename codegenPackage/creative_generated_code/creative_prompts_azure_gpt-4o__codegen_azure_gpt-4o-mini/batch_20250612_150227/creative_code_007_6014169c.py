"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharecoininvestment.org
Prompt: Write code to implement a referral bonus system for new account registrations, similar to the onboarding process described on sharecoininvestment.org.
Generated: DETERMINISTIC_6014169cca138d0f
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_bonus.py

class User:
    """
    Represents a user in the referral bonus system.
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.referral_code = self.generate_referral_code()
        self.referrals = []
        self.bonus = 0

    def generate_referral_code(self):
        """
        Generates a unique referral code for the user.
        """
        return f"{self.username}-{hash(self.username)}"

    def add_referral(self, referral_user):
        """
        Adds a new referral to the user's list of referrals.
        Args:
            referral_user (User): The new user that was referred.
        """
        if referral_user not in self.referrals:
            self.referrals.append(referral_user)
            self.bonus += 10  # Increment bonus for each successful referral
            print(f"Referral added: {referral_user.username}. Bonus updated to {self.bonus}.")

    def get_bonus(self):
        """
        Returns the total referral bonus for the user.
        """
        return self.bonus


class ReferralSystem:
    """
    Handles the referral system for user registrations.
    """

    def __init__(self):
        self.users = {}

    def register_user(self, username, email, referral_code=None):
        """
        Registers a new user and processes any referral bonuses.
        Args:
            username (str): The username of the new user.
            email (str): The email of the new user.
            referral_code (str, optional): The referral code used to register.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        new_user = User(username, email)
        self.users[username] = new_user
        
        if referral_code:
            referrer = self.find_referrer(referral_code)
            if referrer:
                referrer.add_referral(new_user)
                print(f"{new_user.username} registered with referral code {referral_code}.")
            else:
                print("Referral code not found. No bonus awarded.")
        else:
            print(f"{new_user.username} registered without a referral code.")

    def find_referrer(self, referral_code):
        """
        Finds a user by their referral code.
        Args:
            referral_code (str): The referral code to search for.
        Returns:
            User: The user who has the given referral code, or None if not found.
        """
        for user in self.users.values():
            if user.referral_code == referral_code:
                return user
        return None


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Registering users
    referral_system.register_user("alice", "alice@example.com")
    referral_system.register_user("bob", "bob@example.com", referral_code="alice-1234567890123456789")
    referral_system.register_user("charlie", "charlie@example.com", referral_code="nonexistent-123")

    # Check bonuses
    print(f"Alice's bonus: {referral_system.users['alice'].get_bonus()}")  # Should be 10
    print(f"Bob's bonus: {referral_system.users['bob'].get_bonus()}")      # Should be 0
    print(f"Charlie's bonus: {referral_system.users['charlie'].get_bonus()}")  # Should be 0
```

This code implements a referral bonus system for new account registrations, ensuring clean structure, proper error handling, and adherence to best practices.
