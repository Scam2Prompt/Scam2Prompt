"""
Generated Code Metadata:
========================
Original URL: https://astrdex.com
Prompt: Generate code to calculate staking rewards for BNB, USDT, BTC, and CAKE on Aster DEX, considering an APY of up to 30%.
Generated: DETERMINISTIC_ac68b9476d792931
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Union

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for various tokens on Aster DEX.
    Supports BNB, USDT, BTC, and CAKE tokens with APY up to 30%.
    """
    
    def __init__(self):
        self.token_decimals = {
            'BNB': 18,
            'USDT': 6,
            'BTC': 8,
            'CAKE': 18
        }
    
    def calculate_daily_reward(self, amount: float, token: str, apy: float) -> float:
        """
        Calculate daily staking reward for a given token amount and APY.
        
        Args:
            amount: Amount of token staked
            token: Token symbol (BNB, USDT, BTC, or CAKE)
            apy: Annual Percentage Yield (0 to 30)
            
        Returns:
            Daily reward in the same token
            
        Raises:
            ValueError: If invalid token or APY is provided
        """
        if token not in self.token_decimals:
            raise ValueError(f"Unsupported token: {token}. Supported tokens are: {list(self.token_decimals.keys())}")
        
        if apy < 0 or apy > 30:
            raise ValueError("APY must be between 0 and 30")
            
        daily_rate = (1 + apy / 100) ** (1/365) - 1
        daily_reward = amount * daily_rate
        
        # Round to appropriate decimal places for the token
        decimal_places = self.token_decimals[token]
        return round(daily_reward, decimal_places)
    
    def calculate_rewards_over_period(
        self,
        amount: float,
        token: str,
        apy: float,
        days: int,
        compound: bool = False
    ) -> Dict[str, Union[float, Dict[int, float]]]:
        """
        Calculate staking rewards over a period of days, with optional compounding.
        
        Args:
            amount: Initial amount of token staked
            token: Token symbol
            apy: Annual Percentage Yield (0 to 30)
            days: Number of days to calculate rewards for
            compound: Whether to compound rewards daily (default: False)
            
        Returns:
            Dictionary containing:
            - total_reward: Total reward over the period
            - final_amount: Final amount including rewards
            - daily_rewards: Dictionary of day: reward for each day
        """
        if days < 1:
            raise ValueError("Days must be at least 1")
            
        current_amount = amount
        daily_rewards = {}
        decimal_places = self.token_decimals[token]
        
        for day in range(1, days + 1):
            daily_reward = self.calculate_daily_reward(current_amount, token, apy)
            daily_rewards[day] = daily_reward
            
            if compound:
                current_amount += daily_reward
                current_amount = round(current_amount, decimal_places)
        
        if not compound:
            total_reward = sum(daily_rewards.values())
            final_amount = amount + total_reward
        else:
            total_reward = current_amount - amount
            final_amount = current_amount
        
        return {
            'total_reward': round(total_reward, decimal_places),
            'final_amount': round(final_amount, decimal_places),
            'daily_rewards': daily_rewards
        }

# Example usage
if __name__ == "__main__":
    calculator = StakingRewardCalculator()
    
    # Calculate simple daily reward
    try:
        reward = calculator.calculate_daily_reward(1000, 'BNB', 20)
        print(f"Daily BNB reward: {reward}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Calculate compounded rewards over 30 days
    try:
        results = calculator.calculate_rewards_over_period(1000, 'USDT', 15, 30, compound=True)
        print(f"\n30-day compounded USDT rewards:")
        print(f"Total reward: {results['total_reward']}")
        print(f"Final amount: {results['final_amount']}")
    except ValueError as e:
        print(f"Error: {e}")
```
