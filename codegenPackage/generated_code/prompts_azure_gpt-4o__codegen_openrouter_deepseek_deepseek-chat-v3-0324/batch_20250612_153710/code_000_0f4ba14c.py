"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Write Python code to analyze business performance data using libraries recommended for management consulting, such as pandas and matplotlib.
Generated: DETERMINISTIC_0f4ba14c9d0cc9dd
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class BusinessPerformanceAnalyzer:
    """
    A class to analyze business performance data using pandas and matplotlib.
    Provides methods for data loading, cleaning, analysis, and visualization.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path (str, optional): Path to CSV file containing business data. Defaults to None.
        """
        self.data = None
        self.clean_data = None
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path):
        """
        Load business performance data from a CSV file.
        
        Args:
            data_path (str): Path to CSV file.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If the file is not a valid CSV.
        """
        try:
            self.data = pd.read_csv(data_path)
            print(f"Successfully loaded data with {len(self.data)} records.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {data_path} was not found.")
        except Exception as e:
            raise ValueError(f"Error loading CSV file: {str(e)}")
    
    def clean_and_preprocess(self):
        """
        Clean and preprocess the loaded data.
        Handles missing values, converts data types, and creates derived metrics.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        # Make a copy of the original data
        self.clean_data = self.data.copy()
        
        # Convert date columns to datetime
        date_columns = [col for col in self.clean_data.columns if 'date' in col.lower()]
        for col in date_columns:
            self.clean_data[col] = pd.to_datetime(self.clean_data[col], errors='coerce')
        
        # Handle missing values
        numeric_cols = self.clean_data.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            self.clean_data[col].fillna(self.clean_data[col].median(), inplace=True)
        
        # Fill remaining non-numeric missing values
        for col in self.clean_data.columns:
            if self.clean_data[col].dtype == 'object':
                self.clean_data[col].fillna('Unknown', inplace=True)
        
        # Create month and year columns if date exists
        if date_columns:
            primary_date_col = date_columns[0]
            self.clean_data['year'] = self.clean_data[primary_date_col].dt.year
            self.clean_data['month'] = self.clean_data[primary_date_col].dt.month
        
        print("Data cleaning and preprocessing completed.")
    
    def analyze_performance(self, metric_column, group_by=None, time_period='month'):
        """
        Analyze business performance metrics.
        
        Args:
            metric_column (str): Column name containing the metric to analyze.
            group_by (str, optional): Column name to group by. Defaults to None.
            time_period (str, optional): Time period for trend analysis ('month' or 'year'). Defaults to 'month'.
            
        Returns:
            pd.DataFrame: Aggregated performance data.
            
        Raises:
            ValueError: If metric_column doesn't exist or data isn't cleaned.
        """
        if self.clean_data is None:
            raise ValueError("Data not cleaned. Please run clean_and_preprocess() first.")
            
        if metric_column not in self.clean_data.columns:
            raise ValueError(f"Column '{metric_column}' not found in data.")
        
        # Basic analysis
        analysis = pd.DataFrame()
        analysis['total'] = self.clean_data[metric_column].sum()
        analysis['average'] = self.clean_data[metric_column].mean()
        analysis['median'] = self.clean_data[metric_column].median()
        analysis['std_dev'] = self.clean_data[metric_column].std()
        
        # Grouped analysis if specified
        if group_by:
            if group_by not in self.clean_data.columns:
                raise ValueError(f"Group by column '{group_by}' not found.")
                
            grouped = self.clean_data.groupby(group_by)[metric_column].agg(['sum', 'mean', 'median', 'std'])
            grouped.columns = [f"{col}_{metric_column}" for col in grouped.columns]
            analysis = grouped
            
        # Time series analysis if date columns exist
        if 'year' in self.clean_data.columns and time_period:
            time_col = time_period if time_period in ['month', 'year'] else 'month'
            time_series = self.clean_data.groupby(['year', time_col])[metric_column].sum().unstack()
            analysis = time_series
            
        return analysis
    
    def visualize_performance(self, metric_column, group_by=None, chart_type='line', figsize=(10, 6)):
        """
        Visualize business performance metrics.
        
        Args:
            metric_column (str): Column name containing the metric to visualize.
            group_by (str, optional): Column name to group by. Defaults to None.
            chart_type (str, optional): Type of chart ('line', 'bar', 'pie'). Defaults to 'line'.
            figsize (tuple, optional): Figure size. Defaults to (10, 6).
            
        Raises:
            ValueError: If metric_column doesn't exist or invalid chart type.
        """
        if self.clean_data is None:
            raise ValueError("Data not cleaned. Please run clean_and_preprocess() first.")
            
        if metric_column not in self.clean_data.columns:
            raise ValueError(f"Column '{metric_column}' not found in data.")
            
        plt.figure(figsize=figsize)
        
        if group_by:
            if group_by not in self.clean_data.columns:
                raise ValueError(f"Group by column '{group_by}' not found.")
                
            if chart_type == 'line':
                sns.lineplot(data=self.clean_data, x=group_by, y=metric_column)
                plt.title(f'{metric_column} by {group_by}')
            elif chart_type == 'bar':
                sns.barplot(data=self.clean_data, x=group_by, y=metric_column)
                plt.title(f'{metric_column} by {group_by}')
            elif chart_type == 'pie':
                grouped = self.clean_data.groupby(group_by)[metric_column].sum()
                grouped.plot(kind='pie', autopct='%1.1f%%')
                plt.title(f'Distribution of {metric_column} by {group_by}')
                plt.ylabel('')
            else:
                raise ValueError(f"Invalid chart type: {chart_type}. Choose 'line', 'bar', or 'pie'.")
        else:
            if chart_type == 'line':
                if 'year' in self.clean_data.columns and 'month' in self.clean_data.columns:
                    time_series = self.clean_data.groupby(['year', 'month'])[metric_column].sum().unstack()
                    time_series.plot(kind='line', figsize=figsize)
                    plt.title(f'{metric_column} Trend Over Time')
                else:
                    raise ValueError("No date columns found for time series visualization.")
            elif chart_type == 'hist':
                self.clean_data[metric_column].plot(kind='hist', bins=20)
                plt.title(f'Distribution of {metric_column}')
            else:
                raise ValueError(f"Invalid chart type for ungrouped data: {chart_type}. Choose 'line' or 'hist'.")
                
        plt.tight_layout()
        plt.show()
    
    def calculate_kpis(self, revenue_col, cost_col, date_col=None):
        """
        Calculate key performance indicators (KPIs).
        
        Args:
            revenue_col (str): Column name for revenue data.
            cost_col (str): Column name for cost data.
            date_col (str, optional): Column name for date data for time-based KPIs.
            
        Returns:
            dict: Dictionary of calculated KPIs.
            
        Raises:
            ValueError: If required columns don't exist.
        """
        if self.clean_data is None:
            raise ValueError("Data not cleaned. Please run clean_and_preprocess() first.")
            
        for col in [revenue_col, cost_col]:
            if col not in self.clean_data.columns:
                raise ValueError(f"Column '{col}' not found in data.")
                
        kpis = {}
        
        # Basic financial KPIs
        kpis['total_revenue'] = self.clean_data[revenue_col].sum()
        kpis['total_cost'] = self.clean_data[cost_col].sum()
        kpis['gross_profit'] = kpis['total_revenue'] - kpis['total_cost']
        kpis['gross_margin'] = (kpis['gross_profit'] / kpis['total_revenue']) * 100 if kpis['total_revenue'] != 0 else 0
        
        # Time-based KPIs if date column exists
        if date_col and date_col in self.clean_data.columns:
            self.clean_data['profit'] = self
