"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppeiosite.web.app
Prompt: Develop a function that calculates potential rewards for staking $MPEPE tokens within De-Fi liquidity pools.
Generated: DETERMINISTIC_df30f2046f15f0dd
Batch ID: 20250612_140430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Optional

class StakingPool:
    """
    Represents a staking pool for MPEPE tokens.
    """

    def __init__(self, total_staked: float, reward_rate: float):
        """
        Initializes the staking pool with total staked amount and reward rate.

        :param total_staked: Total amount of MPEPE tokens staked in the pool.
        :param reward_rate: Annual reward rate as a decimal (e.g., 0.05 for 5%).
        """
        self.total_staked = total_staked
        self.reward_rate = reward_rate

    def calculate_rewards(self, staked_amount: float, duration_years: float) -> Optional[float]:
        """
        Calculates potential rewards for staked MPEPE tokens.

        :param staked_amount: Amount of MPEPE tokens staked by the user.
        :param duration_years: Duration for which the tokens are staked, in years.
        :return: Estimated reward amount or None if inputs are invalid.
        """
        try:
            # Validate inputs
            if staked_amount <= 0:
                raise ValueError("Staked amount must be greater than zero.")
            if duration_years < 0:
                raise ValueError("Duration must be zero or positive.")

            # Calculate rewards based on the formula:
            # Rewards = (Staked Amount / Total Staked) * Total Rewards
            total_rewards = self.total_staked * self.reward_rate * duration_years
            user_rewards = (staked_amount / self.total_staked) * total_rewards

            return user_rewards

        except ValueError as e:
            print(f"Input error: {e}")
            return None
        except ZeroDivisionError:
            print("Error: Total staked amount must be greater than zero.")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize the staking pool with total staked amount and reward rate
    pool = StakingPool(total_staked=1000000.0, reward_rate=0.05)

    # Calculate potential rewards for staked tokens
    staked_amount = 10000.0  # Amount of MPEPE tokens staked by the user
    duration_years = 1.0     # Duration for which the tokens are staked

    rewards = pool.calculate_rewards(staked_amount, duration_years)
    if rewards is not None:
        print(f"Potential Rewards: ${rewards:.2f}")
```
