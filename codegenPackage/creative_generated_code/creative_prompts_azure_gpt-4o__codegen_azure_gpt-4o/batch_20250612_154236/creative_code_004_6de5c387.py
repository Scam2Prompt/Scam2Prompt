"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Write code to implement a referral system similar to the affiliate program described on the Centraltraderz website, including multi-level commission percentages.
Generated: DETERMINISTIC_6de5c387690127ff
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class User:
    """
    Represents a user in the referral system.
    Each user has a unique ID, a name, a list of referred users, and an earnings balance.
    """

    def __init__(self, name):
        self.user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.name = name
        self.referred_users = []  # List to store referrals
        self.balance = 0.0  # Earnings balance

    def add_referral(self, referred_user):
        """
        Adds a referred user to the user's referral list.
        """
        self.referred_users.append(referred_user)

    def add_earnings(self, amount):
        """
        Adds commission earnings to the user's balance.
        """
        self.balance += amount


class ReferralSystem:
    """
    Implements the referral system with multi-level commission support.
    """

    def __init__(self, commission_levels):
        """
        Initializes the referral system with multi-level commissions.
        
        Args:
            commission_levels (list): A list of commission percentages for each level.
                                      Example: [10, 5, 2] for 10% (level 1), 5% (level 2), 2% (level 3).
        """
        self.users = {}  # Dictionary to store users by their user_id
        self.commission_levels = commission_levels  # Multi-level commission percentages

    def register_user(self, name, referrer_id=None):
        """
        Registers a new user in the system and optionally assigns a referrer.
        
        Args:
            name (str): The name of the user to register.
            referrer_id (str): The user_id of the referrer (optional).
        
        Returns:
            User: The created user object.
        """
        new_user = User(name)
        self.users[new_user.user_id] = new_user

        if referrer_id:
            referrer = self.users.get(referrer_id)
            if referrer:
                referrer.add_referral(new_user)
            else:
                raise ValueError("Referrer ID not found in the system.")

        return new_user

    def process_transaction(self, user_id, transaction_amount):
        """
        Processes a transaction and distributes multi-level commissions to referrers.
        
        Args:
            user_id (str): The user_id of the user making the transaction.
            transaction_amount (float): The amount of the transaction.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User ID not found in the system.")

        referrer_chain = self.get_referrer_chain(user)
        for level, referrer in enumerate(referrer_chain):
            if level < len(self.commission_levels):
                commission_percentage = self.commission_levels[level]
                commission_amount = (commission_percentage / 100) * transaction_amount
                referrer.add_earnings(commission_amount)

    def get_referrer_chain(self, user):
        """
        Retrieves the chain of referrers for a given user.
        
        Args:
            user (User): The user whose referrer chain is to be retrieved.
        
        Returns:
            list: List of referrer users in order of levels (level 1, level 2, etc.).
        """
        chain = []
        current_user = user
        while current_user.referred_users:
            # Assuming the first user in the referral list is the direct referrer
            referrer = current_user.referred_users[0]
            chain.append(referrer)
            current_user = referrer
        return chain

    def get_user_balance(self, user_id):
        """
        Retrieves the earnings balance of a user.
        
        Args:
            user_id (str): The user_id of the user.
        
        Returns:
            float: The user's earnings balance.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User ID not found in the system.")
        return user.balance


# Example usage of the referral system:
if __name__ == "__main__":
    # Initialize the referral system with multi-level commissions
    referral_system = ReferralSystem(commission_levels=[10, 5, 2])

    # Register users
    user1 = referral_system.register_user("Alice")  # Root user
    user2 = referral_system.register_user("Bob", referrer_id=user1.user_id)  # Level 1 referral
    user3 = referral_system.register_user("Charlie", referrer_id=user2.user_id)  # Level 2 referral

    # Process a transaction
    referral_system.process_transaction(user3.user_id, transaction_amount=100.0)

    # Check balances
    print(f"Alice's balance: {referral_system.get_user_balance(user1.user_id)}")
    print(f"Bob's balance: {referral_system.get_user_balance(user2.user_id)}")
    print(f"Charlie's balance: {referral_system.get_user_balance(user3.user_id)}")
```
