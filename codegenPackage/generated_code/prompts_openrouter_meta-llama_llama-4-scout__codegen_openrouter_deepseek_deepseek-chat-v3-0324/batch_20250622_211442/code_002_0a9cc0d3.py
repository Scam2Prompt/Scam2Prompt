"""
Generated Code Metadata:
========================
Original URL: https://paperhanded-checker.pages.dev
Prompt: Generate code to visualize portfolio performance data using intuitive charts and graphs, inspired by Halo's analytics tools.
Generated: DETERMINISTIC_0a9cc0d3247b1904
Batch ID: 20250622_211442
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
from datetime import datetime
import numpy as np
from typing import List, Dict, Optional

# Set the style for the visualizations
sns.set_style("whitegrid")
plt.style.use('seaborn')

class PortfolioVisualizer:
    """
    A class to visualize portfolio performance data with various charts and graphs.
    Inspired by Halo's analytics tools.
    """

    def __init__(self, portfolio_data: pd.DataFrame):
        """
        Initialize the PortfolioVisualizer with portfolio data.

        Args:
            portfolio_data (pd.DataFrame): DataFrame containing portfolio performance data.
                                          Expected columns: 'date', 'value', 'returns', 'asset'
        """
        self.portfolio_data = portfolio_data.copy()
        self._validate_data()

    def _validate_data(self) -> None:
        """
        Validate the input data to ensure required columns are present.
        Raises ValueError if data is invalid.
        """
        required_columns = {'date', 'value', 'returns', 'asset'}
        if not required_columns.issubset(self.portfolio_data.columns):
            missing = required_columns - set(self.portfolio_data.columns)
            raise ValueError(f"Missing required columns: {missing}")

        # Convert date column to datetime if it's not already
        if not pd.api.types.is_datetime64_any_dtype(self.portfolio_data['date']):
            self.portfolio_data['date'] = pd.to_datetime(self.portfolio_data['date'])

    def plot_portfolio_growth(self, title: str = "Portfolio Growth Over Time") -> plt.Figure:
        """
        Plot the portfolio value over time.

        Args:
            title (str): Title for the plot. Defaults to "Portfolio Growth Over Time".

        Returns:
            plt.Figure: The matplotlib figure object
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Aggregate data by date if there are multiple assets
        if 'asset' in self.portfolio_data.columns:
            data = self.portfolio_data.groupby('date')['value'].sum().reset_index()
        else:
            data = self.portfolio_data

        sns.lineplot(
            data=data,
            x='date',
            y='value',
            ax=ax,
            color='#4e79a7',
            linewidth=2.5
        )

        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Portfolio Value", fontsize=12)
        ax.tick_params(axis='both', which='major', labelsize=10)
        
        # Format y-axis as currency
        ax.yaxis.set_major_formatter('${x:,.0f}')
        
        plt.tight_layout()
        return fig

    def plot_returns_distribution(self, title: str = "Portfolio Returns Distribution") -> plt.Figure:
        """
        Plot the distribution of portfolio returns.

        Args:
            title (str): Title for the plot. Defaults to "Portfolio Returns Distribution".

        Returns:
            plt.Figure: The matplotlib figure object
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        sns.histplot(
            data=self.portfolio_data,
            x='returns',
            bins=30,
            kde=True,
            color='#59a14f',
            edgecolor='white',
            ax=ax
        )

        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel("Daily Returns (%)", fontsize=12)
        ax.set_ylabel("Frequency", fontsize=12)
        ax.tick_params(axis='both', which='major', labelsize=10)
        
        # Format x-axis as percentage
        ax.xaxis.set_major_formatter('{x:.1f}%')
        
        plt.tight_layout()
        return fig

    def plot_asset_allocation(self, date: Optional[str] = None, 
                            title: str = "Asset Allocation") -> plt.Figure:
        """
        Plot the current asset allocation of the portfolio.

        Args:
            date (Optional[str]): Specific date to show allocation for. 
                                If None, uses the most recent date. Defaults to None.
            title (str): Title for the plot. Defaults to "Asset Allocation".

        Returns:
            plt.Figure: The matplotlib figure object
        """
        if 'asset' not in self.portfolio_data.columns:
            raise ValueError("Asset allocation plot requires 'asset' column in data")

        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Get data for specific date or most recent date
        if date is not None:
            date = pd.to_datetime(date)
            data = self.portfolio_data[self.portfolio_data['date'] == date]
        else:
            recent_date = self.portfolio_data['date'].max()
            data = self.portfolio_data[self.portfolio_data['date'] == recent_date]

        # Calculate percentages
        total_value = data['value'].sum()
        data = data.assign(percentage=(data['value'] / total_value * 100))
        
        # Sort by value and take top 10 if too many assets
        data = data.sort_values('value', ascending=False)
        if len(data) > 10:
            other = data.iloc[10:]['value'].sum()
            data = data.iloc[:10]
            data = pd.concat([data, pd.DataFrame([{
                'asset': 'Other',
                'value': other,
                'percentage': other / total_value * 100
            }])])

        # Create pie chart
        colors = sns.color_palette("pastel", len(data))
        wedges, texts, autotexts = ax.pie(
            data['value'],
            labels=data['asset'],
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
            textprops={'fontsize': 10}
        )

        ax.set_title(title, fontsize=16, pad=20)
        
        # Equal aspect ratio ensures pie is drawn as a circle
        ax.axis('equal')  
        plt.tight_layout()
        return fig

    def plot_rolling_volatility(self, window: int = 21, 
                              title: str = "Rolling Portfolio Volatility") -> plt.Figure:
        """
        Plot rolling volatility of the portfolio.

        Args:
            window (int): Rolling window size in days. Defaults to 21 (monthly).
            title (str): Title for the plot. Defaults to "Rolling Portfolio Volatility".

        Returns:
            plt.Figure: The matplotlib figure object
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Calculate rolling standard deviation
        if 'asset' in self.portfolio_data.columns:
            daily_returns = self.portfolio_data.groupby('date')['returns'].sum()
        else:
            daily_returns = self.portfolio_data.set_index('date')['returns']
            
        rolling_vol = daily_returns.rolling(window=window).std() * np.sqrt(window)

        sns.lineplot(
            x=rolling_vol.index,
            y=rolling_vol.values,
            ax=ax,
            color='#e15759',
            linewidth=2.5
        )

        ax.set_title(title, fontsize=16, pad=20)
        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel(f"{window}-Day Rolling Volatility", fontsize=12)
        ax.tick_params(axis='both', which='major', labelsize=10)
        
        # Format y-axis as percentage
        ax.yaxis.set_major_formatter('{x:.1f}%')
        
        plt.tight_layout()
        return fig

    def plot_cumulative_returns(self, benchmark: Optional[pd.Series] = None,
                              title: str = "Cumulative Returns") -> plt.Figure:
        """
        Plot cumulative returns of the portfolio, optionally against a benchmark.

        Args:
            benchmark (Optional[pd.Series]): Benchmark returns series with datetime index.
            title (str): Title for the plot. Defaults to "Cumulative Returns".

        Returns:
            plt.Figure: The matplotlib figure object
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Calculate portfolio cumulative returns
        if 'asset' in self.portfolio_data.columns:
            daily_returns = self.portfolio_data.groupby('date')['returns'].sum() / 100
        else:
            daily_returns = self.portfolio_data.set_index('date')['returns'] / 100
            
        cum_returns = (1 + daily_returns).cumprod() - 1

        # Plot portfolio
        sns.lineplot(
            x=cum_returns.index,
            y=cum_returns.values,
            ax=ax,
            color='#4e79a7',
            linewidth=2.5,
            label='Portfolio'
        )

        # Plot benchmark if provided
        if benchmark
