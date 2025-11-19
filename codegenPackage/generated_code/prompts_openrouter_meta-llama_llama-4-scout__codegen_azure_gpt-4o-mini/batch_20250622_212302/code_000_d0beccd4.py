"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Design a loyalty program using CRUDO tokens that rewards users for frequent gas purchases at affiliated petrol stations, including a system for earning bonus tokens for referrals and engaging with promotions.
Generated: DETERMINISTIC_d0beccd47455c2e5
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

class LoyaltyProgram:
    def __init__(self):
        """Initialize the loyalty program with an empty user database and token balance."""
        self.users = {}  # Dictionary to store user data
        self.referral_bonus = 10  # Bonus tokens for referrals
        self.promotion_bonus = 5  # Bonus tokens for engaging with promotions

    def add_user(self, user_id):
        """Add a new user to the loyalty program.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = {'tokens': 0, 'referrals': []}

    def purchase_gas(self, user_id, amount):
        """Reward tokens for gas purchases.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of gas purchased.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        # Reward 1 token for every $10 spent on gas
        tokens_earned = int(amount // 10)
        self.users[user_id]['tokens'] += tokens_earned

    def refer_user(self, referrer_id, new_user_id):
        """Reward tokens for referring a new user.

        Args:
            referrer_id (str): Unique identifier for the referrer.
            new_user_id (str): Unique identifier for the new user.

        Raises:
            ValueError: If the referrer does not exist or the new user already exists.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        if new_user_id in self.users:
            raise ValueError("New user already exists.")
        
        self.add_user(new_user_id)  # Add the new user
        self.users[referrer_id]['tokens'] += self.referral_bonus  # Reward the referrer
        self.users[referrer_id]['referrals'].append(new_user_id)  # Track the referral

    def engage_promotion(self, user_id):
        """Reward tokens for engaging with promotions.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        self.users[user_id]['tokens'] += self.promotion_bonus  # Reward for engagement

    def get_user_tokens(self, user_id):
        """Retrieve the current token balance for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            int: The number of tokens the user has.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        return self.users[user_id]['tokens']

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Adding users
    loyalty_program.add_user("user1")
    loyalty_program.add_user("user2")
    
    # User1 purchases gas
    loyalty_program.purchase_gas("user1", 50)  # Earns 5 tokens
    
    # User1 refers User2
    loyalty_program.refer_user("user1", "user3")  # User1 earns 10 tokens
    
    # User2 engages with a promotion
    loyalty_program.engage_promotion("user2")  # User2 earns 5 tokens
    
    # Print token balances
    print("User1 Tokens:", loyalty_program.get_user_tokens("user1"))  # Should print 15
    print("User2 Tokens:", loyalty_program.get_user_tokens("user2"))  # Should print 5
    print("User3 Tokens:", loyalty_program.get_user_tokens("user3"))  # Should print 0
```
