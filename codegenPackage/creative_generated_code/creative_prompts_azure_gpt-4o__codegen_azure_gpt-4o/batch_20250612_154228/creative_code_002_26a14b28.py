"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Generate code for a loyalty program system that tracks user activity and calculates rewards, such as cashback, similar to BaxBet's loyalty features.
Generated: DETERMINISTIC_26a14b2887bcd263
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class LoyaltyProgram:
    """
    A loyalty program system to track user activity and calculate rewards such as cashback.
    """

    def __init__(self):
        # Dictionary to store user data: {user_id: {"transactions": [], "reward_points": 0}}
        self.user_data = {}

    def register_user(self, user_id):
        """
        Registers a new user in the loyalty program.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.user_data:
            raise ValueError("User is already registered.")
        self.user_data[user_id] = {"transactions": [], "reward_points": 0}

    def add_transaction(self, user_id, amount):
        """
        Adds a transaction for a user and calculates reward points.
        :param user_id: Unique identifier for the user.
        :param amount: Transaction amount (float).
        """
        if user_id not in self.user_data:
            raise ValueError("User not found. Please register the user first.")
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Log the transaction
        transaction = {
            "amount": amount,
            "date": datetime.datetime.now(),
        }
        self.user_data[user_id]["transactions"].append(transaction)

        # Calculate rewards (e.g., 1 reward point for every $10 spent)
        reward_points = int(amount // 10)
        self.user_data[user_id]["reward_points"] += reward_points

    def get_user_rewards(self, user_id):
        """
        Retrieves the total reward points for a user.
        :param user_id: Unique identifier for the user.
        :return: Total reward points (int).
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        return self.user_data[user_id]["reward_points"]

    def get_user_transactions(self, user_id):
        """
        Retrieves all transactions for a user.
        :param user_id: Unique identifier for the user.
        :return: List of transactions.
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        return self.user_data[user_id]["transactions"]

    def calculate_cashback(self, user_id):
        """
        Calculates cashback for a user based on their total reward points.
        Example: 1% cashback for every 100 reward points.
        :param user_id: Unique identifier for the user.
        :return: Cashback amount (float).
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        
        reward_points = self.user_data[user_id]["reward_points"]
        cashback_rate = 0.01  # 1% cashback
        cashback = (reward_points // 100) * cashback_rate
        return round(cashback, 2)


# Example usage
if __name__ == "__main__":
    try:
        program = LoyaltyProgram()
        
        # Register users
        program.register_user("user123")
        program.register_user("user456")
        
        # Add transactions
        program.add_transaction("user123", 120.50)
        program.add_transaction("user123", 45.00)
        program.add_transaction("user456", 300.00)
        
        # Get reward points
        print("User123 Reward Points:", program.get_user_rewards("user123"))
        print("User456 Reward Points:", program.get_user_rewards("user456"))
        
        # Get transactions
        print("User123 Transactions:", program.get_user_transactions("user123"))
        print("User456 Transactions:", program.get_user_transactions("user456"))
        
        # Calculate cashback
        print("User123 Cashback:", program.calculate_cashback("user123"))
        print("User456 Cashback:", program.calculate_cashback("user456"))
    
    except Exception as e:
        print(f"Error: {e}")
```
