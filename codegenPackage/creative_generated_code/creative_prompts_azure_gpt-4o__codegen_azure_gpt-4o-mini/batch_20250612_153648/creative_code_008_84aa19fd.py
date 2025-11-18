"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.pages.dev
Prompt: Create a function to calculate the profitability of staking and locking MGP tokens on Magpie XYZ, including rewards in WOM and additional MGP.
Generated: DETERMINISTIC_84aa19fd356051e6
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate the profitability of staking and locking MGP tokens on Magpie XYZ.
    
    Attributes:
        mgp_staked (float): The amount of MGP tokens staked.
        reward_rate_wom (float): The reward rate for WOM tokens (in percentage).
        reward_rate_mgp (float): The reward rate for additional MGP tokens (in percentage).
        staking_duration (int): The duration for which the tokens are staked (in days).
    """
    
    def __init__(self, mgp_staked: float, reward_rate_wom: float, reward_rate_mgp: float, staking_duration: int):
        """
        Initializes the StakingCalculator with the provided parameters.

        Args:
            mgp_staked (float): The amount of MGP tokens staked.
            reward_rate_wom (float): The reward rate for WOM tokens (in percentage).
            reward_rate_mgp (float): The reward rate for additional MGP tokens (in percentage).
            staking_duration (int): The duration for which the tokens are staked (in days).

        Raises:
            ValueError: If any of the inputs are negative or if staking_duration is zero.
        """
        if mgp_staked < 0 or reward_rate_wom < 0 or reward_rate_mgp < 0 or staking_duration <= 0:
            raise ValueError("MGP staked and reward rates must be non-negative, and staking duration must be greater than zero.")

        self.mgp_staked = mgp_staked
        self.reward_rate_wom = reward_rate_wom / 100  # Convert percentage to decimal
        self.reward_rate_mgp = reward_rate_mgp / 100  # Convert percentage to decimal
        self.staking_duration = staking_duration

    def calculate_rewards(self) -> dict:
        """
        Calculates the total rewards from staking MGP tokens.

        Returns:
            dict: A dictionary containing the total WOM and MGP rewards.
        """
        # Calculate rewards
        total_wom_rewards = self.mgp_staked * self.reward_rate_wom * self.staking_duration
        total_mgp_rewards = self.mgp_staked * self.reward_rate_mgp * self.staking_duration
        
        return {
            "Total WOM Rewards": total_wom_rewards,
            "Total MGP Rewards": total_mgp_rewards
        }

# Example usage
if __name__ == "__main__":
    try:
        mgp_amount = 1000  # Amount of MGP tokens staked
        wom_reward_rate = 5  # Reward rate for WOM tokens (5%)
        mgp_reward_rate = 3  # Reward rate for additional MGP tokens (3%)
        duration = 30  # Staking duration in days

        # Initialize the staking calculator
        staking_calculator = StakingCalculator(mgp_amount, wom_reward_rate, mgp_reward_rate, duration)

        # Calculate and print the rewards
        rewards = staking_calculator.calculate_rewards()
        print("Rewards from staking:")
        print(f"Total WOM Rewards: {rewards['Total WOM Rewards']:.2f}")
        print(f"Total MGP Rewards: {rewards['Total MGP Rewards']:.2f}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
