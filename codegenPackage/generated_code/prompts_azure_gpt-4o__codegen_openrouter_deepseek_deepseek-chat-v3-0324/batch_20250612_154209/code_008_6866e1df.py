"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Generate Python code to evaluate the effectiveness of hedging strategies in global financial markets, inspired by the advisory services offered by GCap Markets.
Generated: DETERMINISTIC_6866e1df47af365e
Batch ID: 20250612_154209
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
from scipy.stats import norm
from typing import Tuple, Dict, List, Optional
import yfinance as yf
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

class HedgingStrategyEvaluator:
    """
    A class to evaluate the effectiveness of various hedging strategies in global financial markets.
    Inspired by GCap Markets' advisory services.
    """
    
    def __init__(self, tickers: List[str], start_date: str, end_date: str, hedge_ratio: float = 1.0):
        """
        Initialize the evaluator with market data.
        
        Args:
            tickers: List of ticker symbols (e.g., ['SPY', 'TLT'] for S&P 500 and long-term Treasuries)
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            hedge_ratio: Initial hedge ratio (default 1.0)
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.hedge_ratio = hedge_ratio
        self.data = self._fetch_data()
        self.returns = self._calculate_returns()
        
    def _fetch_data(self) -> pd.DataFrame:
        """Fetch historical price data from Yahoo Finance."""
        try:
            data = yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close']
            if len(self.tickers) == 1:
                data = data.to_frame()
                data.columns = self.tickers
            return data.dropna()
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def _calculate_returns(self) -> pd.DataFrame:
        """Calculate daily log returns."""
        return np.log(self.data / self.data.shift(1)).dropna()
    
    def calculate_var(self, confidence_level: float = 0.95) -> Dict[str, float]:
        """
        Calculate Value at Risk (VaR) for each asset.
        
        Args:
            confidence_level: Confidence level for VaR calculation (default 0.95)
            
        Returns:
            Dictionary of VaR values for each asset
        """
        var_dict = {}
        for ticker in self.tickers:
            mean = self.returns[ticker].mean()
            std_dev = self.returns[ticker].std()
            var = norm.ppf(1 - confidence_level, mean, std_dev)
            var_dict[ticker] = var
            
        return var_dict
    
    def calculate_cvar(self, confidence_level: float = 0.95) -> Dict[str, float]:
        """
        Calculate Conditional Value at Risk (CVaR) for each asset.
        
        Args:
            confidence_level: Confidence level for CVaR calculation (default 0.95)
            
        Returns:
            Dictionary of CVaR values for each asset
        """
        cvar_dict = {}
        var_dict = self.calculate_var(confidence_level)
        
        for ticker in self.tickers:
            returns_below_var = self.returns[ticker][self.returns[ticker] <= var_dict[ticker]]
            cvar = returns_below_var.mean()
            cvar_dict[ticker] = cvar
            
        return cvar_dict
    
    def calculate_optimal_hedge_ratio(self) -> float:
        """
        Calculate optimal hedge ratio using OLS regression.
        
        Returns:
            Optimal hedge ratio (beta) between the first two assets
        """
        if len(self.tickers) < 2:
            raise ValueError("At least two assets required for hedge ratio calculation")
            
        x = self.returns[self.tickers[0]].values
        y = self.returns[self.tickers[1]].values
        
        # Add constant for intercept
        x = np.vstack([x, np.ones(len(x))]).T
        
        # Calculate OLS coefficients
        beta = np.linalg.lstsq(x, y, rcond=None)[0][0]
        
        return beta
    
    def evaluate_hedge_performance(self, hedge_ratio: Optional[float] = None) -> Dict[str, float]:
        """
        Evaluate performance metrics of the hedged portfolio.
        
        Args:
            hedge_ratio: Hedge ratio to use (defaults to instance hedge_ratio)
            
        Returns:
            Dictionary containing performance metrics
        """
        if len(self.tickers) < 2:
            raise ValueError("At least two assets required for hedge evaluation")
            
        hr = hedge_ratio if hedge_ratio is not None else self.hedge_ratio
        
        # Calculate hedged portfolio returns
        portfolio_returns = self.returns[self.tickers[0]] - hr * self.returns[self.tickers[1]]
        
        # Calculate performance metrics
        metrics = {
            'mean_return': portfolio_returns.mean(),
            'volatility': portfolio_returns.std(),
            'sharpe_ratio': portfolio_returns.mean() / portfolio_returns.std() * np.sqrt(252),
            'var_95': norm.ppf(0.05, portfolio_returns.mean(), portfolio_returns.std()),
            'cvar_95': portfolio_returns[portfolio_returns <= norm.ppf(0.05, portfolio_returns.mean(), portfolio_returns.std())].mean()
        }
        
        return metrics
    
    def rolling_hedge_analysis(self, window: int = 63) -> pd.DataFrame:
        """
        Perform rolling window analysis of hedge effectiveness.
        
        Args:
            window: Rolling window size in days (default 63, approx 3 months)
            
        Returns:
            DataFrame with rolling hedge metrics
        """
        if len(self.tickers) < 2:
            raise ValueError("At least two assets required for hedge analysis")
            
        results = []
        
        for i in range(window, len(self.returns)):
            subset = self.returns.iloc[i-window:i]
            
            # Calculate rolling hedge ratio
            x = subset[self.tickers[0]].values
            y = subset[self.tickers[1]].values
            x = np.vstack([x, np.ones(len(x))]).T
            beta = np.linalg.lstsq(x, y, rcond=None)[0][0]
            
            # Calculate portfolio metrics
            portfolio_returns = subset[self.tickers[0]] - beta * subset[self.tickers[1]]
            
            metrics = {
                'date': self.returns.index[i],
                'hedge_ratio': beta,
                'portfolio_return': portfolio_returns.mean(),
                'portfolio_volatility': portfolio_returns.std(),
                'sharpe_ratio': portfolio_returns.mean() / portfolio_returns.std() * np.sqrt(252)
            }
            
            results.append(metrics)
            
        return pd.DataFrame(results).set_index('date')
    
    def plot_hedge_performance(self, window: int = 63) -> None:
        """
        Plot hedge performance metrics over time.
        
        Args:
            window: Rolling window size in days (default 63)
        """
        rolling_metrics = self.rolling_hedge_analysis(window)
        
        plt.figure(figsize=(15, 10))
        
        plt.subplot(3, 1, 1)
        plt.plot(rolling_metrics.index, rolling_metrics['hedge_ratio'], label='Hedge Ratio')
        plt.title('Rolling Hedge Ratio')
        plt.legend()
        
        plt.subplot(3, 1, 2)
        plt.plot(rolling_metrics.index, rolling_metrics['portfolio_return'], label='Portfolio Return')
        plt.plot(rolling_metrics.index, rolling_metrics['portfolio_volatility'], label='Portfolio Volatility')
        plt.title('Return and Volatility')
        plt.legend()
        
        plt.subplot(3, 1, 3)
        plt.plot(rolling_metrics.index, rolling_metrics['sharpe_ratio'], label='Sharpe Ratio')
        plt.title('Risk-Adjusted Performance')
        plt.legend()
        
        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with S&P 500 and 20+ Year Treasury ETFs
        evaluator = HedgingStrategyEvaluator(
            tickers=['SPY', 'TLT'],
            start_date='2020-01-01',
            end_date='2023-01-01'
        )
        
        # Calculate risk metrics
        print("VaR (95%):", evaluator.calculate_var())
        print("CVaR (95%):", evaluator.calculate_cvar())
        
        # Calculate optimal hedge ratio
        optimal_ratio = evaluator.calculate_optimal_hedge_ratio()
        print(f"Optimal Hedge Ratio: {optimal_ratio:.4f}")
        
        # Evaluate hedge performance
        print("\nHedge Performance Metrics:")
        print(evaluator.evaluate_hedge_performance(optimal_ratio))
        
        # Plot rolling performance
        evaluator.plot_hedge_performance()
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
