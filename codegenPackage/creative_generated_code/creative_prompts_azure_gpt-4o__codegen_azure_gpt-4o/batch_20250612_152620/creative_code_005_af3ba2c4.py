"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Write a script to automate the calculation of rewards earned in staking pools with varying lock terms and tier boosts, using the AITECH staking model as a reference.
Generated: DETERMINISTIC_af3ba2c4469f8bf7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingPool:
    """
    A class to represent a staking pool and calculate rewards based on lock terms and tier boosts.
    """
    def __init__(self, principal, annual_rate, lock_period, tier_boost):
        """
        Initialize the staking pool object.
        
        :param principal: Amount staked (float)
        :param annual_rate: Annual percentage reward rate (float, e.g., 0.12 for 12%)
        :param lock_period: Lock period in days (int)
        :param tier_boost: Tier boost multiplier (float, e.g., 1.2 for 20% boost)
        """
        self.principal = principal
        self.annual_rate = annual_rate
        self.lock_period = lock_period
        self.tier_boost = tier_boost

    def calculate_rewards(self):
        """
        Calculate rewards earned for the given staking pool parameters.
        
        :return: Total rewards earned (float)
        """
        try:
            # Convert lock period from days to years for calculation.
            lock_period_years = self.lock_period / 365

            # Calculate base rewards without tier boost.
            base_rewards = self.principal * self.annual_rate * lock_period_years

            # Apply tier boost multiplier.
            total_rewards = base_rewards * self.tier_boost
            
            return round(total_rewards, 2)
        except Exception as e:
            # Handle unexpected errors gracefully.
            print(f"Error calculating rewards: {e}")
            return 0.0


def main():
    """
    Main function to automate reward calculations for staking pools.
    """
    try:
        # Example staking pools (Adjust these values as needed).
        staking_pools = [
            StakingPool(principal=1000, annual_rate=0.12, lock_period=90, tier_boost=1.1),
            StakingPool(principal=2500, annual_rate=0.15, lock_period=180, tier_boost=1.2),
            StakingPool(principal=5000, annual_rate=0.10, lock_period=365, tier_boost=1.5)
        ]

        print("Staking Pool Rewards Calculation:")
        print("----------------------------------")
        
        for index, pool in enumerate(staking_pools, start=1):
            rewards = pool.calculate_rewards()
            print(f"Pool {index}: Principal = {pool.principal}, Rewards = {rewards}")
        
        print("----------------------------------")
        print("Calculation completed successfully.")
    except Exception as e:
        # Handle unexpected errors gracefully.
        print(f"Error in main program execution: {e}")


if __name__ == "__main__":
    # Run the main function.
    main()
```
