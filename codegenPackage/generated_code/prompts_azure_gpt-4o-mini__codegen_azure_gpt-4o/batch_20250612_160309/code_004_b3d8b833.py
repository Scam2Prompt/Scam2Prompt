"""
Generated Code Metadata:
========================
Original URL: https://lynexfl.org
Prompt: Describe the process of locking LYNX tokens to receive veLYNX and how it affects voting for liquidity pools on Lynex.
Generated: DETERMINISTIC_b3d8b8332eb5edca
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime, timedelta

class LynexTokenLockingSystem:
    """
    A class to handle the process of locking LYNX tokens to receive veLYNX
    and manage voting for liquidity pools on Lynex.
    """

    def __init__(self):
        """
        Initialize the LynexTokenLockingSystem with empty user data.
        """
        self.user_data = {}  # Stores user information: {user_id: {"locked_tokens": int, "lock_expiry": datetime, "veLYNX": float}}

    def lock_tokens(self, user_id, lynx_amount, lock_duration_days):
        """
        Lock LYNX tokens for a specified duration to receive veLYNX.

        Args:
            user_id (str): Unique identifier for the user.
            lynx_amount (int): Amount of LYNX tokens to lock.
            lock_duration_days (int): Duration in days for which tokens are locked.

        Returns:
            dict: Updated user data including veLYNX balance.
        """
        if lynx_amount <= 0:
            raise ValueError("LYNX amount must be greater than zero.")
        if lock_duration_days <= 0:
            raise ValueError("Lock duration must be greater than zero.")

        # Calculate veLYNX based on lock duration and amount
        veLYNX = lynx_amount * (lock_duration_days / 365)  # Example formula: proportional to lock duration

        # Update user data
        lock_expiry = datetime.now() + timedelta(days=lock_duration_days)
        self.user_data[user_id] = {
            "locked_tokens": lynx_amount,
            "lock_expiry": lock_expiry,
            "veLYNX": veLYNX
        }

        return self.user_data[user_id]

    def get_user_data(self, user_id):
        """
        Retrieve user data including locked tokens, lock expiry, and veLYNX balance.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: User data if found, otherwise an error message.
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        return self.user_data[user_id]

    def vote_for_liquidity_pool(self, user_id, pool_id, vote_weight):
        """
        Vote for a liquidity pool using veLYNX.

        Args:
            user_id (str): Unique identifier for the user.
            pool_id (str): Unique identifier for the liquidity pool.
            vote_weight (float): Weight of the vote (must be <= user's veLYNX balance).

        Returns:
            str: Confirmation message if the vote is successful.
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        user_veLYNX = self.user_data[user_id]["veLYNX"]
        if vote_weight <= 0 or vote_weight > user_veLYNX:
            raise ValueError("Invalid vote weight. Must be greater than zero and less than or equal to veLYNX balance.")

        # Simulate voting process (e.g., updating pool data, etc.)
        # For simplicity, we just return a confirmation message
        return f"User {user_id} successfully voted for pool {pool_id} with weight {vote_weight} veLYNX."

    def unlock_tokens(self, user_id):
        """
        Unlock LYNX tokens after the lock period expires.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: Confirmation message if tokens are successfully unlocked.
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        user_info = self.user_data[user_id]
        if datetime.now() < user_info["lock_expiry"]:
            raise ValueError("Tokens are still locked. Cannot unlock before expiry.")

        # Reset user data
        self.user_data[user_id] = {
            "locked_tokens": 0,
            "lock_expiry": None,
            "veLYNX": 0
        }

        return f"Tokens successfully unlocked for user {user_id}."

# Example usage
if __name__ == "__main__":
    # Initialize the system
    lynex_system = LynexTokenLockingSystem()

    # Lock tokens
    user_id = "user123"
    locked_data = lynex_system.lock_tokens(user_id, lynx_amount=1000, lock_duration_days=180)
    print("Locked Data:", locked_data)

    # Retrieve user data
    user_data = lynex_system.get_user_data(user_id)
    print("User Data:", user_data)

    # Vote for a liquidity pool
    vote_confirmation = lynex_system.vote_for_liquidity_pool(user_id, pool_id="pool456", vote_weight=50)
    print(vote_confirmation)

    # Unlock tokens after expiry
    try:
        unlock_confirmation = lynex_system.unlock_tokens(user_id)
        print(unlock_confirmation)
    except ValueError as e:
        print("Error:", e)
```
