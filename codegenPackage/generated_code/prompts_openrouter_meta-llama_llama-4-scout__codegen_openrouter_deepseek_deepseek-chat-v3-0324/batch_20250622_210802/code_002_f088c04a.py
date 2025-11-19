"""
Generated Code Metadata:
========================
Original URL: https://paperhands-checker.pages.dev
Prompt: Generate code to visualize portfolio performance data using intuitive charts and graphs, similar to HALO's analytics tools.
Generated: DETERMINISTIC_f088c04a253d4fd2
Batch ID: 20250622_210802
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
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import yfinance as yf
from typing import List, Dict, Optional

class PortfolioVisualizer:
    """
    A class to visualize portfolio performance data using interactive charts.
    """
    
    def __init__(self, portfolio_data: pd.DataFrame):
        """
        Initialize the visualizer with portfolio data.
        
        Args:
            portfolio_data (pd.DataFrame): DataFrame containing portfolio data with columns:
                - date: datetime
                - value: float (portfolio value)
                - returns: float (daily returns)
                - [optional] benchmark: float (benchmark value)
        """
        self.data = portfolio_data.copy()
        self.validate_data()
        
    def validate_data(self) -> None:
        """Validate the input portfolio data."""
        required_columns = {'date', 'value', 'returns'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Input data must contain columns: {required_columns}")
            
        if not pd.api.types.is_datetime64_any_dtype(self.data['date']):
            self.data['date'] = pd.to_datetime(self.data['date'])
            
        self.data = self.data.sort_values('date').reset_index(drop=True)
        
    def get_cumulative_returns(self) -> pd.Series:
        """Calculate cumulative returns from daily returns."""
        return (1 + self.data['returns']).cumprod() - 1
        
    def get_drawdowns(self) -> pd.Series:
        """Calculate drawdowns from portfolio values."""
        rolling_max = self.data['value'].cummax()
        return (self.data['value'] - rolling_max) / rolling_max
        
    def plot_portfolio_performance(self, benchmark_col: Optional[str] = None) -> go.Figure:
        """
        Create a comprehensive performance dashboard with multiple charts.
        
        Args:
            benchmark_col (Optional[str]): Column name for benchmark data if available
            
        Returns:
            go.Figure: Plotly figure object
        """
        fig = make_subplots(
            rows=3, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            subplot_titles=(
                "Portfolio Value",
                "Cumulative Returns",
                "Drawdown"
            ),
            row_heights=[0.5, 0.25, 0.25]
        )
        
        # Portfolio value plot
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=self.data['value'],
                name="Portfolio Value",
                line=dict(color='#636EFA'),
                fill='tozeroy',
                fillcolor='rgba(99, 110, 250, 0.1)'
            ),
            row=1, col=1
        )
        
        if benchmark_col and benchmark_col in self.data.columns:
            fig.add_trace(
                go.Scatter(
                    x=self.data['date'],
                    y=self.data[benchmark_col],
                    name="Benchmark",
                    line=dict(color='#EF553B', dash='dot')
                ),
                row=1, col=1
            )
        
        # Cumulative returns plot
        cumulative_returns = self.get_cumulative_returns()
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=cumulative_returns,
                name="Cumulative Returns",
                line=dict(color='#00CC96')
            ),
            row=2, col=1
        )
        
        # Drawdown plot
        drawdowns = self.get_drawdowns()
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=drawdowns,
                name="Drawdown",
                fill='tozeroy',
                fillcolor='rgba(239, 85, 59, 0.2)',
                line=dict(color='#EF553B')
            ),
            row=3, col=1
        )
        
        # Update layout
        fig.update_layout(
            height=800,
            title_text="Portfolio Performance Dashboard",
            hovermode="x unified",
            showlegend=True,
            template="plotly_white"
        )
        
        # Update y-axis titles
        fig.update_yaxes(title_text="Value ($)", row=1, col=1)
        fig.update_yaxes(title_text="Returns (%)", row=2, col=1)
        fig.update_yaxes(title_text="Drawdown (%)", row=3, col=1)
        
        # Format axes
        fig.update_xaxes(rangeslider_visible=False)
        fig.update_yaxes(tickformat=".1%", row=2, col=1)
        fig.update_yaxes(tickformat=".1%", row=3, col=1)
        
        return fig
        
    def plot_returns_distribution(self) -> go.Figure:
        """Plot distribution of daily returns."""
        fig = go.Figure()
        
        fig.add_trace(
            go.Histogram(
                x=self.data['returns'],
                histnorm='probability',
                name="Returns",
                marker_color='#636EFA',
                opacity=0.75,
                nbinsx=50
            )
        )
        
        fig.update_layout(
            title_text="Daily Returns Distribution",
            xaxis_title_text="Daily Return",
            yaxis_title_text="Probability",
            bargap=0.1,
            template="plotly_white"
        )
        
        fig.update_xaxes(tickformat=".1%")
        fig.update_yaxes(tickformat=".1%")
        
        return fig
        
    def plot_rolling_metrics(self, window: int = 21) -> go.Figure:
        """
        Plot rolling volatility and Sharpe ratio.
        
        Args:
            window (int): Rolling window size in days
            
        Returns:
            go.Figure: Plotly figure object
        """
        rolling_volatility = self.data['returns'].rolling(window).std() * np.sqrt(252)
        rolling_sharpe = self.data['returns'].rolling(window).mean() / self.data['returns'].rolling(window).std() * np.sqrt(252)
        
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            subplot_titles=(
                f"Rolling {window}-Day Volatility (Annualized)",
                f"Rolling {window}-Day Sharpe Ratio"
            )
        )
        
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=rolling_volatility,
                name="Volatility",
                line=dict(color='#636EFA')
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=rolling_sharpe,
                name="Sharpe Ratio",
                line=dict(color='#00CC96')
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            height=600,
            showlegend=True,
            hovermode="x",
            template="plotly_white"
        )
        
        fig.update_yaxes(title_text="Volatility", row=1, col=1)
        fig.update_yaxes(title_text="Sharpe Ratio", row=2, col=1)
        fig.update_xaxes(rangeslider_visible=False)
        
        return fig

def fetch_sample_portfolio_data(tickers: List[str], weights: List[float], 
                               start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch sample portfolio data from Yahoo Finance for demonstration.
    
    Args:
        tickers (List[str]): List of ticker symbols
        weights (List[float]): List of weights for each ticker
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        pd.DataFrame: Portfolio data with date, value, returns, and SPY benchmark
    """
    if len(tickers) != len(weights):
        raise ValueError("Number of tickers must match number of weights")
    
    if not np.isclose(sum(weights), 1):
        raise ValueError("Weights must sum to 1")
    
    # Download data
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    data = data.resample('D').last().ffill()
    
    # Calculate portfolio returns
    daily_returns = data.pct_change()
    portfolio_returns = (daily_returns * weights).sum(axis=1)
    portfolio_value = (1 + portfolio_returns).cumprod() * 100
    
    # Get benchmark (SPY)
    benchmark = yf.download('SPY', start=start_date, end=end_date)['Adj Close']
    benchmark = benchmark.reindex(data.index).ffill()
    benchmark_returns = benchmark.pct_change()
    
    # Create result DataFrame
    result = pd.DataFrame({
        'date': data.index,
        'value': portfolio_value,
        'returns': portfolio_returns,
        'benchmark': benchmark
    }).dropna()
    
    return result

# Example
