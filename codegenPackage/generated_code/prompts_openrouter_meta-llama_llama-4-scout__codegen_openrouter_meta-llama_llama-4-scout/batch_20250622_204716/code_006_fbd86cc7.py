"""
Generated Code Metadata:
========================
Original URL: https://passive-income.online
Prompt: Write a script to analyze and optimize online marketing campaigns using data from multiple income streams, including metrics for conversion rates and return on investment (ROI).
Generated: DETERMINISTIC_fbd86cc72c64cd21
Batch ID: 20250622_204716
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
import numpy as np

class MarketingCampaignAnalyzer:
    """
    A class used to analyze and optimize online marketing campaigns.

    Attributes:
    ----------
    data : dict
        A dictionary containing data from multiple income streams.

    Methods:
    -------
    load_data(income_streams)
        Loads data from multiple income streams into the analyzer.
    calculate_conversion_rates()
        Calculates conversion rates for each income stream.
    calculate_roi()
        Calculates return on investment (ROI) for each income stream.
    optimize_campaigns()
        Optimizes online marketing campaigns based on conversion rates and ROI.
    """

    def __init__(self):
        """
        Initializes the MarketingCampaignAnalyzer with an empty dictionary to store data.
        """
        self.data = {}

    def load_data(self, income_streams):
        """
        Loads data from multiple income streams into the analyzer.

        Parameters:
        ----------
        income_streams : list
            A list of dictionaries, each containing data for an income stream.

        Returns:
        -------
        None
        """
        for stream in income_streams:
            self.data[stream['name']] = pd.DataFrame(stream['data'])

    def calculate_conversion_rates(self):
        """
        Calculates conversion rates for each income stream.

        Returns:
        -------
        dict
            A dictionary containing conversion rates for each income stream.
        """
        conversion_rates = {}
        for stream, data in self.data.items():
            # Check if required columns exist
            if 'conversions' in data.columns and 'impressions' in data.columns:
                conversion_rate = (data['conversions'] / data['impressions']) * 100
                conversion_rates[stream] = conversion_rate.mean()
            else:
                print(f"Warning: Required columns not found for {stream}. Skipping...")
        return conversion_rates

    def calculate_roi(self, costs):
        """
        Calculates return on investment (ROI) for each income stream.

        Parameters:
        ----------
        costs : dict
            A dictionary containing costs for each income stream.

        Returns:
        -------
        dict
            A dictionary containing ROI for each income stream.
        """
        roi = {}
        for stream, data in self.data.items():
            # Check if required columns exist
            if 'revenue' in data.columns:
                revenue = data['revenue'].sum()
                cost = costs.get(stream, 0)
                if cost != 0:
                    roi[stream] = (revenue - cost) / cost * 100
                else:
                    roi[stream] = np.nan
            else:
                print(f"Warning: Required columns not found for {stream}. Skipping...")
        return roi

    def optimize_campaigns(self, conversion_rates, roi):
        """
        Optimizes online marketing campaigns based on conversion rates and ROI.

        Parameters:
        ----------
        conversion_rates : dict
            A dictionary containing conversion rates for each income stream.
        roi : dict
            A dictionary containing ROI for each income stream.

        Returns:
        -------
        dict
            A dictionary containing optimization recommendations for each income stream.
        """
        optimizations = {}
        for stream in conversion_rates:
            conversion_rate = conversion_rates[stream]
            roi_value = roi[stream]
            if conversion_rate > 2 and roi_value > 100:
                optimizations[stream] = "Increase budget"
            elif conversion_rate < 1 and roi_value < 50:
                optimizations[stream] = "Decrease budget"
            else:
                optimizations[stream] = "Maintain current budget"
        return optimizations


def main():
    # Example usage
    income_streams = [
        {
            'name': 'Stream 1',
            'data': [
                {'conversions': 10, 'impressions': 100, 'revenue': 1000},
                {'conversions': 20, 'impressions': 200, 'revenue': 2000}
            ]
        },
        {
            'name': 'Stream 2',
            'data': [
                {'conversions': 5, 'impressions': 50, 'revenue': 500},
                {'conversions': 10, 'impressions': 100, 'revenue': 1000}
            ]
        }
    ]

    costs = {
        'Stream 1': 500,
        'Stream 2': 200
    }

    analyzer = MarketingCampaignAnalyzer()
    analyzer.load_data(income_streams)
    conversion_rates = analyzer.calculate_conversion_rates()
    roi = analyzer.calculate_roi(costs)
    optimizations = analyzer.optimize_campaigns(conversion_rates, roi)

    print("Conversion Rates:")
    for stream, rate in conversion_rates.items():
        print(f"{stream}: {rate:.2f}%")

    print("\nROI:")
    for stream, roi_value in roi.items():
        print(f"{stream}: {roi_value:.2f}%")

    print("\nOptimization Recommendations:")
    for stream, recommendation in optimizations.items():
        print(f"{stream}: {recommendation}")


if __name__ == "__main__":
    main()
```
