"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Explain how to implement a loyalty rewards program using the CNK token for consumers in a coffee trading ecosystem, as detailed on the Crypto N' Kafe platform.
Generated: DETERMINISTIC_968a20a58fbaf913
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Setting up logging for better error tracking
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class LoyaltyRewardsProgram:
    def __init__(self):
        """Initialize the loyalty rewards program with an empty user database and reward token balance."""
        self.user_data = {}  # Store user information and rewards
        self.CNK_token_balance = 0  # Total CNK tokens available for rewards
    
    def add_user(self, user_id):
        """
        Adds a new user to the loyalty rewards program.
        
        Args:
            user_id (str): The unique identifier for the user.
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = {'points': 0, 'transactions': []}
            logging.info(f"User {user_id} added to the loyalty program.")
        else:
            logging.warning(f"User {user_id} already exists in the loyalty program.")
    
    def record_transaction(self, user_id, amount):
        """
        Records a transaction made by the user and awards loyalty points.
        
        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount spent in the transaction.
        
        Raises:
            ValueError: If the amount is less than or equal to zero or user does not exist.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        if user_id not in self.user_data:
            raise ValueError("User does not exist in the loyalty program.")
        
        self.user_data[user_id]['points'] += int(amount)  # 1 point per currency unit spent
        self.user_data[user_id]['transactions'].append(amount)
        logging.info(f"Transaction of {amount} recorded for user {user_id}. Points awarded: {int(amount)}.")

    def redeem_rewards(self, user_id, points_to_redeem):
        """
        Redeems loyalty points for CNK tokens.
        
        Args:
            user_id (str): The unique identifier for the user.
            points_to_redeem (int): The number of points the user wants to redeem.
        
        Raises:
            ValueError: If insufficient points or user does not exist.
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist in the loyalty program.")
        
        if points_to_redeem > self.user_data[user_id]['points']:
            raise ValueError("Insufficient points to redeem.")
        
        # Assuming 1 point = 0.01 CNK token
        cnk_tokens = points_to_redeem * 0.01
        self.user_data[user_id]['points'] -= points_to_redeem
        self.CNK_token_balance -= cnk_tokens  # Deduct from total CNK tokens available
        logging.info(f"{points_to_redeem} points redeemed for user {user_id}. CNK tokens awarded: {cnk_tokens}.")
    
    def get_user_info(self, user_id):
        """
        Retrieves user information including points and transactions.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Returns:
            dict: User data including points and transaction history.
        
        Raises:
            ValueError: If user does not exist.
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist in the loyalty program.")
        
        return self.user_data[user_id]

    def set_cnk_token_balance(self, amount):
        """
        Sets the total CNK token balance for rewards.
        
        Args:
            amount (float): Total amount of CNK tokens available for rewards.
        """
        if amount < 0:
            raise ValueError("CNK token balance cannot be negative.")
        self.CNK_token_balance = amount
        logging.info(f"CNK token balance set to: {self.CNK_token_balance}")

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyRewardsProgram()
    loyalty_program.set_cnk_token_balance(1000)  # Set initial CNK token balance
    loyalty_program.add_user("user123")
    loyalty_program.record_transaction("user123", 50)  # User spends $50
    loyalty_program.redeem_rewards("user123", 50)  # Redeem 50 points
    user_info = loyalty_program.get_user_info("user123")
    print(json.dumps(user_info, indent=2))  # Display user info in JSON format
```
