"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Provide code to implement a feature that allows users to claim free credits ("สล็อตใช้วอเลทเครดิตฟรี") after wallet-based deposits in an online slot game.
Generated: DETERMINISTIC_f6daf0cafc7ac694
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WalletCreditSystem:
    """
    A class to manage wallet-based deposits and the claiming of free credits
    in an online slot game.
    """

    def __init__(self):
        # Dictionary to hold user data
        self.user_data = {}

    def add_user(self, user_id):
        """
        Add a new user to the system.

        Args:
            user_id (str): The unique identifier for the user.
        """
        if user_id in self.user_data:
            raise ValueError("User already exists.")
        self.user_data[user_id] = {
            'balance': 0,
            'free_credits': 0,
            'deposit_history': []
        }

    def deposit(self, user_id, amount):
        """
        Process a deposit and award free credits based on the deposit amount.

        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount to be deposited.

        Raises:
            ValueError: If the user does not exist or the deposit amount is invalid.
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Update user balance and deposit history
        self.user_data[user_id]['balance'] += amount
        self.user_data[user_id]['deposit_history'].append(amount)

        # Award free credits (e.g., 10% of the deposit amount)
        free_credits = amount * 0.10
        self.user_data[user_id]['free_credits'] += free_credits
        print(f"User {user_id} deposited {amount}, awarded {free_credits} free credits.")

    def claim_free_credits(self, user_id):
        """
        Allow the user to claim their free credits.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            float: The amount of free credits claimed.

        Raises:
            ValueError: If the user does not exist or has no free credits to claim.
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        if self.user_data[user_id]['free_credits'] <= 0:
            raise ValueError("No free credits available to claim.")

        # Claim all available free credits
        claimed_credits = self.user_data[user_id]['free_credits']
        self.user_data[user_id]['free_credits'] = 0  # Reset after claiming
        print(f"User {user_id} claimed {claimed_credits} free credits.")
        return claimed_credits

    def get_user_info(self, user_id):
        """
        Retrieve information about the user.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            dict: User information including balance and free credits.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        return self.user_data[user_id]


# Example usage
if __name__ == "__main__":
    system = WalletCreditSystem()
    
    # Add a new user
    user_id = "user123"
    system.add_user(user_id)

    # User deposits money
    system.deposit(user_id, 100)

    # User claims free credits
    claimed_credits = system.claim_free_credits(user_id)
    print(f"Claimed free credits: {claimed_credits}")

    # Retrieve user info
    user_info = system.get_user_info(user_id)
    print(f"User info: {user_info}")
```
