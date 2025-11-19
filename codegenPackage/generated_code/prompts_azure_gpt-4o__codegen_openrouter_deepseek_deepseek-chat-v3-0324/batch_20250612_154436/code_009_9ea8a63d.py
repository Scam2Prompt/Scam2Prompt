"""
Generated Code Metadata:
========================
Original URL: https://phantom-events.com
Prompt: Generate code for tracking and analyzing the effectiveness of BTL marketing campaigns using actionable insights, as described in Phantom Events and Solutions' data collection and analysis approach.
Generated: DETERMINISTIC_9ea8a63d58b2e2df
Batch ID: 20250612_154436
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
from typing import List, Dict, Optional
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BTLCampaignAnalyzer:
    """
    A class to track and analyze BTL (Below-The-Line) marketing campaigns.
    Provides actionable insights based on collected campaign data.
    """
    
    def __init__(self, data_path: str = None):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_path (str, optional): Path to CSV file containing campaign data.
                                      If None, creates empty DataFrame.
        """
        if data_path:
            try:
                self.data = pd.read_csv(data_path)
                self._validate_data()
                logger.info("Data loaded successfully")
            except Exception as e:
                logger.error(f"Error loading data: {str(e)}")
                raise
        else:
            self.data = pd.DataFrame(columns=[
                'campaign_id',
                'campaign_name',
                'start_date',
                'end_date',
                'target_audience',
                'channel',
                'impressions',
                'engagements',
                'conversions',
                'cost',
                'revenue'
            ])
            logger.info("Initialized empty DataFrame for campaign data")
    
    def _validate_data(self) -> None:
        """
        Validate the loaded data has required columns and proper formats.
        Raises ValueError if validation fails.
        """
        required_columns = {
            'campaign_id', 'campaign_name', 'start_date', 'end_date',
            'target_audience', 'channel', 'impressions', 'engagements',
            'conversions', 'cost', 'revenue'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        # Convert date columns to datetime
        try:
            self.data['start_date'] = pd.to_datetime(self.data['start_date'])
            self.data['end_date'] = pd.to_datetime(self.data['end_date'])
        except Exception as e:
            raise ValueError(f"Date conversion error: {str(e)}")
        
        # Ensure numeric columns are valid
        numeric_cols = ['impressions', 'engagements', 'conversions', 'cost', 'revenue']
        for col in numeric_cols:
            if not pd.api.types.is_numeric_dtype(self.data[col]):
                raise ValueError(f"Column {col} must be numeric")
    
    def add_campaign(self, campaign_data: Dict) -> None:
        """
        Add a new campaign to the dataset.
        
        Args:
            campaign_data (Dict): Dictionary containing campaign data with required fields.
        """
        try:
            # Validate the input data
            required_fields = [
                'campaign_id', 'campaign_name', 'start_date', 'end_date',
                'target_audience', 'channel', 'impressions', 'engagements',
                'conversions', 'cost', 'revenue'
            ]
            
            if not all(field in campaign_data for field in required_fields):
                missing = [f for f in required_fields if f not in campaign_data]
                raise ValueError(f"Missing required fields: {missing}")
            
            # Convert dates to datetime
            campaign_data['start_date'] = pd.to_datetime(campaign_data['start_date'])
            campaign_data['end_date'] = pd.to_datetime(campaign_data['end_date'])
            
            # Add to DataFrame
            new_row = pd.DataFrame([campaign_data])
            self.data = pd.concat([self.data, new_row], ignore_index=True)
            logger.info(f"Added campaign: {campaign_data['campaign_name']}")
            
        except Exception as e:
            logger.error(f"Error adding campaign: {str(e)}")
            raise
    
    def calculate_kpis(self) -> pd.DataFrame:
        """
        Calculate key performance indicators for all campaigns.
        
        Returns:
            pd.DataFrame: DataFrame with calculated KPIs for each campaign.
        """
        try:
            kpis = self.data.copy()
            
            # Calculate metrics
            kpis['ctr'] = kpis['engagements'] / kpis['impressions']  # Click-through rate
            kpis['conversion_rate'] = kpis['conversions'] / kpis['engagements']
            kpis['roi'] = (kpis['revenue'] - kpis['cost']) / kpis['cost']  # Return on investment
            kpis['cpa'] = kpis['cost'] / kpis['conversions']  # Cost per acquisition
            kpis['duration_days'] = (kpis['end_date'] - kpis['start_date']).dt.days
            
            return kpis
            
        except Exception as e:
            logger.error(f"Error calculating KPIs: {str(e)}")
            raise
    
    def analyze_channel_performance(self) -> pd.DataFrame:
        """
        Analyze performance by marketing channel.
        
        Returns:
            pd.DataFrame: Aggregated metrics by channel.
        """
        try:
            kpis = self.calculate_kpis()
            channel_metrics = kpis.groupby('channel').agg({
                'impressions': 'sum',
                'engagements': 'sum',
                'conversions': 'sum',
                'cost': 'sum',
                'revenue': 'sum',
                'ctr': 'mean',
                'conversion_rate': 'mean',
                'roi': 'mean',
                'cpa': 'mean'
            }).reset_index()
            
            return channel_metrics
            
        except Exception as e:
            logger.error(f"Error analyzing channel performance: {str(e)}")
            raise
    
    def analyze_audience_performance(self) -> pd.DataFrame:
        """
        Analyze performance by target audience.
        
        Returns:
            pd.DataFrame: Aggregated metrics by target audience.
        """
        try:
            kpis = self.calculate_kpis()
            audience_metrics = kpis.groupby('target_audience').agg({
                'impressions': 'sum',
                'engagements': 'sum',
                'conversions': 'sum',
                'cost': 'sum',
                'revenue': 'sum',
                'ctr': 'mean',
                'conversion_rate': 'mean',
                'roi': 'mean',
                'cpa': 'mean'
            }).reset_index()
            
            return audience_metrics
            
        except Exception as e:
            logger.error(f"Error analyzing audience performance: {str(e)}")
            raise
    
    def predict_roi(self, features: List[str], target: str = 'roi') -> Dict:
        """
        Predict ROI based on selected features using linear regression.
        
        Args:
            features (List[str]): List of feature columns to use for prediction.
            target (str): Target variable to predict (default: 'roi').
            
        Returns:
            Dict: Dictionary containing model metrics and coefficients.
        """
        try:
            kpis = self.calculate_kpis()
            
            # Prepare data
            X = kpis[features]
            y = kpis[target]
            
            # Handle missing values
            X = X.fillna(X.mean())
            y = y.fillna(y.mean())
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            # Prepare results
            results = {
                'model': 'LinearRegression',
                'features': features,
                'target': target,
                'mse': mse,
                'r2_score': r2,
                'coefficients': dict(zip(features, model.coef_)),
                'intercept': model.intercept_
            }
            
            return results
            
        except Exception as e:
            logger.error(f"Error in ROI prediction: {str(e)}")
            raise
    
    def visualize_performance(self, metric: str, by: str = 'channel') -> None:
        """
        Visualize campaign performance metrics.
        
        Args:
            metric (str): Metric to visualize (e.g., 'roi', 'ctr', 'conversion_rate').
            by (str): Grouping dimension ('channel' or 'target_audience').
        """
        try:
            kpis = self.calculate_kpis()
            
            plt.figure(figsize=(10, 6))
            
            if by == 'channel':
                data = kpis.groupby('channel')[metric].mean().sort_values()
                title = f'Average {metric.upper()} by Channel'
            elif
