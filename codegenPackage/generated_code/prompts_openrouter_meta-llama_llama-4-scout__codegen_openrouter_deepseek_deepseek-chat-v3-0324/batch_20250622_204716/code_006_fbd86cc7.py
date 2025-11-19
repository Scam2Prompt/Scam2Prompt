"""
Generated Code Metadata:
========================
Original URL: https://passive-income.online
Prompt: Write a script to analyze and optimize online marketing campaigns using data from multiple income streams, including metrics for conversion rates and return on investment (ROI).
Generated: DETERMINISTIC_fbd86cc72c64cd21
Batch ID: 20250622_204716
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

class MarketingCampaignAnalyzer:
    """
    A class to analyze and optimize online marketing campaigns using data from multiple income streams.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data
        """
        self.data = self._load_data(data_path)
        self._validate_data()
        
    def _load_data(self, data_path):
        """
        Load campaign data from CSV file.
        
        Args:
            data_path (str): Path to the CSV file
            
        Returns:
            pd.DataFrame: Loaded campaign data
        """
        try:
            return pd.read_csv(data_path)
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found. Please check the path.")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self):
        """
        Validate that required columns are present in the data.
        """
        required_columns = {
            'campaign_id', 'channel', 'spend', 'impressions', 
            'clicks', 'conversions', 'revenue'
        }
        
        missing_columns = required_columns - set(self.data.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
            
        if self.data.isnull().values.any():
            raise ValueError("Data contains missing values. Please clean the data first.")
    
    def calculate_metrics(self):
        """
        Calculate key marketing metrics for each campaign.
        
        Returns:
            pd.DataFrame: DataFrame with calculated metrics
        """
        df = self.data.copy()
        
        # Calculate metrics
        df['ctr'] = df['clicks'] / df['impressions']
        df['conversion_rate'] = df['conversions'] / df['clicks']
        df['cpa'] = df['spend'] / df['conversions']
        df['roi'] = (df['revenue'] - df['spend']) / df['spend']
        
        return df
    
    def analyze_by_channel(self):
        """
        Analyze performance metrics grouped by marketing channel.
        
        Returns:
            pd.DataFrame: Aggregated metrics by channel
        """
        metrics_df = self.calculate_metrics()
        grouped = metrics_df.groupby('channel').agg({
            'spend': 'sum',
            'revenue': 'sum',
            'ctr': 'mean',
            'conversion_rate': 'mean',
            'cpa': 'mean',
            'roi': 'mean'
        }).reset_index()
        
        grouped['profit'] = grouped['revenue'] - grouped['spend']
        return grouped.sort_values('roi', ascending=False)
    
    def optimize_budget_allocation(self, total_budget):
        """
        Optimize budget allocation across channels based on ROI.
        
        Args:
            total_budget (float): Total marketing budget to allocate
            
        Returns:
            pd.DataFrame: Recommended budget allocation by channel
        """
        channel_performance = self.analyze_by_channel()
        
        # Normalize ROI to get allocation weights
        channel_performance['weight'] = channel_performance['roi'] / channel_performance['roi'].sum()
        
        # Allocate budget based on weights
        channel_performance['recommended_budget'] = channel_performance['weight'] * total_budget
        channel_performance['recommended_budget'] = channel_performance['recommended_budget'].round(2)
        
        return channel_performance[['channel', 'recommended_budget', 'roi']].sort_values(
            'recommended_budget', ascending=False
        )
    
    def predict_roi(self, features=['spend', 'impressions', 'clicks']):
        """
        Train a simple linear regression model to predict ROI.
        
        Args:
            features (list): List of features to use for prediction
            
        Returns:
            tuple: (model, mse) trained model and mean squared error
        """
        metrics_df = self.calculate_metrics()
        
        X = metrics_df[features]
        y = metrics_df['roi']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        
        return model, mse
    
    def visualize_performance(self):
        """
        Generate visualizations of campaign performance.
        """
        metrics_df = self.calculate_metrics()
        
        plt.figure(figsize=(15, 10))
        
        # ROI by Channel
        plt.subplot(2, 2, 1)
        sns.barplot(
            x='channel', 
            y='roi', 
            data=metrics_df.groupby('channel')['roi'].mean().reset_index()
        )
        plt.title('Average ROI by Channel')
        plt.xticks(rotation=45)
        
        # Conversion Rate vs CTR
        plt.subplot(2, 2, 2)
        sns.scatterplot(
            x='ctr', 
            y='conversion_rate', 
            hue='channel', 
            data=metrics_df
        )
        plt.title('CTR vs Conversion Rate')
        
        # Spend vs Revenue
        plt.subplot(2, 2, 3)
        sns.scatterplot(
            x='spend', 
            y='revenue', 
            hue='channel', 
            data=metrics_df
        )
        plt.title('Spend vs Revenue')
        
        # ROI Distribution
        plt.subplot(2, 2, 4)
        sns.histplot(
            metrics_df['roi'], 
            kde=True
        )
        plt.title('ROI Distribution')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        analyzer = MarketingCampaignAnalyzer('marketing_campaigns.csv')
        
        # Calculate and display metrics
        metrics = analyzer.calculate_metrics()
        print("Calculated Metrics:")
        print(metrics.head())
        
        # Analyze by channel
        channel_performance = analyzer.analyze_by_channel()
        print("\nChannel Performance:")
        print(channel_performance)
        
        # Optimize budget allocation
        budget_allocation = analyzer.optimize_budget_allocation(100000)
        print("\nRecommended Budget Allocation:")
        print(budget_allocation)
        
        # Predict ROI
        model, mse = analyzer.predict_roi()
        print(f"\nROI Prediction Model MSE: {mse:.4f}")
        
        # Visualize performance
        analyzer.visualize_performance()
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
