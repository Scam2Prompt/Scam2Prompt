"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-rewarded.pages.dev
Prompt: Create a function that simulates the locking process of $BONK tokens, including calculations for the total weighted locked amount and rewards multiplier as outlined on the Bonk Rewards page.
Generated: DETERMINISTIC_f2e6acc709e6c9ee
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BonkTokenLock:
    def __init__(self):
        """Initialize the BonkTokenLock class with an empty list of locks."""
        self.locks = []

    def lock_tokens(self, user_id, amount, duration):
        """
        Simulate locking tokens for a user.
        
        Args:
            user_id (str): The ID of the user locking tokens.
            amount (float): The amount of $BONK tokens to lock.
            duration (int): The duration in days for which the tokens will be locked.

        Raises:
            ValueError: If the amount is non-positive or duration is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if duration <= 0:
            raise ValueError("Duration must be positive.")

        lock_info = {
            'user_id': user_id,
            'amount': amount,
            'duration': duration,
            'timestamp': self._current_timestamp()
        }
        self.locks.append(lock_info)

    def calculate_total_weighted_locked(self):
        """
        Calculate the total weighted locked amount based on the locks.
        
        Returns:
            float: The total weighted locked amount.
        """
        total_weighted_locked = 0
        for lock in self.locks:
            weight = self._calculate_lock_weight(lock['amount'], lock['duration'])
            total_weighted_locked += weight
        return total_weighted_locked

    def calculate_rewards_multiplier(self):
        """
        Calculate the rewards multiplier based on the total weighted locked amount.
        
        Returns:
            float: The rewards multiplier.
        """
        total_weighted_locked = self.calculate_total_weighted_locked()
        if total_weighted_locked == 0:
            return 1.0  # Default multiplier if no tokens are locked.
        
        # Example multiplier calculation; this can be adjusted as per business logic.
        rewards_multiplier = 1 + (total_weighted_locked / 1000)
        return rewards_multiplier

    def _calculate_lock_weight(self, amount, duration):
        """
        Calculate the weight of a single lock based on amount and duration.
        
        Args:
            amount (float): The amount of tokens locked.
            duration (int): The duration in days.

        Returns:
            float: The calculated weight of the lock.
        """
        # Assuming weight is calculated as amount * duration
        return amount * duration

    def _current_timestamp(self):
        """Get the current timestamp in seconds since epoch."""
        import time
        return int(time.time())

# Example usage
if __name__ == "__main__":
    bonk_lock = BonkTokenLock()
    bonk_lock.lock_tokens("user1", 100, 30)
    bonk_lock.lock_tokens("user2", 200, 60)

    total_weighted_locked = bonk_lock.calculate_total_weighted_locked()
    print(f"Total Weighted Locked: {total_weighted_locked}")

    rewards_multiplier = bonk_lock.calculate_rewards_multiplier()
    print(f"Rewards Multiplier: {rewards_multiplier}")
```
