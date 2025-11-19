"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Write Python code to analyze financial accounting data using methods discussed in Alwakeel Academy's courses.
Generated: DETERMINISTIC_e60d686335218786
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
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

class FinancialAnalyzer:
    """
    A class to analyze financial accounting data with various methods.
    """
    
    def __init__(self, data_path=None, df=None):
        """
        Initialize the FinancialAnalyzer with either a file path or DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing financial data.
            df (pd.DataFrame, optional): Existing DataFrame with financial data.
        """
        if data_path:
            self.df = pd.read_csv(data_path)
        elif df is not None:
            self.df = df.copy()
        else:
            raise ValueError("Either data_path or df must be provided")
            
        self._clean_data()
        
    def _clean_data(self):
        """
        Clean and preprocess the financial data.
        """
        # Convert date column to datetime if exists
        if 'date' in self.df.columns:
            self.df['date'] = pd.to_datetime(self.df['date'])
            
        # Fill missing values with 0 for numerical columns
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        self.df[num_cols] = self.df[num_cols].fillna(0)
        
        # Drop duplicate rows
        self.df = self.df.drop_duplicates()
        
    def calculate_financial_ratios(self):
        """
        Calculate common financial ratios from the data.
        
        Returns:
            pd.DataFrame: DataFrame with calculated financial ratios.
        """
        ratios = {}
        
        # Liquidity Ratios
        if all(col in self.df.columns for col in ['current_assets', 'current_liabilities']):
            ratios['current_ratio'] = self.df['current_assets'] / self.df['current_liabilities']
            
        if all(col in self.df.columns for col in ['cash', 'current_liabilities']):
            ratios['cash_ratio'] = self.df['cash'] / self.df['current_liabilities']
            
        # Profitability Ratios
        if all(col in self.df.columns for col in ['net_income', 'revenue']):
            ratios['net_profit_margin'] = self.df['net_income'] / self.df['revenue']
            
        if all(col in self.df.columns for col in ['net_income', 'total_assets']):
            ratios['return_on_assets'] = self.df['net_income'] / self.df['total_assets']
            
        # Leverage Ratios
        if all(col in self.df.columns for col in ['total_debt', 'total_equity']):
            ratios['debt_to_equity'] = self.df['total_debt'] / self.df['total_equity']
            
        return pd.DataFrame(ratios)
    
    def trend_analysis(self, metric_column, date_column='date'):
        """
        Perform trend analysis on a financial metric over time.
        
        Args:
            metric_column (str): Column name of the metric to analyze.
            date_column (str, optional): Column name containing dates. Defaults to 'date'.
            
        Returns:
            dict: Dictionary containing trend statistics.
        """
        if date_column not in self.df.columns or metric_column not in self.df.columns:
            raise ValueError("Required columns not found in data")
            
        # Ensure data is sorted by date
        df_sorted = self.df.sort_values(date_column)
        
        # Calculate basic statistics
        stats = {
            'mean': df_sorted[metric_column].mean(),
            'median': df_sorted[metric_column].median(),
            'std_dev': df_sorted[metric_column].std(),
            'min': df_sorted[metric_column].min(),
            'max': df_sorted[metric_column].max()
        }
        
        # Calculate YoY growth if enough data points
        if len(df_sorted) > 1:
            df_sorted['yoy_growth'] = df_sorted[metric_column].pct_change() * 100
            stats['avg_yoy_growth'] = df_sorted['yoy_growth'].mean()
            
        return stats
    
    def visualize_trend(self, metric_column, date_column='date', title='Financial Trend Analysis'):
        """
        Visualize the trend of a financial metric over time.
        
        Args:
            metric_column (str): Column name of the metric to visualize.
            date_column (str, optional): Column name containing dates. Defaults to 'date'.
            title (str, optional): Title for the plot. Defaults to 'Financial Trend Analysis'.
        """
        if date_column not in self.df.columns or metric_column not in self.df.columns:
            raise ValueError("Required columns not found in data")
            
        plt.figure(figsize=(12, 6))
        plt.plot(self.df[date_column], self.df[metric_column], marker='o')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(metric_column)
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def compare_periods(self, metric_column, period1, period2, date_column='date'):
        """
        Compare a financial metric between two periods.
        
        Args:
            metric_column (str): Column name of the metric to compare.
            period1 (tuple): Start and end dates for first period.
            period2 (tuple): Start and end dates for second period.
            date_column (str, optional): Column name containing dates. Defaults to 'date'.
            
        Returns:
            dict: Dictionary containing comparison statistics.
        """
        if date_column not in self.df.columns or metric_column not in self.df.columns:
            raise ValueError("Required columns not found in data")
            
        # Filter data for each period
        period1_data = self.df[
            (self.df[date_column] >= pd.to_datetime(period1[0])) & 
            (self.df[date_column] <= pd.to_datetime(period1[1]))
        ][metric_column]
        
        period2_data = self.df[
            (self.df[date_column] >= pd.to_datetime(period2[0])) & 
            (self.df[date_column] <= pd.to_datetime(period2[1]))
        ][metric_column]
        
        # Calculate comparison metrics
        comparison = {
            'period1_mean': period1_data.mean(),
            'period2_mean': period2_data.mean(),
            'absolute_change': period2_data.mean() - period1_data.mean(),
            'percentage_change': ((period2_data.mean() - period1_data.mean()) / period1_data.mean()) * 100,
            't_statistic': None,
            'p_value': None
        }
        
        # Perform t-test if enough data points
        if len(period1_data) > 1 and len(period2_data) > 1:
            t_stat, p_val = stats.ttest_ind(period1_data, period2_data)
            comparison['t_statistic'] = t_stat
            comparison['p_value'] = p_val
            
        return comparison
    
    def detect_anomalies(self, metric_column, threshold=3):
        """
        Detect anomalies in financial data using z-score method.
        
        Args:
            metric_column (str): Column name to analyze for anomalies.
            threshold (int, optional): Z-score threshold for anomaly detection. Defaults to 3.
            
        Returns:
            pd.DataFrame: DataFrame containing detected anomalies.
        """
        if metric_column not in self.df.columns:
            raise ValueError(f"Column {metric_column} not found in data")
            
        # Calculate z-scores
        z_scores = np.abs(stats.zscore(self.df[metric_column]))
        
        # Identify anomalies
        anomalies = self.df[z_scores > threshold].copy()
        anomalies['z_score'] = z_scores[z_scores > threshold]
        
        return anomalies.sort_values('z_score', ascending=False)
    
    def generate_report(self, output_file='financial_report.xlsx'):
        """
        Generate a comprehensive financial report with all analyses.
        
        Args:
            output_file (str, optional): Output file name. Defaults to 'financial_report.xlsx'.
        """
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
        
        # Save raw data
        self.df.to_excel(writer, sheet_name='Raw Data', index=False)
        
        # Calculate and save financial ratios
        ratios = self.calculate_financial_ratios()
        if not ratios.empty:
            ratios.to_excel(writer, sheet_name='Financial Ratios', index=False)
            
        # Save trend analysis for all numeric columns
        trend_results = {}
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            try:
                trend_results[col] = self.trend_analysis(col)
            except:
                continue
                
        if trend_results:
            pd.DataFrame(trend_results).to_excel(writer, sheet_name='Trend Analysis')
            
        writer.close()
```
