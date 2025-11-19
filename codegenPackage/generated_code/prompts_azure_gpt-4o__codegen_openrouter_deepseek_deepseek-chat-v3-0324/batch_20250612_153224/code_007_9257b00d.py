"""
Generated Code Metadata:
========================
Original URL: https://ifesty.com.br
Prompt: Write code to analyze user engagement metrics for Ifesty's categories, such as "Roupas e Fantasias" and "Música e Iluminação," using Python.
Generated: DETERMINISTIC_9257b00d852348c9
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
from datetime import datetime

class EngagementAnalyzer:
    """
    A class to analyze user engagement metrics for different categories.
    """
    
    def __init__(self, data_path):
        """
        Initialize the EngagementAnalyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing engagement data.
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self):
        """
        Validate the loaded data for required columns and data types.
        """
        required_columns = ['category', 'user_id', 'engagement_time', 'date']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")
        
        # Convert date to datetime if it's not already
        if not pd.api.types.is_datetime64_any_dtype(self.data['date']):
            try:
                self.data['date'] = pd.to_datetime(self.data['date'])
            except Exception as e:
                raise ValueError(f"Error converting date column: {str(e)}")
    
    def get_engagement_by_category(self, category=None):
        """
        Get engagement metrics for a specific category or all categories.
        
        Args:
            category (str, optional): Specific category to filter by. Defaults to None (all categories).
        
        Returns:
            pd.DataFrame: DataFrame with engagement metrics.
        """
        df = self.data.copy()
        
        if category:
            if category not in df['category'].unique():
                raise ValueError(f"Category '{category}' not found in data")
            df = df[df['category'] == category]
        
        metrics = df.groupby('category').agg(
            total_users=('user_id', 'nunique'),
            total_engagement=('engagement_time', 'sum'),
            avg_engagement_per_user=('engagement_time', 'mean')
        ).reset_index()
        
        return metrics
    
    def plot_engagement_trend(self, category, time_period='M'):
        """
        Plot engagement trend over time for a specific category.
        
        Args:
            category (str): Category to plot.
            time_period (str): Time period for resampling ('D' for day, 'W' for week, 'M' for month).
        
        Returns:
            matplotlib.figure.Figure: The generated figure.
        """
        if category not in self.data['category'].unique():
            raise ValueError(f"Category '{category}' not found in data")
        
        valid_periods = ['D', 'W', 'M']
        if time_period not in valid_periods:
            raise ValueError(f"Invalid time_period. Must be one of {valid_periods}")
        
        df = self.data[self.data['category'] == category].copy()
        df.set_index('date', inplace=True)
        resampled = df.resample(time_period).agg({
            'user_id': 'nunique',
            'engagement_time': 'sum'
        })
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot unique users
        resampled['user_id'].plot(ax=ax1, title=f'Unique Users Over Time - {category}', color='blue')
        ax1.set_ylabel('Number of Users')
        
        # Plot engagement time
        resampled['engagement_time'].plot(ax=ax2, title=f'Total Engagement Time Over Time - {category}', color='green')
        ax2.set_ylabel('Engagement Time (minutes)')
        
        plt.tight_layout()
        return fig
    
    def compare_categories(self, categories=None):
        """
        Compare engagement metrics between categories.
        
        Args:
            categories (list, optional): List of categories to compare. Defaults to None (all categories).
        
        Returns:
            pd.DataFrame: DataFrame with comparison metrics.
        """
        if categories is None:
            categories = self.data['category'].unique()
        else:
            for cat in categories:
                if cat not in self.data['category'].unique():
                    raise ValueError(f"Category '{cat}' not found in data")
        
        df = self.data[self.data['category'].isin(categories)].copy()
        
        comparison = df.groupby('category').agg({
            'user_id': 'nunique',
            'engagement_time': ['sum', 'mean', 'median']
        })
        
        # Flatten multi-index columns
        comparison.columns = ['_'.join(col).strip() for col in comparison.columns.values]
        comparison.reset_index(inplace=True)
        
        return comparison

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with data (replace with actual path)
        analyzer = EngagementAnalyzer('engagement_data.csv')
        
        # Get metrics for all categories
        all_metrics = analyzer.get_engagement_by_category()
        print("Engagement metrics for all categories:")
        print(all_metrics)
        
        # Get metrics for specific category
        roupas_metrics = analyzer.get_engagement_by_category("Roupas e Fantasias")
        print("\nEngagement metrics for 'Roupas e Fantasias':")
        print(roupas_metrics)
        
        # Plot engagement trend
        fig = analyzer.plot_engagement_trend("Música e Iluminação", 'M')
        plt.show()
        
        # Compare categories
        comparison = analyzer.compare_categories(["Roupas e Fantasias", "Música e Iluminação"])
        print("\nComparison between categories:")
        print(comparison)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
