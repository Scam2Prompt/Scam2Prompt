"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Create a script to simulate the payout system on Coinmining, ensuring users can withdraw their earnings once they meet the minimum withdrawal threshold.
Generated: DETERMINISTIC_0dc0ba0689802bad
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    def __init__(self, username):
        """
        Initializes a new user with a username, balance, and minimum withdrawal threshold.
        
        Args:
            username (str): The username of the new user.
        """
        self.username = username
        self.balance = 0.0  # User's balance in cryptocurrency
        self.min_withdrawal = 50.0  # Minimum withdrawal threshold

    def earn(self, amount):
        """
        Simulates the user earning a certain amount of cryptocurrency.
        
        Args:
            amount (float): The amount of cryptocurrency earned.
        """
        if amount <= 0:
            raise ValueError("Amount earned must be positive.")
        
        self.balance += amount
        print(f"{self.username} earned {amount}. New balance: {self.balance}")

    def withdraw(self):
        """
        Allows the user to withdraw their earnings if they meet the minimum threshold.
        
        Returns:
            float: The amount withdrawn.
        
        Raises:
            ValueError: If balance is less than the minimum withdrawal threshold.
        """
        if self.balance < self.min_withdrawal:
            raise ValueError(f"Insufficient balance to withdraw. Current balance: {self.balance}")

        amount_withdrawn = self.balance
        self.balance = 0.0  # Reset balance after withdrawal
        print(f"{self.username} withdrew {amount_withdrawn}. New balance: {self.balance}")
        return amount_withdrawn

def main():
    """
    Main function to simulate user earnings and withdrawals.
    """
    try:
        user1 = User("Alice")
        user1.earn(30)  # Alice earns 30
        user1.earn(25)  # Alice earns another 25
        
        # Attempt to withdraw earnings
        user1.withdraw()  # This will raise an error due to insufficient balance
        
    except ValueError as e:
        print(f"Error: {e}")

    try:
        user2 = User("Bob")
        user2.earn(60)  # Bob earns 60
        
        # Successful withdrawal
        user2.withdraw()  # This should succeed
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
