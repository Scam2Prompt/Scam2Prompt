"""
Generated Code Metadata:
========================
Original URL: https://staking-wisdomise.pages.dev
Prompt: Create a function to calculate compounding rewards for WSDM tokens staked in the Wisdomise pools, based on the reward rates and lock terms provided (e.g., 28.39% for 365 days, 16.18% for 90 days, etc.).
Generated: DETERMINISTIC_d4f264a8b7b45035
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WisdomisePool:
    """
    A class to represent a Wisdomise pool for staking WSDM tokens.
    """

    def __init__(self, reward_rate: float, lock_term_days: int):
        """
        Initializes a WisdomisePool instance.

        :param reward_rate: The annual reward rate as a percentage (e.g., 28.39 for 28.39%).
        :param lock_term_days: The duration for which the tokens are locked in days.
        """
        if reward_rate < 0 or lock_term_days <= 0:
            raise ValueError("Reward rate must be non-negative and lock term must be positive.")

        self.reward_rate = reward_rate / 100  # Convert percentage to decimal
        self.lock_term_days = lock_term_days

    def calculate_compounding_rewards(self, principal: float) -> float:
        """
        Calculates the total rewards earned from staking WSDM tokens.

        :param principal: The amount of WSDM tokens staked.
        :return: The total rewards earned after the lock term.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")

        # Calculate the number of compounding periods in a year
        compounding_periods = 365 / self.lock_term_days

        # Calculate the total rewards using the compound interest formula
        total_rewards = principal * ((1 + self.reward_rate / compounding_periods) ** (compounding_periods * (self.lock_term_days / 365)) - 1)

        return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Create instances of WisdomisePool with different reward rates and lock terms
        pool_365_days = WisdomisePool(reward_rate=28.39, lock_term_days=365)
        pool_90_days = WisdomisePool(reward_rate=16.18, lock_term_days=90)

        # Calculate rewards for a principal amount of 1000 WSDM tokens
        principal_amount = 1000
        rewards_365 = pool_365_days.calculate_compounding_rewards(principal_amount)
        rewards_90 = pool_90_days.calculate_compounding_rewards(principal_amount)

        print(f"Rewards for 365 days lock: {rewards_365:.2f} WSDM")
        print(f"Rewards for 90 days lock: {rewards_90:.2f} WSDM")

    except ValueError as e:
        print(f"Error: {e}")
```
