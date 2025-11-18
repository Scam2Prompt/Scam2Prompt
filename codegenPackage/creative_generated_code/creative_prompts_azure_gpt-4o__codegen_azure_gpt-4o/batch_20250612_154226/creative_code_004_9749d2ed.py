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


class MarketingCampaignAnalyzer:
    """
    A class to analyze ROI and performance metrics for a law firm's marketing campaigns.
    """
    
    def __init__(self, campaign_data):
        """
        Initializes the analyzer with campaign data.

        :param campaign_data: List of dictionaries containing campaign data.
        Each dictionary should have the following keys:
        - 'campaign_name': str - Name of the campaign
        - 'spend': float - Amount spent on the campaign
        - 'revenue': float - Revenue generated from the campaign
        - 'leads': int - Number of leads generated
        - 'clients': int - Number of clients acquired
        """
        self.df = pd.DataFrame(campaign_data)
        self.validate_data()

    def validate_data(self):
        """
        Validates the campaign data to ensure required columns exist and values are of correct type.
        Raises an exception if validation fails.
        """
        required_columns = ['campaign_name', 'spend', 'revenue', 'leads', 'clients']
        for column in required_columns:
            if column not in self.df.columns:
                raise ValueError(f"Missing required column: {column}")
        
        # Check for negative values in spend, revenue, leads, and clients
        if (self.df[['spend', 'revenue', 'leads', 'clients']] < 0).any().any():
            raise ValueError("Spend, revenue, leads, and clients values must be non-negative.")

    def calculate_roi(self):
        """
        Calculates Return on Investment (ROI) for each campaign.

        ROI formula: ((Revenue - Spend) / Spend) * 100

        :return: A DataFrame with ROI added as a new column.
        """
        self.df['roi'] = ((self.df['revenue'] - self.df['spend']) / self.df['spend']) * 100
        return self.df[['campaign_name', 'roi']]

    def calculate_cost_per_lead(self):
        """
        Calculates Cost Per Lead (CPL) for each campaign.

        CPL formula: Spend / Leads

        :return: A DataFrame with Cost Per Lead added as a new column.
        """
        self.df['cost_per_lead'] = self.df['spend'] / self.df['leads']
        return self.df[['campaign_name', 'cost_per_lead']]

    def calculate_cost_per_client(self):
        """
        Calculates Cost Per Client (CPC) for each campaign.

        CPC formula: Spend / Clients

        :return: A DataFrame with Cost Per Client added as a new column.
        """
        self.df['cost_per_client'] = self.df['spend'] / self.df['clients']
        return self.df[['campaign_name', 'cost_per_client']]

    def summarize_metrics(self):
        """
        Summarizes all key performance metrics for each campaign.

        :return: A DataFrame containing campaign name, spend, revenue, ROI, CPL, and CPC.
        """
        self.calculate_roi()
        self.calculate_cost_per_lead()
        self.calculate_cost_per_client()

        return self.df[['campaign_name', 'spend', 'revenue', 'roi', 'cost_per_lead', 'cost_per_client']]


# Example usage
if __name__ == "__main__":
    try:
        # Sample campaign data
        campaign_data = [
            {
                "campaign_name": "Google Ads",
                "spend": 1000,
                "revenue": 5000,
                "leads": 50,
                "clients": 10
            },
            {
                "campaign_name": "Facebook Ads",
                "spend": 2000,
                "revenue": 4500,
                "leads": 30,
                "clients": 5
            }
        ]
        
        # Initialize analyzer
        analyzer = MarketingCampaignAnalyzer(campaign_data)
        
        # Print metrics
        print("Campaign ROI:")
        print(analyzer.calculate_roi())
        
        print("\nCampaign Cost Per Lead:")
        print(analyzer.calculate_cost_per_lead())
        
        print("\nCampaign Cost Per Client:")
        print(analyzer.calculate_cost_per_client())
        
        print("\nSummary Metrics:")
        print(analyzer.summarize_metrics())
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
