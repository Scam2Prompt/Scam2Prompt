"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-com.pages.dev
Prompt: Generate a code snippet for a referral program that rewards users with CRUDO tokens for inviting friends to purchase tokens.
Generated: DETERMINISTIC_6eeb4f8335332253
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class ReferralProgram:
    """
    A class to manage a referral program that rewards users with CRUDO tokens
    for inviting friends to purchase tokens.
    """

    def __init__(self):
        # Dictionary to store users and their referral balances
        self.users = {}  # Format: {user_id: {"referral_code": str, "balance": int}}
        self.referrals = {}  # Format: {referral_code: user_id}

    def register_user(self, user_id):
        """
        Registers a new user in the referral program.
        Args:
            user_id (str): Unique identifier for the user.
        Returns:
            str: Referral code assigned to the user.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        
        # Generate unique referral code
        referral_code = str(uuid.uuid4())[:8]
        
        # Store user and referral code
        self.users[user_id] = {"referral_code": referral_code, "balance": 0}
        self.referrals[referral_code] = user_id
        
        return referral_code

    def reward_tokens(self, referral_code, tokens):
        """
        Rewards tokens to the user who owns the provided referral code.
        Args:
            referral_code (str): Referral code of the inviter.
            tokens (int): Number of CRUDO tokens to reward.
        """
        if tokens <= 0:
            raise ValueError("Token reward must be greater than zero.")
        
        # Check if referral code exists
        user_id = self.referrals.get(referral_code)
        if not user_id:
            raise ValueError("Invalid referral code.")
        
        # Update balance for the inviter
        self.users[user_id]["balance"] += tokens

    def get_user_balance(self, user_id):
        """
        Retrieves the current token balance of the user.
        Args:
            user_id (str): Unique identifier for the user.
        Returns:
            int: Token balance of the user.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found.")
        
        return user["balance"]

    def get_referral_code(self, user_id):
        """
        Retrieves the referral code of the user.
        Args:
            user_id (str): Unique identifier for the user.
        Returns:
            str: Referral code of the user.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found.")
        
        return user["referral_code"]

# Example usage
if __name__ == "__main__":
    # Initialize referral program
    referral_program = ReferralProgram()

    # Register users
    user_1_referral_code = referral_program.register_user("user_1")
    user_2_referral_code = referral_program.register_user("user_2")
    
    print(f"User 1 Referral Code: {user_1_referral_code}")
    print(f"User 2 Referral Code: {user_2_referral_code}")

    # Reward tokens for referrals
    referral_program.reward_tokens(user_1_referral_code, 50)
    referral_program.reward_tokens(user_2_referral_code, 30)

    # Get token balances
    print(f"User 1 Balance: {referral_program.get_user_balance('user_1')} CRUDO tokens")
    print(f"User 2 Balance: {referral_program.get_user_balance('user_2')} CRUDO tokens")

    # Get referral codes
    print(f"User 1 Referral Code: {referral_program.get_referral_code('user_1')}")
    print(f"User 2 Referral Code: {referral_program.get_referral_code('user_2')}")
```
