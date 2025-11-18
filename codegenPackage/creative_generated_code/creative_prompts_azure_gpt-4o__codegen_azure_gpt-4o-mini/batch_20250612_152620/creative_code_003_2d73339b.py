"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Generate code to calculate compounding rewards for a staking pool with tier boosts and lock terms, as described in the AITECH staking system.
Generated: DETERMINISTIC_2d73339b5229b9c4
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPool:
    """
    A class to represent a Staking Pool that calculates compounding rewards 
    based on tier boosts and lock terms.
    """

    def __init__(self, initial_stake: float, annual_rate: float, lock_term_years: int, tier_boost: float):
        """
        Initializes the StakingPool with parameters.

        :param initial_stake: The initial amount staked.
        :param annual_rate: The annual interest rate as a decimal.
        :param lock_term_years: The number of years the stake is locked.
        :param tier_boost: The additional percentage boost based on the staking tier.
        """
        if initial_stake <= 0:
            raise ValueError("Initial stake must be greater than 0.")
        if annual_rate < 0:
            raise ValueError("Annual rate must not be negative.")
        if lock_term_years <= 0:
            raise ValueError("Lock term years must be greater than 0.")
        if tier_boost < 0:
            raise ValueError("Tier boost must not be negative.")

        self.initial_stake = initial_stake
        self.annual_rate = annual_rate
        self.lock_term_years = lock_term_years
        self.tier_boost = tier_boost

    def calculate_total_reward(self) -> float:
        """
        Calculates the total reward from staking, including compounding and tier boosts.

        :return: The total amount after rewards.
        """
        # Calculate total rate after applying tier boost
        total_rate = self.annual_rate + self.tier_boost

        # Calculate total amount using compound interest formula
        total_amount = self.initial_stake * (1 + total_rate) ** self.lock_term_years

        return total_amount

    def display_results(self):
        """
        Prints the initial stake, total reward, and the breakdown of the rewards.
        """
        total_reward = self.calculate_total_reward()
        print(f"Initial Stake: ${self.initial_stake:.2f}")
        print(f"Total Reward after {self.lock_term_years} years: ${total_reward:.2f}")
        print(f"Total Earnings: ${total_reward - self.initial_stake:.2f}")

if __name__ == "__main__":
    try:
        # Example parameters for staking pool
        initial_stake = 1000.0  # Initial amount staked
        annual_rate = 0.05       # Annual interest rate (5%)
        lock_term_years = 3      # Lock term in years
        tier_boost = 0.02        # Additional tier boost (2%)

        # Create an instance of StakingPool
        staking_pool = StakingPool(initial_stake, annual_rate, lock_term_years, tier_boost)

        # Display the results
        staking_pool.display_results()

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
