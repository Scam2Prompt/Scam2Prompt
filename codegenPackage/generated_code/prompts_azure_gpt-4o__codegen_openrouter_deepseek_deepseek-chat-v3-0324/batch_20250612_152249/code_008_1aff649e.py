"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Create a program to compare the performance of the leveraged pair trading strategy against a buy-and-hold strategy using APR calculations, as detailed on 2xEther.com.
Generated: DETERMINISTIC_1aff649eb185742a
Batch ID: 20250612_152249
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
from scipy.stats import linregress
from typing import Tuple, Dict, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TradingStrategyAnalyzer:
    """
    A class to analyze and compare the performance of leveraged pair trading vs buy-and-hold strategies.
    """
    
    def __init__(self, asset1_prices: pd.Series, asset2_prices: pd.Series, leverage: float = 2.0):
        """
        Initialize the analyzer with price data for two assets.
        
        Args:
            asset1_prices: Historical prices of asset 1 (e.g., ETH)
            asset2_prices: Historical prices of asset 2 (e.g., BTC)
            leverage: Leverage factor for the pair trading strategy (default: 2.0)
        """
        if len(asset1_prices) != len(asset2_prices):
            raise ValueError("Price series must have the same length")
            
        self.asset1_prices = asset1_prices
        self.asset2_prices = asset2_prices
        self.leverage = leverage
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input data."""
        if self.leverage <= 0:
            raise ValueError("Leverage must be positive")
        if any(self.asset1_prices <= 0) or any(self.asset2_prices <= 0):
            raise ValueError("Prices must be positive")
            
    def calculate_returns(self, prices: pd.Series) -> pd.Series:
        """Calculate daily returns from price series."""
        return prices.pct_change().dropna()
    
    def calculate_apy(self, daily_returns: pd.Series, days_per_year: int = 365) -> float:
        """
        Calculate Annual Percentage Yield (APY) from daily returns.
        
        Args:
            daily_returns: Series of daily returns
            days_per_year: Number of trading days in a year (default: 365)
            
        Returns:
            APY as a decimal (e.g., 0.10 for 10%)
        """
        if len(daily_returns) == 0:
            return 0.0
            
        total_return = (1 + daily_returns).prod() - 1
        n_periods = len(daily_returns) / days_per_year
        return (1 + total_return) ** (1 / n_periods) - 1
    
    def buy_and_hold_performance(self) -> Dict[str, float]:
        """Calculate buy-and-hold performance for both assets."""
        asset1_returns = self.calculate_returns(self.asset1_prices)
        asset2_returns = self.calculate_returns(self.asset2_prices)
        
        return {
            'asset1_apy': self.calculate_apy(asset1_returns),
            'asset2_apy': self.calculate_apy(asset2_returns)
        }
    
    def _calculate_hedge_ratio(self) -> float:
        """Calculate hedge ratio using linear regression."""
        slope, _, _, _, _ = linregress(self.asset1_prices, self.asset2_prices)
        return slope
    
    def leveraged_pair_trading_performance(self) -> Dict[str, float]:
        """
        Calculate performance of leveraged pair trading strategy.
        
        Returns:
            Dictionary containing strategy APY and other metrics
        """
        try:
            # Calculate spread
            hedge_ratio = self._calculate_hedge_ratio()
            spread = self.asset1_prices - hedge_ratio * self.asset2_prices
            
            # Normalize spread
            normalized_spread = (spread - spread.mean()) / spread.std()
            
            # Generate signals (simple mean-reversion strategy)
            entry_threshold = 1.0
            exit_threshold = 0.0
            
            position = 0
            strategy_returns = []
            
            for i in range(1, len(normalized_spread)):
                if position == 0 and normalized_spread[i-1] > entry_threshold:
                    position = -1  # Short spread
                elif position == 0 and normalized_spread[i-1] < -entry_threshold:
                    position = 1  # Long spread
                elif position != 0 and abs(normalized_spread[i-1]) < exit_threshold:
                    position = 0  # Exit position
                
                # Calculate daily return with leverage
                asset1_ret = self.asset1_prices[i] / self.asset1_prices[i-1] - 1
                asset2_ret = self.asset2_prices[i] / self.asset2_prices[i-1] - 1
                daily_ret = position * (asset1_ret - hedge_ratio * asset2_ret) * self.leverage
                strategy_returns.append(daily_ret)
            
            strategy_returns = pd.Series(strategy_returns)
            apy = self.calculate_apy(strategy_returns)
            
            return {
                'strategy_apy': apy,
                'hedge_ratio': hedge_ratio,
                'sharpe_ratio': self._calculate_sharpe_ratio(strategy_returns)
            }
            
        except Exception as e:
            logger.error(f"Error calculating pair trading performance: {str(e)}")
            raise
    
    def _calculate_sharpe_ratio(self, returns: pd.Series, risk_free_rate: float = 0.0) -> float:
        """Calculate annualized Sharpe ratio."""
        excess_returns = returns - risk_free_rate / 252
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)
    
    def compare_strategies(self) -> Dict[str, Dict[str, float]]:
        """Compare performance of both strategies."""
        try:
            bh_results = self.buy_and_hold_performance()
            pt_results = self.leveraged_pair_trading_performance()
            
            return {
                'buy_and_hold': bh_results,
                'pair_trading': pt_results,
                'comparison': {
                    'outperformance': pt_results['strategy_apy'] - max(bh_results['asset1_apy'], bh_results['asset2_apy'])
                }
            }
        except Exception as e:
            logger.error(f"Error comparing strategies: {str(e)}")
            raise

def load_sample_data() -> Tuple[pd.Series, pd.Series]:
    """Load sample price data for demonstration."""
    np.random.seed(42)
    n_days = 365 * 3  # 3 years of daily data
    base_prices = np.cumprod(1 + np.random.normal(0.0005, 0.01, n_days))
    correlated_prices = base_prices * 0.8 + np.random.normal(0, 0.005, n_days)
    
    dates = pd.date_range(start='2020-01-01', periods=n_days)
    asset1 = pd.Series(base_prices, index=dates, name='ETH')
    asset2 = pd.Series(correlated_prices, index=dates, name='BTC')
    
    return asset1, asset2

def plot_results(results: Dict[str, Dict[str, float]]) -> None:
    """Visualize strategy comparison results."""
    strategies = ['buy_and_hold', 'pair_trading']
    labels = ['ETH Buy & Hold', 'BTC Buy & Hold', 'Leveraged Pair Trading']
    
    bh_apys = [results['buy_and_hold']['asset1_apy'], 
               results['buy_and_hold']['asset2_apy']]
    pt_apy = results['pair_trading']['strategy_apy']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, bh_apys + [pt_apy])
    
    # Color the bars
    bars[0].set_color('blue')
    bars[1].set_color('orange')
    bars[2].set_color('green')
    
    plt.title('Strategy Performance Comparison (APY)')
    plt.ylabel('Annual Percentage Yield')
    plt.xticks(rotation=45)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.1%}',
                 ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

def main():
    """Main execution function."""
    try:
        # Load sample data (replace with real data in production)
        eth_prices, btc_prices = load_sample_data()
        
        # Initialize analyzer
        analyzer = TradingStrategyAnalyzer(eth_prices, btc_prices, leverage=2.0)
        
        # Compare strategies
        results = analyzer.compare_strategies()
        
        # Print results
        print("\nStrategy Performance Results:")
        print(f"ETH Buy & Hold
