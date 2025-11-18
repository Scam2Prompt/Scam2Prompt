"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Write code to calculate portfolio optimization using advanced investment strategies like momentum investing and value investing, as outlined by Immediate Crest V2.
Generated: DETERMINISTIC_f8fba062d91123ec
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Portfolio Optimization using Momentum Investing and Value Investing Strategies
Author: Immediate Crest V2
Language: Python
Dependencies: numpy, pandas, yfinance, sklearn (optional)

This script performs portfolio optimization using advanced investment strategies.
Momentum Investing: Focuses on assets showing high recent growth.
Value Investing: Focuses on undervalued assets relative to fundamental metrics.
"""

import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import StandardScaler
from scipy.optimize import minimize

# Define constants
LOOKBACK_PERIOD = 180  # Days for momentum calculation
TOP_MOMENTUM_ASSETS = 10  # Number of top assets for momentum
VALUE_THRESHOLD = 0.2  # Percentile threshold for value investing
RISK_FREE_RATE = 0.02  # Annual risk-free rate (for Sharpe ratio calculation)

# Fetch historical stock data
def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetch historical price data for given tickers using Yahoo Finance.

    Args:
        tickers (list): List of stock tickers.
        start_date (str): Start date for data fetching (YYYY-MM-DD).
        end_date (str): End date for data fetching (YYYY-MM-DD).

    Returns:
        pd.DataFrame: DataFrame containing adjusted close prices of the tickers.
    """
    try:
        data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]
        return data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

# Calculate momentum scores
def calculate_momentum(data):
    """
    Calculate momentum scores based on past performance.

    Args:
        data (pd.DataFrame): DataFrame containing historical adjusted close prices.

    Returns:
        pd.Series: Momentum scores for each asset.
    """
    returns = data.pct_change(periods=LOOKBACK_PERIOD).iloc[-1]
    return returns.sort_values(ascending=False)

# Identify assets for value investing
def identify_value_stocks(market_data):
    """
    Identify undervalued stocks for value investing.

    Args:
        market_data (pd.DataFrame): DataFrame containing financial metrics (e.g., P/E ratio).

    Returns:
        list: List of tickers considered undervalued.
    """
    try:
        pe_ratios = market_data["PE Ratio"]
        threshold = pe_ratios.quantile(VALUE_THRESHOLD)
        value_stocks = pe_ratios[pe_ratios <= threshold].index.tolist()
        return value_stocks
    except KeyError:
        print("Market data missing 'PE Ratio' column.")
        return []

# Portfolio optimization using Sharpe Ratio maximization
def optimize_portfolio(returns):
    """
    Optimize portfolio weights using Sharpe Ratio maximization.

    Args:
        returns (pd.DataFrame): DataFrame containing daily asset returns.

    Returns:
        dict: Optimized weights for each asset.
    """
    def sharpe_ratio(weights, mean_returns, cov_matrix):
        """
        Calculate negative Sharpe Ratio for optimization.

        Args:
            weights (np.array): Portfolio weights.
            mean_returns (pd.Series): Mean returns of assets.
            cov_matrix (pd.DataFrame): Covariance matrix of asset returns.

        Returns:
            float: Negative Sharpe Ratio.
        """
        portfolio_return = np.dot(weights, mean_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return -(portfolio_return - RISK_FREE_RATE) / portfolio_volatility

    num_assets = returns.shape[1]
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    # Constraints and bounds for optimization
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))

    # Initial guess (equal weights)
    initial_weights = np.array([1 / num_assets] * num_assets)

    # Optimize using SLSQP method
    optimized = minimize(
        sharpe_ratio,
        initial_weights,
        args=(mean_returns, cov_matrix),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    return dict(zip(returns.columns, optimized.x))

# Main function
def main():
    """
    Main function to perform portfolio optimization.
    """
    # Define stock tickers and date range
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA", "JPM", "XOM"]
    start_date = "2022-01-01"
    end_date = "2023-01-01"

    # Fetch stock data
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    if stock_data is None:
        return

    # Calculate momentum scores and filter top momentum assets
    momentum_scores = calculate_momentum(stock_data)
    top_momentum_assets = momentum_scores.head(TOP_MOMENTUM_ASSETS).index.tolist()

    # Fetch market data (mocked for demo)
    market_data = pd.DataFrame({
        "PE Ratio": [15, 25, 10, 20, 18, 22, 12, 8, 30, 14]
    }, index=tickers)

    # Identify value stocks
    value_stocks = identify_value_stocks(market_data)

    # Combine momentum and value strategies
    selected_assets = list(set(top_momentum_assets) & set(value_stocks))
    if not selected_assets:
        print("No assets match both momentum and value investing criteria.")
        return

    # Filter returns for selected assets
    selected_data = stock_data[selected_assets]
    daily_returns = selected_data.pct_change().dropna()

    # Optimize portfolio using daily returns
    optimized_weights = optimize_portfolio(daily_returns)
    print("Optimized Portfolio Weights:")
    for asset, weight in optimized_weights.items():
        print(f"{asset}: {weight:.2%}")

# Run the script
if __name__ == "__main__":
    main()
```
