"""
Generated Code Metadata:
========================
Original URL: https://battlebarkers.app
Prompt: Write a code snippet to visualize the performance of a portfolio using a library like Matplotlib or Seaborn.
Generated: DETERMINISTIC_fe0e3ad86dfbc577
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def visualize_portfolio_performance(
    portfolio_values: pd.Series,
    benchmark_values: pd.Series = None,
    title: str = "Portfolio Performance",
    xlabel: str = "Date",
    ylabel: str = "Value",
    figsize: tuple = (12, 6),
    grid: bool = True,
    style: str = "seaborn"
) -> plt.Figure:
    """
    Visualize portfolio performance over time with optional benchmark comparison.

    Args:
        portfolio_values: Pandas Series with dates as index and portfolio values.
        benchmark_values: Optional Pandas Series with benchmark values for comparison.
        title: Title of the plot.
        xlabel: Label for the x-axis.
        ylabel: Label for the y-axis.
        figsize: Tuple specifying figure size (width, height).
        grid: Boolean to show grid lines.
        style: Matplotlib style to use.

    Returns:
        matplotlib.figure.Figure: The generated figure object.
    """
    plt.style.use(style)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot portfolio values
    portfolio_values.plot(ax=ax, label="Portfolio", linewidth=2)
    
    # Plot benchmark if provided
    if benchmark_values is not None:
        benchmark_values.plot(ax=ax, label="Benchmark", linestyle="--", linewidth=2)
    
    # Calculate and plot cumulative returns if data is numeric
    if pd.api.types.is_numeric_dtype(portfolio_values):
        ax2 = ax.twinx()
        cumulative_returns = (portfolio_values / portfolio_values.iloc[0] - 1) * 100
        cumulative_returns.plot(
            ax=ax2, 
            color="green", 
            alpha=0.3, 
            label="Cumulative Return %"
        )
        ax2.set_ylabel("Cumulative Return (%)")
        ax2.legend(loc="upper right")
    
    # Formatting
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc="upper left")
    
    if grid:
        ax.grid(True, linestyle="--", alpha=0.6)
    
    fig.tight_layout()
    return fig

# Example usage
if __name__ == "__main__":
    # Generate sample data
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    portfolio = np.cumprod(1 + np.random.normal(0.001, 0.02, len(dates))) * 100
    benchmark = np.cumprod(1 + np.random.normal(0.0008, 0.015, len(dates))) * 100
    
    portfolio_series = pd.Series(portfolio, index=dates, name="Portfolio")
    benchmark_series = pd.Series(benchmark, index=dates, name="Benchmark")
    
    # Visualize
    fig = visualize_portfolio_performance(
        portfolio_series,
        benchmark_series,
        title="Portfolio vs Benchmark Performance",
        ylabel="Portfolio Value ($)"
    )
    plt.show()
```
