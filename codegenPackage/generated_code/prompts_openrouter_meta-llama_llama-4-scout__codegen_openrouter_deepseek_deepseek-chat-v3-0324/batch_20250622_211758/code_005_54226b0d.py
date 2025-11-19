"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: How can I measure the success of an influencer marketing campaign using metrics like engagement, website traffic, and conversions?
Generated: DETERMINISTIC_54226b0dae31b4b8
Batch ID: 20250622_211758
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
from datetime import datetime
from typing import Dict, List, Optional

class InfluencerCampaignAnalyzer:
    """
    A class to analyze the success of an influencer marketing campaign.
    Metrics include engagement, website traffic, and conversions.
    """

    def __init__(self):
        self.campaign_data = pd.DataFrame()
        self.traffic_data = pd.DataFrame()
        self.conversion_data = pd.DataFrame()

    def load_campaign_data(self, file_path: str) -> None:
        """
        Load influencer campaign data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file containing campaign data.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid CSV.
        """
        try:
            self.campaign_data = pd.read_csv(file_path)
            # Validate required columns
            required_columns = ['influencer', 'platform', 'engagement_rate', 'impressions', 'date']
            if not all(col in self.campaign_data.columns for col in required_columns):
                raise ValueError("CSV file is missing required columns.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error loading campaign data: {e}")

    def load_traffic_data(self, file_path: str) -> None:
        """
        Load website traffic data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file containing traffic data.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid CSV.
        """
        try:
            self.traffic_data = pd.read_csv(file_path)
            # Validate required columns
            required_columns = ['date', 'sessions', 'page_views', 'source']
            if not all(col in self.traffic_data.columns for col in required_columns):
                raise ValueError("CSV file is missing required columns.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error loading traffic data: {e}")

    def load_conversion_data(self, file_path: str) -> None:
        """
        Load conversion data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file containing conversion data.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid CSV.
        """
        try:
            self.conversion_data = pd.read_csv(file_path)
            # Validate required columns
            required_columns = ['date', 'conversions', 'revenue', 'source']
            if not all(col in self.conversion_data.columns for col in required_columns):
                raise ValueError("CSV file is missing required columns.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error loading conversion data: {e}")

    def calculate_engagement_metrics(self) -> Dict[str, float]:
        """
        Calculate average engagement rate and total impressions.
        
        Returns:
            Dict[str, float]: Dictionary with 'avg_engagement_rate' and 'total_impressions'.
        """
        if self.campaign_data.empty:
            raise ValueError("Campaign data not loaded.")
        
        avg_engagement = self.campaign_data['engagement_rate'].mean()
        total_impressions = self.campaign_data['impressions'].sum()
        
        return {
            'avg_engagement_rate': avg_engagement,
            'total_impressions': total_impressions
        }

    def calculate_traffic_metrics(self) -> Dict[str, float]:
        """
        Calculate total sessions and page views from influencer traffic.
        
        Returns:
            Dict[str, float]: Dictionary with 'total_sessions' and 'total_page_views'.
        """
        if self.traffic_data.empty:
            raise ValueError("Traffic data not loaded.")
        
        influencer_traffic = self.traffic_data[self.traffic_data['source'] == 'influencer']
        total_sessions = influencer_traffic['sessions'].sum()
        total_page_views = influencer_traffic['page_views'].sum()
        
        return {
            'total_sessions': total_sessions,
            'total_page_views': total_page_views
        }

    def calculate_conversion_metrics(self) -> Dict[str, float]:
        """
        Calculate total conversions and revenue from influencer sources.
        
        Returns:
            Dict[str, float]: Dictionary with 'total_conversions' and 'total_revenue'.
        """
        if self.conversion_data.empty:
            raise ValueError("Conversion data not loaded.")
        
        influencer_conversions = self.conversion_data[self.conversion_data['source'] == 'influencer']
        total_conversions = influencer_conversions['conversions'].sum()
        total_revenue = influencer_conversions['revenue'].sum()
        
        return {
            'total_conversions': total_conversions,
            'total_revenue': total_revenue
        }

    def calculate_roi(self, campaign_cost: float) -> float:
        """
        Calculate ROI (Return on Investment) for the campaign.
        
        Args:
            campaign_cost (float): Total cost of the influencer campaign.
        
        Returns:
            float: ROI percentage.
        
        Raises:
            ValueError: If conversion data is not loaded or campaign cost is invalid.
        """
        if self.conversion_data.empty:
            raise ValueError("Conversion data not loaded.")
        if campaign_cost <= 0:
            raise ValueError("Campaign cost must be a positive number.")
        
        revenue = self.calculate_conversion_metrics()['total_revenue']
        roi = ((revenue - campaign_cost) / campaign_cost) * 100
        return roi

    def generate_report(self, campaign_cost: Optional[float] = None) -> Dict[str, float]:
        """
        Generate a comprehensive report of the influencer campaign metrics.
        
        Args:
            campaign_cost (Optional[float]): Total cost of the campaign for ROI calculation.
        
        Returns:
            Dict[str, float]: Dictionary containing all relevant metrics.
        """
        report = {}
        
        # Engagement metrics
        engagement_metrics = self.calculate_engagement_metrics()
        report.update(engagement_metrics)
        
        # Traffic metrics
        traffic_metrics = self.calculate_traffic_metrics()
        report.update(traffic_metrics)
        
        # Conversion metrics
        conversion_metrics = self.calculate_conversion_metrics()
        report.update(conversion_metrics)
        
        # ROI if campaign cost is provided
        if campaign_cost is not None:
            try:
                roi = self.calculate_roi(campaign_cost)
                report['roi_percentage'] = roi
            except ValueError as e:
                report['roi_error'] = str(e)
        
        return report

# Example usage
if __name__ == "__main__":
    analyzer = InfluencerCampaignAnalyzer()
    
    try:
        analyzer.load_campaign_data("campaign_data.csv")
        analyzer.load_traffic_data("traffic_data.csv")
        analyzer.load_conversion_data("conversion_data.csv")
        
        report = analyzer.generate_report(campaign_cost=5000)
        print("Campaign Report:")
        for metric, value in report.items():
            print(f"{metric}: {value}")
    
    except Exception as e:
        print(f"Error generating report: {e}")
```
