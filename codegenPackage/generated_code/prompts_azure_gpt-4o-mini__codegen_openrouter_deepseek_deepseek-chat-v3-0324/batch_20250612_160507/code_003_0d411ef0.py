"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Generate a Python script that helps CEOs and CFOs visualize financial insights for better decision-making in organizational growth.
Generated: DETERMINISTIC_0d411ef0bba1fd71
Batch ID: 20250612_160507
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
from typing import Optional, Dict, List, Union

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class FinancialVisualizer:
    """
    A class to help CEOs and CFOs visualize financial insights for better decision-making.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the FinancialVisualizer with financial data.
        
        Args:
            data_path (str): Path to the financial data file (CSV or Excel)
        """
        self.data_path = data_path
        self.data = self._load_data()
        self._validate_data()
        
    def _load_data(self) -> pd.DataFrame:
        """
        Load financial data from file.
        
        Returns:
            pd.DataFrame: Loaded financial data
        """
        try:
            if self.data_path.endswith('.csv'):
                return pd.read_csv(self.data_path)
            elif self.data_path.endswith(('.xls', '.xlsx')):
                return pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate the loaded financial data for required columns.
        """
        required_columns = ['date', 'revenue', 'expenses', 'profit']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        if not pd.api.types.is_numeric_dtype(self.data['revenue']):
            raise ValueError("Revenue must be numeric")
            
        if not pd.api.types.is_numeric_dtype(self.data['expenses']):
            raise ValueError("Expenses must be numeric")
            
        if not pd.api.types.is_numeric_dtype(self.data['profit']):
            raise ValueError("Profit must be numeric")
            
        try:
            self.data['date'] = pd.to_datetime(self.data['date'])
        except:
            raise ValueError("Date column must be convertible to datetime")
    
    def plot_revenue_trend(self, time_period: str = 'monthly', save_path: Optional[str] = None) -> None:
        """
        Plot revenue trend over time.
        
        Args:
            time_period (str): Time period for aggregation ('daily', 'weekly', 'monthly', 'quarterly', 'yearly')
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        valid_periods = ['daily', 'weekly', 'monthly', 'quarterly', 'yearly']
        if time_period not in valid_periods:
            raise ValueError(f"Invalid time_period. Must be one of {valid_periods}")
            
        df = self.data.copy()
        df.set_index('date', inplace=True)
        
        if time_period == 'daily':
            resampled = df['revenue'].resample('D').sum()
        elif time_period == 'weekly':
            resampled = df['revenue'].resample('W').sum()
        elif time_period == 'monthly':
            resampled = df['revenue'].resample('M').sum()
        elif time_period == 'quarterly':
            resampled = df['revenue'].resample('Q').sum()
        else:  # yearly
            resampled = df['revenue'].resample('Y').sum()
            
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=resampled, marker='o')
        plt.title(f'Revenue Trend ({time_period.capitalize()})', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Revenue ($)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def plot_expense_breakdown(self, top_n: int = 5, save_path: Optional[str] = None) -> None:
        """
        Plot expense breakdown by category.
        
        Args:
            top_n (int): Number of top expense categories to display
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        if 'category' not in self.data.columns:
            raise ValueError("Data must contain 'category' column for expense breakdown")
            
        expense_by_category = self.data.groupby('category')['expenses'].sum().sort_values(ascending=False)
        
        if top_n > 0:
            expense_by_category = expense_by_category.head(top_n)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=expense_by_category.values, y=expense_by_category.index, palette='viridis')
        plt.title(f'Top {top_n} Expense Categories', fontsize=14)
        plt.xlabel('Total Expenses ($)', fontsize=12)
        plt.ylabel('Category', fontsize=12)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def plot_profit_margin(self, window: int = 3, save_path: Optional[str] = None) -> None:
        """
        Plot rolling profit margin over time.
        
        Args:
            window (int): Rolling window size for calculating profit margin
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        df = self.data.copy()
        df.set_index('date', inplace=True)
        df['profit_margin'] = (df['profit'] / df['revenue']) * 100
        
        rolling_margin = df['profit_margin'].rolling(window=window).mean()
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=rolling_margin, color='purple')
        plt.title(f'Rolling {window}-Period Profit Margin (%)', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Profit Margin (%)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def plot_financial_health(self, save_path: Optional[str] = None) -> None:
        """
        Plot comprehensive financial health metrics.
        
        Args:
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        df = self.data.copy()
        df.set_index('date', inplace=True)
        
        fig, axes = plt.subplots(3, 1, figsize=(12, 12))
        
        # Revenue plot
        sns.lineplot(data=df['revenue'], ax=axes[0], color='green')
        axes[0].set_title('Revenue Over Time', fontsize=12)
        axes[0].set_ylabel('Revenue ($)', fontsize=10)
        
        # Expenses plot
        sns.lineplot(data=df['expenses'], ax=axes[1], color='red')
        axes[1].set_title('Expenses Over Time', fontsize=12)
        axes[1].set_ylabel('Expenses ($)', fontsize=10)
        
        # Profit plot
        sns.lineplot(data=df['profit'], ax=axes[2], color='blue')
        axes[2].set_title('Profit Over Time', fontsize=12)
        axes[2].set_ylabel('Profit ($)', fontsize=10)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def generate_financial_report(self, report_path: str) -> None:
        """
        Generate a comprehensive financial report with multiple visualizations.
        
        Args:
            report_path (str): Path to save the report (PDF format)
        """
        from matplotlib.backends.backend_pdf import PdfPages
        
        with PdfPages(report_path) as pdf:
            # Revenue trend
            self.plot_revenue_trend('monthly')
            pdf.savefig()
            plt.close()
            
            # Expense breakdown
            try:
                self.plot_expense_breakdown(top_n=5)
                pdf.savefig()
                plt.close()
            except ValueError:
                pass
            
            # Profit margin
            self.plot_profit_margin(window=3)
            pdf.savefig()
            plt.close()
            
            # Financial health
            self.plot_financial_health()
            pdf.savefig()
            plt.close()
            
            # Add summary statistics
            plt.figure(figsize=(8, 4))
            plt.
