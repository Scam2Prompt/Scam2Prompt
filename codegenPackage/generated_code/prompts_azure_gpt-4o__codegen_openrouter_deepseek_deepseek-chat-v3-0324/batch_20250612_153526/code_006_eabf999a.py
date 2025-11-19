"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Create a Python script to simulate staking rewards distribution for $SCOTTY tokens over a 3-year period, factoring in the dynamic rewards rate and pool percentage.
Generated: DETERMINISTIC_eabf999ace3865d7
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import List, Dict, Tuple

class StakingSimulator:
    """
    Simulates staking rewards distribution for $SCOTTY tokens over a specified period.
    Handles dynamic rewards rates and pool percentages.
    """
    
    def __init__(
        self,
        initial_supply: float,
        staking_period_days: int,
        reward_pool_percentage: float,
        reward_rates: List[Tuple[float, float]],  # [(days, rate), ...]
        compounding_frequency: int = 1  # 1 for daily, 7 for weekly, etc.
    ):
        """
        Initialize the staking simulator.
        
        Args:
            initial_supply: Initial token supply
            staking_period_days: Total staking period in days
            reward_pool_percentage: Percentage of supply allocated to rewards pool
            reward_rates: List of tuples (days, rate) defining reward rate changes
            compounding_frequency: How often rewards are compounded (in days)
        """
        self.initial_supply = initial_supply
        self.staking_period_days = staking_period_days
        self.reward_pool_percentage = reward_pool_percentage
        self.reward_rates = self._validate_reward_rates(reward_rates)
        self.compounding_frequency = compounding_frequency
        
        # Calculate reward pool size
        self.reward_pool = initial_supply * (reward_pool_percentage / 100)
        
        # Initialize tracking variables
        self.current_date = datetime.now()
        self.daily_data = []
        
    def _validate_reward_rates(self, reward_rates: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """Validate and sort reward rates by days."""
        if not reward_rates:
            raise ValueError("At least one reward rate must be provided")
            
        # Sort by days
        sorted_rates = sorted(reward_rates, key=lambda x: x[0])
        
        # Check for negative values
        for days, rate in sorted_rates:
            if days < 0 or rate < 0:
                raise ValueError("Days and rates must be non-negative")
                
        return sorted_rates
    
    def _get_current_rate(self, day: int) -> float:
        """Get the current reward rate for a given day."""
        current_rate = 0.0
        for threshold, rate in self.reward_rates:
            if day >= threshold:
                current_rate = rate
        return current_rate
    
    def simulate(self, staked_amount: float) -> Dict[str, List]:
        """
        Run the staking simulation.
        
        Args:
            staked_amount: Amount of tokens staked by the user
            
        Returns:
            Dictionary containing daily data and summary statistics
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive")
            
        total_days = self.staking_period_days
        current_amount = staked_amount
        total_rewards = 0.0
        
        self.daily_data = []
        
        for day in range(1, total_days + 1):
            # Get current rate
            current_rate = self._get_current_rate(day)
            
            # Calculate daily reward
            daily_reward = current_amount * (current_rate / 100 / 365)
            
            # Only compound at specified frequency
            if day % self.compounding_frequency == 0:
                current_amount += daily_reward * self.compounding_frequency
                total_rewards += daily_reward * self.compounding_frequency
            else:
                total_rewards += daily_reward
                
            # Record daily data
            self.daily_data.append({
                'day': day,
                'date': self.current_date + timedelta(days=day),
                'current_amount': current_amount,
                'daily_reward': daily_reward,
                'total_rewards': total_rewards,
                'current_rate': current_rate
            })
            
        return {
            'daily_data': self.daily_data,
            'summary': {
                'initial_staked': staked_amount,
                'final_amount': current_amount,
                'total_rewards': total_rewards,
                'apy': self.calculate_apy(staked_amount, current_amount),
                'reward_pool_remaining': self.reward_pool - total_rewards
            }
        }
    
    @staticmethod
    def calculate_apy(initial: float, final: float, years: float = 1.0) -> float:
        """
        Calculate APY based on initial and final amounts.
        
        Args:
            initial: Initial amount
            final: Final amount
            years: Time period in years
            
        Returns:
            APY as percentage
        """
        if initial <= 0:
            return 0.0
        return ((final / initial) ** (1 / years) - 1) * 100
    
    def generate_report(self, simulation_data: Dict) -> str:
        """Generate a human-readable report of the simulation results."""
        summary = simulation_data['summary']
        
        report = [
            "SCOTTY Token Staking Simulation Report",
            "=====================================",
            f"Initial Staked Amount: {summary['initial_staked']:,.2f} SCOTTY",
            f"Final Amount: {summary['final_amount']:,.2f} SCOTTY",
            f"Total Rewards Earned: {summary['total_rewards']:,.2f} SCOTTY",
            f"Estimated APY: {summary['apy']:.2f}%",
            f"Reward Pool Remaining: {summary['reward_pool_remaining']:,.2f} SCOTTY",
            "\nReward Rate Schedule:"
        ]
        
        for days, rate in self.reward_rates:
            report.append(f"  After {days} days: {rate}% APR")
            
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Configuration
    INITIAL_SUPPLY = 1_000_000_000  # 1B tokens
    STAKING_PERIOD_DAYS = 3 * 365  # 3 years
    REWARD_POOL_PERCENTAGE = 20.0  # 20% of supply allocated to rewards
    REWARD_RATES = [
        (0, 50.0),    # 50% APR for first 6 months
        (180, 30.0),  # 30% APR for next 6 months
        (365, 20.0),  # 20% APR for second year
        (730, 10.0)   # 10% APR for third year
    ]
    COMPOUNDING_FREQUENCY = 7  # Weekly compounding
    
    # Initialize simulator
    simulator = StakingSimulator(
        initial_supply=INITIAL_SUPPLY,
        staking_period_days=STAKING_PERIOD_DAYS,
        reward_pool_percentage=REWARD_POOL_PERCENTAGE,
        reward_rates=REWARD_RATES,
        compounding_frequency=COMPOUNDING_FREQUENCY
    )
    
    # Run simulation with 10,000 tokens staked
    results = simulator.simulate(staked_amount=10_000)
    
    # Generate and print report
    print(simulator.generate_report(results))
```
