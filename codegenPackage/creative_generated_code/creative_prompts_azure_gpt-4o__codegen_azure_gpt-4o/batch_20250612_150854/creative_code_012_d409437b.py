"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategrowth.site
Prompt: Create a program to simulate the impact of international events on investment portfolios, inspired by Coin Growth’s focus on global market dynamics.
Generated: DETERMINISTIC_d409437bf1f99c61
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class InvestmentPortfolio:
    """
    Represents an investment portfolio which consists of various assets.
    Each asset has its own allocation percentage and growth rate.
    """
    
    def __init__(self, assets=None):
        """
        Initialize the portfolio with a dictionary of assets.
        Each asset has a name, allocation percentage, and growth rate.
        
        :param assets: Dictionary where keys are asset names and values are tuples 
                       (allocation_percentage, growth_rate).
        """
        if assets is None:
            assets = {}
        self.assets = assets

    def add_asset(self, name, allocation_percentage, growth_rate):
        """
        Add a new asset to the portfolio.
        
        :param name: Name of the asset.
        :param allocation_percentage: Percentage of total investment allocated to this asset.
        :param growth_rate: Expected annual growth rate (in percentage) of this asset.
        """
        if name in self.assets:
            raise ValueError("Asset already exists in the portfolio.")
        if allocation_percentage <= 0 or allocation_percentage > 100:
            raise ValueError("Allocation percentage must be between 0 and 100.")
        
        self.assets[name] = (allocation_percentage, growth_rate)

    def simulate_event_impact(self, event_factor):
        """
        Simulate the impact of an international event on the portfolio.
        
        :param event_factor: A dictionary where keys are asset names and values are
                             percentage changes in growth rate caused by the event.
        :return: A dictionary containing the updated growth rates after the event impact.
        """
        updated_growth_rates = {}
        for asset, (allocation_percentage, growth_rate) in self.assets.items():
            impact = event_factor.get(asset, 0)
            updated_growth_rate = growth_rate + impact
            # Ensure growth rate cannot drop below -100%
            updated_growth_rate = max(updated_growth_rate, -100)
            updated_growth_rates[asset] = updated_growth_rate
        return updated_growth_rates

    def simulate_portfolio_growth(self, years, updated_growth_rates=None):
        """
        Simulate the portfolio's growth over a given number of years.
        
        :param years: Number of years to simulate growth.
        :param updated_growth_rates: Dictionary of growth rates to use instead of the original.
        :return: Total growth of the portfolio over the specified years.
        """
        total_growth = 0
        for asset, (allocation_percentage, growth_rate) in self.assets.items():
            effective_growth_rate = updated_growth_rates.get(asset, growth_rate) if updated_growth_rates else growth_rate
            growth = (allocation_percentage / 100) * ((1 + effective_growth_rate / 100) ** years - 1)
            total_growth += growth
        return total_growth


# Simulated international event factors
def generate_event_factor(assets):
    """
    Generate a random event factor for each asset in the portfolio.
    Positive or negative impact ranges between -10% and +10%.
    
    :param assets: List of asset names in the portfolio.
    :return: Dictionary where keys are asset names and values are random percentage changes.
    """
    return {asset: random.uniform(-10, 10) for asset in assets}


# Example usage
if __name__ == "__main__":
    # Create an investment portfolio
    portfolio = InvestmentPortfolio()
    portfolio.add_asset("Stocks", 50, 8)
    portfolio.add_asset("Bonds", 30, 4)
    portfolio.add_asset("Real Estate", 20, 6)

    # Print initial state
    print("Initial Portfolio:", portfolio.assets)

    # Generate random event impact
    event_factor = generate_event_factor(portfolio.assets.keys())
    print("Event Factor Impact:", event_factor)

    # Simulate event impact
    updated_rates = portfolio.simulate_event_impact(event_factor)
    print("Updated Growth Rates:", updated_rates)

    # Simulate portfolio growth over 5 years
    growth_before_event = portfolio.simulate_portfolio_growth(5)
    growth_after_event = portfolio.simulate_portfolio_growth(5, updated_rates)

    print(f"Portfolio Growth Over 5 Years (Before Event): {growth_before_event:.2f}%")
    print(f"Portfolio Growth Over 5 Years (After Event): {growth_after_event:.2f}%")
```
