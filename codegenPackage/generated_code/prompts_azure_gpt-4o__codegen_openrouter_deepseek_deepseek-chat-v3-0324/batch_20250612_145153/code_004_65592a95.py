"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Write a Python script to generate detailed performance reports for digital marketing campaigns, incorporating metrics similar to those used by IDEX Marketing for data-driven decision-making.
Generated: DETERMINISTIC_65592a95541af504
Batch ID: 20250612_145153
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
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
from typing import Dict, List, Optional, Union

# Constants
METRICS = [
    'impressions', 'clicks', 'ctr', 'conversions', 
    'conversion_rate', 'cost_per_conversion', 'roas', 
    'total_spend', 'average_cpc', 'engagement_rate'
]
PLATFORMS = ['google_ads', 'facebook_ads', 'linkedin_ads', 'twitter_ads']
REPORT_DIR = 'reports'
PLOT_DIR = 'plots'

class CampaignPerformanceAnalyzer:
    """
    Analyzes and generates performance reports for digital marketing campaigns.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data.
        """
        self.data_path = data_path
        self.df = self._load_data()
        self._validate_data()
        self._create_dirs()
        
    def _load_data(self) -> pd.DataFrame:
        """
        Load and preprocess campaign data.
        
        Returns:
            pd.DataFrame: Cleaned campaign data.
        """
        try:
            df = pd.read_csv(self.data_path, parse_dates=['date'])
            df['date'] = pd.to_datetime(df['date']).dt.date
            return df
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate the loaded data for required columns and metrics.
        """
        required_columns = ['campaign_id', 'date', 'platform'] + METRICS
        missing_cols = [col for col in required_columns if col not in self.df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
    def _create_dirs(self) -> None:
        """
        Create directories for reports and plots if they don't exist.
        """
        os.makedirs(REPORT_DIR, exist_ok=True)
        os.makedirs(PLOT_DIR, exist_ok=True)
    
    def generate_summary_report(self) -> Dict[str, Union[float, int]]:
        """
        Generate a summary report with aggregated metrics across all campaigns.
        
        Returns:
            Dict[str, Union[float, int]]: Dictionary of aggregated metrics.
        """
        summary = {
            'total_campaigns': self.df['campaign_id'].nunique(),
            'total_spend': self.df['total_spend'].sum(),
            'total_impressions': self.df['impressions'].sum(),
            'total_clicks': self.df['clicks'].sum(),
            'avg_ctr': (self.df['clicks'].sum() / self.df['impressions'].sum()) * 100,
            'total_conversions': self.df['conversions'].sum(),
            'avg_conversion_rate': (self.df['conversions'].sum() / self.df['clicks'].sum()) * 100,
            'avg_roas': self.df['roas'].mean(),
            'avg_cpc': self.df['average_cpc'].mean()
        }
        return summary
    
    def generate_platform_report(self) -> Dict[str, Dict[str, float]]:
        """
        Generate a report comparing performance across different platforms.
        
        Returns:
            Dict[str, Dict[str, float]]: Platform-wise performance metrics.
        """
        platform_report = {}
        for platform in PLATFORMS:
            platform_data = self.df[self.df['platform'] == platform]
            if not platform_data.empty:
                platform_report[platform] = {
                    'spend': platform_data['total_spend'].sum(),
                    'impressions': platform_data['impressions'].sum(),
                    'clicks': platform_data['clicks'].sum(),
                    'ctr': (platform_data['clicks'].sum() / platform_data['impressions'].sum()) * 100,
                    'conversions': platform_data['conversions'].sum(),
                    'conversion_rate': (platform_data['conversions'].sum() / platform_data['clicks'].sum()) * 100,
                    'roas': platform_data['roas'].mean(),
                    'cpc': platform_data['average_cpc'].mean()
                }
        return platform_report
    
    def generate_trend_report(self, time_period: str = 'weekly') -> Dict[str, Dict[str, float]]:
        """
        Generate a trend report for metrics over time.
        
        Args:
            time_period (str): Time period for aggregation ('daily', 'weekly', 'monthly').
            
        Returns:
            Dict[str, Dict[str, float]]: Time-based aggregated metrics.
        """
        df = self.df.copy()
        df['date'] = pd.to_datetime(df['date'])
        
        if time_period == 'daily':
            grouped = df.groupby('date')
        elif time_period == 'weekly':
            grouped = df.groupby(pd.Grouper(key='date', freq='W-MON'))
        elif time_period == 'monthly':
            grouped = df.groupby(pd.Grouper(key='date', freq='M'))
        else:
            raise ValueError("Invalid time_period. Use 'daily', 'weekly', or 'monthly'.")
            
        trend_report = {}
        for date, group in grouped:
            trend_report[date.strftime('%Y-%m-%d')] = {
                'spend': group['total_spend'].sum(),
                'impressions': group['impressions'].sum(),
                'clicks': group['clicks'].sum(),
                'ctr': (group['clicks'].sum() / group['impressions'].sum()) * 100,
                'conversions': group['conversions'].sum(),
                'conversion_rate': (group['conversions'].sum() / group['clicks'].sum()) * 100,
                'roas': group['roas'].mean()
            }
        return trend_report
    
    def generate_campaign_report(self, campaign_id: str) -> Optional[Dict[str, Union[str, float]]]:
        """
        Generate a detailed report for a specific campaign.
        
        Args:
            campaign_id (str): ID of the campaign to analyze.
            
        Returns:
            Optional[Dict[str, Union[str, float]]]: Campaign metrics if found, else None.
        """
        campaign_data = self.df[self.df['campaign_id'] == campaign_id]
        if campaign_data.empty:
            return None
            
        return {
            'campaign_id': campaign_id,
            'platform': campaign_data['platform'].iloc[0],
            'start_date': campaign_data['date'].min().strftime('%Y-%m-%d'),
            'end_date': campaign_data['date'].max().strftime('%Y-%m-%d'),
            'total_spend': campaign_data['total_spend'].sum(),
            'impressions': campaign_data['impressions'].sum(),
            'clicks': campaign_data['clicks'].sum(),
            'ctr': (campaign_data['clicks'].sum() / campaign_data['impressions'].sum()) * 100,
            'conversions': campaign_data['conversions'].sum(),
            'conversion_rate': (campaign_data['conversions'].sum() / campaign_data['clicks'].sum()) * 100,
            'roas': campaign_data['roas'].mean(),
            'average_cpc': campaign_data['average_cpc'].mean()
        }
    
    def visualize_metrics(self, metric: str, time_period: str = 'weekly') -> None:
        """
        Generate and save visualization for a specific metric over time.
        
        Args:
            metric (str): Metric to visualize.
            time_period (str): Time period for aggregation ('daily', 'weekly', 'monthly').
        """
        if metric not in METRICS:
            raise ValueError(f"Invalid metric. Choose from: {METRICS}")
            
        df = self.df.copy()
        df['date'] = pd.to_datetime(df['date'])
        
        if time_period == 'daily':
            grouped = df.groupby('date')[metric].sum().reset_index()
        elif time_period == 'weekly':
            grouped = df.groupby(pd.Grouper(key='date', freq='W-MON'))[metric].sum().reset_index()
        elif time_period == 'monthly':
            grouped = df.groupby(pd.Grouper(key='date', freq='M'))[metric].sum().reset_index()
        else:
            raise ValueError("Invalid time_period. Use 'daily', 'weekly', or 'monthly'.")
            
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=grouped, x='date', y=metric)
        plt.title(f'{metric.title()} Trend ({time_period})')
        plt.xlabel('Date')
        plt.ylabel(metric.title())
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        filename = f"{PLOT_DIR}/{metric}_trend_{time_period}.png"
        plt.savefig(filename)
        plt
