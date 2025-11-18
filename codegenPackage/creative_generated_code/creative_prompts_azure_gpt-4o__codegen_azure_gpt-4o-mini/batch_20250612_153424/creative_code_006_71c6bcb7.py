"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.se
Prompt: Develop a program to calculate the ROI of link-building campaigns, incorporating Puffer's emphasis on measurable growth and long-term SEO benefits.
Generated: DETERMINISTIC_71c6bcb74cd53c0b
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class LinkBuildingCampaignROI:
    def __init__(self, campaign_data):
        """
        Initializes the LinkBuildingCampaignROI with campaign data.

        :param campaign_data: A pandas DataFrame containing at least 'cost', 'traffic_increase', and 'revenue' columns.
        """
        self.campaign_data = campaign_data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains necessary columns.
        Raises ValueError if any required column is missing.
        """
        required_columns = ['cost', 'traffic_increase', 'revenue']
        for column in required_columns:
            if column not in self.campaign_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_roi(self):
        """
        Calculates the ROI for each campaign in the DataFrame.

        ROI is calculated using the formula: ROI = (Net Profit / Cost) * 100
        Net Profit is defined as Revenue - Cost.

        :return: A pandas DataFrame with an additional 'roi' column.
        """
        # Calculate Net Profit
        self.campaign_data['net_profit'] = self.campaign_data['revenue'] - self.campaign_data['cost']

        # Calculate ROI
        self.campaign_data['roi'] = (self.campaign_data['net_profit'] / self.campaign_data['cost']) * 100

        return self.campaign_data

    def summarize_campaigns(self):
        """
        Summarizes the campaign results, providing average ROI and total investment.

        :return: A summary dictionary containing average ROI and total cost.
        """
        total_cost = self.campaign_data['cost'].sum()
        average_roi = self.campaign_data['roi'].mean()

        return {
            'total_investment': total_cost,
            'average_roi': average_roi
        }

# Example usage
if __name__ == '__main__':
    # Sample data for campaigns
    data = {
        'cost': [500, 1000, 1500],
        'traffic_increase': [200, 500, 800],
        'revenue': [750, 1300, 2000]
    }

    # Create a DataFrame
    campaign_df = pd.DataFrame(data)

    try:
        # Initialize ROI calculator
        roi_calculator = LinkBuildingCampaignROI(campaign_df)

        # Calculate ROI
        result_df = roi_calculator.calculate_roi()
        print("Campaign ROI Results:\n", result_df)

        # Get summary of campaigns
        summary = roi_calculator.summarize_campaigns()
        print("Campaign Summary:\n", summary)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
