"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crownadvertise.com
Prompt: Create a Python script to analyze and optimize print media campaigns for a digital marketing agency, referencing Crown Advertising's strategies.
Generated: DETERMINISTIC_4208fb1cf7f8d6a1
Batch ID: 20250612_153224
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
import seaborn as sns

class PrintMediaCampaignAnalyzer:
    def __init__(self, campaign_data: pd.DataFrame):
        """
        Initializes the analyzer with campaign data.

        Parameters:
        campaign_data (pd.DataFrame): A DataFrame containing campaign metrics.
        """
        if not isinstance(campaign_data, pd.DataFrame):
            raise ValueError("campaign_data must be a pandas DataFrame.")
        self.campaign_data = campaign_data

    def calculate_roi(self) -> pd.DataFrame:
        """
        Calculates Return on Investment (ROI) for each campaign.

        Returns:
        pd.DataFrame: A DataFrame with campaigns and their respective ROI.
        """
        try:
            # Calculating ROI: (Revenue - Cost) / Cost
            self.campaign_data['ROI'] = (self.campaign_data['Revenue'] - self.campaign_data['Cost']) / self.campaign_data['Cost']
            return self.campaign_data[['Campaign', 'ROI']]
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")

    def visualize_roi(self):
        """
        Visualizes the ROI of each campaign using a bar plot.
        """
        roi_data = self.calculate_roi()
        plt.figure(figsize=(10, 6))
        sns.barplot(x='ROI', y='Campaign', data=roi_data, palette='viridis')
        plt.title('ROI of Print Media Campaigns')
        plt.xlabel('Return on Investment (ROI)')
        plt.ylabel('Campaigns')
        plt.axvline(0, color='red', linestyle='--')  # Line at ROI = 0 for reference
        plt.show()

    def optimize_campaigns(self):
        """
        Optimizes campaigns by recommending adjustments based on ROI.
        
        Returns:
        pd.DataFrame: Recommendations for each campaign.
        """
        roi_data = self.calculate_roi()
        recommendations = []

        for index, row in roi_data.iterrows():
            if row['ROI'] < 0:
                recommendations.append((row['Campaign'], 'Consider reducing budget or re-evaluating strategy.'))
            elif row['ROI'] > 0.5:
                recommendations.append((row['Campaign'], 'Consider increasing budget to maximize returns.'))
            else:
                recommendations.append((row['Campaign'], 'Maintain current strategy.'))

        return pd.DataFrame(recommendations, columns=['Campaign', 'Recommendation'])

def main():
    # Sample campaign data
    data = {
        'Campaign': ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D'],
        'Cost': [1000, 1500, 700, 900],
        'Revenue': [1200, 1800, 600, 1500]
    }

    # Create DataFrame
    campaign_df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = PrintMediaCampaignAnalyzer(campaign_df)

    # Calculate and display ROI
    print("ROI for each Campaign:")
    print(analyzer.calculate_roi())

    # Visualize ROI
    analyzer.visualize_roi()

    # Get and display recommendations for optimization
    recommendations = analyzer.optimize_campaigns()
    print("Campaign Optimization Recommendations:")
    print(recommendations)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
