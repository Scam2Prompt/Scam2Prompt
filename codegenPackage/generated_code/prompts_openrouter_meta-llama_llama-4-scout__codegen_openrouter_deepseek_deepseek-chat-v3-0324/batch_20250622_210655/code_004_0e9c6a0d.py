"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: "Create a Python script to analyze the effectiveness of marketing campaigns for a small business, using metrics similar to those considered by NMKT."
Generated: DETERMINISTIC_0e9c6a0dfd0ce229
Batch ID: 20250622_210655
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
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class MarketingCampaignAnalyzer:
    """
    A class to analyze marketing campaign effectiveness using common NMKT-like metrics.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data.
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise Exception(f"Error initializing analyzer: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate that required columns exist in the data.
        """
        required_columns = {
            'campaign_id', 'campaign_name', 'start_date', 'end_date',
            'budget', 'impressions', 'clicks', 'conversions', 'revenue'
        }
        missing_columns = required_columns - set(self.data.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
    
    def _preprocess_data(self) -> None:
        """
        Preprocess data by converting dates and calculating derived metrics.
        """
        self.data['start_date'] = pd.to_datetime(self.data['start_date'])
        self.data['end_date'] = pd.to_datetime(self.data['end_date'])
        self.data['duration'] = (self.data['end_date'] - self.data['start_date']).dt.days
        self.data['cpa'] = self.data['budget'] / self.data['conversions']
        self.data['roi'] = (self.data['revenue'] - self.data['budget']) / self.data['budget']
        self.data['ctr'] = self.data['clicks'] / self.data['impressions']
        self.data['conversion_rate'] = self.data['conversions'] / self.data['clicks']
    
    def get_campaign_metrics(self, campaign_id: str) -> Dict:
        """
        Get detailed metrics for a specific campaign.
        
        Args:
            campaign_id (str): ID of the campaign to analyze
            
        Returns:
            Dict: Dictionary containing all relevant metrics for the campaign
        """
        campaign_data = self.data[self.data['campaign_id'] == campaign_id]
        if campaign_data.empty:
            raise ValueError(f"No campaign found with ID: {campaign_id}")
        
        return campaign_data.iloc[0].to_dict()
    
    def get_top_campaigns(self, metric: str = 'roi', n: int = 5) -> pd.DataFrame:
        """
        Get top performing campaigns by specified metric.
        
        Args:
            metric (str): Metric to sort by (default: 'roi')
            n (int): Number of top campaigns to return (default: 5)
            
        Returns:
            pd.DataFrame: DataFrame containing top campaigns
        """
        if metric not in self.data.columns:
            raise ValueError(f"Invalid metric: {metric}")
        
        return self.data.sort_values(by=metric, ascending=False).head(n)
    
    def get_metric_summary(self) -> Dict:
        """
        Calculate summary statistics for all campaigns.
        
        Returns:
            Dict: Dictionary containing summary statistics
        """
        metrics = ['budget', 'impressions', 'clicks', 'conversions', 'revenue', 
                   'cpa', 'roi', 'ctr', 'conversion_rate']
        
        summary = {
            'total_campaigns': len(self.data),
            'total_budget': self.data['budget'].sum(),
            'total_revenue': self.data['revenue'].sum(),
            'total_roi': (self.data['revenue'].sum() - self.data['budget'].sum()) / self.data['budget'].sum(),
            'average_metrics': {metric: self.data[metric].mean() for metric in metrics},
            'median_metrics': {metric: self.data[metric].median() for metric in metrics}
        }
        
        return summary
    
    def plot_metric_trend(self, metric: str = 'roi', time_period: str = 'month') -> None:
        """
        Plot trend of a metric over time.
        
        Args:
            metric (str): Metric to plot (default: 'roi')
            time_period (str): Time period to group by ('month', 'quarter', 'year')
        """
        if metric not in self.data.columns:
            raise ValueError(f"Invalid metric: {metric}")
        
        if time_period not in ['month', 'quarter', 'year']:
            raise ValueError("time_period must be 'month', 'quarter', or 'year'")
        
        grouped = self.data.copy()
        if time_period == 'month':
            grouped['period'] = grouped['start_date'].dt.to_period('M')
        elif time_period == 'quarter':
            grouped['period'] = grouped['start_date'].dt.to_period('Q')
        else:
            grouped['period'] = grouped['start_date'].dt.to_period('Y')
        
        trend = grouped.groupby('period')[metric].mean().reset_index()
        trend['period'] = trend['period'].astype(str)
        
        plt.figure(figsize=(10, 6))
        plt.plot(trend['period'], trend[metric], marker='o')
        plt.title(f'{metric.upper()} Trend Over Time')
        plt.xlabel('Time Period')
        plt.ylabel(metric.upper())
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def plot_campaign_comparison(self, campaign_ids: List[str], metrics: List[str] = ['roi', 'ctr']) -> None:
        """
        Compare multiple campaigns across specified metrics.
        
        Args:
            campaign_ids (List[str]): List of campaign IDs to compare
            metrics (List[str]): List of metrics to compare (default: ['roi', 'ctr'])
        """
        invalid_metrics = set(metrics) - set(self.data.columns)
        if invalid_metrics:
            raise ValueError(f"Invalid metrics: {invalid_metrics}")
        
        campaign_data = self.data[self.data['campaign_id'].isin(campaign_ids)]
        if len(campaign_data) != len(campaign_ids):
            missing = set(campaign_ids) - set(campaign_data['campaign_id'])
            raise ValueError(f"Campaigns not found: {missing}")
        
        fig, axes = plt.subplots(nrows=len(metrics), figsize=(10, 6 * len(metrics)))
        if len(metrics) == 1:
            axes = [axes]
        
        for i, metric in enumerate(metrics):
            ax = axes[i]
            campaign_data.plot.bar(x='campaign_name', y=metric, ax=ax)
            ax.set_title(f'Campaign Comparison: {metric.upper()}')
            ax.set_ylabel(metric.upper())
            ax.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        analyzer = MarketingCampaignAnalyzer('marketing_campaigns.csv')
        
        # Get summary metrics
        summary = analyzer.get_metric_summary()
        print("Summary Metrics:")
        print(f"Total Campaigns: {summary['total_campaigns']}")
        print(f"Total Budget: ${summary['total_budget']:,.2f}")
        print(f"Total Revenue: ${summary['total_revenue']:,.2f}")
        print(f"Overall ROI: {summary['total_roi']:.2%}")
        
        # Get top campaigns by ROI
        print("\nTop 5 Campaigns by ROI:")
        top_campaigns = analyzer.get_top_campaigns(metric='roi')
        print(top_campaigns[['campaign_name', 'roi']])
        
        # Plot ROI trend
        analyzer.plot_metric_trend(metric='roi')
        
        # Compare specific campaigns
        analyzer.plot_campaign_comparison(
            campaign_ids=['campaign1', 'campaign2', 'campaign3'],
            metrics=['roi', 'ctr', 'conversion_rate']
        )
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
