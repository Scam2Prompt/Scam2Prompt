"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: Develop a program to analyze ROI metrics from marketing campaigns, inspired by Creo Collective's case studies like "Record ROI: Coreview."
Generated: DETERMINISTIC_fcd1bf79c55c2f04
Batch ID: 20250612_152249
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
from typing import Dict, List, Tuple, Optional

class ROIAnalyzer:
    """
    A class to analyze ROI metrics from marketing campaigns.
    Inspired by Creo Collective's case studies like "Record ROI: Coreview".
    
    Attributes:
        campaign_data (pd.DataFrame): DataFrame containing campaign metrics
        cost_columns (List[str]): List of column names representing costs
        revenue_columns (List[str]): List of column names representing revenue
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the ROIAnalyzer with campaign data.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data
        """
        try:
            self.campaign_data = pd.read_csv(data_path)
            self._validate_data()
            
            # Default columns (can be changed with set_metric_columns)
            self.cost_columns = ['ad_spend', 'production_cost', 'agency_fees']
            self.revenue_columns = ['direct_revenue', 'attributed_revenue']
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error initializing ROIAnalyzer: {str(e)}")
    
    def _validate_data(self) -> None:
        """Validate that required columns exist in the dataset."""
        required_columns = ['campaign_id', 'start_date', 'end_date']
        missing_columns = [col for col in required_columns if col not in self.campaign_data.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns in data: {missing_columns}")
    
    def set_metric_columns(self, cost_columns: List[str], revenue_columns: List[str]) -> None:
        """
        Set which columns should be used for cost and revenue calculations.
        
        Args:
            cost_columns (List[str]): List of column names representing costs
            revenue_columns (List[str]): List of column names representing revenue
        """
        missing_cost = [col for col in cost_columns if col not in self.campaign_data.columns]
        missing_revenue = [col for col in revenue_columns if col not in self.campaign_data.columns]
        
        if missing_cost:
            raise ValueError(f"Cost columns not found in data: {missing_cost}")
        if missing_revenue:
            raise ValueError(f"Revenue columns not found in data: {missing_revenue}")
            
        self.cost_columns = cost_columns
        self.revenue_columns = revenue_columns
    
    def calculate_roi(self, campaign_id: Optional[str] = None) -> Dict[str, float]:
        """
        Calculate ROI metrics for a specific campaign or all campaigns.
        
        Args:
            campaign_id (Optional[str]): Specific campaign ID to analyze. If None, analyzes all.
            
        Returns:
            Dict[str, float]: Dictionary containing ROI metrics
        """
        try:
            data = self.campaign_data if campaign_id is None else \
                   self.campaign_data[self.campaign_data['campaign_id'] == campaign_id]
            
            if len(data) == 0:
                raise ValueError(f"No data found for campaign_id: {campaign_id}")
            
            total_cost = data[self.cost_columns].sum().sum()
            total_revenue = data[self.revenue_columns].sum().sum()
            
            roi = ((total_revenue - total_cost) / total_cost) * 100 if total_cost != 0 else float('inf')
            
            return {
                'total_cost': total_cost,
                'total_revenue': total_revenue,
                'roi_percentage': roi,
                'profit': total_revenue - total_cost
            }
            
        except Exception as e:
            raise Exception(f"Error calculating ROI: {str(e)}")
    
    def calculate_roi_by_time_period(self, period: str = 'month') -> pd.DataFrame:
        """
        Calculate ROI metrics grouped by time period.
        
        Args:
            period (str): Time period to group by ('day', 'week', 'month', 'quarter', 'year')
            
        Returns:
            pd.DataFrame: DataFrame with ROI metrics by time period
        """
        valid_periods = ['day', 'week', 'month', 'quarter', 'year']
        if period not in valid_periods:
            raise ValueError(f"Invalid period. Must be one of: {valid_periods}")
        
        try:
            data = self.campaign_data.copy()
            data['start_date'] = pd.to_datetime(data['start_date'])
            data['period'] = data['start_date'].dt.to_period(period[0].upper())
            
            grouped = data.groupby('period').apply(
                lambda x: pd.Series({
                    'total_cost': x[self.cost_columns].sum().sum(),
                    'total_revenue': x[self.revenue_columns].sum().sum()
                })
            )
            
            grouped['roi_percentage'] = ((grouped['total_revenue'] - grouped['total_cost']) / 
                                        grouped['total_cost']) * 100
            grouped['profit'] = grouped['total_revenue'] - grouped['total_cost']
            
            return grouped.reset_index()
            
        except Exception as e:
            raise Exception(f"Error calculating ROI by time period: {str(e)}")
    
    def plot_roi_trend(self, period: str = 'month') -> None:
        """
        Plot ROI trend over time.
        
        Args:
            period (str): Time period to group by ('day', 'week', 'month', 'quarter', 'year')
        """
        try:
            roi_data = self.calculate_roi_by_time_period(period)
            
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=roi_data, x='period', y='roi_percentage')
            plt.title(f'ROI Trend by {period.capitalize()}')
            plt.xlabel(period.capitalize())
            plt.ylabel('ROI Percentage')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise Exception(f"Error plotting ROI trend: {str(e)}")
    
    def compare_campaigns(self, metric: str = 'roi_percentage', top_n: int = 5) -> pd.DataFrame:
        """
        Compare campaigns based on a specific metric.
        
        Args:
            metric (str): Metric to compare ('roi_percentage', 'profit', 'total_cost', 'total_revenue')
            top_n (int): Number of top campaigns to return
            
        Returns:
            pd.DataFrame: DataFrame with top campaigns by the specified metric
        """
        valid_metrics = ['roi_percentage', 'profit', 'total_cost', 'total_revenue']
        if metric not in valid_metrics:
            raise ValueError(f"Invalid metric. Must be one of: {valid_metrics}")
        
        try:
            data = self.campaign_data.copy()
            
            # Calculate metrics for each campaign
            campaign_metrics = []
            for campaign_id in data['campaign_id'].unique():
                metrics = self.calculate_roi(campaign_id)
                metrics['campaign_id'] = campaign_id
                campaign_metrics.append(metrics)
            
            metrics_df = pd.DataFrame(campaign_metrics)
            
            # Sort and return top_n
            ascending = False if metric in ['roi_percentage', 'profit'] else True
            return metrics_df.sort_values(by=metric, ascending=ascending).head(top_n)
            
        except Exception as e:
            raise Exception(f"Error comparing campaigns: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = ROIAnalyzer("marketing_campaigns.csv")
        
        # Calculate overall ROI
        overall_roi = analyzer.calculate_roi()
        print(f"Overall ROI: {overall_roi['roi_percentage']:.2f}%")
        
        # Calculate ROI by month
        monthly_roi = analyzer.calculate_roi_by_time_period('month')
        print("\nMonthly ROI:")
        print(monthly_roi)
        
        # Plot ROI trend
        analyzer.plot_roi_trend('month')
        
        # Compare top campaigns
        top_campaigns = analyzer.compare_campaigns(metric='roi_percentage', top_n=3)
        print("\nTop 3 Campaigns by ROI:")
        print(top_campaigns)
        
    except Exception as e:
        print(f"Error in ROI analysis: {str(e)}")
```
