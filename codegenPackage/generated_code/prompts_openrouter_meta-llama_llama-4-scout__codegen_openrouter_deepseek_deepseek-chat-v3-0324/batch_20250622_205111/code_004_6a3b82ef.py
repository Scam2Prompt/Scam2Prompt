"""
Generated Code Metadata:
========================
Original URL: https://tokenfi-teal.vercel.app
Prompt: Design a staking strategy for a user who wants to maximize their rewards on the TokenFi platform, considering the Supercharger ranks and exclusive perks, and write a simple algorithm to achieve this.
Generated: DETERMINISTIC_6a3b82ef88a14fcf
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class TokenFiStakingStrategy:
    """
    Implements a staking strategy to maximize rewards on TokenFi platform considering Supercharger ranks and perks.
    """
    
    def __init__(self, user_balance: float, supercharger_tiers: Dict[str, Tuple[float, float, float]]):
        """
        Initialize the staking strategy with user's balance and Supercharger tier details.
        
        Args:
            user_balance: Total amount of tokens the user can stake
            supercharger_tiers: Dictionary mapping tier names to (min_stake, max_stake, reward_multiplier)
        """
        self.user_balance = user_balance
        self.supercharger_tiers = supercharger_tiers
        self.validate_inputs()
    
    def validate_inputs(self):
        """Validate that inputs are positive and tiers are properly defined."""
        if self.user_balance <= 0:
            raise ValueError("User balance must be positive")
        if not self.supercharger_tiers:
            raise ValueError("Supercharger tiers must be provided")
        
        for tier_name, (min_stake, max_stake, multiplier) in self.supercharger_tiers.items():
            if min_stake < 0 or max_stake < min_stake or multiplier <= 0:
                raise ValueError(f"Invalid tier parameters for {tier_name}")
    
    def calculate_optimal_staking(self) -> Dict[str, float]:
        """
        Calculate optimal staking amounts across tiers to maximize rewards.
        
        Returns:
            Dictionary mapping tier names to optimal stake amounts
        """
        # Sort tiers by reward multiplier (descending) and min stake (ascending)
        sorted_tiers = sorted(
            self.supercharger_tiers.items(),
            key=lambda x: (-x[1][2], x[1][0])
        )
        
        allocation = {}
        remaining_balance = self.user_balance
        
        for tier_name, (min_stake, max_stake, multiplier) in sorted_tiers:
            if remaining_balance <= 0:
                allocation[tier_name] = 0
                continue
            
            # Calculate possible stake amount for this tier
            stake_amount = min(max_stake, remaining_balance)
            
            # Ensure we meet minimum stake requirement
            if stake_amount < min_stake:
                # Check if we can reallocate from lower tiers
                if self._can_reallocate(allocation, min_stake - stake_amount):
                    stake_amount = min_stake
                else:
                    stake_amount = 0
            
            allocation[tier_name] = stake_amount
            remaining_balance -= stake_amount
        
        return allocation
    
    def _can_reallocate(self, allocation: Dict[str, float], needed_amount: float) -> bool:
        """
        Check if we can reallocate funds from lower tiers to meet a needed amount.
        
        Args:
            allocation: Current allocation dictionary
            needed_amount: Amount needed to meet minimum stake
            
        Returns:
            True if reallocation is possible, False otherwise
        """
        # Get tiers sorted by priority (lowest first for reallocation)
        realloc_tiers = sorted(
            allocation.items(),
            key=lambda x: (self.supercharger_tiers[x[0]][2], x[1])
        )
        
        for tier_name, current_stake in realloc_tiers:
            if current_stake <= 0:
                continue
                
            # Calculate how much we can take from this tier
            min_stake = self.supercharger_tiers[tier_name][0]
            available = current_stake - min_stake
            
            if available > 0:
                transfer_amount = min(available, needed_amount)
                allocation[tier_name] -= transfer_amount
                needed_amount -= transfer_amount
                
                if needed_amount <= 0:
                    return True
        
        return False
    
    def calculate_total_rewards(self, allocation: Dict[str, float]) -> float:
        """
        Calculate total rewards based on allocation strategy.
        
        Args:
            allocation: Dictionary mapping tier names to stake amounts
            
        Returns:
            Total estimated rewards
        """
        total_rewards = 0.0
        for tier_name, amount in allocation.items():
            if amount > 0:
                multiplier = self.supercharger_tiers[tier_name][2]
                total_rewards += amount * multiplier
        return total_rewards


# Example usage
if __name__ == "__main__":
    # Define Supercharger tiers: {tier_name: (min_stake, max_stake, reward_multiplier)}
    supercharger_tiers = {
        "Diamond": (10000, 50000, 1.5),
        "Platinum": (5000, 20000, 1.3),
        "Gold": (1000, 10000, 1.2),
        "Silver": (500, 5000, 1.1),
        "Bronze": (100, 1000, 1.05)
    }
    
    try:
        user_balance = 25000  # Example user balance
        strategy = TokenFiStakingStrategy(user_balance, supercharger_tiers)
        optimal_allocation = strategy.calculate_optimal_staking()
        total_rewards = strategy.calculate_total_rewards(optimal_allocation)
        
        print("Optimal Staking Allocation:")
        for tier, amount in optimal_allocation.items():
            print(f"{tier}: {amount:,.2f}")
        print(f"\nTotal Estimated Rewards: {total_rewards:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
