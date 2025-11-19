"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Generate a code snippet for a digital marketing tool that tracks Return on Investment (ROI) for online campaigns, inspired by Romain Rissoan's approach to digital transformation.
Generated: DETERMINISTIC_9f3746c3bd0f6f04
Batch ID: 20250612_161745
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

class ROICalculator:
    """
    A class to calculate Return on Investment (ROI) for digital marketing campaigns.
    
    Attributes:
        campaign_data (DataFrame): A DataFrame containing campaign information.
    """

    def __init__(self, campaign_data):
        """
        Initializes the ROICalculator with campaign data.

        Parameters:
            campaign_data (DataFrame): DataFrame with columns ['campaign_name', 'cost', 'revenue'].
        """
        self.campaign_data = campaign_data

    def validate_data(self):
        """
        Validates the campaign data to ensure required columns are present and contain valid values.

        Raises:
            ValueError: If required columns are missing or contain invalid data.
        """
        required_columns = ['campaign_name', 'cost', 'revenue']
        for column in required_columns:
            if column not in self.campaign_data.columns:
                raise ValueError(f"Missing required column: {column}")

        if self.campaign_data[['cost', 'revenue']].isnull().values.any():
            raise ValueError("Campaign data contains null values in 'cost' or 'revenue' columns.")

    def calculate_roi(self):
        """
        Calculates ROI for each campaign and returns a DataFrame with results.

        Returns:
            DataFrame: A DataFrame with campaign names and their respective ROI.
        """
        self.validate_data()  # Validate data before processing

        # Calculate ROI for each campaign
        self.campaign_data['ROI'] = (self.campaign_data['revenue'] - self.campaign_data['cost']) / self.campaign_data['cost'] * 100

        # Return relevant columns
        return self.campaign_data[['campaign_name', 'ROI']]

    def display_results(self):
        """
        Displays the ROI results in a formatted manner.
        """
        try:
            roi_results = self.calculate_roi()
            print("ROI Results for Campaigns:")
            print(roi_results.to_string(index=False))
        except Exception as e:
            print(f"An error occurred while calculating ROI: {e}")

# Example usage
if __name__ == "__main__":
    # Sample campaign data
    data = {
        'campaign_name': ['Campaign A', 'Campaign B', 'Campaign C'],
        'cost': [1000, 1500, 2000],
        'revenue': [1500, 4000, 2500]
    }

    campaign_df = pd.DataFrame(data)

    roi_calculator = ROICalculator(campaign_df)
    roi_calculator.display_results()
```
