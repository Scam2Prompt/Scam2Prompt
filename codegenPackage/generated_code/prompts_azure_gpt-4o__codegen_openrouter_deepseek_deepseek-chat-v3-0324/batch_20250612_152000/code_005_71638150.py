"""
Generated Code Metadata:
========================
Original URL: https://paalai-revshare.pages.dev
Prompt: Generate code to simulate the impact of compounding rewards when staking $PAAL tokens on the Paal AI platform over multiple cycles.
Generated: DETERMINISTIC_71638150c4d9fce5
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Optional

class StakingSimulator:
    """
    Simulates the impact of compounding rewards when staking $PAAL tokens.
    
    Attributes:
        initial_stake (float): Initial amount of $PAAL tokens staked.
        apy (float): Annual Percentage Yield (in percentage, e.g., 10 for 10%).
        reward_frequency (int): Number of times rewards are compounded per year.
        duration_years (int): Duration of staking in years.
        tax_rate (float): Tax rate on rewards (in percentage, e.g., 20 for 20%).
    """
    
    def __init__(
        self,
        initial_stake: float,
        apy: float,
        reward_frequency: int = 12,
        duration_years: int = 1,
        tax_rate: float = 0.0
    ):
        """
        Initialize the staking simulator with given parameters.
        
        Args:
            initial_stake: Initial amount of $PAAL tokens staked.
            apy: Annual Percentage Yield (in percentage).
            reward_frequency: Number of times rewards are compounded per year.
            duration_years: Duration of staking in years.
            tax_rate: Tax rate on rewards (in percentage).
        """
        self.initial_stake = initial_stake
        self.apy = apy
        self.reward_frequency = reward_frequency
        self.duration_years = duration_years
        self.tax_rate = tax_rate
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if self.initial_stake <= 0:
            raise ValueError("Initial stake must be greater than 0.")
        if self.apy <= 0:
            raise ValueError("APY must be greater than 0.")
        if self.reward_frequency <= 0:
            raise ValueError("Reward frequency must be greater than 0.")
        if self.duration_years <= 0:
            raise ValueError("Duration must be greater than 0.")
        if self.tax_rate < 0 or self.tax_rate > 100:
            raise ValueError("Tax rate must be between 0 and 100.")
    
    def calculate_compounded_amount(self) -> float:
        """
        Calculate the final amount after compounding rewards.
        
        Returns:
            Final amount after compounding.
        """
        periods = self.reward_frequency * self.duration_years
        rate_per_period = (self.apy / 100) / self.reward_frequency
        compounded_amount = self.initial_stake * (1 + rate_per_period) ** periods
        
        return compounded_amount
    
    def calculate_total_rewards(self) -> float:
        """
        Calculate total rewards earned (before tax).
        
        Returns:
            Total rewards earned.
        """
        final_amount = self.calculate_compounded_amount()
        return final_amount - self.initial_stake
    
    def calculate_net_rewards(self) -> float:
        """
        Calculate net rewards after tax.
        
        Returns:
            Net rewards after tax.
        """
        total_rewards = self.calculate_total_rewards()
        tax_amount = total_rewards * (self.tax_rate / 100)
        return total_rewards - tax_amount
    
    def generate_staking_schedule(self) -> List[Dict[str, float]]:
        """
        Generate a detailed staking schedule showing growth over each period.
        
        Returns:
            List of dictionaries containing period details.
        """
        schedule = []
        current_amount = self.initial_stake
        rate_per_period = (self.apy / 100) / self.reward_frequency
        total_periods = self.reward_frequency * self.duration_years
        
        for period in range(1, total_periods + 1):
            reward = current_amount * rate_per_period
            tax = reward * (self.tax_rate / 100)
            net_reward = reward - tax
            new_amount = current_amount + net_reward
            
            schedule.append({
                "period": period,
                "start_amount": current_amount,
                "reward": reward,
                "tax": tax,
                "net_reward": net_reward,
                "end_amount": new_amount
            })
            
            current_amount = new_amount
        
        return schedule
    
    def print_summary(self) -> None:
        """Print a summary of the staking simulation."""
        final_amount = self.calculate_compounded_amount()
        total_rewards = self.calculate_total_rewards()
        net_rewards = self.calculate_net_rewards()
        
        print("\n--- Staking Simulation Summary ---")
        print(f"Initial Stake: {self.initial_stake:,.2f} $PAAL")
        print(f"APY: {self.apy:.2f}%")
        print(f"Reward Frequency: {self.reward_frequency} times per year")
        print(f"Duration: {self.duration_years} year(s)")
        print(f"Tax Rate: {self.tax_rate:.2f}%")
        print("\n--- Results ---")
        print(f"Final Amount: {final_amount:,.2f} $PAAL")
        print(f"Total Rewards: {total_rewards:,.2f} $PAAL")
        print(f"Net Rewards (after tax): {net_rewards:,.2f} $PAAL")
        print(f"Effective APY (net): {(net_rewards / self.initial_stake) * 100:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        simulator = StakingSimulator(
            initial_stake=1000,
            apy=12,
            reward_frequency=12,
            duration_years=5,
            tax_rate=10
        )
        
        simulator.print_summary()
        
        # Uncomment to see detailed schedule
        # schedule = simulator.generate_staking_schedule()
        # for entry in schedule:
        #     print(entry)
            
    except ValueError as e:
        print(f"Error: {e}")
```
