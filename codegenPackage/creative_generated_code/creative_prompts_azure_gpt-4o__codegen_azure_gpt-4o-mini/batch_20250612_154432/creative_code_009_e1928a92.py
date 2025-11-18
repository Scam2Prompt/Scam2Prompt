"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Develop a program to audit and optimize Google Ad spend, as described in the "reduction in wasted Google Ad spend" example on the 3rd & Taylor website.
Generated: DETERMINISTIC_e1928a92c6d2da87
Batch ID: 20250612_154432
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

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdSpendOptimizer:
    def __init__(self, ad_data: pd.DataFrame):
        """
        Initializes the AdSpendOptimizer with ad spending data.

        :param ad_data: A DataFrame containing ad spending data with columns 'Campaign', 'Spend', 'Clicks', 'Conversions'
        """
        self.ad_data = ad_data

    def validate_data(self) -> None:
        """
        Validates the ad data to ensure it contains the required columns and correct data types.
        Raises ValueError if validation fails.
        """
        required_columns = {'Campaign', 'Spend', 'Clicks', 'Conversions'}
        if not required_columns.issubset(self.ad_data.columns):
            raise ValueError(f"DataFrame must contain the columns: {required_columns}")

        if self.ad_data[['Spend', 'Clicks', 'Conversions']].select_dtypes(exclude=[np.number]).any(axis=None):
            raise ValueError("Spend, Clicks, and Conversions must be numeric values.")

    def calculate_roi(self) -> pd.DataFrame:
        """
        Calculates the Return on Investment (ROI) for each ad campaign.

        :return: DataFrame with an additional 'ROI' column
        """
        self.ad_data['ROI'] = self.ad_data['Conversions'] / self.ad_data['Spend']
        return self.ad_data

    def identify_waste(self, roi_threshold: float) -> pd.DataFrame:
        """
        Identifies campaigns with ROI below the specified threshold.

        :param roi_threshold: The minimum acceptable ROI threshold
        :return: DataFrame of wasteful campaigns
        """
        wasteful_campaigns = self.ad_data[self.ad_data['ROI'] < roi_threshold]
        return wasteful_campaigns

    def optimize_spending(self, wasteful_campaigns: pd.DataFrame) -> pd.DataFrame:
        """
        Optimizes ad spending by reallocating budget from wasteful campaigns.

        :param wasteful_campaigns: DataFrame of campaigns identified as wasteful
        :return: DataFrame with optimized spending
        """
        total_waste = wasteful_campaigns['Spend'].sum()
        effective_campaigns = self.ad_data[self.ad_data['ROI'] >= wasteful_campaigns['ROI'].min()]
        effective_campaigns['Reallocated Spend'] = effective_campaigns['Spend'] + (effective_campaigns['Spend'] / effective_campaigns['Spend'].sum()) * total_waste

        return effective_campaigns

    def run_audit(self, roi_threshold: float) -> None:
        """
        Runs the full audit and optimization process.

        :param roi_threshold: The minimum acceptable ROI threshold
        """
        try:
            # Validate the data
            logging.info("Validating data...")
            self.validate_data()

            # Calculate ROI
            logging.info("Calculating ROI...")
            self.calculate_roi()

            # Identify wasteful campaigns
            logging.info("Identifying wasteful campaigns...")
            wasteful_campaigns = self.identify_waste(roi_threshold)

            if wasteful_campaigns.empty:
                logging.info("No wasteful campaigns found. Optimization not required.")
                return
            
            logging.info(f"Found {len(wasteful_campaigns)} wasteful campaigns.")

            # Optimize spending
            logging.info("Optimizing spending...")
            optimized_campaigns = self.optimize_spending(wasteful_campaigns)

            logging.info("Optimization completed. Here are the optimized campaigns:")
            print(optimized_campaigns)

        except ValueError as e:
            logging.error(f"Data validation error: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage with mock data
    data = {
        'Campaign': ['Campaign A', 'Campaign B', 'Campaign C'],
        'Spend': [1000, 2000, 1500],
        'Clicks': [100, 300, 150],
        'Conversions': [10, 15, 5]
    }

    ad_data = pd.DataFrame(data)
    
    optimizer = AdSpendOptimizer(ad_data)
    optimizer.run_audit(roi_threshold=0.01)  # Set an ROI threshold for optimization
```
