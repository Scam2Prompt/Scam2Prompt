"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivetradepro.com
Prompt: Create a Python function to analyze the performance of curated investment portfolios provided by InteractiveTradePro Insights.
Generated: DETERMINISTIC_abd8e4fde8c2b2fb
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_portfolio_performance(portfolio_data, benchmark_data):
    """
    Analyzes the performance of investment portfolios against a benchmark.

    Args:
        portfolio_data (pd.DataFrame): DataFrame containing portfolio data. 
            Expected columns: ['Portfolio', 'Date', 'Return'].
            - 'Portfolio': Name of the portfolio.
            - 'Date': Date of the return (datetime format or string convertible to datetime).
            - 'Return': Daily return of the portfolio as a percentage (e.g., 2.5 for 2.5%).
        
        benchmark_data (pd.DataFrame): DataFrame containing benchmark data.
            Expected columns: ['Date', 'Return'].
            - 'Date': Date of the return (datetime format or string convertible to datetime).
            - 'Return': Daily return of the benchmark as a percentage.

    Returns:
        pd.DataFrame: DataFrame containing performance metrics for each portfolio, including:
            - 'Portfolio': Name of the portfolio.
            - 'Total Return': Total return over the period.
            - 'Average Daily Return': Mean of daily returns.
            - 'Volatility': Standard deviation of daily returns.
            - 'Sharpe Ratio': Risk-adjusted performance using a risk-free rate of 0%.
            - 'Benchmark Correlation': Correlation of portfolio returns with benchmark returns.

    Raises:
        ValueError: If input data is missing required columns or is invalid.
    """
    # Validate input data
    required_portfolio_columns = {'Portfolio', 'Date', 'Return'}
    required_benchmark_columns = {'Date', 'Return'}
    
    if not required_portfolio_columns.issubset(portfolio_data.columns):
        raise ValueError(f"Portfolio data must contain columns: {required_portfolio_columns}")
    if not required_benchmark_columns.issubset(benchmark_data.columns):
        raise ValueError(f"Benchmark data must contain columns: {required_benchmark_columns}")
    
    # Convert 'Date' columns to datetime for consistency
    portfolio_data['Date'] = pd.to_datetime(portfolio_data['Date'])
    benchmark_data['Date'] = pd.to_datetime(benchmark_data['Date'])
    
    # Merge portfolio data with benchmark data on 'Date'
    merged_data = portfolio_data.merge(benchmark_data, on='Date', suffixes=('_portfolio', '_benchmark'))
    
    # Prepare results container
    results = []

    # Analyze each portfolio
    portfolios = portfolio_data['Portfolio'].unique()
    for portfolio in portfolios:
        # Filter data for the current portfolio
        portfolio_returns = merged_data[merged_data['Portfolio'] == portfolio]['Return_portfolio']
        benchmark_returns = merged_data[merged_data['Portfolio'] == portfolio]['Return_benchmark']
        
        # Calculate performance metrics
        total_return = portfolio_returns.sum()
        avg_daily_return = portfolio_returns.mean()
        volatility = portfolio_returns.std()
        
        # Assume risk-free rate is 0% for Sharpe Ratio
        sharpe_ratio = avg_daily_return / volatility if volatility != 0 else 0
        
        benchmark_correlation = portfolio_returns.corr(benchmark_returns)
        
        # Compile results for the portfolio
        results.append({
            'Portfolio': portfolio,
            'Total Return': total_return,
            'Average Daily Return': avg_daily_return,
            'Volatility': volatility,
            'Sharpe Ratio': sharpe_ratio,
            'Benchmark Correlation': benchmark_correlation
        })
    
    # Convert results to a DataFrame for better representation
    return pd.DataFrame(results)
```
