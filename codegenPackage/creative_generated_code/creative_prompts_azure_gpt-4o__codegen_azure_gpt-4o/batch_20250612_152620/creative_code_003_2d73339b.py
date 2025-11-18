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
from datetime import datetime, timedelta

class StakingPool:
    """
    A class to calculate compounding rewards for a staking pool 
    with tier boosts and lock terms.
    """

    def __init__(self, base_reward_rate, tiers, lock_terms):
        """
        Initializes the staking pool with base reward rate, tier boosts, and lock terms.

        :param base_reward_rate: Base annual reward rate as a decimal (e.g., 0.05 for 5%)
        :param tiers: Dict of tier names and their boost percentages (e.g., {"Silver": 0.02, "Gold": 0.05})
        :param lock_terms: Dict defining lock terms and their corresponding reward multipliers
                          (e.g., {"3M": 1.1, "6M": 1.25, "12M": 1.5})
        """
        self.base_reward_rate = base_reward_rate
        self.tiers = tiers
        self.lock_terms = lock_terms

    def calculate_rewards(self, principal, tier, lock_term, staking_start_date, staking_end_date):
        """
        Calculates the compounded staking rewards based on tier, lock term, and duration.

        :param principal: The amount being staked
        :param tier: The tier of the user ("Silver", "Gold", etc.)
        :param lock_term: The lock term ("3M", "6M", "12M", etc.)
        :param staking_start_date: The date staking begins (datetime object)
        :param staking_end_date: The date staking ends (datetime object)
        :return: Total rewards earned (float)
        """
        # Validate inputs
        if tier not in self.tiers:
            raise ValueError(f"Invalid tier: {tier}. Valid tiers are: {list(self.tiers.keys())}")
        if lock_term not in self.lock_terms:
            raise ValueError(f"Invalid lock term: {lock_term}. Valid terms are: {list(self.lock_terms.keys())}")
        if staking_end_date <= staking_start_date:
            raise ValueError("Staking end date must be after the staking start date.")

        # Calculate duration in years
        duration_days = (staking_end_date - staking_start_date).days
        duration_years = duration_days / 365.0

        # Calculate adjusted reward rate
        tier_boost = self.tiers[tier]  # Tier boost percentage
        lock_multiplier = self.lock_terms[lock_term]  # Lock term multiplier
        adjusted_rate = self.base_reward_rate + tier_boost
        adjusted_rate *= lock_multiplier

        # Compound rewards calculation
        # Formula: A = P * (1 + r/n)^(n*t)
        # Compounding frequency (daily compounding assumed)
        compounding_frequency = 365
        total_rewards = principal * ((1 + adjusted_rate / compounding_frequency) ** (compounding_frequency * duration_years) - 1)

        return total_rewards


# Example usage
if __name__ == "__main__":
    # Define staking pool configuration
    base_reward_rate = 0.05  # Base reward rate: 5% annually
    tiers = {
        "Silver": 0.02,  # Silver tier adds 2% boost
        "Gold": 0.05    # Gold tier adds 5% boost
    }
    lock_terms = {
        "3M": 1.1,   # 3-month lock increases reward by 10%
        "6M": 1.25,  # 6-month lock increases reward by 25%
        "12M": 1.5   # 12-month lock increases reward by 50%
    }

    # Create staking pool instance
    staking_pool = StakingPool(base_reward_rate, tiers, lock_terms)

    # Parameters
    principal_amount = 1000.0  # $1000 staked
    user_tier = "Gold"
    lock_term = "6M"
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    try:
        # Calculate rewards
        rewards = staking_pool.calculate_rewards(principal_amount, user_tier, lock_term, start_date, end_date)
        print(f"Total rewards earned: ${rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
