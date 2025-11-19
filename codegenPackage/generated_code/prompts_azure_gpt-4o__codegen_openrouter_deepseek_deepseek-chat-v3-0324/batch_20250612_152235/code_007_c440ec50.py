"""
Generated Code Metadata:
========================
Original URL: https://alphaonlineservices.com
Prompt: Develop a script for tracking and analyzing the performance of digital marketing campaigns, integrating design thinking and data-driven strategies similar to those used by Alpha Online Services.
Generated: DETERMINISTIC_c440ec50142f53d4
Batch ID: 20250612_152235
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
import seaborn as sns
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

class CampaignAnalyzer:
    """
    A class to track and analyze digital marketing campaign performance.
    Integrates design thinking and data-driven strategies.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the CampaignAnalyzer with optional data path.
        
        Args:
            data_path (str, optional): Path to campaign data CSV file. Defaults to None.
        """
        self.data = None
        self.insights = {}
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path):
        """
        Load campaign data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data.
            
        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the file is not a valid CSV or has missing required columns.
        """
        try:
            self.data = pd.read_csv(data_path)
            required_columns = ['campaign_id', 'date', 'impressions', 'clicks', 
                              'conversions', 'spend', 'revenue']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            # Convert date to datetime and calculate additional metrics
            self.data['date'] = pd.to_datetime(self.data['date'])
            self._calculate_metrics()
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {data_path}")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _calculate_metrics(self):
        """Calculate key performance metrics for the campaign data."""
        self.data['ctr'] = self.data['clicks'] / self.data['impressions']
        self.data['conversion_rate'] = self.data['conversions'] / self.data['clicks']
        self.data['cpa'] = self.data['spend'] / self.data['conversions']
        self.data['roi'] = (self.data['revenue'] - self.data['spend']) / self.data['spend']
    
    def generate_insights(self):
        """Generate key insights from the campaign data."""
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        # Basic statistics
        self.insights['summary_stats'] = {
            'total_campaigns': len(self.data['campaign_id'].unique()),
            'total_spend': self.data['spend'].sum(),
            'total_revenue': self.data['revenue'].sum(),
            'avg_ctr': self.data['ctr'].mean(),
            'avg_conversion_rate': self.data['conversion_rate'].mean(),
            'avg_cpa': self.data['cpa'].mean(),
            'avg_roi': self.data['roi'].mean()
        }
        
        # Time-based trends
        time_series = self.data.groupby(pd.Grouper(key='date', freq='W')).agg({
            'spend': 'sum',
            'revenue': 'sum',
            'impressions': 'sum',
            'clicks': 'sum',
            'conversions': 'sum'
        })
        time_series['roi'] = (time_series['revenue'] - time_series['spend']) / time_series['spend']
        self.insights['time_series'] = time_series
        
        # Best performing campaigns
        self.insights['top_campaigns'] = self.data.sort_values('roi', ascending=False).head(5)
        
        return self.insights
    
    def visualize_performance(self, save_path=None):
        """
        Generate visualizations for campaign performance.
        
        Args:
            save_path (str, optional): Path to save the visualizations. Defaults to None.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        plt.figure(figsize=(15, 10))
        
        # ROI over time
        plt.subplot(2, 2, 1)
        self.insights['time_series']['roi'].plot(title='ROI Over Time')
        plt.ylabel('ROI')
        
        # Spend vs Revenue
        plt.subplot(2, 2, 2)
        sns.scatterplot(data=self.data, x='spend', y='revenue', hue='roi')
        plt.title('Spend vs Revenue')
        
        # Conversion Rate Distribution
        plt.subplot(2, 2, 3)
        sns.histplot(self.data['conversion_rate'], bins=20, kde=True)
        plt.title('Conversion Rate Distribution')
        
        # Top Campaigns
        plt.subplot(2, 2, 4)
        top_campaigns = self.insights['top_campaigns']
        sns.barplot(data=top_campaigns, x='campaign_id', y='roi')
        plt.title('Top Performing Campaigns by ROI')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.show()
    
    def predict_performance(self, features, target, test_size=0.2):
        """
        Build a predictive model for campaign performance.
        
        Args:
            features (list): List of feature columns to use for prediction.
            target (str): Target column to predict.
            test_size (float, optional): Size of test set. Defaults to 0.2.
            
        Returns:
            dict: Model evaluation metrics and feature importance.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        # Prepare data
        X = self.data[features]
        y = self.data[target]
        
        # Handle missing values
        X = X.fillna(X.mean())
        y = y.fillna(y.mean())
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Feature importance
        importance = pd.DataFrame({
            'feature': features,
            'coefficient': model.coef_
        }).sort_values('coefficient', key=abs, ascending=False)
        
        return {
            'model': model,
            'metrics': {
                'mse': mse,
                'r2': r2
            },
            'feature_importance': importance
        }
    
    def optimize_campaign(self, campaign_id, budget_range, step=100):
        """
        Optimize budget allocation for a specific campaign.
        
        Args:
            campaign_id (str): ID of the campaign to optimize.
            budget_range (tuple): (min_budget, max_budget) range to test.
            step (int, optional): Budget increment step. Defaults to 100.
            
        Returns:
            pd.DataFrame: Results of budget optimization.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        campaign_data = self.data[self.data['campaign_id'] == campaign_id]
        if campaign_data.empty:
            raise ValueError(f"Campaign {campaign_id} not found in data.")
            
        # Build predictive model for this campaign
        features = ['spend', 'impressions', 'clicks']
        target = 'revenue'
        model_result = self.predict_performance(features, target)
        model = model_result['model']
        
        # Test different budget levels
        budgets = np.arange(budget_range[0], budget_range[1] + step, step)
        results = []
        
        for budget in budgets:
            # Predict performance at this budget level
            # (Assuming impressions and clicks scale linearly with spend)
            avg_impressions_per_dollar = campaign_data['impressions'].mean() / campaign_data['spend'].mean()
            avg_clicks_per_dollar = campaign_data['clicks'].mean() / campaign_data['spend'].mean()
            
            pred_input = np.array([[
                budget,
                budget * avg_impressions_per_dollar,
                budget * avg_clicks_per_dollar
            ]])
            
            pred_revenue = model.predict(pred_input)[0]
            pred_roi = (pred_revenue - budget) / budget
            
            results.append({
                'budget': budget,
                'predicted_revenue': pred_revenue,
                'predicted_roi': pred_roi
            })
        
        return pd.DataFrame(results
