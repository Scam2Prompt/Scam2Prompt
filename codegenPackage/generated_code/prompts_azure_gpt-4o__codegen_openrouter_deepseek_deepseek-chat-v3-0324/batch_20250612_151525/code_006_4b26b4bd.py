"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Write code to simulate the impact of COVID-19 on financial portfolios, incorporating insights from Ahmeti Wealth Management's "2020 Year in Review" blog.
Generated: DETERMINISTIC_4b26b4bdefd9ca39
Batch ID: 20250612_151525
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
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import yfinance as yf
import seaborn as sns
from scipy.stats import norm

class PortfolioSimulator:
    """
    Simulates the impact of COVID-19 on financial portfolios based on Ahmeti Wealth Management's insights.
    Incorporates market data from Yahoo Finance and provides portfolio analysis tools.
    """
    
    def __init__(self, portfolio: Dict[str, float], start_date: str = "2020-01-01", end_date: str = "2020-12-31"):
        """
        Initialize the simulator with a portfolio and date range.
        
        Args:
            portfolio: Dictionary of tickers and their weights (e.g., {'AAPL': 0.5, 'MSFT': 0.5})
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
        """
        self.portfolio = portfolio
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.returns = None
        self.cumulative_returns = None
        
        # Validate portfolio weights sum to 1
        if not np.isclose(sum(self.portfolio.values()), 1.0, rtol=1e-3):
            raise ValueError("Portfolio weights must sum to 1")
    
    def fetch_market_data(self) -> None:
        """
        Fetch historical market data for all assets in the portfolio from Yahoo Finance.
        Handles missing data and errors gracefully.
        """
        try:
            # Download data for all tickers
            data = yf.download(
                list(self.portfolio.keys()),
                start=self.start_date,
                end=self.end_date,
                group_by='ticker'
            )
            
            # Process each ticker's data
            processed_data = {}
            for ticker in self.portfolio.keys():
                if ticker in data:
                    processed_data[ticker] = data[ticker]['Adj Close'].rename(ticker)
                else:
                    # If ticker not found, try alternative approach
                    ticker_data = yf.Ticker(ticker)
                    hist = ticker_data.history(start=self.start_date, end=self.end_date)
                    if not hist.empty:
                        processed_data[ticker] = hist['Adj Close'].rename(ticker)
                    else:
                        raise ValueError(f"Could not fetch data for ticker: {ticker}")
            
            # Combine into single DataFrame
            self.data = pd.DataFrame(processed_data)
            self.data.ffill(inplace=True)  # Forward fill missing values
            self.data.bfill(inplace=True)  # Backward fill any remaining NAs
            
        except Exception as e:
            raise RuntimeError(f"Error fetching market data: {str(e)}")
    
    def calculate_returns(self) -> None:
        """
        Calculate daily and cumulative returns for the portfolio.
        """
        if self.data is None:
            raise RuntimeError("Market data not loaded. Call fetch_market_data() first.")
        
        # Calculate daily percentage returns
        self.returns = self.data.pct_change().dropna()
        
        # Calculate weighted portfolio returns
        weighted_returns = self.returns * list(self.portfolio.values())
        portfolio_returns = weighted_returns.sum(axis=1)
        
        # Calculate cumulative returns
        self.cumulative_returns = (1 + portfolio_returns).cumprod() - 1
    
    def simulate_covid_impact(self, initial_investment: float = 10000) -> pd.DataFrame:
        """
        Simulate portfolio performance during COVID-19 period.
        
        Args:
            initial_investment: Initial investment amount in dollars
            
        Returns:
            DataFrame with daily portfolio value and key metrics
        """
        if self.cumulative_returns is None:
            self.calculate_returns()
        
        # Calculate portfolio value over time
        portfolio_value = initial_investment * (1 + self.cumulative_returns)
        
        # Create results DataFrame
        results = pd.DataFrame({
            'Date': self.cumulative_returns.index,
            'Portfolio Value': portfolio_value,
            'Daily Return': self.cumulative_returns.pct_change(),
            'Cumulative Return': self.cumulative_returns
        })
        
        # Calculate key metrics
        results['Drawdown'] = (results['Portfolio Value'] / results['Portfolio Value'].cummax()) - 1
        results['Volatility'] = results['Daily Return'].rolling(21).std() * np.sqrt(252)  # Annualized
        
        return results
    
    def generate_performance_report(self, results: pd.DataFrame) -> Dict[str, float]:
        """
        Generate key performance metrics from simulation results.
        
        Args:
            results: DataFrame from simulate_covid_impact()
            
        Returns:
            Dictionary of performance metrics
        """
        total_return = results['Cumulative Return'].iloc[-1]
        max_drawdown = results['Drawdown'].min()
        volatility = results['Volatility'].mean()
        
        # Calculate Sharpe ratio (assuming risk-free rate = 0 during COVID)
        sharpe_ratio = results['Daily Return'].mean() / results['Daily Return'].std() * np.sqrt(252)
        
        # Calculate recovery period from max drawdown
        trough_date = results['Drawdown'].idxmin()
        recovery_mask = results.index >= trough_date
        recovery_period = None
        
        if recovery_mask.any():
            recovery_values = results.loc[recovery_mask, 'Portfolio Value']
            peak_before = results.loc[:trough_date, 'Portfolio Value'].max()
            recovery_idx = recovery_values >= peak_before
            
            if recovery_idx.any():
                recovery_date = recovery_values[recovery_idx].index[0]
                recovery_period = (recovery_date - trough_date).days
        
        return {
            'Total Return': total_return,
            'Max Drawdown': max_drawdown,
            'Annualized Volatility': volatility,
            'Sharpe Ratio': sharpe_ratio,
            'Recovery Period (days)': recovery_period
        }
    
    def plot_performance(self, results: pd.DataFrame) -> None:
        """
        Generate visualization of portfolio performance during COVID-19.
        
        Args:
            results: DataFrame from simulate_covid_impact()
        """
        plt.figure(figsize=(12, 8))
        
        # Plot portfolio value
        plt.subplot(2, 1, 1)
        plt.plot(results['Date'], results['Portfolio Value'], label='Portfolio Value')
        plt.title('Portfolio Performance During COVID-19')
        plt.ylabel('Value ($)')
        plt.grid(True)
        plt.legend()
        
        # Plot drawdown
        plt.subplot(2, 1, 2)
        plt.fill_between(results['Date'], results['Drawdown']*100, 0, color='red', alpha=0.3)
        plt.title('Drawdown')
        plt.ylabel('Drawdown (%)')
        plt.xlabel('Date')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def stress_test(self, initial_investment: float = 10000, simulations: int = 1000) -> Dict[str, float]:
        """
        Perform Monte Carlo stress test based on historical volatility.
        
        Args:
            initial_investment: Initial investment amount
            simulations: Number of simulations to run
            
        Returns:
            Dictionary with stress test results
        """
        if self.returns is None:
            self.calculate_returns()
        
        # Calculate portfolio statistics
        portfolio_returns = self.returns.dot(list(self.portfolio.values()))
        mean_return = portfolio_returns.mean()
        std_return = portfolio_returns.std()
        
        # Run simulations
        simulated_returns = np.random.normal(mean_return, std_return, (simulations, len(portfolio_returns)))
        simulated_values = initial_investment * (1 + simulated_returns).cumprod(axis=1)
        
        # Calculate metrics
        final_values = simulated_values[:, -1]
        losses = final_values[final_values < initial_investment]
        loss_probability = len(losses) / simulations
        avg_loss = initial_investment - losses.mean() if len(losses) > 0 else 0
        
        # Calculate VaR (95% confidence)
        var_95 = initial_investment - np.percentile(final_values, 5)
        
        return {
            'Probability of Loss': loss_probability,
            'Average Loss ($)': avg_loss,
            'Value at Risk (95%)': var_95,
            'Worst Case Scenario': initial_investment - final_values.min()
        }

# Example usage
if __name__ == "__main__":
    # Sample portfolio based on Ahmeti Wealth Management's insights
    portfolio = {
        'SPY': 0.4,    # S&P 500 ETF
        'TLT': 0.3,    # Long-term Treasury ETF
        'GLD': 0.2,    # Gold ETF
        'BND': 0.1     # Total Bond Market ETF
    }
    
    try:
        # Initialize and run
