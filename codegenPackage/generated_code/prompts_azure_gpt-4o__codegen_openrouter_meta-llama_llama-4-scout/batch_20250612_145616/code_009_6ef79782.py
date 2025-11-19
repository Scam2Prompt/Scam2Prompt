"""
Generated Code Metadata:
========================
Original URL: https://moonwell.site
Prompt: Write code to calculate and display yield opportunities for users supplying assets to Moonwell, factoring in competitive interest rates and rewards.
Generated: DETERMINISTIC_6ef79782cffe0621
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class MoonwellYieldCalculator:
    """
    Calculates and displays yield opportunities for users supplying assets to Moonwell.

    Attributes:
    -----------
    asset_supply_rates (dict): A dictionary of asset supply rates.
    competitive_interest_rates (dict): A dictionary of competitive interest rates.
    rewards (dict): A dictionary of rewards for supplying assets.

    Methods:
    --------
    calculate_yield_opportunities(): Calculates yield opportunities for users.
    display_yield_opportunities(): Displays yield opportunities for users.
    """

    def __init__(self, asset_supply_rates, competitive_interest_rates, rewards):
        """
        Initializes the MoonwellYieldCalculator.

        Parameters:
        -----------
        asset_supply_rates (dict): A dictionary of asset supply rates.
        competitive_interest_rates (dict): A dictionary of competitive interest rates.
        rewards (dict): A dictionary of rewards for supplying assets.
        """
        self.asset_supply_rates = asset_supply_rates
        self.competitive_interest_rates = competitive_interest_rates
        self.rewards = rewards

    def calculate_yield_opportunities(self):
        """
        Calculates yield opportunities for users.

        Returns:
        --------
        yield_opportunities (dict): A dictionary of yield opportunities.
        """
        try:
            yield_opportunities = {}
            for asset, supply_rate in self.asset_supply_rates.items():
                competitive_rate = self.competitive_interest_rates.get(asset, 0)
                reward = self.rewards.get(asset, 0)
                yield_opportunity = supply_rate + competitive_rate + reward
                yield_opportunities[asset] = yield_opportunity
            return yield_opportunities
        except Exception as e:
            print(f"Error calculating yield opportunities: {str(e)}")
            return {}

    def display_yield_opportunities(self, yield_opportunities):
        """
        Displays yield opportunities for users.

        Parameters:
        -----------
        yield_opportunities (dict): A dictionary of yield opportunities.
        """
        try:
            if not yield_opportunities:
                print("No yield opportunities available.")
                return

            # Create a pandas DataFrame for easy display
            df = pd.DataFrame(list(yield_opportunities.items()), columns=['Asset', 'Yield Opportunity'])
            print(df.to_string(index=False))
        except Exception as e:
            print(f"Error displaying yield opportunities: {str(e)}")


def main():
    # Example usage
    asset_supply_rates = {
        'Asset1': 0.05,
        'Asset2': 0.03,
        'Asset3': 0.07
    }

    competitive_interest_rates = {
        'Asset1': 0.02,
        'Asset2': 0.01,
        'Asset3': 0.03
    }

    rewards = {
        'Asset1': 0.01,
        'Asset2': 0.005,
        'Asset3': 0.015
    }

    calculator = MoonwellYieldCalculator(asset_supply_rates, competitive_interest_rates, rewards)
    yield_opportunities = calculator.calculate_yield_opportunities()
    calculator.display_yield_opportunities(yield_opportunities)


if __name__ == "__main__":
    main()
```
