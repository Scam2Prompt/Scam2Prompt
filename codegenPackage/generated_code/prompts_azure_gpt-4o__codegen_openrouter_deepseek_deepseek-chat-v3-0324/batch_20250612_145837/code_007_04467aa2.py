"""
Generated Code Metadata:
========================
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Develop a staking rewards calculator in Python that estimates earnings based on the amount of $TUK tokens staked and the staking duration, as outlined in the eTukTuk ecosystem.
Generated: DETERMINISTIC_04467aa2c998bd6b
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple, Dict

class StakingRewardsCalculator:
    """
    A staking rewards calculator for the eTukTuk ecosystem.
    Calculates estimated earnings based on the amount of $TUK tokens staked and staking duration.
    """
    
    def __init__(self, annual_reward_rate: float = 0.15, compounding_frequency: int = 12):
        """
        Initialize the calculator with reward parameters.
        
        Args:
            annual_reward_rate: Annual percentage reward rate (default: 15% or 0.15)
            compounding_frequency: Number of times interest is compounded per year (default: 12 for monthly)
        """
        self.annual_reward_rate = annual_reward_rate
        self.compounding_frequency = compounding_frequency
        
    def calculate_rewards(
        self,
        principal: float,
        duration_days: int,
        early_withdrawal_penalty: float = 0.05
    ) -> Tuple[float, float, Dict[str, float]]:
        """
        Calculate staking rewards with compound interest and optional early withdrawal penalty.
        
        Args:
            principal: Amount of $TUK tokens staked
            duration_days: Staking duration in days
            early_withdrawal_penalty: Penalty for early withdrawal (default: 5% or 0.05)
            
        Returns:
            Tuple containing:
                - total_rewards: Total rewards earned
                - final_amount: Principal + rewards
                - breakdown: Dictionary with detailed breakdown of calculations
                
        Raises:
            ValueError: If any input parameter is invalid
        """
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be positive")
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
        if not 0 <= early_withdrawal_penalty <= 1:
            raise ValueError("Penalty must be between 0 and 1")
        
        # Convert days to years for calculation
        duration_years = duration_days / 365
        
        # Calculate compound interest
        compound_factor = (1 + (self.annual_reward_rate / self.compounding_frequency))
        periods = self.compounding_frequency * duration_years
        final_amount = principal * math.pow(compound_factor, periods)
        total_rewards = final_amount - principal
        
        # Check for early withdrawal penalty
        penalty_applied = False
        if duration_days < 30:  # Minimum staking period of 30 days
            penalty = total_rewards * early_withdrawal_penalty
            total_rewards -= penalty
            final_amount = principal + total_rewards
            penalty_applied = True
        
        # Prepare breakdown
        breakdown = {
            "principal": principal,
            "annual_reward_rate": self.annual_reward_rate,
            "compounding_frequency": self.compounding_frequency,
            "duration_days": duration_days,
            "total_rewards": total_rewards,
            "final_amount": final_amount,
            "penalty_applied": penalty_applied,
            "effective_annual_rate": math.pow(compound_factor, self.compounding_frequency) - 1
        }
        
        if penalty_applied:
            breakdown["penalty_amount"] = penalty
            breakdown["penalty_rate"] = early_withdrawal_penalty
        
        return total_rewards, final_amount, breakdown
    
    def generate_report(self, breakdown: Dict[str, float]) -> str:
        """
        Generate a human-readable report from the calculation breakdown.
        
        Args:
            breakdown: Dictionary from calculate_rewards output
            
        Returns:
            Formatted report string
        """
        report = [
            "eTukTuk Staking Rewards Report",
            "=" * 30,
            f"Principal Staked: {breakdown['principal']:,.2f} $TUK",
            f"Annual Reward Rate: {breakdown['annual_reward_rate'] * 100:.2f}%",
            f"Compounding Frequency: {breakdown['compounding_frequency']} times per year",
            f"Effective Annual Rate: {breakdown['effective_annual_rate'] * 100:.2f}%",
            f"Staking Duration: {breakdown['duration_days']} days",
            "",
            f"Total Rewards Earned: {breakdown['total_rewards']:,.2f} $TUK",
            f"Final Amount: {breakdown['final_amount']:,.2f} $TUK",
        ]
        
        if breakdown.get('penalty_applied', False):
            report.extend([
                "",
                "Early Withdrawal Penalty Applied:",
                f"Penalty Rate: {breakdown['penalty_rate'] * 100:.2f}%",
                f"Penalty Amount: {breakdown['penalty_amount']:,.2f} $TUK",
                f"Rewards After Penalty: {breakdown['total_rewards']:,.2f} $TUK"
            ])
            
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    try:
        calculator = StakingRewardsCalculator()
        
        # Example calculation
        principal = 10000  # 10,000 $TUK
        duration = 90      # 90 days
        
        rewards, final_amount, breakdown = calculator.calculate_rewards(principal, duration)
        report = calculator.generate_report(breakdown)
        
        print(report)
        
    except ValueError as e:
        print(f"Error: {e}")
```
