"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivadainfotech.com
Prompt: Write code to track and optimize ad performance for hospitals using Vivada Infotech's SKLS method, focusing on patient acquisition.
Generated: DETERMINISTIC_2b44f5c99c37b93f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import logging
from datetime import datetime

# Set up logging for tracking the application's behavior
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdPerformanceTracker:
    """
    A class to track and optimize ad performance for hospitals using Vivada Infotech's SKLS method.
    Focuses on patient acquisition through analyzing ad data and patient conversion metrics.
    """

    def __init__(self, ad_data: pd.DataFrame):
        """
        Initializes the AdPerformanceTracker with ad data.
        
        :param ad_data: A DataFrame containing ad performance data.
        """
        self.ad_data = ad_data
        self.optimized_data = pd.DataFrame()

    def validate_data(self):
        """
        Validates the ad data for expected structure and values.
        Raises ValueError if the data is not valid.
        """
        required_columns = ['ad_id', 'impressions', 'clicks', 'conversions', 'cost']
        for column in required_columns:
            if column not in self.ad_data.columns:
                raise ValueError(f"Missing required column: {column}")
        logging.info("Data validation successful.")

    def calculate_metrics(self):
        """
        Calculates important metrics for ad performance.
        Adds metrics to the optimized_data DataFrame.
        """
        try:
            self.optimized_data['CTR'] = self.ad_data['clicks'] / self.ad_data['impressions']
            self.optimized_data['CPC'] = self.ad_data['cost'] / self.ad_data['clicks']
            self.optimized_data['conversion_rate'] = self.ad_data['conversions'] / self.ad_data['clicks']
            self.optimized_data['ROI'] = (self.ad_data['conversions'] * 100) / self.ad_data['cost']
            logging.info("Metrics calculated successfully.")
        except ZeroDivisionError as e:
            logging.error("Division by zero encountered while calculating metrics: %s", e)
        except Exception as e:
            logging.error("An error occurred while calculating metrics: %s", e)

    def optimize_ads(self, threshold: float):
        """
        Optimizes ads based on a defined threshold for conversion rate.
        
        :param threshold: The minimum conversion rate for ads to be considered effective.
        :return: A DataFrame of optimized ad performance.
        """
        try:
            self.optimized_data['is_effective'] = self.optimized_data['conversion_rate'] >= threshold
            optimized_ads = self.optimized_data[self.optimized_data['is_effective']]
            logging.info(f"Ads optimized. {optimized_ads.shape[0]} ads meet the effectiveness threshold.")
            return optimized_ads
        except Exception as e:
            logging.error("An error occurred during the ad optimization process: %s", e)
            return pd.DataFrame()  # Return empty DataFrame on error

    def report(self, optimized_ads: pd.DataFrame):
        """
        Generates a summary report of the optimized ads.
        
        :param optimized_ads: A DataFrame of optimized ad performance.
        """
        if optimized_ads.empty:
            logging.warning("No effective ads to report on.")
            return
        logging.info("Optimized Ads Report:")
        for index, row in optimized_ads.iterrows():
            logging.info(f"Ad ID: {row['ad_id']} | CTR: {row['CTR']:.2%} | "
                         f"CPC: ${row['CPC']:.2f} | Conversion Rate: {row['conversion_rate']:.2%} | "
                         f"ROI: {row['ROI']:.2f}%")

if __name__ == "__main__":
    # Sample ad performance data for demonstration
    sample_data = {
        'ad_id': [1, 2, 3, 4, 5],
        'impressions': [1000, 2000, 1500, 0, 500],  # One ad with zero impressions to test error handling
        'clicks': [100, 150, 120, 0, 50],
        'conversions': [10, 15, 12, 0, 5],
        'cost': [200, 300, 250, 0, 100]
    }
    
    ad_data_df = pd.DataFrame(sample_data)

    # Initialize tracker and run processes
    tracker = AdPerformanceTracker(ad_data_df)

    try:
        tracker.validate_data()
        tracker.calculate_metrics()
        optimized_ads = tracker.optimize_ads(threshold=0.1)  # 10% conversion rate as threshold
        tracker.report(optimized_ads)
    except ValueError as e:
        logging.error("Invalid data encountered: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
```
