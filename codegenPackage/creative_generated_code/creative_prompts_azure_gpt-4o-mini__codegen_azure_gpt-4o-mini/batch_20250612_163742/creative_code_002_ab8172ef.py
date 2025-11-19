"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: What is the significance of the 90-day lock period for MOR tokens after staking stETH in the Morpheus ecosystem?
Generated: DETERMINISTIC_ab8172ef62df2fff
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MORTokenStaking:
    """
    Class to manage the staking of stETH in the Morpheus ecosystem
    and the associated 90-day lock period for MOR tokens.
    """

    def __init__(self):
        self.staked_tokens = {}
        self.lock_period = 90  # Lock period in days

    def stake_tokens(self, user_id, amount):
        """
        Stake stETH tokens for a user, initiating a 90-day lock period for MOR tokens.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of stETH tokens to stake.

        Raises:
            ValueError: If the amount is less than or equal to zero.
            KeyError: If the user already has staked tokens.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        if user_id in self.staked_tokens:
            raise KeyError("User has already staked tokens.")

        # Store the amount staked and the timestamp for the lock period
        self.staked_tokens[user_id] = {
            "amount": amount,
            "stake_timestamp": self.current_timestamp()
        }

    def current_timestamp(self):
        """
        Get the current timestamp in days since epoch.

        Returns:
            float: Current timestamp in days.
        """
        import time
        return time.time() / (24 * 3600)  # Convert seconds to days

    def can_withdraw(self, user_id):
        """
        Check if the user can withdraw their MOR tokens after the lock period.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            bool: True if the user can withdraw, False otherwise.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.staked_tokens:
            raise KeyError("User has not staked any tokens.")

        stake_info = self.staked_tokens[user_id]
        days_staked = self.current_timestamp() - stake_info["stake_timestamp"]
        return days_staked >= self.lock_period

    def withdraw_tokens(self, user_id):
        """
        Withdraw staked MOR tokens after the lock period has ended.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            KeyError: If the user has not staked any tokens.
            RuntimeError: If the lock period has not yet ended.
        """
        if user_id not in self.staked_tokens:
            raise KeyError("User has not staked any tokens.")

        if not self.can_withdraw(user_id):
            raise RuntimeError("Lock period has not ended; withdrawal not allowed.")

        # Logic to withdraw tokens (placeholder)
        amount = self.staked_tokens[user_id]["amount"]
        del self.staked_tokens[user_id]  # Remove staked info after withdrawal
        return amount  # Return the amount withdrawn


# Example usage:
if __name__ == "__main__":
    staking_system = MORTokenStaking()
    
    try:
        staking_system.stake_tokens("user123", 10.0)
        print("Tokens staked successfully.")
        
        # Simulate waiting for 90 days (for demonstration purposes)
        import time
        time.sleep(1)  # Replace with actual waiting logic in production
        
        if staking_system.can_withdraw("user123"):
            amount_withdrawn = staking_system.withdraw_tokens("user123")
            print(f"Successfully withdrew {amount_withdrawn} MOR tokens.")
        else:
            print("Cannot withdraw tokens yet; lock period is still active.")
    
    except (ValueError, KeyError, RuntimeError) as e:
        print(f"Error: {e}")
```
