"""
Generated Code Metadata:
========================
Original URL: https://halo-orb.pages.dev
Prompt: Generate code to visualize portfolio performance data using intuitive charts and graphs, as described in HALO's analytics features.
Generated: DETERMINISTIC_2b878aa44fdf9784
Batch ID: 20250622_210348
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
from typing import List, Dict, Optional
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class PortfolioVisualizer:
    """
    A class to visualize portfolio performance data with various charts and graphs.
    """
    
    def __init__(self, portfolio_data: pd.DataFrame):
        """
        Initialize the PortfolioVisualizer with portfolio data.
        
        Args:
            portfolio_data (pd.DataFrame): DataFrame containing portfolio performance data.
                                          Expected columns: ['date', 'value', 'returns', 'benchmark', 'sector']
        """
        self.data = portfolio_data
        self._validate_data()
        
    def _validate_data(self) -> None:
        """
        Validate the input data structure and content.
        Raises ValueError if data doesn't meet requirements.
        """
        required_columns = {'date', 'value', 'returns'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        if self.data.isnull().values.any():
            raise ValueError("Data contains null values")
            
        try:
            self.data['date'] = pd.to_datetime(self.data['date'])
        except ValueError:
            raise ValueError("Date column must be convertible to datetime")
            
    def plot_value_over_time(self, title: str = "Portfolio Value Over Time") -> go.Figure:
        """
        Create a line chart showing portfolio value over time.
        
        Args:
            title (str): Chart title
            
        Returns:
            go.Figure: Plotly figure object
        """
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=self.data['date'],
            y=self.data['value'],
            mode='lines',
            name='Portfolio Value',
            line=dict(color='royalblue', width=2)
        ))
        
        if 'benchmark' in self.data.columns:
            fig.add_trace(go.Scatter(
                x=self.data['date'],
                y=self.data['benchmark'],
                mode='lines',
                name='Benchmark',
                line=dict(color='gray', width=1, dash='dot')
            ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Date',
            yaxis_title='Value',
            hovermode='x unified',
            template='plotly_white'
        )
        
        return fig
    
    def plot_returns_distribution(self, bins: int = 30, title: str = "Returns Distribution") -> go.Figure:
        """
        Create a histogram showing the distribution of portfolio returns.
        
        Args:
            bins (int): Number of bins for histogram
            title (str): Chart title
            
        Returns:
            go.Figure: Plotly figure object
        """
        fig = go.Figure()
        
        fig.add_trace(go.Histogram(
            x=self.data['returns'],
            nbinsx=bins,
            name='Returns',
            marker_color='royalblue',
            opacity=0.75
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Returns',
            yaxis_title='Frequency',
            bargap=0.1,
            template='plotly_white'
        )
        
        return fig
    
    def plot_cumulative_returns(self, title: str = "Cumulative Returns") -> go.Figure:
        """
        Create a line chart showing cumulative returns over time.
        
        Args:
            title (str): Chart title
            
        Returns:
            go.Figure: Plotly figure object
        """
        cumulative_returns = (1 + self.data['returns']).cumprod() - 1
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=self.data['date'],
            y=cumulative_returns,
            mode='lines',
            name='Portfolio',
            line=dict(color='royalblue', width=2)
        ))
        
        if 'benchmark' in self.data.columns:
            benchmark_cumulative = (1 + self.data['benchmark']).cumprod() - 1
            fig.add_trace(go.Scatter(
                x=self.data['date'],
                y=benchmark_cumulative,
                mode='lines',
                name='Benchmark',
                line=dict(color='gray', width=1, dash='dot')
            ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Date',
            yaxis_title='Cumulative Returns',
            hovermode='x unified',
            template='plotly_white'
        )
        
        return fig
    
    def plot_drawdown(self, title: str = "Portfolio Drawdown") -> go.Figure:
        """
        Create a line chart showing portfolio drawdown over time.
        
        Args:
            title (str): Chart title
            
        Returns:
            go.Figure: Plotly figure object
        """
        cumulative_returns = (1 + self.data['returns']).cumprod()
        peak = cumulative_returns.cummax()
        drawdown = (cumulative_returns - peak) / peak
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=self.data['date'],
            y=drawdown,
            mode='lines',
            name='Drawdown',
            line=dict(color='red', width=2),
            fill='tozeroy',
            fillcolor='rgba(255, 0, 0, 0.2)'
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Date',
            yaxis_title='Drawdown',
            hovermode='x',
            template='plotly_white',
            yaxis_tickformat=".1%"
        )
        
        return fig
    
    def plot_sector_allocation(self, title: str = "Sector Allocation") -> go.Figure:
        """
        Create a pie chart showing sector allocation (if sector data exists).
        
        Args:
            title (str): Chart title
            
        Returns:
            go.Figure: Plotly figure object
        """
        if 'sector' not in self.data.columns:
            raise ValueError("Sector data not available in portfolio data")
            
        sector_counts = self.data['sector'].value_counts()
        
        fig = go.Figure()
        
        fig.add_trace(go.Pie(
            labels=sector_counts.index,
            values=sector_counts.values,
            hole=0.3,
            marker_colors=plt.cm.Paired.colors
        ))
        
        fig.update_layout(
            title=title,
            template='plotly_white'
        )
        
        return fig
    
    def plot_rolling_volatility(self, window: int = 21, title: str = "Rolling Volatility") -> go.Figure:
        """
        Create a line chart showing rolling volatility.
        
        Args:
            window (int): Rolling window size in days
            title (str): Chart title
            
        Returns:
            go.Figure: Plotly figure object
        """
        rolling_vol = self.data['returns'].rolling(window=window).std() * np.sqrt(252)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=self.data['date'],
            y=rolling_vol,
            mode='lines',
            name='Volatility',
            line=dict(color='purple', width=2)
        ))
        
        fig.update_layout(
            title=f"{title} ({window}-day window)",
            xaxis_title='Date',
            yaxis_title='Annualized Volatility',
            hovermode='x',
            template='plotly_white',
            yaxis_tickformat=".1%"
        )
        
        return fig
    
    def create_dashboard(self) -> go.Figure:
        """
        Create a comprehensive dashboard with multiple portfolio visualizations.
        
        Returns:
            go.Figure: Plotly figure object with subplots
        """
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=(
                "Portfolio Value Over Time",
                "Cumulative Returns",
                "Drawdown Analysis",
                "Returns Distribution",
                "Rolling Volatility (21-day)",
                "Sector Allocation" if 'sector' in self.data.columns else ""
            ),
            specs=[
                [{"type": "xy"}, {"type": "xy"}],
                [{"type": "xy"}, {"type": "xy"}],
                [{"type": "xy"}, {"type": "domain" if 'sector' in self.data.columns else "xy"}]
            ]
        )
        
        # Portfolio Value
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=self.data['value'],
                mode='lines',
                name='Portfolio Value',
                line=dict(color='royalblue', width=2)
            ),
            row=1, col=1
        )
        
        # Cumulative Returns
        cumulative_returns = (1 + self.data['returns']).cumprod() - 1
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=cumulative_returns,
                mode='lines',
                name='Portfolio Returns',
                line
