"""
Generated Code Metadata:
========================
Original URL: https://azterdex.com
Prompt: Generate code to calculate staking rewards for assets like BNB, USDT, BTC, and CAKE on Aster, considering up to 30%+ APY.
Generated: DETERMINISTIC_5a00f539a26e7fc0
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
    A class to calculate staking rewards for various assets considering different APYs.
    Supports assets like BNB, USDT, BTC, and CAKE.
    """
    
    def __init__(self):
        # Default APY values (can be updated)
        self.default_apy = {
            'BNB': 0.10,  # 10% APY
            'USDT': 0.08,  # 8% APY
            'BTC': 0.12,  # 12% APY
            'CAKE': 0.30  # 30% APY
        }
    
    def set_apy(self, asset: str, apy: float) -> None:
        """
        Set custom APY for a specific asset.
        
        Args:
            asset: The asset symbol (e.g., 'BNB', 'USDT')
            apy: The annual percentage yield (0.30 for 30%)
            
        Raises:
            ValueError: If APY is negative or asset is not supported
        """
        if apy < 0:
            raise ValueError("APY cannot be negative")
        if asset not in self.default_apy:
            raise ValueError(f"Asset {asset} not supported")
        self.default_apy[asset] = apy
    
    def calculate_rewards(
        self,
        asset: str,
        amount: float,
        days: int,
        apy: Union[float, None] = None
    ) -> Dict[str, float]:
        """
        Calculate staking rewards for a given asset, amount, and duration.
        
        Args:
            asset: The asset symbol (e.g., 'BNB', 'USDT')
            amount: The amount of asset being staked
            days: Number of days to stake
            apy: Optional custom APY (uses default if None)
            
        Returns:
            Dictionary containing:
            - 'rewards': Total rewards earned
            - 'total': Total amount after rewards
            
        Raises:
            ValueError: If inputs are invalid
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if days <= 0:
            raise ValueError("Days must be positive")
        
        try:
            effective_apy = apy if apy is not None else self.default_apy[asset]
        except KeyError:
            raise ValueError(f"Asset {asset} not supported")
        
        if effective_apy < 0:
            raise ValueError("APY cannot be negative")
        
        # Calculate daily rate (compounding daily)
        daily_rate = (1 + effective_apy) ** (1/365) - 1
        total_amount = amount * (1 + daily_rate) ** days
        rewards = total_amount - amount
        
        return {
            'rewards': rewards,
            'total': total_amount
        }
    
    def calculate_apy_to_reach_target(
        self,
        asset: str,
        amount: float,
        target_amount: float,
        days: int
    ) -> float:
        """
        Calculate required APY to reach a target amount from staking.
        
        Args:
            asset: The asset symbol
            amount: Initial staked amount
            target_amount: Desired total amount
            days: Number of days to stake
            
        Returns:
            Required APY (as decimal)
            
        Raises:
            ValueError: If inputs are invalid
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if target_amount <= amount:
            raise ValueError("Target amount must be greater than initial amount")
        if days <= 0:
            raise ValueError("Days must be positive")
        
        # Calculate required daily growth rate
        required_growth = (target_amount / amount) ** (1/days) - 1
        required_apy = (1 + required_growth) ** 365 - 1
        
        return required_apy

# Example usage
if __name__ == "__main__":
    calculator = StakingRewardCalculator()
    
    # Calculate rewards with default APY
    bnb_rewards = calculator.calculate_rewards('BNB', 1000, 30)
    print(f"BNB rewards after 30 days: {bnb_rewards}")
    
    # Calculate with custom APY
    cake_rewards = calculator.calculate_rewards('CAKE', 500, 90, 0.35)
    print(f"CAKE rewards after 90 days at 35% APY: {cake_rewards}")
    
    # Calculate required APY to reach target
    required_apy = calculator.calculate_apy_to_reach_target('USDT', 1000, 1100, 60)
    print(f"Required APY to reach $1100 from $1000 in 60 days: {required_apy*100:.2f}%")
```
