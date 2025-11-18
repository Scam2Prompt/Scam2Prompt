"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getretiksale.pages.dev
Prompt: Generate code for implementing a tier-based rewards system for Retik DeFi debit cards, including cashback percentages for Silver, Gold, and Diamond tiers.
Generated: DETERMINISTIC_16a624a715e92b22
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TieredRewardsSystem:
    """
    A class to represent a tier-based rewards system for Retik DeFi debit cards.
    """

    # Define cashback percentages for each tier
    CASHBACK_PERCENTAGES = {
        'Silver': 0.01,  # 1% cashback
        'Gold': 0.02,    # 2% cashback
        'Diamond': 0.03   # 3% cashback
    }

    def __init__(self):
        """
        Initialize the rewards system with no users.
        """
        self.users = {}

    def add_user(self, user_id, tier):
        """
        Adds a user with a specified tier to the rewards system.

        :param user_id: Unique identifier for the user
        :param tier: User's tier (Silver, Gold, or Diamond)
        :raises ValueError: If the tier is not valid
        """
        if tier not in self.CASHBACK_PERCENTAGES:
            raise ValueError("Invalid tier. Must be one of: Silver, Gold, Diamond.")
        
        self.users[user_id] = {
            'tier': tier,
            'cashback_accumulated': 0.0
        }
    
    def calculate_cashback(self, user_id, amount_spent):
        """
        Calculate cashback for a user based on their tier and amount spent.

        :param user_id: Unique identifier for the user
        :param amount_spent: Amount spent by the user
        :raises KeyError: If the user does not exist
        :return: The cashback amount earned in this transaction
        """
        if user_id not in self.users:
            raise KeyError("User not found.")
        
        tier = self.users[user_id]['tier']
        cashback_percentage = self.CASHBACK_PERCENTAGES[tier]
        cashback_amount = amount_spent * cashback_percentage
        
        # Update the user's accumulated cashback
        self.users[user_id]['cashback_accumulated'] += cashback_amount
        
        return cashback_amount

    def get_user_cashback(self, user_id):
        """
        Retrieve the total cashback accumulated by a user.

        :param user_id: Unique identifier for the user
        :raises KeyError: If the user does not exist
        :return: The total cashback accumulated by the user
        """
        if user_id not in self.users:
            raise KeyError("User not found.")
        
        return self.users[user_id]['cashback_accumulated']


# Example usage
if __name__ == "__main__":
    rewards_system = TieredRewardsSystem()
    
    # Add users to the rewards system
    rewards_system.add_user('user1', 'Gold')
    rewards_system.add_user('user2', 'Silver')

    # Calculate cashback for user1
    try:
        cashback = rewards_system.calculate_cashback('user1', 100.0)
        print(f"User1 Cashback Earned: ${cashback:.2f}")
    except Exception as e:
        print(f"Error: {e}")

    # Get total cashback accumulated by user2
    try:
        total_cashback_user2 = rewards_system.get_user_cashback('user2')
        print(f"User2 Total Cashback: ${total_cashback_user2:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
