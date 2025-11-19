"""
Generated Code Metadata:
========================
Original URL: https://aitech-c09.pages.dev
Prompt: Write a script to automate the calculation of rewards earned in staking pools with varying lock terms and tier boosts, using the AITECH staking model as a reference.
Generated: DETERMINISTIC_af3ba2c4469f8bf7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional, Tuple

class StakingRewardCalculator:
    """
    A class to calculate staking rewards based on lock terms and tier boosts.
    Reference model: AITECH staking model.
    """
    
    def __init__(
        self,
        base_apr: float,
        lock_term_boost: Dict[int, float],
        tier_boost: Dict[str, float],
        compounding_frequency: int = 365
    ):
        """
        Initialize the calculator with staking parameters.
        
        Args:
            base_apr: Base annual percentage rate (as decimal, e.g., 0.1 for 10%)
            lock_term_boost: Dictionary mapping lock terms (days) to boost multipliers
            tier_boost: Dictionary mapping tier names to boost multipliers
            compounding_frequency: Number of compounding periods per year (default: daily)
        """
        self.base_apr = base_apr
        self.lock_term_boost = lock_term_boost
        self.tier_boost = tier_boost
        self.compounding_frequency = compounding_frequency
        
        # Validate inputs
        if not self._validate_parameters():
            raise ValueError("Invalid staking parameters provided")

    def _validate_parameters(self) -> bool:
        """Validate that all parameters are within acceptable ranges."""
        if self.base_apr <= 0:
            return False
        if any(boost <= 0 for boost in self.lock_term_boost.values()):
            return False
        if any(boost <= 0 for boost in self.tier_boost.values()):
            return False
        if self.compounding_frequency <= 0:
            return False
        return True

    def calculate_rewards(
        self,
        principal: float,
        lock_term_days: int,
        tier: str,
        days_staked: Optional[int] = None
    ) -> Tuple[float, Dict[str, float]]:
        """
        Calculate total rewards earned for a staking position.
        
        Args:
            principal: Amount of tokens staked
            lock_term_days: Number of days tokens are locked
            tier: Staker tier (must match keys in tier_boost)
            days_staked: Optional actual days staked (defaults to lock_term_days)
            
        Returns:
            Tuple of (total_rewards, breakdown) where breakdown contains:
            - base_rewards
            - lock_term_boosted
            - tier_boosted
            - total_boost_multiplier
        """
        if days_staked is None:
            days_staked = lock_term_days
            
        if days_staked <= 0:
            raise ValueError("Days staked must be positive")
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if lock_term_days not in self.lock_term_boost:
            raise ValueError(f"Invalid lock term: {lock_term_days}")
        if tier not in self.tier_boost:
            raise ValueError(f"Invalid tier: {tier}")

        # Calculate effective APR with boosts
        lock_boost = self.lock_term_boost[lock_term_days]
        tier_boost = self.tier_boost[tier]
        total_boost = lock_boost * tier_boost
        effective_apr = self.base_apr * total_boost

        # Calculate rewards with daily compounding
        periods = days_staked * (self.compounding_frequency / 365)
        rate_per_period = effective_apr / self.compounding_frequency
        total_amount = principal * math.pow(1 + rate_per_period, periods)
        total_rewards = total_amount - principal

        # Calculate base rewards without boosts for breakdown
        base_amount = principal * math.pow(1 + self.base_apr / self.compounding_frequency, periods)
        base_rewards = base_amount - principal

        breakdown = {
            "base_rewards": base_rewards,
            "lock_term_boosted": base_rewards * (lock_boost - 1),
            "tier_boosted": base_rewards * lock_boost * (tier_boost - 1),
            "total_boost_multiplier": total_boost
        }

        return (total_rewards, breakdown)

    def calculate_rewards_for_multiple_positions(
        self,
        positions: List[Dict[str, float]]
    ) -> Dict[str, float]:
        """
        Calculate rewards for multiple staking positions.
        
        Args:
            positions: List of dictionaries with keys:
                - principal
                - lock_term_days
                - tier
                - days_staked (optional)
                
        Returns:
            Dictionary with total rewards and breakdown by position
        """
        results = {
            "total_rewards": 0.0,
            "positions": []
        }
        
        for idx, position in enumerate(positions):
            try:
                rewards, breakdown = self.calculate_rewards(**position)
                results["total_rewards"] += rewards
                results["positions"].append({
                    "position_id": idx + 1,
                    "rewards": rewards,
                    "breakdown": breakdown
                })
            except ValueError as e:
                raise ValueError(f"Error in position {idx + 1}: {str(e)}")
                
        return results


# Example usage (would typically be in a separate file)
if __name__ == "__main__":
    # Example configuration matching AITECH-like model
    calculator = StakingRewardCalculator(
        base_apr=0.1,  # 10% base APR
        lock_term_boost={
            30: 1.0,    # 30-day lock: 1x
            90: 1.5,    # 90-day lock: 1.5x
            180: 2.0,   # 180-day lock: 2x
            365: 3.0    # 365-day lock: 3x
        },
        tier_boost={
            "basic": 1.0,
            "silver": 1.2,
            "gold": 1.5,
            "platinum": 2.0
        }
    )
    
    # Example positions
    positions = [
        {"principal": 1000, "lock_term_days": 90, "tier": "silver"},
        {"principal": 5000, "lock_term_days": 180, "tier": "gold", "days_staked": 150}
    ]
    
    try:
        results = calculator.calculate_rewards_for_multiple_positions(positions)
        print("Total rewards:", results["total_rewards"])
        for pos in results["positions"]:
            print(f"Position {pos['position_id']}:")
            print(f"  Rewards: {pos['rewards']:.2f}")
            print("  Breakdown:")
            for k, v in pos["breakdown"].items():
                print(f"    {k}: {v:.2f}")
    except ValueError as e:
        print("Error calculating rewards:", e)
```
