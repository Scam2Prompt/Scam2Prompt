"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: Write code to estimate the impact of cryptocurrency exposure in the ARK Venture Fund, using historical Bitcoin Investment Trust (GBTC) data.
Generated: DETERMINISTIC_28df065f222dbcfa
Batch ID: 20250612_154131
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
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Constants
GBTC_TICKER = "GBTC"
START_DATE = "2020-01-01"
END_DATE = datetime.now().strftime("%Y-%m-%d")
RISK_FREE_RATE = 0.02  # Annual risk-free rate (2%)

def fetch_gbtc_data():
    """
    Fetch historical GBTC data from Yahoo Finance.
    Returns:
        pd.DataFrame: DataFrame with GBTC historical data
    """
    try:
        gbtc_data = yf.download(GBTC_TICKER, start=START_DATE, end=END_DATE)
        if gbtc_data.empty:
            raise ValueError("No data returned for GBTC")
        return gbtc_data
    except Exception as e:
        print(f"Error fetching GBTC data: {e}")
        return None

def calculate_daily_returns(data):
    """
    Calculate daily returns from price data.
    Args:
        data (pd.DataFrame): DataFrame with 'Adj Close' column
    Returns:
        pd.Series: Daily returns
    """
    if 'Adj Close' not in data.columns:
        raise ValueError("DataFrame must contain 'Adj Close' column")
    return data['Adj Close'].pct_change().dropna()

def calculate_metrics(returns):
    """
    Calculate key financial metrics from returns.
    Args:
        returns (pd.Series): Daily returns
    Returns:
        dict: Dictionary of calculated metrics
    """
    if returns.empty:
        raise ValueError("Returns data is empty")
    
    annualized_return = (1 + returns.mean()) ** 252 - 1
    annualized_volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = (annualized_return - RISK_FREE_RATE) / annualized_volatility
    
    return {
        'annualized_return': annualized_return,
        'annualized_volatility': annualized_volatility,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': (returns.cumsum().expanding().max() - returns.cumsum()).max()
    }

def analyze_correlation(fund_returns, gbtc_returns):
    """
    Analyze correlation between fund returns and GBTC returns.
    Args:
        fund_returns (pd.Series): Fund daily returns
        gbtc_returns (pd.Series): GBTC daily returns
    Returns:
        dict: Correlation metrics
    """
    if len(fund_returns) != len(gbtc_returns):
        raise ValueError("Return series must have same length")
    
    correlation, p_value = pearsonr(fund_returns, gbtc_returns)
    beta = np.cov(fund_returns, gbtc_returns)[0, 1] / np.var(gbtc_returns)
    
    return {
        'correlation': correlation,
        'p_value': p_value,
        'beta': beta
    }

def plot_performance(gbtc_data, fund_data=None):
    """
    Plot performance comparison between GBTC and optional fund data.
    Args:
        gbtc_data (pd.DataFrame): GBTC historical data
        fund_data (pd.DataFrame, optional): Fund historical data
    """
    plt.figure(figsize=(12, 6))
    
    # Normalize prices to 100 at start date for comparison
    norm_gbtc = (gbtc_data['Adj Close'] / gbtc_data['Adj Close'].iloc[0]) * 100
    plt.plot(norm_gbtc.index, norm_gbtc, label='GBTC', color='orange')
    
    if fund_data is not None and 'Adj Close' in fund_data.columns:
        norm_fund = (fund_data['Adj Close'] / fund_data['Adj Close'].iloc[0]) * 100
        plt.plot(norm_fund.index, norm_fund, label='ARK Venture Fund', color='blue')
    
    plt.title('Normalized Performance Comparison')
    plt.xlabel('Date')
    plt.ylabel('Normalized Price (Base 100)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def estimate_exposure_impact(gbtc_metrics, correlation_metrics):
    """
    Estimate impact of cryptocurrency exposure based on metrics.
    Args:
        gbtc_metrics (dict): GBTC performance metrics
        correlation_metrics (dict): Correlation metrics between fund and GBTC
    Returns:
        dict: Estimated impact metrics
    """
    exposure_impact = {
        'estimated_crypto_return_contribution': gbtc_metrics['annualized_return'] * correlation_metrics['beta'],
        'estimated_crypto_risk_contribution': gbtc_metrics['annualized_volatility'] * correlation_metrics['beta'],
        'crypto_beta': correlation_metrics['beta']
    }
    return exposure_impact

def main():
    """
    Main function to execute the analysis.
    """
    try:
        # Fetch GBTC data
        gbtc_data = fetch_gbtc_data()
        if gbtc_data is None:
            return
        
        # Calculate GBTC metrics
        gbtc_returns = calculate_daily_returns(gbtc_data)
        gbtc_metrics = calculate_metrics(gbtc_returns)
        
        print("\nGBTC Performance Metrics:")
        for metric, value in gbtc_metrics.items():
            print(f"{metric.replace('_', ' ').title()}: {value:.4f}")
        
        # Example fund data (replace with actual ARK Venture Fund data)
        # In a real implementation, you would fetch actual fund data here
        print("\nNote: Using simulated fund data for demonstration")
        np.random.seed(42)
        simulated_fund_returns = gbtc_returns * 0.3 + np.random.normal(0, 0.01, len(gbtc_returns))
        simulated_fund_returns = pd.Series(simulated_fund_returns, index=gbtc_returns.index)
        
        # Calculate correlation metrics
        correlation_metrics = analyze_correlation(simulated_fund_returns, gbtc_returns)
        
        print("\nCorrelation Metrics:")
        for metric, value in correlation_metrics.items():
            print(f"{metric.replace('_', ' ').title()}: {value:.4f}")
        
        # Estimate exposure impact
        exposure_impact = estimate_exposure_impact(gbtc_metrics, correlation_metrics)
        
        print("\nEstimated Cryptocurrency Exposure Impact:")
        for metric, value in exposure_impact.items():
            print(f"{metric.replace('_', ' ').title()}: {value:.4f}")
        
        # Plot performance
        plot_performance(gbtc_data)
        
    except Exception as e:
        print(f"Error in analysis: {e}")

if __name__ == "__main__":
    main()
```
