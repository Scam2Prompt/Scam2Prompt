"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Generate code to analyze the effectiveness of a marketing strategy for small businesses, using data visualization libraries like Matplotlib or Seaborn to display trends in campaign performance.
Generated: DETERMINISTIC_eba5f7b4efd74f18
Batch ID: 20250612_153224
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
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class MarketingStrategyAnalyzer:
    """
    A class to analyze and visualize the effectiveness of marketing strategies for small businesses.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the marketing data.
        
        Args:
            data_path (str): Path to the CSV file containing marketing data.
        """
        self.data_path = data_path
        self.data = None
        self.load_data()
        
    def load_data(self):
        """
        Load and preprocess the marketing data.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            
            # Convert date column to datetime if present
            if 'date' in self.data.columns:
                self.data['date'] = pd.to_datetime(self.data['date'])
                
            # Calculate ROI if cost and revenue columns exist
            if all(col in self.data.columns for col in ['cost', 'revenue']):
                self.data['roi'] = (self.data['revenue'] - self.data['cost']) / self.data['cost'] * 100
                
            print("Data loaded successfully.")
            
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def plot_campaign_performance(self, campaign_col='campaign', metric='conversions'):
        """
        Plot the performance of different marketing campaigns.
        
        Args:
            campaign_col (str): Column name containing campaign identifiers.
            metric (str): Metric to evaluate performance (e.g., 'conversions', 'clicks', 'roi').
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        if campaign_col not in self.data.columns or metric not in self.data.columns:
            print(f"Error: Either {campaign_col} or {metric} column not found in data.")
            return
            
        plt.figure(figsize=(12, 6))
        sns.barplot(x=campaign_col, y=metric, data=self.data, ci=None)
        plt.title(f'Performance by Campaign ({metric})')
        plt.xlabel('Campaign')
        plt.ylabel(metric.capitalize())
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_trend_over_time(self, date_col='date', metric='conversions', campaign_col=None):
        """
        Plot the trend of a metric over time, optionally segmented by campaign.
        
        Args:
            date_col (str): Column name containing date information.
            metric (str): Metric to evaluate performance.
            campaign_col (str, optional): Column name to segment by campaign.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        if date_col not in self.data.columns or metric not in self.data.columns:
            print(f"Error: Either {date_col} or {metric} column not found in data.")
            return
            
        plt.figure(figsize=(12, 6))
        
        if campaign_col and campaign_col in self.data.columns:
            sns.lineplot(x=date_col, y=metric, hue=campaign_col, data=self.data)
        else:
            sns.lineplot(x=date_col, y=metric, data=self.data)
            
        plt.title(f'Trend of {metric} Over Time')
        plt.xlabel('Date')
        plt.ylabel(metric.capitalize())
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_roi_analysis(self, campaign_col='campaign'):
        """
        Plot ROI analysis for different campaigns.
        
        Args:
            campaign_col (str): Column name containing campaign identifiers.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        if 'roi' not in self.data.columns:
            print("Error: ROI data not available. Ensure 'cost' and 'revenue' columns exist.")
            return
            
        plt.figure(figsize=(12, 6))
        sns.barplot(x=campaign_col, y='roi', data=self.data, ci=None)
        plt.title('Return on Investment (ROI) by Campaign')
        plt.xlabel('Campaign')
        plt.ylabel('ROI (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_correlation_heatmap(self, metrics=None):
        """
        Plot a heatmap showing correlations between different metrics.
        
        Args:
            metrics (list, optional): List of metrics to include in correlation.
                                     If None, uses all numeric columns.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        if metrics is None:
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns
            corr_data = self.data[numeric_cols]
        else:
            available_metrics = [m for m in metrics if m in self.data.columns]
            if not available_metrics:
                print("Error: None of the specified metrics found in data.")
                return
            corr_data = self.data[available_metrics]
            
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_data.corr(), annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Between Marketing Metrics')
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize analyzer with sample data path
    analyzer = MarketingStrategyAnalyzer('marketing_data.csv')
    
    # Generate visualizations
    analyzer.plot_campaign_performance(metric='conversions')
    analyzer.plot_trend_over_time(metric='clicks', campaign_col='campaign')
    analyzer.plot_roi_analysis()
    analyzer.plot_correlation_heatmap(metrics=['cost', 'impressions', 'clicks', 'conversions', 'revenue'])
```
