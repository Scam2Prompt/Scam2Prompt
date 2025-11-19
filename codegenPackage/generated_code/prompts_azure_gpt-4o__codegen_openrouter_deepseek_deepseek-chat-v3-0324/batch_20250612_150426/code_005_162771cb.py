"""
Generated Code Metadata:
========================
Original URL: https://invistribe.com
Prompt: Develop a Python program to calculate potential earnings based on the Fortunity reward tiers (Bronze, Silver, Gold) and simulate the growth of income over time.
Generated: DETERMINISTIC_162771cb25bcce89
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

class FortunityEarningsCalculator:
    """
    A class to calculate potential earnings based on Fortunity reward tiers and simulate income growth over time.
    """
    
    def __init__(self):
        """
        Initialize the calculator with reward tiers and their respective multipliers.
        """
        self.reward_tiers = {
            'Bronze': {'multiplier': 1.05, 'min_investment': 1000},
            'Silver': {'multiplier': 1.10, 'min_investment': 5000},
            'Gold': {'multiplier': 1.15, 'min_investment': 10000}
        }
    
    def validate_input(self, initial_investment: float, years: int, tier: str) -> Tuple[bool, str]:
        """
        Validate user inputs for correctness.
        
        Args:
            initial_investment: The initial investment amount
            years: Number of years to project
            tier: Reward tier (Bronze, Silver, Gold)
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if initial_investment <= 0:
            return False, "Initial investment must be positive."
        if years <= 0:
            return False, "Years must be positive."
        if tier not in self.reward_tiers:
            return False, f"Invalid tier. Must be one of: {list(self.reward_tiers.keys())}"
        if initial_investment < self.reward_tiers[tier]['min_investment']:
            return False, f"Minimum investment for {tier} tier is {self.reward_tiers[tier]['min_investment']}"
        return True, ""
    
    def calculate_earnings(self, initial_investment: float, years: int, tier: str) -> List[float]:
        """
        Calculate projected earnings over time based on reward tier.
        
        Args:
            initial_investment: The initial investment amount
            years: Number of years to project
            tier: Reward tier (Bronze, Silver, Gold)
            
        Returns:
            List of annual earnings including the initial investment
        """
        multiplier = self.reward_tiers[tier]['multiplier']
        earnings = [initial_investment]
        
        for _ in range(years):
            earnings.append(earnings[-1] * multiplier)
            
        return earnings
    
    def plot_earnings(self, earnings: List[float], tier: str) -> None:
        """
        Generate a plot of the earnings growth over time.
        
        Args:
            earnings: List of annual earnings
            tier: Reward tier used for the calculation
        """
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(earnings)), earnings, marker='o')
        plt.title(f'Projected Earnings Growth ({tier} Tier)')
        plt.xlabel('Years')
        plt.ylabel('Amount ($)')
        plt.grid(True)
        plt.show()
    
    def run_simulation(self) -> None:
        """
        Run the earnings simulation with user input and display results.
        """
        print("Fortunity Earnings Calculator")
        print("-----------------------------")
        
        try:
            # Get user input
            initial_investment = float(input("Enter initial investment amount: $"))
            years = int(input("Enter number of years to project: "))
            tier = input("Enter reward tier (Bronze, Silver, Gold): ").capitalize()
            
            # Validate input
            is_valid, error_msg = self.validate_input(initial_investment, years, tier)
            if not is_valid:
                print(f"Error: {error_msg}")
                return
            
            # Calculate and display results
            earnings = self.calculate_earnings(initial_investment, years, tier)
            
            print("\nProjected Earnings:")
            for year, amount in enumerate(earnings):
                print(f"Year {year}: ${amount:,.2f}")
            
            # Plot results
            self.plot_earnings(earnings, tier)
            
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator = FortunityEarningsCalculator()
    calculator.run_simulation()
```
