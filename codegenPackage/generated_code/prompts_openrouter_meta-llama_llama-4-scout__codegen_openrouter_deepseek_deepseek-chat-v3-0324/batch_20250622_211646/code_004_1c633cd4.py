"""
Generated Code Metadata:
========================
Original URL: https://nft-eth30.vercel.app
Prompt: Design an algorithm to proportionally reward users with gETH tokens based on their Ethereum gas fees expenditure, as described in the gETH token architecture.
Generated: DETERMINISTIC_1c633cd4e4a3e1d4
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List
from dataclasses import dataclass
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 18

@dataclass
class UserGasExpenditure:
    """Data class representing a user's gas expenditure"""
    user_address: str
    gas_fees_spent: Decimal  # in ETH

class ProportionalRewardCalculator:
    """
    Calculates proportional gETH token rewards based on users' gas fees expenditure.
    
    Attributes:
        total_gas_fees (Decimal): Total gas fees spent by all users (in ETH)
        reward_pool (Decimal): Total gETH tokens to be distributed
        users_data (List[UserGasExpenditure]): List of user gas expenditure data
    """
    
    def __init__(self, reward_pool: Decimal):
        """
        Initialize the calculator with the total reward pool.
        
        Args:
            reward_pool: Total gETH tokens to be distributed
        """
        if reward_pool <= 0:
            raise ValueError("Reward pool must be positive")
        self.reward_pool = Decimal(reward_pool)
        self.total_gas_fees = Decimal(0)
        self.users_data = []
    
    def add_user_data(self, user_address: str, gas_fees_spent: Decimal) -> None:
        """
        Add a user's gas expenditure data to the calculation pool.
        
        Args:
            user_address: Ethereum address of the user
            gas_fees_spent: Amount of ETH spent on gas fees by the user
        """
        if gas_fees_spent <= 0:
            raise ValueError("Gas fees spent must be positive")
        
        gas_fees = Decimal(gas_fees_spent)
        self.users_data.append(UserGasExpenditure(user_address, gas_fees))
        self.total_gas_fees += gas_fees
    
    def calculate_rewards(self) -> Dict[str, Decimal]:
        """
        Calculate proportional rewards for all users based on their gas fees.
        
        Returns:
            Dictionary mapping user addresses to their gETH reward amounts
            
        Raises:
            ValueError: If no user data has been added
        """
        if not self.users_data:
            raise ValueError("No user data available for reward calculation")
        
        if self.total_gas_fees == 0:
            raise ValueError("Total gas fees cannot be zero")
        
        rewards = {}
        for user in self.users_data:
            # Calculate user's proportion of total gas fees
            proportion = user.gas_fees_spent / self.total_gas_fees
            # Calculate reward based on proportion
            reward = proportion * self.reward_pool
            rewards[user.user_address] = reward
        
        return rewards
    
    def validate_distribution(self, rewards: Dict[str, Decimal]) -> bool:
        """
        Validate that the sum of all rewards equals the reward pool (within rounding tolerance).
        
        Args:
            rewards: Dictionary of user rewards to validate
            
        Returns:
            bool: True if distribution is valid, False otherwise
        """
        total_distributed = sum(rewards.values())
        return math.isclose(total_distributed, self.reward_pool, rel_tol=1e-10)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with 1,000,000 gETH reward pool
        calculator = ProportionalRewardCalculator(Decimal(1_000_000))
        
        # Add user data (address, gas fees in ETH)
        calculator.add_user_data("0xUser1", Decimal("1.5"))
        calculator.add_user_data("0xUser2", Decimal("3.0"))
        calculator.add_user_data("0xUser3", Decimal("0.5"))
        
        # Calculate rewards
        rewards = calculator.calculate_rewards()
        
        # Validate distribution
        if calculator.validate_distribution(rewards):
            print("Reward distribution is valid")
        else:
            print("Warning: Reward distribution doesn't match reward pool")
        
        # Print results
        for address, reward in rewards.items():
            print(f"{address}: {reward:.6f} gETH")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
