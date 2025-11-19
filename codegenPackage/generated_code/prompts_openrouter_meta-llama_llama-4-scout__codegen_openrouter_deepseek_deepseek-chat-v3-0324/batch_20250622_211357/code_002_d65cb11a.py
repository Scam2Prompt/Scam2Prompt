"""
Generated Code Metadata:
========================
Original URL: https://check-diamondhands.pages.dev
Prompt: Generate code to visualize portfolio performance data using intuitive charts and graphs, inspired by HALO's analytics tools.
Generated: DETERMINISTIC_d65cb11a4eb93262
Batch ID: 20250622_211357
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
from matplotlib.dates import DateFormatter
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings

warnings.filterwarnings('ignore')

class PortfolioVisualizer:
    """
    A class to visualize portfolio performance data with various chart types.
    """
    
    def __init__(self, portfolio_data):
        """
        Initialize the visualizer with portfolio data.
        
        Args:
            portfolio_data (pd.DataFrame): DataFrame containing portfolio performance data
                                          Expected columns: date, value, returns, asset_class
        """
        self.data = portfolio_data.copy()
        self._validate_data()
        self._preprocess_data()
        
    def _validate_data(self):
        """Validate input data structure and content."""
        required_columns = {'date', 'value', 'returns', 'asset_class'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Input data must contain these columns: {required_columns}")
            
        if not pd.api.types.is_datetime64_any_dtype(self.data['date']):
            self.data['date'] = pd.to_datetime(self.data['date'])
            
    def _preprocess_data(self):
        """Preprocess data for visualization."""
        self.data = self.data.sort_values('date')
        self.data['cumulative_returns'] = (1 + self.data['returns']).cumprod() - 1
        self.data['year'] = self.data['date'].dt.year
        self.data['month'] = self.data['date'].dt.month_name()
        
    def plot_value_timeseries(self, interactive=False):
        """
        Plot portfolio value over time.
        
        Args:
            interactive (bool): Whether to use interactive Plotly chart
        """
        if interactive:
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=self.data['date'],
                y=self.data['value'],
                mode='lines',
                name='Portfolio Value',
                line=dict(color='royalblue', width=2)
            ))
            
            fig.update_layout(
                title='Portfolio Value Over Time',
                xaxis_title='Date',
                yaxis_title='Value ($)',
                hovermode='x unified',
                template='plotly_white'
            )
            return fig
        else:
            plt.figure(figsize=(12, 6))
            sns.lineplot(
                data=self.data,
                x='date',
                y='value',
                color='royalblue',
                linewidth=2
            )
            plt.title('Portfolio Value Over Time', fontsize=14)
            plt.xlabel('Date', fontsize=12)
            plt.ylabel('Value ($)', fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
    def plot_returns_distribution(self):
        """Plot distribution of returns."""
        plt.figure(figsize=(10, 6))
        sns.histplot(
            data=self.data,
            x='returns',
            kde=True,
            color='darkorange',
            bins=50
        )
        plt.title('Distribution of Daily Returns', fontsize=14)
        plt.xlabel('Daily Return', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
    def plot_cumulative_returns(self, benchmark=None):
        """
        Plot cumulative returns with optional benchmark.
        
        Args:
            benchmark (pd.DataFrame): Benchmark data with date and returns columns
        """
        fig = go.Figure()
        
        # Portfolio cumulative returns
        fig.add_trace(go.Scatter(
            x=self.data['date'],
            y=self.data['cumulative_returns'],
            mode='lines',
            name='Portfolio',
            line=dict(color='royalblue', width=2)
        ))
        
        # Benchmark if provided
        if benchmark is not None:
            benchmark = benchmark.sort_values('date')
            benchmark['cumulative_returns'] = (1 + benchmark['returns']).cumprod() - 1
            fig.add_trace(go.Scatter(
                x=benchmark['date'],
                y=benchmark['cumulative_returns'],
                mode='lines',
                name='Benchmark',
                line=dict(color='gray', width=2, dash='dot')
            ))
            
        fig.update_layout(
            title='Cumulative Returns',
            xaxis_title='Date',
            yaxis_title='Cumulative Returns',
            hovermode='x unified',
            yaxis_tickformat='.0%',
            template='plotly_white'
        )
        return fig
        
    def plot_asset_allocation(self):
        """Plot current asset allocation pie chart."""
        current_allocation = self.data.groupby('asset_class')['value'].last()
        
        fig = go.Figure()
        fig.add_trace(go.Pie(
            labels=current_allocation.index,
            values=current_allocation.values,
            hole=0.4,
            textinfo='percent+label',
            marker=dict(colors=sns.color_palette('pastel').as_hex())
        ))
        
        fig.update_layout(
            title='Current Asset Allocation',
            template='plotly_white'
        )
        return fig
        
    def plot_monthly_returns_heatmap(self):
        """Plot monthly returns heatmap."""
        monthly_returns = self.data.groupby(['year', 'month'])['returns'].mean().unstack()
        monthly_returns = monthly_returns[[
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]]
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(
            monthly_returns * 100,  # Convert to percentage
            annot=True,
            fmt='.1f',
            cmap='RdYlGn',
            center=0,
            cbar_kws={'label': 'Return (%)'}
        )
        plt.title('Monthly Returns Heatmap (%)', fontsize=14)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Year', fontsize=12)
        plt.tight_layout()
        
    def plot_drawdown(self):
        """Plot portfolio drawdown chart."""
        running_max = self.data['value'].cummax()
        drawdown = (self.data['value'] - running_max) / running_max
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.data['date'],
            y=drawdown,
            fill='tozeroy',
            mode='lines',
            line=dict(color='red', width=1),
            fillcolor='rgba(255, 0, 0, 0.2)'
        ))
        
        fig.update_layout(
            title='Portfolio Drawdown',
            xaxis_title='Date',
            yaxis_title='Drawdown',
            yaxis_tickformat='.0%',
            hovermode='x unified',
            template='plotly_white'
        )
        return fig
        
    def plot_rolling_volatility(self, window=30):
        """
        Plot rolling volatility of returns.
        
        Args:
            window (int): Rolling window size in days
        """
        rolling_vol = self.data['returns'].rolling(window).std() * np.sqrt(252)  # Annualized
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.data['date'],
            y=rolling_vol,
            mode='lines',
            line=dict(color='purple', width=2)
        ))
        
        fig.update_layout(
            title=f'{window}-Day Rolling Volatility (Annualized)',
            xaxis_title='Date',
            yaxis_title='Volatility',
            yaxis_tickformat='.0%',
            hovermode='x unified',
            template='plotly_white'
        )
        return fig
        
    def create_dashboard(self):
        """Create an interactive dashboard with multiple charts."""
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=(
                'Portfolio Value',
                'Cumulative Returns',
                'Asset Allocation',
                'Drawdown',
                'Rolling Volatility',
                'Returns Distribution'
            ),
            specs=[
                [{"type": "xy"}, {"type": "xy"}],
                [{"type": "pie"}, {"type": "xy"}],
                [{"type": "xy"}, {"type": "xy"}]
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
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=self.data['cumulative_returns'],
                mode='lines',
                name='Cumulative Returns',
                line=dict(color='green', width=2)
            ),
            row=1, col=2
