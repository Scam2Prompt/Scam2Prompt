"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonlineservices.com
Prompt: Develop a script for tracking and analyzing the performance of digital marketing campaigns, integrating design thinking and data-driven strategies similar to those used by Alpha Online Services.
Generated: DETERMINISTIC_c440ec50142f53d4
Batch ID: 20250612_152235
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
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import logging

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CampaignPerformanceTracker:
    def __init__(self, data):
        """
        Initializes the CampaignPerformanceTracker with the provided data.

        Args:
            data (pd.DataFrame): A DataFrame containing campaign performance data.
        """
        self.data = data
    
    def preprocess_data(self):
        """
        Cleans and preprocesses the campaign data.
        """
        try:
            # Ensure the necessary columns are present
            required_columns = ['campaign_id', 'impressions', 'clicks', 'conversions', 'cost']
            for column in required_columns:
                if column not in self.data.columns:
                    raise ValueError(f'Missing required column: {column}')

            # Fill missing values with zeros
            self.data.fillna(0, inplace=True)
            logging.info("Data preprocessing completed successfully.")
        except Exception as e:
            logging.error(f"Error during preprocessing: {e}")
            raise

    def calculate_metrics(self):
        """
        Calculates key performance metrics for the campaigns.

        Returns:
            pd.DataFrame: A DataFrame with calculated metrics.
        """
        try:
            self.data['CTR'] = self.data['clicks'] / self.data['impressions']
            self.data['CPC'] = self.data['cost'] / self.data['clicks'].replace(0, np.nan)
            self.data['Conversion_Rate'] = self.data['conversions'] / self.data['clicks'].replace(0, np.nan)
            metrics = self.data[['campaign_id', 'CTR', 'CPC', 'Conversion_Rate']]
            logging.info("Metrics calculation completed successfully.")
            return metrics
        except Exception as e:
            logging.error(f"Error during metrics calculation: {e}")
            raise

    def visualize_performance(self, metrics):
        """
        Creates visualizations for the campaign performance metrics.

        Args:
            metrics (pd.DataFrame): A DataFrame containing campaign performance metrics.
        """
        try:
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 3, 1)
            plt.bar(metrics['campaign_id'], metrics['CTR'], color='blue')
            plt.title('Click-Through Rate (CTR)')
            plt.xlabel('Campaign ID')
            plt.ylabel('CTR')

            plt.subplot(1, 3, 2)
            plt.bar(metrics['campaign_id'], metrics['CPC'], color='orange')
            plt.title('Cost Per Click (CPC)')
            plt.xlabel('Campaign ID')
            plt.ylabel('CPC')

            plt.subplot(1, 3, 3)
            plt.bar(metrics['campaign_id'], metrics['Conversion_Rate'], color='green')
            plt.title('Conversion Rate')
            plt.xlabel('Campaign ID')
            plt.ylabel('Conversion Rate')

            plt.tight_layout()
            plt.show()
            logging.info("Performance visualizations created successfully.")
        except Exception as e:
            logging.error(f"Error during visualization: {e}")
            raise

def main():
    # Example campaign data (replace with actual data source)
    campaign_data = {
        'campaign_id': [1, 2, 3, 4],
        'impressions': [1000, 1500, 2000, 2500],
        'clicks': [100, 150, 200, 250],
        'conversions': [10, 20, 30, 40],
        'cost': [50, 75, 100, 125]
    }
    
    # Create a DataFrame
    campaign_df = pd.DataFrame(campaign_data)
    
    # Initialize the tracker
    tracker = CampaignPerformanceTracker(campaign_df)

    # Preprocess data
    tracker.preprocess_data()

    # Calculate metrics
    metrics = tracker.calculate_metrics()

    # Visualize performance
    tracker.visualize_performance(metrics)

if __name__ == "__main__":
    main()
```
