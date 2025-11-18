"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creocollective.io
Prompt: Develop a program to analyze ROI metrics from marketing campaigns, inspired by Creo Collective's case studies like "Record ROI: Coreview."
Generated: DETERMINISTIC_fcd1bf79c55c2f04
Batch ID: 20250612_152249
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

class MarketingCampaignROIAnalyzer:
    """
    A class to analyze ROI metrics from marketing campaigns.
    """

    def __init__(self, campaign_data_file):
        """
        Initializes the analyzer with campaign data.

        :param campaign_data_file: str, path to the CSV file containing campaign data
        """
        try:
            self.data = pd.read_csv(campaign_data_file)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {campaign_data_file} not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the provided file.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the data: {e}")

    def _validate_data(self):
        """
        Validates the data to ensure it contains necessary columns.
        Raises an error if the data is invalid.
        """
        required_columns = ['campaign_name', 'investment', 'revenue']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_roi(self):
        """
        Calculate the ROI for each campaign.

        :return: DataFrame with campaign names and their corresponding ROI
        """
        self.data['ROI'] = (self.data['revenue'] - self.data['investment']) / self.data['investment'] * 100
        return self.data[['campaign_name', 'ROI']]

    def plot_roi(self):
        """
        Plot the ROI of campaigns in a bar chart.
        """
        roi_data = self.calculate_roi()
        plt.figure(figsize=(10, 6))
        plt.barh(roi_data['campaign_name'], roi_data['ROI'], color='skyblue')
        plt.xlabel('ROI (%)')
        plt.title('ROI of Marketing Campaigns')
        plt.axvline(0, color='red', linestyle='--')  # Line at ROI = 0 for reference
        plt.grid(axis='x')
        plt.show()

    def analyze(self):
        """
        Run the analysis and plot the results.
        """
        roi_results = self.calculate_roi()
        print(roi_results)
        self.plot_roi()


if __name__ == "__main__":
    # Path to the campaign data CSV file
    campaign_data_file = 'campaigns.csv'
    
    try:
        roi_analyzer = MarketingCampaignROIAnalyzer(campaign_data_file)
        roi_analyzer.analyze()
    except Exception as e:
        print(f"Error during analysis: {e}")
``` 

Make sure to create a CSV file named `campaigns.csv` with the necessary data before running the code. The CSV should contain columns: `campaign_name`, `investment`, and `revenue`.
