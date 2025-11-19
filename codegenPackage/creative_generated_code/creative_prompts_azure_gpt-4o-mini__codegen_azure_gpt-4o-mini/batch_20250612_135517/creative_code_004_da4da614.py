"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livinglargfx.com
Prompt: Outline a strategy for diversifying an investment portfolio using the asset classes available on livinglargfx, including cryptocurrencies and stock indices.
Generated: DETERMINISTIC_da4da614a05166ae
Batch ID: 20250612_135517
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
    A class to represent an investment portfolio with various asset classes.
    """
    
    def __init__(self):
        """
        Initializes an empty investment portfolio.
        """
        self.assets = {
            "stocks": [],
            "bonds": [],
            "real_estate": [],
            "cryptocurrencies": [],
            "commodities": [],
            "cash": []
        }
    
    def add_asset(self, asset_class, asset_name, allocation_percentage):
        """
        Adds an asset to the portfolio under the specified asset class.
        
        :param asset_class: Class of the asset (e.g., stocks, bonds)
        :param asset_name: Name of the asset to add
        :param allocation_percentage: Percentage of the portfolio to allocate
        :raises ValueError: If the allocation percentage is not valid
        """
        if allocation_percentage < 0 or allocation_percentage > 100:
            raise ValueError("Allocation percentage must be between 0 and 100.")
        
        self.assets[asset_class].append({
            "name": asset_name,
            "allocation": allocation_percentage
        })

    def diversify_portfolio(self):
        """
        Diversifies the portfolio by redistributing the allocations among asset classes.
        This function ensures that no single asset class exceeds a certain percentage of the total portfolio.
        """
        total_allocation = self.calculate_total_allocation()
        max_allocation = 30  # Define maximum allocation per asset class

        for asset_class, assets in self.assets.items():
            current_allocation = sum(asset['allocation'] for asset in assets)
            if current_allocation > max_allocation:
                # Reduce allocation for this asset class
                reduction_percentage = current_allocation - max_allocation
                self.rebalance_asset_class(asset_class, reduction_percentage)
            elif current_allocation < max_allocation:
                # Opportunity to increase allocation if below max
                self.increase_allocation(asset_class, max_allocation - current_allocation)

    def rebalance_asset_class(self, asset_class, reduction_percentage):
        """
        Reduces allocation for a specific asset class.
        
        :param asset_class: Class of the asset to rebalance
        :param reduction_percentage: Amount to reduce from the total allocation of the class
        """
        for asset in self.assets[asset_class]:
            if asset['allocation'] > 0:
                # Calculate reduction per asset proportionally
                reduction_amount = (reduction_percentage / sum(a['allocation'] for a in self.assets[asset_class])) * asset['allocation']
                asset['allocation'] -= reduction_amount

    def increase_allocation(self, asset_class, increase_percentage):
        """
        Increases the allocation for the specified asset class.
        
        :param asset_class: Class of the asset to increase allocation for
        :param increase_percentage: Amount to add to the total allocation of the class
        """
        # Randomly select an asset to increase allocation
        if self.assets[asset_class]:
            asset = random.choice(self.assets[asset_class])
            asset['allocation'] += increase_percentage

    def calculate_total_allocation(self):
        """
        Calculates the total allocation of all assets in the portfolio.
        
        :return: Total allocation percentage across all asset classes.
        """
        return sum(asset['allocation'] for assets in self.assets.values() for asset in assets)

    def display_portfolio(self):
        """
        Displays the current state of the investment portfolio.
        """
        for asset_class, assets in self.assets.items():
            print(f"--- {asset_class.capitalize()} ---")
            for asset in assets:
                print(f"Asset: {asset['name']}, Allocation: {asset['allocation']}%")
            print()  # Newline for better readability


# Example of creating and managing an investment portfolio
if __name__ == "__main__":
    try:
        portfolio = InvestmentPortfolio()
        portfolio.add_asset("stocks", "S&P 500", 25)
        portfolio.add_asset("bonds", "US Treasury", 20)
        portfolio.add_asset("cryptocurrencies", "Bitcoin", 40)
        portfolio.add_asset("real_estate", "REIT", 15)
        
        print("Initial Portfolio:")
        portfolio.display_portfolio()
        
        portfolio.diversify_portfolio()
        
        print("Diversified Portfolio:")
        portfolio.display_portfolio()
        
    except ValueError as e:
        print(f"Error: {e}")
```
