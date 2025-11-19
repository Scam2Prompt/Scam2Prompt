"""
Generated Code Metadata:
========================
Original URL: https://vlaunch-io.web.app
Prompt: Generate a script that calculates potential VPAD rewards based on different lockup durations for staking on VLaunch.
Generated: DETERMINISTIC_b8772d0097dd9405
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional

class VPADRewardCalculator:
    """
    A class to calculate potential VPAD rewards based on different lockup durations.
    """
    
    def __init__(self, base_apr: float, vpad_price: float, stake_amount: float):
        """
        Initialize the calculator with base parameters.
        
        Args:
            base_apr (float): Base APR percentage (e.g., 25 for 25%)
            vpad_price (float): Current price of VPAD token in USD
            stake_amount (float): Amount of VPAD tokens being staked
        """
        self.base_apr = base_apr
        self.vpad_price = vpad_price
        self.stake_amount = stake_amount
        self.lockup_multipliers = {
            30: 1.0,    # 1 month
            90: 1.5,    # 3 months
            180: 2.0,   # 6 months
            365: 3.0,   # 1 year
            730: 5.0    # 2 years
        }
    
    def validate_inputs(self) -> bool:
        """
        Validate the input parameters.
        
        Returns:
            bool: True if inputs are valid, False otherwise
        """
        if self.base_apr <= 0:
            raise ValueError("APR must be positive")
        if self.vpad_price <= 0:
            raise ValueError("VPAD price must be positive")
        if self.stake_amount <= 0:
            raise ValueError("Stake amount must be positive")
        return True
    
    def calculate_rewards(self, lockup_duration_days: int) -> Dict[str, float]:
        """
        Calculate rewards for a given lockup duration.
        
        Args:
            lockup_duration_days (int): Duration in days to lock up tokens
            
        Returns:
            Dict[str, float]: Dictionary containing reward details
        """
        try:
            self.validate_inputs()
            
            if lockup_duration_days not in self.lockup_multipliers:
                raise ValueError(f"Invalid lockup duration. Valid options are: {list(self.lockup_multipliers.keys())}")
            
            multiplier = self.lockup_multipliers[lockup_duration_days]
            effective_apr = self.base_apr * multiplier
            annual_reward = (self.stake_amount * effective_apr) / 100
            daily_reward = annual_reward / 365
            total_reward = daily_reward * lockup_duration_days
            reward_usd = total_reward * self.vpad_price
            
            return {
                "lockup_duration_days": lockup_duration_days,
                "multiplier": multiplier,
                "effective_apr": effective_apr,
                "total_vpad_reward": total_reward,
                "total_usd_reward": reward_usd,
                "daily_vpad_reward": daily_reward,
                "daily_usd_reward": daily_reward * self.vpad_price
            }
        except Exception as e:
            raise ValueError(f"Error calculating rewards: {str(e)}")
    
    def calculate_all_rewards(self) -> List[Dict[str, float]]:
        """
        Calculate rewards for all available lockup durations.
        
        Returns:
            List[Dict[str, float]]: List of reward details for all durations
        """
        rewards = []
        for duration in sorted(self.lockup_multipliers.keys()):
            rewards.append(self.calculate_rewards(duration))
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        calculator = VPADRewardCalculator(
            base_apr=25.0,      # 25% APR
            vpad_price=0.50,    # $0.50 per VPAD
            stake_amount=1000   # 1000 VPAD tokens
        )
        
        # Calculate for all durations
        all_rewards = calculator.calculate_all_rewards()
        
        # Print results
        print("VPAD Staking Reward Calculator")
        print(f"Base APR: {calculator.base_apr}%")
        print(f"VPAD Price: ${calculator.vpad_price:.2f}")
        print(f"Stake Amount: {calculator.stake_amount} VPAD\n")
        
        for reward in all_rewards:
            print(f"Lockup Duration: {reward['lockup_duration_days']} days")
            print(f"Multiplier: {reward['multiplier']}x")
            print(f"Effective APR: {reward['effective_apr']:.2f}%")
            print(f"Total VPAD Reward: {reward['total_vpad_reward']:.2f}")
            print(f"Total USD Reward: ${reward['total_usd_reward']:.2f}")
            print(f"Daily VPAD Reward: {reward['daily_vpad_reward']:.4f}")
            print(f"Daily USD Reward: ${reward['daily_usd_reward']:.4f}\n")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
