"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://master-brain.com
Prompt: Write code to track and measure the effectiveness of BTL and ATL advertising strategies, as implemented by Master-Brain.
Generated: DETERMINISTIC_0cf15b50b8ba3406
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List

class AdvertisingStrategyTracker:
    """
    A class to track and measure the effectiveness of BTL (Below The Line) and ATL (Above The Line) advertising strategies.
    """

    def __init__(self):
        """Initialize the AdvertisingStrategyTracker with an empty DataFrame."""
        self.data = pd.DataFrame(columns=['date', 'strategy', 'spend', 'reach', 'conversion'])

    def add_campaign(self, date: str, strategy: str, spend: float, reach: int, conversion: int):
        """
        Add a new advertising campaign to the tracker.

        Args:
            date (str): The date of the campaign in 'YYYY-MM-DD' format.
            strategy (str): The advertising strategy ('BTL' or 'ATL').
            spend (float): The amount spent on the campaign.
            reach (int): The number of people reached by the campaign.
            conversion (int): The number of conversions resulting from the campaign.
        """
        if strategy not in ['BTL', 'ATL']:
            raise ValueError("Strategy must be either 'BTL' or 'ATL'.")
        if spend < 0 or reach < 0 or conversion < 0:
            raise ValueError("Spend, reach, and conversion must be non-negative.")

        new_campaign = {
            'date': pd.to_datetime(date),
            'strategy': strategy,
            'spend': spend,
            'reach': reach,
            'conversion': conversion
        }
        self.data = self.data.append(new_campaign, ignore_index=True)

    def calculate_effectiveness(self) -> pd.DataFrame:
        """
        Calculate the effectiveness of the campaigns.

        Returns:
            pd.DataFrame: A DataFrame containing the effectiveness metrics for each strategy.
        """
        effectiveness = self.data.groupby('strategy').agg({
            'spend': 'sum',
            'reach': 'sum',
            'conversion': 'sum'
        })
        effectiveness['cost_per_reach'] = effectiveness['spend'] / effectiveness['reach']
        effectiveness['conversion_rate'] = effectiveness['conversion'] / effectiveness['reach']
        return effectiveness.reset_index()

    def plot_effectiveness(self, effectiveness: pd.DataFrame):
        """
        Plot the effectiveness metrics for each advertising strategy.

        Args:
            effectiveness (pd.DataFrame): The DataFrame containing the effectiveness metrics.
        """
        effectiveness.plot(x='strategy', y=['cost_per_reach', 'conversion_rate'], kind='bar', figsize=(10, 6))
        plt.title('Effectiveness of Advertising Strategies')
        plt.xlabel('Advertising Strategy')
        plt.ylabel('Metrics')
        plt.xticks(rotation=0)
        plt.legend(['Cost per Reach', 'Conversion Rate'])
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    tracker = AdvertisingStrategyTracker()
    try:
        tracker.add_campaign('2023-10-01', 'BTL', 5000, 1000, 100)
        tracker.add_campaign('2023-10-05', 'ATL', 8000, 5000, 200)
        tracker.add_campaign('2023-10-10', 'BTL', 3000, 800, 50)

        effectiveness = tracker.calculate_effectiveness()
        print(effectiveness)

        tracker.plot_effectiveness(effectiveness)
    except ValueError as e:
        print(f"Error: {e}")
```
