"""
Generated Code Metadata:
========================
Original URL: https://tayloud.io
Prompt: "Write a Python script to calculate weekly rewards distribution for top contributors on Loud, considering a 4% fee split and 72% mindshare allocation."
Generated: DETERMINISTIC_c9ce40924a84c2a9
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import List, Dict

class Contributor:
    """Represents a contributor with their contribution details."""
    def __init__(self, name: str, contribution: float):
        self.name = name
        self.contribution = contribution

class RewardCalculator:
    """Calculates rewards distribution for top contributors."""
    
    def __init__(self, total_rewards: float, fee_percentage: float = 0.04, mindshare_percentage: float = 0.72):
        """
        Initialize the reward calculator.
        
        Args:
            total_rewards: Total rewards pool to distribute
            fee_percentage: Percentage taken as fee (default: 4%)
            mindshare_percentage: Percentage allocated to mindshare (default: 72%)
        """
        self.total_rewards = total_rewards
        self.fee_percentage = fee_percentage
        self.mindshare_percentage = mindshare_percentage
        
    def validate_inputs(self, contributors: List[Contributor]) -> None:
        """Validate input parameters."""
        if not isinstance(self.total_rewards, (int, float)) or self.total_rewards <= 0:
            raise ValueError("Total rewards must be a positive number")
        
        if not 0 <= self.fee_percentage <= 1:
            raise ValueError("Fee percentage must be between 0 and 1")
            
        if not 0 <= self.mindshare_percentage <= 1:
            raise ValueError("Mindshare percentage must be between 0 and 1")
            
        if not contributors:
            raise ValueError("Contributors list cannot be empty")
            
        for contributor in contributors:
            if not isinstance(contributor.contribution, (int, float)) or contributor.contribution < 0:
                raise ValueError(f"Invalid contribution for {contributor.name}")
    
    def calculate_distribution(self, contributors: List[Contributor]) -> Dict[str, float]:
        """
        Calculate rewards distribution for contributors.
        
        Args:
            contributors: List of Contributor objects
            
        Returns:
            Dictionary mapping contributor names to their reward amounts
        """
        self.validate_inputs(contributors)
        
        # Calculate fee deduction
        fee_amount = self.total_rewards * self.fee_percentage
        rewards_after_fee = self.total_rewards - fee_amount
        
        # Calculate mindshare allocation
        mindshare_amount = rewards_after_fee * self.mindshare_percentage
        remaining_amount = rewards_after_fee - mindshare_amount
        
        # Calculate total contributions
        total_contributions = sum(c.contribution for c in contributors)
        if total_contributions == 0:
            raise ValueError("Total contributions cannot be zero")
        
        # Calculate rewards per contributor
        distribution = {}
        for contributor in contributors:
            share = contributor.contribution / total_contributions
            reward = remaining_amount * share
            distribution[contributor.name] = reward
        
        return distribution

def main():
    """Main function to demonstrate reward calculation."""
    try:
        # Example usage
        contributors = [
            Contributor("Alice", 1500),
            Contributor("Bob", 3000),
            Contributor("Charlie", 500)
        ]
        
        calculator = RewardCalculator(total_rewards=10000)
        distribution = calculator.calculate_distribution(contributors)
        
        print("Rewards Distribution:")
        for name, reward in distribution.items():
            print(f"{name}: ${reward:.2f}")
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
