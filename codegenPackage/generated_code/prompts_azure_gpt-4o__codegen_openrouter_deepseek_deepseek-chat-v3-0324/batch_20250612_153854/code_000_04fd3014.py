"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Write Python code to analyze investment portfolios, focusing on private equity opportunities as described by Alghanim Capital's expertise in strategic growth and investment lifecycle management.
Generated: DETERMINISTIC_04fd3014f519d03f
Batch ID: 20250612_153854
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
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class PortfolioAnalyzer:
    """
    A class to analyze investment portfolios with a focus on private equity opportunities.
    """
    
    def __init__(self, portfolio_data):
        """
        Initialize the PortfolioAnalyzer with portfolio data.
        
        Args:
            portfolio_data (pd.DataFrame): DataFrame containing portfolio investment data
        """
        self.portfolio = portfolio_data.copy()
        self._validate_data()
        
    def _validate_data(self):
        """
        Validate the input portfolio data for required columns and data types.
        Raises ValueError if validation fails.
        """
        required_columns = {
            'investment_name': str,
            'sector': str,
            'investment_date': 'datetime64[ns]',
            'initial_investment': float,
            'current_value': float,
            'ownership_percentage': float,
            'stage': str,
            'country': str
        }
        
        missing_cols = [col for col in required_columns if col not in self.portfolio.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        for col, dtype in required_columns.items():
            if not pd.api.types.is_dtype_equal(self.portfolio[col].dtype, dtype):
                try:
                    self.portfolio[col] = self.portfolio[col].astype(dtype)
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Column '{col}' cannot be converted to {dtype}: {str(e)}")
    
    def calculate_returns(self):
        """
        Calculate various return metrics for the portfolio.
        
        Returns:
            pd.DataFrame: DataFrame with calculated return metrics
        """
        df = self.portfolio.copy()
        
        # Calculate absolute returns
        df['absolute_return'] = df['current_value'] - df['initial_investment']
        
        # Calculate percentage returns
        df['return_percentage'] = (df['absolute_return'] / df['initial_investment']) * 100
        
        # Calculate annualized returns
        current_date = pd.to_datetime(datetime.now())
        df['holding_period_years'] = (current_date - df['investment_date']).dt.days / 365.25
        df['annualized_return'] = ((1 + (df['return_percentage'] / 100)) ** (1 / df['holding_period_years']) - 1) * 100
        
        return df
    
    def analyze_by_sector(self):
        """
        Analyze portfolio performance by sector.
        
        Returns:
            pd.DataFrame: Aggregated metrics by sector
        """
        df = self.calculate_returns()
        sector_analysis = df.groupby('sector').agg({
            'initial_investment': 'sum',
            'current_value': 'sum',
            'absolute_return': 'sum',
            'return_percentage': 'mean',
            'annualized_return': 'mean'
        }).sort_values('absolute_return', ascending=False)
        
        sector_analysis['portfolio_percentage'] = (sector_analysis['initial_investment'] / 
                                                  sector_analysis['initial_investment'].sum()) * 100
        
        return sector_analysis
    
    def analyze_by_stage(self):
        """
        Analyze portfolio performance by investment stage.
        
        Returns:
            pd.DataFrame: Aggregated metrics by investment stage
        """
        df = self.calculate_returns()
        stage_analysis = df.groupby('stage').agg({
            'initial_investment': 'sum',
            'current_value': 'sum',
            'absolute_return': 'sum',
            'return_percentage': 'mean',
            'annualized_return': 'mean'
        }).sort_values('absolute_return', ascending=False)
        
        stage_analysis['portfolio_percentage'] = (stage_analysis['initial_investment'] / 
                                                 stage_analysis['initial_investment'].sum()) * 100
        
        return stage_analysis
    
    def analyze_by_geography(self):
        """
        Analyze portfolio performance by geography.
        
        Returns:
            pd.DataFrame: Aggregated metrics by country
        """
        df = self.calculate_returns()
        geo_analysis = df.groupby('country').agg({
            'initial_investment': 'sum',
            'current_value': 'sum',
            'absolute_return': 'sum',
            'return_percentage': 'mean',
            'annualized_return': 'mean'
        }).sort_values('absolute_return', ascending=False)
        
        geo_analysis['portfolio_percentage'] = (geo_analysis['initial_investment'] / 
                                               geo_analysis['initial_investment'].sum()) * 100
        
        return geo_analysis
    
    def calculate_portfolio_concentration(self):
        """
        Calculate concentration metrics for the portfolio.
        
        Returns:
            dict: Dictionary containing concentration metrics
        """
        df = self.portfolio.copy()
        
        # Calculate Herfindahl-Hirschman Index (HHI) for sector concentration
        sector_shares = df.groupby('sector')['initial_investment'].sum() / df['initial_investment'].sum()
        hhi_sector = (sector_shares ** 2).sum() * 10000
        
        # Calculate HHI for geography concentration
        geo_shares = df.groupby('country')['initial_investment'].sum() / df['initial_investment'].sum()
        hhi_geo = (geo_shares ** 2).sum() * 10000
        
        # Calculate top 5 investments concentration
        top5_concentration = (df.nlargest(5, 'initial_investment')['initial_investment'].sum() / 
                             df['initial_investment'].sum()) * 100
        
        return {
            'sector_hhi': hhi_sector,
            'geography_hhi': hhi_geo,
            'top5_concentration': top5_concentration
        }
    
    def calculate_portfolio_performance(self):
        """
        Calculate overall portfolio performance metrics.
        
        Returns:
            dict: Dictionary containing portfolio performance metrics
        """
        df = self.calculate_returns()
        
        total_investment = df['initial_investment'].sum()
        total_value = df['current_value'].sum()
        total_return = total_value - total_investment
        total_return_pct = (total_return / total_investment) * 100
        
        # Calculate weighted average annualized return
        weighted_annualized = np.average(
            df['annualized_return'], 
            weights=df['initial_investment']
        )
        
        # Calculate IRR (simplified approximation)
        cash_flows = [-df['initial_investment'].sum()]
        current_value = df['current_value'].sum()
        holding_period = df['holding_period_years'].mean()
        irr = ((current_value / total_investment) ** (1 / holding_period) - 1) * 100
        
        return {
            'total_investment': total_investment,
            'total_current_value': total_value,
            'total_return': total_return,
            'total_return_percentage': total_return_pct,
            'weighted_annualized_return': weighted_annualized,
            'approximate_irr': irr
        }
    
    def generate_performance_report(self):
        """
        Generate a comprehensive performance report for the portfolio.
        
        Returns:
            dict: Dictionary containing all performance metrics
        """
        return {
            'portfolio_performance': self.calculate_portfolio_performance(),
            'sector_analysis': self.analyze_by_sector(),
            'stage_analysis': self.analyze_by_stage(),
            'geography_analysis': self.analyze_by_geography(),
            'concentration_metrics': self.calculate_portfolio_concentration()
        }
    
    def plot_sector_allocation(self):
        """
        Plot a pie chart showing sector allocation of the portfolio.
        """
        sector_allocation = self.portfolio.groupby('sector')['initial_investment'].sum()
        plt.figure(figsize=(10, 8))
        sector_allocation.plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            title='Portfolio Sector Allocation'
        )
        plt.ylabel('')
        plt.show()
    
    def plot_performance_by_sector(self):
        """
        Plot a bar chart showing performance by sector.
        """
        sector_perf = self.analyze_by_sector()
        plt.figure(figsize=(12, 6))
        sns.barplot(
            x=sector_perf.index,
            y='return_percentage',
            data=sector_perf,
            palette='viridis'
        )
        plt.title('Average Return Percentage by Sector')
        plt.xlabel('Sector')
        plt.ylabel('Return (%)')
        plt.xticks(rotation=45)
        plt.show()
    
    def plot_value_over_time(self, investment_name):
        """
        Plot the value trajectory of a specific investment.
        
        Args:
            investment_name (str): Name of the investment to plot
        """
        # This is a placeholder - in a real implementation
