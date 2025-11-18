"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Write code to analyze ROI and performance metrics for a law firm's marketing campaigns, similar to the transparent metrics offered by ClaimLink Legal Solutions.
Generated: DETERMINISTIC_9749d2ed0ff6b868
Batch ID: 20250612_154226
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

class MarketingCampaignAnalyzer:
    """
    A class to analyze ROI and performance metrics for marketing campaigns.
    """

    def __init__(self, campaign_data: pd.DataFrame):
        """
        Initializes the MarketingCampaignAnalyzer with campaign data.

        Args:
            campaign_data (pd.DataFrame): A DataFrame containing campaign data with columns:
                                            'Campaign_Name', 'Investment', 'Leads_Generated', 
                                            'Conversions', and 'Revenue'.
        """
        self.campaign_data = campaign_data

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for each campaign.

        Returns:
            pd.DataFrame: A DataFrame with campaigns and their respective ROI.
        """
        try:
            self.campaign_data['ROI'] = (self.campaign_data['Revenue'] - self.campaign_data['Investment']) / self.campaign_data['Investment'] * 100
            return self.campaign_data[['Campaign_Name', 'ROI']]
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating ROI: {e}")

    def performance_summary(self):
        """
        Summarizes key performance metrics for the campaigns.

        Returns:
            dict: A dictionary containing total investment, total revenue, 
                  total leads generated, total conversions, and overall ROI.
        """
        try:
            total_investment = self.campaign_data['Investment'].sum()
            total_revenue = self.campaign_data['Revenue'].sum()
            total_leads = self.campaign_data['Leads_Generated'].sum()
            total_conversions = self.campaign_data['Conversions'].sum()
            overall_roi = (total_revenue - total_investment) / total_investment * 100
            
            summary = {
                'Total Investment': total_investment,
                'Total Revenue': total_revenue,
                'Total Leads': total_leads,
                'Total Conversions': total_conversions,
                'Overall ROI': overall_roi
            }
            return summary
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while summarizing performance metrics: {e}")

    def plot_roi(self):
        """
        Plots the ROI of each campaign as a bar chart.

        Raises:
            ValueError: If there are no campaigns to plot.
        """
        try:
            roi_data = self.calculate_roi()
            if roi_data.empty:
                raise ValueError("No data available to plot.")

            plt.figure(figsize=(10, 6))
            plt.bar(roi_data['Campaign_Name'], roi_data['ROI'], color='skyblue')
            plt.title('ROI of Marketing Campaigns')
            plt.xlabel('Campaign Name')
            plt.ylabel('ROI (%)')
            plt.xticks(rotation=45)
            plt.axhline(0, color='red', linestyle='--')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred while plotting ROI: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample campaign data
    data = {
        'Campaign_Name': ['Campaign A', 'Campaign B', 'Campaign C'],
        'Investment': [1000, 1500, 1200],
        'Leads_Generated': [50, 75, 60],
        'Conversions': [5, 10, 8],
        'Revenue': [3000, 4000, 3500]
    }
    
    campaign_df = pd.DataFrame(data)
    analyzer = MarketingCampaignAnalyzer(campaign_df)
    
    # Display ROI calculations
    print(analyzer.calculate_roi())
    
    # Display performance summary
    print(analyzer.performance_summary())
    
    # Plot ROI
    analyzer.plot_roi()
```
