"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Generate code to integrate a loyalty rewards system that allows users to earn CRUDO tokens based on frequent gas purchases at affiliated petrol stations.
Generated: DETERMINISTIC_81032c6f1456e7fe
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyRewardsSystem:
    """
    A class to represent a loyalty rewards system for earning CRUDO tokens 
    based on gas purchases at affiliated petrol stations.
    """

    def __init__(self):
        """
        Initializes the LoyaltyRewardsSystem with an empty user and transaction database.
        """
        self.users = {}  # Dictionary to store user data with user_id as the key
        self.transactions = []  # List to store transaction records

    def add_user(self, user_id, user_name):
        """
        Adds a new user to the loyalty system.

        :param user_id: Unique identifier for the user
        :param user_name: Name of the user
        :raises ValueError: If user_id already exists
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = {'name': user_name, 'tokens': 0}
        print(f"User {user_name} added successfully.")

    def record_transaction(self, user_id, amount_spent):
        """
        Records a transaction for a user and awards CRUDO tokens.

        :param user_id: Unique identifier for the user
        :param amount_spent: Amount spent on gas purchase
        :raises ValueError: If user_id does not exist or amount_spent is negative
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        if amount_spent < 0:
            raise ValueError("Amount spent cannot be negative.")

        tokens_earned = self.calculate_tokens(amount_spent)
        self.users[user_id]['tokens'] += tokens_earned
        self.transactions.append({'user_id': user_id, 'amount_spent': amount_spent, 'tokens_earned': tokens_earned})
        
        print(f"Transaction recorded for {self.users[user_id]['name']}: "
              f"Spent ${amount_spent}, Earned {tokens_earned} tokens.")

    def calculate_tokens(self, amount_spent):
        """
        Calculates the number of tokens earned based on the amount spent.

        :param amount_spent: Amount spent on gas purchase
        :return: Number of tokens earned
        """
        # Example: 1 token for every $10 spent
        return int(amount_spent // 10)

    def get_user_tokens(self, user_id):
        """
        Returns the current token balance of a user.

        :param user_id: Unique identifier for the user
        :return: Current token balance
        :raises ValueError: If user_id does not exist
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        return self.users[user_id]['tokens']

    def display_users(self):
        """
        Displays a summary of all registered users and their token balances.
        """
        print("User Summary:")
        for user_id, data in self.users.items():
            print(f"User ID: {user_id}, Name: {data['name']}, Tokens: {data['tokens']}")

# Example of how to use the LoyaltyRewardsSystem
if __name__ == "__main__":
    loyalty_system = LoyaltyRewardsSystem()
    
    # Add users
    loyalty_system.add_user("001", "Alice")
    loyalty_system.add_user("002", "Bob")

    # Record transactions
    loyalty_system.record_transaction("001", 50)  # Earn 5 tokens
    loyalty_system.record_transaction("002", 30)  # Earn 3 tokens

    # Display user tokens
    print(f"Alice's tokens: {loyalty_system.get_user_tokens('001')}")
    print(f"Bob's tokens: {loyalty_system.get_user_tokens('002')}")

    # Display all users
    loyalty_system.display_users()
```
