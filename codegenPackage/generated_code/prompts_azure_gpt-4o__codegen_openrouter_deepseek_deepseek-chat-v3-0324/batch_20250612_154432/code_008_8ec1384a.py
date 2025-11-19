"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Create a Python script to calculate marketing-sourced revenue and track performance metrics, inspired by the case studies shared on the 3rd & Taylor website.
Generated: DETERMINISTIC_8ec1384a2542c8f5
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MarketingRevenueAnalyzer:
    """
    A class to calculate marketing-sourced revenue and track performance metrics.
    Inspired by 3rd & Taylor marketing case studies.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with marketing data.
        
        Args:
            data_path (str): Path to the CSV file containing marketing data.
                            Expected columns: ['date', 'campaign', 'channel', 'cost', 'revenue', 'conversions']
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            logger.info("Data loaded and validated successfully")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _validate_data(self) -> None:
        """Validate the input data structure and content."""
        required_columns = {'date', 'campaign', 'channel', 'cost', 'revenue', 'conversions'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        if self.data.isnull().values.any():
            raise ValueError("Data contains null values")
        
        try:
            self.data['date'] = pd.to_datetime(self.data['date'])
        except Exception as e:
            raise ValueError(f"Invalid date format: {str(e)}")
    
    def calculate_roi(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, float]:
        """
        Calculate Return on Investment (ROI) for marketing campaigns.
        
        Args:
            start_date (str, optional): Start date in 'YYYY-MM-DD' format. Defaults to None (earliest date).
            end_date (str, optional): End date in 'YYYY-MM-DD' format. Defaults to None (latest date).
            
        Returns:
            Dict[str, float]: Dictionary with ROI metrics including total and by channel.
        """
        try:
            filtered_data = self._filter_by_date(start_date, end_date)
            
            total_cost = filtered_data['cost'].sum()
            total_revenue = filtered_data['revenue'].sum()
            total_roi = (total_revenue - total_cost) / total_cost if total_cost > 0 else 0
            
            roi_by_channel = {}
            for channel, group in filtered_data.groupby('channel'):
                channel_cost = group['cost'].sum()
                channel_revenue = group['revenue'].sum()
                channel_roi = (channel_revenue - channel_cost) / channel_cost if channel_cost > 0 else 0
                roi_by_channel[channel] = channel_roi
            
            return {
                'total_roi': total_roi,
                'roi_by_channel': roi_by_channel,
                'total_cost': total_cost,
                'total_revenue': total_revenue
            }
        except Exception as e:
            logger.error(f"Error calculating ROI: {str(e)}")
            raise
    
    def calculate_cpa(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, float]:
        """
        Calculate Cost Per Acquisition (CPA) for marketing campaigns.
        
        Args:
            start_date (str, optional): Start date in 'YYYY-MM-DD' format. Defaults to None (earliest date).
            end_date (str, optional): End date in 'YYYY-MM-DD' format. Defaults to None (latest date).
            
        Returns:
            Dict[str, float]: Dictionary with CPA metrics including total and by channel.
        """
        try:
            filtered_data = self._filter_by_date(start_date, end_date)
            
            total_cost = filtered_data['cost'].sum()
            total_conversions = filtered_data['conversions'].sum()
            total_cpa = total_cost / total_conversions if total_conversions > 0 else 0
            
            cpa_by_channel = {}
            for channel, group in filtered_data.groupby('channel'):
                channel_cost = group['cost'].sum()
                channel_conversions = group['conversions'].sum()
                channel_cpa = channel_cost / channel_conversions if channel_conversions > 0 else 0
                cpa_by_channel[channel] = channel_cpa
            
            return {
                'total_cpa': total_cpa,
                'cpa_by_channel': cpa_by_channel,
                'total_cost': total_cost,
                'total_conversions': total_conversions
            }
        except Exception as e:
            logger.error(f"Error calculating CPA: {str(e)}")
            raise
    
    def calculate_conversion_rate(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, float]:
        """
        Calculate conversion rate for marketing campaigns.
        
        Args:
            start_date (str, optional): Start date in 'YYYY-MM-DD' format. Defaults to None (earliest date).
            end_date (str, optional): End date in 'YYYY-MM-DD' format. Defaults to None (latest date).
            
        Returns:
            Dict[str, float]: Dictionary with conversion rate metrics including total and by channel.
        """
        try:
            filtered_data = self._filter_by_date(start_date, end_date)
            
            # Note: This assumes we have impression data. If not, we'd need to modify.
            # For this implementation, we'll use conversions vs. cost as a proxy
            total_cost = filtered_data['cost'].sum()
            total_conversions = filtered_data['conversions'].sum()
            total_conversion_rate = total_conversions / total_cost if total_cost > 0 else 0
            
            conversion_rate_by_channel = {}
            for channel, group in filtered_data.groupby('channel'):
                channel_cost = group['cost'].sum()
                channel_conversions = group['conversions'].sum()
                channel_rate = channel_conversions / channel_cost if channel_cost > 0 else 0
                conversion_rate_by_channel[channel] = channel_rate
            
            return {
                'total_conversion_rate': total_conversion_rate,
                'conversion_rate_by_channel': conversion_rate_by_channel,
                'total_cost': total_cost,
                'total_conversions': total_conversions
            }
        except Exception as e:
            logger.error(f"Error calculating conversion rate: {str(e)}")
            raise
    
    def get_top_performing_campaigns(self, 
                                   metric: str = 'roi', 
                                   n: int = 5,
                                   start_date: Optional[str] = None, 
                                   end_date: Optional[str] = None) -> List[Tuple[str, float]]:
        """
        Get top performing campaigns based on specified metric.
        
        Args:
            metric (str): Metric to evaluate ('roi', 'cpa', 'conversion_rate'). Defaults to 'roi'.
            n (int): Number of top campaigns to return. Defaults to 5.
            start_date (str, optional): Start date in 'YYYY-MM-DD' format. Defaults to None.
            end_date (str, optional): End date in 'YYYY-MM-DD' format. Defaults to None.
            
        Returns:
            List[Tuple[str, float]]: List of tuples containing campaign name and metric value.
        """
        try:
            filtered_data = self._filter_by_date(start_date, end_date)
            
            if metric not in ['roi', 'cpa', 'conversion_rate']:
                raise ValueError("Invalid metric. Choose from 'roi', 'cpa', or 'conversion_rate'")
            
            campaign_groups = filtered_data.groupby('campaign')
            campaign_metrics = []
            
            for campaign, group in campaign_groups:
                cost = group['cost'].sum()
                revenue = group['revenue'].sum()
                conversions = group['conversions'].sum()
                
                if metric == 'roi':
                    value = (revenue - cost) / cost if cost > 0 else 0
                elif metric == 'cpa':
                    value = cost / conversions if conversions > 0 else 0
                elif metric == 'conversion_rate':
                    value = conversions / cost if cost > 0 else 0
                
                campaign_metrics.append((campaign, value))
            
            # Sort descending for roi and conversion_rate, ascending for cpa
            reverse_sort = metric != 'cpa'
            campaign_metrics.sort(key=lambda x: x[1], reverse=reverse_sort)
            
            return campaign_metrics[:n]
        except Exception as e:
            logger.error(f"Error getting top campaigns: {str(e)}")
            raise
    
    def _filter_by_date(self, start_date: Optional[str], end_date: Optional[str]) -> pd.DataFrame:
        """Filter data by date range."""
        filtered = self.data.copy()
        
        if start_date:
            start_date = pd.to_datetime(start_date)
            filtered = filtered[filtered['date'] >=
