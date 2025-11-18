"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-claiming.pages.dev
Prompt: Generate code to implement a referral system for a cryptocurrency presale where users receive 50% extra tokens for purchases over $25, and track top referrers for monthly rewards, as outlined in MoonBag's referral program.
Generated: DETERMINISTIC_df47e3d54e0fa70b
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

class User:
    """Represents a user in the referral system."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.referrals = []  # List to track referred users
        self.tokens = 0      # User's total tokens earned

    def add_referral(self, referral_user: 'User'):
        """Add a referred user to this user's referral list."""
        self.referrals.append(referral_user)

    def purchase(self, amount: float) -> int:
        """Process a purchase and calculate the tokens to be awarded."""
        if amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")

        # Base token calculation (1 token per dollar spent)
        tokens_awarded = int(amount)

        # Award extra tokens for purchases over $25
        if amount > 25:
            extra_tokens = int(0.5 * tokens_awarded)  # 50% extra tokens
            tokens_awarded += extra_tokens

        self.tokens += tokens_awarded
        return tokens_awarded


class ReferralSystem:
    """Manages the referral system and tracks users and their referrals."""
    
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id
        self.top_referrers = []  # List to track top referrers for rewards

    def register_user(self, user_id: str) -> User:
        """Register a new user in the system."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        user = User(user_id)
        self.users[user_id] = user
        return user

    def refer_user(self, referrer_id: str, new_user_id: str):
        """Link a new user to their referrer."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        if new_user_id in self.users:
            raise ValueError("New user ID already exists.")

        new_user = self.register_user(new_user_id)
        referrer = self.users[referrer_id]
        referrer.add_referral(new_user)

    def process_purchase(self, user_id: str, amount: float):
        """Handle a user's purchase and update the referral system."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")

        user = self.users[user_id]
        tokens_awarded = user.purchase(amount)
        self.track_top_referrers(user)

        return tokens_awarded

    def track_top_referrers(self, user: User):
        """Update the list of top referrers based on total tokens earned by referrals."""
        # Update the total tokens earned through referrals
        for referral in user.referrals:
            user.tokens += referral.tokens

        self.update_top_referrers(user)

    def update_top_referrers(self, user: User):
        """Update the top referrers list based on tokens earned."""
        self.top_referrers.append((user.user_id, user.tokens))
        self.top_referrers = sorted(self.top_referrers, key=lambda x: x[1], reverse=True)[:10]  # Keep top 10


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Register users
    user1 = referral_system.register_user("user1")
    user2 = referral_system.register_user("user2")

    # User1 refers User2
    referral_system.refer_user("user1", "user2")

    # Process purchases
    tokens_earned_user2 = referral_system.process_purchase("user2", 30)  # User2 purchases $30
    print(f"Tokens earned by User2: {tokens_earned_user2}")

    # Display top referrers
    print("Top Referrers:", referral_system.top_referrers)
```
