"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claimyourdoge20.pages.dev
Prompt: Create a function that calculates the percentage of staking rewards for a user based on their contribution to the DOGE20 staking pool.
Generated: DETERMINISTIC_6e1be7607b3fe074
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPool:
    def __init__(self, total_staked: float):
        """
        Initializes the StakingPool with the total staked amount.

        Args:
            total_staked (float): Total amount staked in the pool.
        """
        if total_staked <= 0:
            raise ValueError("Total staked amount must be greater than zero.")
        self.total_staked = total_staked

    def calculate_reward_percentage(self, user_staked: float) -> float:
        """
        Calculates the percentage of staking rewards for a user based on their contribution.

        Args:
            user_staked (float): Amount staked by the user.

        Returns:
            float: Percentage of total rewards the user is entitled to, expressed as a percentage.

        Raises:
            ValueError: If user_staked is less than zero or greater than total_staked.
        """
        if user_staked < 0:
            raise ValueError("User staked amount cannot be negative.")
        if user_staked > self.total_staked:
            raise ValueError("User staked amount cannot exceed total staked amount.")

        # Calculate the percentage of the user's stake relative to the total stake
        reward_percentage = (user_staked / self.total_staked) * 100
        return reward_percentage


# Example usage:
if __name__ == "__main__":
    try:
        total_staked_amount = 10000.0  # Example total staked amount
        pool = StakingPool(total_staked_amount)
        
        user_staked_amount = 2500.0  # Example user staked amount
        percentage = pool.calculate_reward_percentage(user_staked_amount)
        
        print(f"User's reward percentage: {percentage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
