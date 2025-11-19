"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Create a Python script to analyze the ROI of social media video campaigns produced by Kraken Media, focusing on metrics like clicks, conversions, and revenue.
Generated: DETERMINISTIC_cee0ce349527f72b
Batch ID: 20250612_151752
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
from typing import Dict, List, Optional, Tuple

class SocialMediaROIAnalyzer:
    """
    A class to analyze the ROI of social media video campaigns.
    Focuses on metrics like clicks, conversions, and revenue.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data.
        """
        self.data_path = data_path
        self.campaign_data = None
        self.load_data()
        
    def load_data(self) -> None:
        """
        Load and preprocess the campaign data from CSV.
        
        Raises:
            FileNotFoundError: If the data file is not found.
            ValueError: If the data file is malformed.
        """
        try:
            self.campaign_data = pd.read_csv(self.data_path)
            
            # Validate required columns
            required_columns = {'campaign_id', 'campaign_name', 'clicks', 
                               'conversions', 'revenue', 'cost'}
            if not required_columns.issubset(self.campaign_data.columns):
                missing = required_columns - set(self.campaign_data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Convert numeric columns, handling potential non-numeric values
            numeric_cols = ['clicks', 'conversions', 'revenue', 'cost']
            for col in numeric_cols:
                self.campaign_data[col] = pd.to_numeric(self.campaign_data[col], errors='coerce')
                
            # Drop rows with missing numeric values
            self.campaign_data.dropna(subset=numeric_cols, inplace=True)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at: {self.data_path}")
        except Exception as e:
            raise ValueError(f"Error processing data: {str(e)}")
    
    def calculate_roi(self) -> pd.DataFrame:
        """
        Calculate ROI (Return on Investment) for each campaign.
        
        Returns:
            pd.DataFrame: DataFrame with ROI and other metrics added.
        """
        if self.campaign_data is None:
            raise ValueError("No data loaded. Call load_data() first.")
            
        data = self.campaign_data.copy()
        
        # Calculate metrics
        data['cpa'] = data['cost'] / data['conversions']
        data['roas'] = data['revenue'] / data['cost']
        data['roi'] = ((data['revenue'] - data['cost']) / data['cost']) * 100
        data['conversion_rate'] = (data['conversions'] / data['clicks']) * 100
        
        return data
    
    def get_top_campaigns(self, metric: str = 'roi', n: int = 5) -> pd.DataFrame:
        """
        Get top performing campaigns by specified metric.
        
        Args:
            metric (str): Metric to sort by (default: 'roi')
            n (int): Number of top campaigns to return (default: 5)
            
        Returns:
            pd.DataFrame: DataFrame of top campaigns
            
        Raises:
            ValueError: If invalid metric is provided
        """
        valid_metrics = {'roi', 'roas', 'conversion_rate', 'revenue', 'clicks'}
        if metric not in valid_metrics:
            raise ValueError(f"Invalid metric. Must be one of: {valid_metrics}")
            
        roi_data = self.calculate_roi()
        return roi_data.nlargest(n, metric)
    
    def plot_metric_trend(self, metric: str = 'roi') -> None:
        """
        Plot the trend of a specified metric across campaigns.
        
        Args:
            metric (str): Metric to plot (default: 'roi')
            
        Raises:
            ValueError: If invalid metric is provided
        """
        valid_metrics = {'roi', 'roas', 'conversion_rate', 'revenue', 'clicks'}
        if metric not in valid_metrics:
            raise ValueError(f"Invalid metric. Must be one of: {valid_metrics}")
            
        roi_data = self.calculate_roi()
        
        plt.figure(figsize=(10, 6))
        plt.bar(roi_data['campaign_name'], roi_data[metric])
        plt.title(f'{metric.upper()} by Campaign')
        plt.xlabel('Campaign Name')
        plt.ylabel(metric.upper())
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    
    def generate_report(self, output_path: Optional[str] = None) -> Dict:
        """
        Generate a comprehensive report of campaign performance.
        
        Args:
            output_path (str, optional): Path to save report as CSV. If None, no file is saved.
            
        Returns:
            Dict: Dictionary containing summary statistics
        """
        roi_data = self.calculate_roi()
        
        report = {
            'total_campaigns': len(roi_data),
            'total_revenue': roi_data['revenue'].sum(),
            'total_cost': roi_data['cost'].sum(),
            'total_clicks': roi_data['clicks'].sum(),
            'total_conversions': roi_data['conversions'].sum(),
            'average_roi': roi_data['roi'].mean(),
            'average_roas': roi_data['roas'].mean(),
            'average_cpa': roi_data['cpa'].mean(),
            'average_conversion_rate': roi_data['conversion_rate'].mean(),
            'top_5_roi_campaigns': self.get_top_campaigns('roi', 5).to_dict('records'),
            'top_5_roas_campaigns': self.get_top_campaigns('roas', 5).to_dict('records')
        }
        
        if output_path:
            try:
                pd.DataFrame.from_dict(report, orient='index').to_csv(output_path)
            except Exception as e:
                print(f"Warning: Could not save report to {output_path}. Error: {str(e)}")
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = SocialMediaROIAnalyzer('campaign_data.csv')
        
        # Generate and print report
        report = analyzer.generate_report('campaign_report.csv')
        print("Campaign Performance Report:")
        for key, value in report.items():
            if isinstance(value, (int, float)):
                print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
            elif key.startswith('top_5'):
                print(f"\n{key.replace('_', ' ').title()}:")
                for campaign in value:
                    print(f"  - {campaign['campaign_name']}: {campaign['roi']:.2f}% ROI")
        
        # Plot ROI trend
        analyzer.plot_metric_trend('roi')
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
