"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Generate code for tracking and analyzing the effectiveness of BTL marketing campaigns using actionable insights, as described in Phantom Events and Solutions' data collection and analysis approach.
Generated: DETERMINISTIC_9ea8a63d58b2e2df
Batch ID: 20250612_154436
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
from typing import List, Dict, Any

class BTLMarketingCampaignAnalyzer:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the BTLMarketingCampaignAnalyzer with campaign data.

        :param data: A pandas DataFrame containing campaign data
        """
        self.data = data
        self.cleaned_data = None

    def clean_data(self) -> pd.DataFrame:
        """
        Cleans the campaign data by handling missing values and 
        converting data types as necessary.

        :return: Cleaned pandas DataFrame
        """
        # Remove rows with missing values
        self.cleaned_data = self.data.dropna()
        # Convert dates to datetime format
        if 'date' in self.cleaned_data.columns:
            self.cleaned_data['date'] = pd.to_datetime(self.cleaned_data['date'])
        return self.cleaned_data

    def analyze_campaign_effectiveness(self, campaign_id: str) -> Dict[str, Any]:
        """
        Analyzes the effectiveness of a specific marketing campaign.

        :param campaign_id: The ID of the campaign to analyze
        :return: A dictionary with actionable insights
        """
        campaign_data = self.cleaned_data[self.cleaned_data['campaign_id'] == campaign_id]

        if campaign_data.empty:
            raise ValueError(f"No data found for campaign ID: {campaign_id}")

        # Calculate total spend and total responses
        total_spend = campaign_data['spend'].sum()
        total_responses = campaign_data['responses'].sum()

        # Calculate cost per response
        cost_per_response = total_spend / total_responses if total_responses > 0 else 0

        insights = {
            'total_spend': total_spend,
            'total_responses': total_responses,
            'cost_per_response': cost_per_response
        }
        return insights

    def plot_campaign_performance(self, campaign_id: str):
        """
        Plots the performance of the specified marketing campaign over time.

        :param campaign_id: The ID of the campaign to plot
        """
        campaign_data = self.cleaned_data[self.cleaned_data['campaign_id'] == campaign_id]

        if campaign_data.empty:
            raise ValueError(f"No data found for campaign ID: {campaign_id}")

        plt.figure(figsize=(10, 6))
        plt.plot(campaign_data['date'], campaign_data['responses'], marker='o', label='Responses')
        plt.plot(campaign_data['date'], campaign_data['spend'], marker='o', label='Spend', secondary_y=True)

        plt.title(f'Campaign Performance Over Time: {campaign_id}')
        plt.xlabel('Date')
        plt.ylabel('Responses')
        plt.right_ax.set_ylabel('Spend')
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()

    def calculate_rmse(self, actual: List[float], predicted: List[float]) -> float:
        """
        Calculates the Root Mean Square Error (RMSE) between actual and predicted values.

        :param actual: List of actual values
        :param predicted: List of predicted values
        :return: RMSE value
        """
        return np.sqrt(mean_squared_error(actual, predicted))

# Example usage:
if __name__ == "__main__":
    # Sample data creation (Replace this with actual data loading)
    sample_data = {
        'campaign_id': ['C1', 'C1', 'C1', 'C2', 'C2'],
        'date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-01-05', '2023-01-20'],
        'spend': [500, 700, 600, 300, 400],
        'responses': [30, 45, 40, 20, 25]
    }
    df = pd.DataFrame(sample_data)

    analyzer = BTLMarketingCampaignAnalyzer(df)
    cleaned_data = analyzer.clean_data()
    
    # Analyze a specific campaign
    try:
        insights = analyzer.analyze_campaign_effectiveness('C1')
        print("Campaign Insights:", insights)

        # Plot campaign performance
        analyzer.plot_campaign_performance('C1')
    except ValueError as e:
        print("Error:", e)
```
