"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: Write code to track and measure the effectiveness of BTL and ATL advertising strategies, as implemented by Master-Brain.
Generated: DETERMINISTIC_0cf15b50b8ba3406
Batch ID: 20250612_154837
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
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AdvertisingStrategyAnalyzer:
    """
    A class to track and measure the effectiveness of BTL (Below The Line) 
    and ATL (Above The Line) advertising strategies.
    """
    
    def __init__(self):
        self.atl_data = pd.DataFrame(columns=['date', 'campaign_name', 'cost', 'impressions', 'clicks', 'conversions'])
        self.btl_data = pd.DataFrame(columns=['date', 'campaign_name', 'cost', 'reach', 'engagements', 'conversions'])
        self.merged_data = pd.DataFrame()
        
    def add_atl_campaign(
        self, 
        date: str, 
        campaign_name: str, 
        cost: float, 
        impressions: int, 
        clicks: int, 
        conversions: int
    ) -> None:
        """
        Add ATL campaign data to the tracker.
        
        Args:
            date: Date of the campaign in YYYY-MM-DD format
            campaign_name: Name of the campaign
            cost: Total cost of the campaign
            impressions: Number of impressions
            clicks: Number of clicks
            conversions: Number of conversions
        """
        try:
            new_row = {
                'date': pd.to_datetime(date),
                'campaign_name': campaign_name,
                'cost': cost,
                'impressions': impressions,
                'clicks': clicks,
                'conversions': conversions
            }
            self.atl_data = self.atl_data.append(new_row, ignore_index=True)
            logger.info(f"Added ATL campaign: {campaign_name}")
        except Exception as e:
            logger.error(f"Error adding ATL campaign: {e}")
            raise
            
    def add_btl_campaign(
        self, 
        date: str, 
        campaign_name: str, 
        cost: float, 
        reach: int, 
        engagements: int, 
        conversions: int
    ) -> None:
        """
        Add BTL campaign data to the tracker.
        
        Args:
            date: Date of the campaign in YYYY-MM-DD format
            campaign_name: Name of the campaign
            cost: Total cost of the campaign
            reach: Number of people reached
            engagements: Number of engagements
            conversions: Number of conversions
        """
        try:
            new_row = {
                'date': pd.to_datetime(date),
                'campaign_name': campaign_name,
                'cost': cost,
                'reach': reach,
                'engagements': engagements,
                'conversions': conversions
            }
            self.btl_data = self.btl_data.append(new_row, ignore_index=True)
            logger.info(f"Added BTL campaign: {campaign_name}")
        except Exception as e:
            logger.error(f"Error adding BTL campaign: {e}")
            raise
    
    def merge_data(self) -> None:
        """
        Merge ATL and BTL data for analysis, adding strategy type column.
        """
        try:
            atl = self.atl_data.copy()
            btl = self.btl_data.copy()
            
            atl['strategy_type'] = 'ATL'
            btl['strategy_type'] = 'BTL'
            
            # Standardize column names for merging
            atl = atl.rename(columns={'impressions': 'reach', 'clicks': 'engagements'})
            
            self.merged_data = pd.concat([atl, btl], ignore_index=True, sort=False)
            logger.info("Successfully merged ATL and BTL data")
        except Exception as e:
            logger.error(f"Error merging data: {e}")
            raise
    
    def calculate_metrics(self) -> pd.DataFrame:
        """
        Calculate key performance metrics for all campaigns.
        
        Returns:
            DataFrame with calculated metrics including:
            - CPA (Cost Per Acquisition)
            - CPM (Cost Per Thousand impressions/reach)
            - CTR (Click Through Rate for ATL, Engagement Rate for BTL)
            - Conversion Rate
        """
        try:
            if self.merged_data.empty:
                self.merge_data()
                
            data = self.merged_data.copy()
            
            # Calculate metrics
            data['cpa'] = data['cost'] / data['conversions']
            data['cpm'] = (data['cost'] / data['reach']) * 1000
            data['ctr'] = data['engagements'] / data['reach']
            data['conversion_rate'] = data['conversions'] / data['engagements']
            
            # Replace infinities with NaN
            data.replace([np.inf, -np.inf], np.nan, inplace=True)
            
            logger.info("Successfully calculated campaign metrics")
            return data
            
        except Exception as e:
            logger.error(f"Error calculating metrics: {e}")
            raise
    
    def compare_strategies(self) -> Dict[str, Dict[str, float]]:
        """
        Compare aggregate metrics between ATL and BTL strategies.
        
        Returns:
            Dictionary containing aggregated metrics for each strategy type
        """
        try:
            metrics = self.calculate_metrics()
            
            comparison = {
                'ATL': {
                    'avg_cpa': metrics[metrics['strategy_type'] == 'ATL']['cpa'].mean(),
                    'avg_cpm': metrics[metrics['strategy_type'] == 'ATL']['cpm'].mean(),
                    'avg_ctr': metrics[metrics['strategy_type'] == 'ATL']['ctr'].mean(),
                    'avg_conversion_rate': metrics[metrics['strategy_type'] == 'ATL']['conversion_rate'].mean()
                },
                'BTL': {
                    'avg_cpa': metrics[metrics['strategy_type'] == 'BTL']['cpa'].mean(),
                    'avg_cpm': metrics[metrics['strategy_type'] == 'BTL']['cpm'].mean(),
                    'avg_ctr': metrics[metrics['strategy_type'] == 'BTL']['ctr'].mean(),
                    'avg_conversion_rate': metrics[metrics['strategy_type'] == 'BTL']['conversion_rate'].mean()
                }
            }
            
            logger.info("Successfully compared ATL and BTL strategies")
            return comparison
            
        except Exception as e:
            logger.error(f"Error comparing strategies: {e}")
            raise
    
    def plot_metrics_over_time(self, metric: str) -> None:
        """
        Plot a specified metric over time for both strategies.
        
        Args:
            metric: One of 'cpa', 'cpm', 'ctr', or 'conversion_rate'
        """
        try:
            metrics = self.calculate_metrics()
            
            if metric not in ['cpa', 'cpm', 'ctr', 'conversion_rate']:
                raise ValueError("Invalid metric specified")
                
            plt.figure(figsize=(12, 6))
            sns.lineplot(
                x='date', 
                y=metric, 
                hue='strategy_type', 
                data=metrics,
                marker='o'
            )
            plt.title(f'{metric.upper()} Over Time by Strategy Type')
            plt.xlabel('Date')
            plt.ylabel(metric.upper())
            plt.grid(True)
            plt.show()
            
            logger.info(f"Successfully plotted {metric} over time")
            
        except Exception as e:
            logger.error(f"Error plotting metrics: {e}")
            raise
    
    def calculate_roi(self, revenue_per_conversion: float) -> pd.DataFrame:
        """
        Calculate ROI for each campaign.
        
        Args:
            revenue_per_conversion: Average revenue generated per conversion
            
        Returns:
            DataFrame with ROI calculations
        """
        try:
            metrics = self.calculate_metrics()
            metrics['revenue'] = metrics['conversions'] * revenue_per_conversion
            metrics['roi'] = (metrics['revenue'] - metrics['cost']) / metrics['cost']
            
            # Replace infinities with NaN
            metrics.replace([np.inf, -np.inf], np.nan, inplace=True)
            
            logger.info("Successfully calculated ROI")
            return metrics
            
        except Exception as e:
            logger.error(f"Error calculating ROI: {e}")
            raise
    
    def predict_conversions(self, future_campaigns: List[Dict[str, float]]) -> List[float]:
        """
        Predict conversions for future campaigns using linear regression.
        
        Args:
            future_campaigns: List of dictionaries containing 'cost' and 'reach' 
                             for future campaigns
                             
        Returns:
            List of predicted conversions
        """
        try:
            metrics = self.calculate_metrics()
            
            # Prepare data for model
            X = metrics[['cost', 'reach']].values
            y = metrics['conversions'].values
            
            # Train model
            model = LinearRegression()
            model
