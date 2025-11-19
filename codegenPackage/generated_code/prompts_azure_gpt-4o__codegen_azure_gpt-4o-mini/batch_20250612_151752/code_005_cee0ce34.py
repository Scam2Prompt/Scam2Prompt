"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Create a Python script to analyze the ROI of social media video campaigns produced by Kraken Media, focusing on metrics like clicks, conversions, and revenue.
Generated: DETERMINISTIC_cee0ce349527f72b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class SocialMediaCampaignAnalyzer:
    """
    A class to analyze the ROI of social media video campaigns.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the data from a CSV file.

        :param data_file: str, path to the CSV file containing campaign data
        """
        self.data_file = data_file
        self.campaign_data = self.load_data()

    def load_data(self):
        """
        Loads campaign data from a CSV file.

        :return: DataFrame containing the campaign data
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_roi(self):
        """
        Calculates the ROI for each campaign based on clicks, conversions, and revenue.

        :return: DataFrame with ROI calculations
        """
        if 'revenue' not in self.campaign_data.columns or 'cost' not in self.campaign_data.columns:
            raise ValueError("Data must contain 'revenue' and 'cost' columns.")

        # Calculate ROI
        self.campaign_data['roi'] = (self.campaign_data['revenue'] - self.campaign_data['cost']) / self.campaign_data['cost']
        return self.campaign_data[['campaign_name', 'roi']]

    def summarize_campaigns(self):
        """
        Summarizes the campaign performance metrics.

        :return: DataFrame with summary statistics
        """
        summary = {
            'total_clicks': self.campaign_data['clicks'].sum(),
            'total_conversions': self.campaign_data['conversions'].sum(),
            'total_revenue': self.campaign_data['revenue'].sum(),
            'total_cost': self.campaign_data['cost'].sum(),
            'average_roi': self.campaign_data['roi'].mean()
        }
        return pd.DataFrame(summary, index=[0])

    def run_analysis(self):
        """
        Runs the complete analysis and returns the results.

        :return: Tuple of ROI DataFrame and summary DataFrame
        """
        roi_data = self.calculate_roi()
        summary_data = self.summarize_campaigns()
        return roi_data, summary_data


if __name__ == "__main__":
    # Path to the CSV file containing campaign data
    data_file_path = 'campaign_data.csv'

    # Create an instance of the analyzer
    analyzer = SocialMediaCampaignAnalyzer(data_file_path)

    # Run the analysis
    try:
        roi_results, summary_results = analyzer.run_analysis()
        print("ROI Results:")
        print(roi_results)
        print("\nSummary Results:")
        print(summary_results)
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```
