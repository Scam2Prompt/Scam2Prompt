"""
Generated Code Metadata:
========================
Original URL: https://appwienerclaim.pages.dev
Prompt: Create a tokenomics analysis for WienerAI, detailing the distribution of $WAI tokens across presale, staking, community rewards, DEX/CEX liquidity, and marketing, and assessing potential impacts on token value.
Generated: DETERMINISTIC_a28d9947bbb25e02
Batch ID: 20250622_204635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Tuple

class TokenomicsAnalyzer:
    """
    Analyzes token distribution and potential impacts on token value.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize tokenomics analyzer with total token supply.
        
        Args:
            total_supply: Total number of tokens in existence
        """
        self.total_supply = total_supply
        self.distribution = {}
        self.lockup_periods = {}
        self.vesting_schedules = {}
        
    def add_distribution(self, category: str, percentage: float, 
                         lockup: int = 0, vesting: Tuple[int, int] = None):
        """
        Add a token distribution category.
        
        Args:
            category: Name of distribution category (e.g., 'Presale')
            percentage: Percentage of total supply allocated
            lockup: Lockup period in days (0 for no lockup)
            vesting: Tuple of (vesting_period_days, cliff_days) or None
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        tokens = (percentage / 100) * self.total_supply
        self.distribution[category] = tokens
        
        if lockup > 0:
            self.lockup_periods[category] = lockup
            
        if vesting:
            self.vesting_schedules[category] = vesting
            
    def calculate_circulating_supply(self, days_passed: int) -> int:
        """
        Calculate circulating supply based on lockups and vesting.
        
        Args:
            days_passed: Number of days since token launch
            
        Returns:
            Number of tokens currently in circulation
        """
        circulating = 0
        
        for category, tokens in self.distribution.items():
            # Check lockup period
            lockup = self.lockup_periods.get(category, 0)
            if days_passed < lockup:
                continue
                
            # Check vesting schedule
            vesting = self.vesting_schedules.get(category, None)
            if vesting:
                vesting_period, cliff = vesting
                if days_passed < cliff:
                    continue
                    
                vested_ratio = min(1, (days_passed - cliff) / vesting_period)
                circulating += tokens * vested_ratio
            else:
                circulating += tokens
                
        return int(circulating)
    
    def plot_distribution(self):
        """Generate pie chart of token distribution."""
        labels = list(self.distribution.keys())
        sizes = list(self.distribution.values())
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        plt.title('Token Distribution')
        plt.show()
        
    def plot_supply_over_time(self, days: int = 365):
        """
        Plot circulating supply over time.
        
        Args:
            days: Number of days to project
        """
        x = np.arange(0, days)
        y = [self.calculate_circulating_supply(day) for day in x]
        
        plt.figure()
        plt.plot(x, y)
        plt.xlabel('Days Since Launch')
        plt.ylabel('Circulating Supply')
        plt.title('Circulating Supply Over Time')
        plt.grid(True)
        plt.show()
        
    def analyze_impact(self) -> Dict[str, str]:
        """
        Analyze potential impacts on token value.
        
        Returns:
            Dictionary of analysis results
        """
        analysis = {}
        
        # Calculate initial circulating supply
        initial_supply = self.calculate_circulating_supply(0)
        initial_percent = (initial_supply / self.total_supply) * 100
        
        analysis['initial_supply'] = f"{initial_percent:.2f}% of tokens circulating at launch"
        
        # Check for large allocations
        for category, tokens in self.distribution.items():
            percent = (tokens / self.total_supply) * 100
            if percent > 20:
                analysis[f'large_allocation_{category}'] = (
                    f"Warning: {category} has {percent:.2f}% allocation - "
                    "potential for price volatility"
                )
                
        # Check lockups
        locked_tokens = sum(
            tokens for category, tokens in self.distribution.items() 
            if self.lockup_periods.get(category, 0) > 0
        )
        locked_percent = (locked_tokens / self.total_supply) * 100
        analysis['locked_supply'] = f"{locked_percent:.2f}% of tokens are locked"
        
        return analysis

# Example usage for WienerAI ($WAI)
if __name__ == "__main__":
    TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
    
    analyzer = TokenomicsAnalyzer(TOTAL_SUPPLY)
    
    # Add distribution categories (example values)
    analyzer.add_distribution("Presale", 30, lockup=30, vesting=(180, 30))
    analyzer.add_distribution("Staking Rewards", 20, lockup=0)
    analyzer.add_distribution("Community Rewards", 15, lockup=0)
    analyzer.add_distribution("DEX Liquidity", 20, lockup=0)
    analyzer.add_distribution("CEX Liquidity", 5, lockup=30)
    analyzer.add_distribution("Marketing", 10, lockup=0, vesting=(365, 90))
    
    # Generate visualizations
    analyzer.plot_distribution()
    analyzer.plot_supply_over_time(days=730)  # 2 years
    
    # Print analysis
    analysis = analyzer.analyze_impact()
    for key, value in analysis.items():
        print(f"{key}: {value}")
```
