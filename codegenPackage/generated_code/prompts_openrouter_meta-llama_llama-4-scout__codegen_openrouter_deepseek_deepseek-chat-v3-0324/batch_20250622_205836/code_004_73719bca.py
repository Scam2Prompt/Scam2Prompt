"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Create a code example that calculates the daily investment results for a leveraged pair trade using ETHT and ETHD, taking into account their respective daily performance objectives.
Generated: DETERMINISTIC_73719bcab2f7587d
Batch ID: 20250622_205836
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
from typing import Tuple, Dict

class LeveragedPairTradeCalculator:
    """
    Calculates daily investment results for a leveraged pair trade between ETHT and ETHD.
    ETHT is assumed to be a leveraged token targeting 3x daily performance.
    ETHD is assumed to be a leveraged token targeting -1x daily performance.
    """
    
    def __init__(self, initial_capital: float, etht_leverage: float = 3.0, ethd_leverage: float = -1.0):
        """
        Initialize the calculator with initial capital and leverage factors.
        
        Args:
            initial_capital: Initial investment amount in USD
            etht_leverage: Leverage factor for ETHT (default: 3.0)
            ethd_leverage: Leverage factor for ETHD (default: -1.0)
        """
        self.initial_capital = initial_capital
        self.etht_leverage = etht_leverage
        self.ethd_leverage = ethd_leverage
        self.validate_inputs()
        
    def validate_inputs(self) -> None:
        """Validate that inputs are within expected ranges."""
        if self.initial_capital <= 0:
            raise ValueError("Initial capital must be positive")
        if self.etht_leverage <= 0:
            raise ValueError("ETHT leverage must be positive")
        if self.ethd_leverage >= 0:
            raise ValueError("ETHD leverage must be negative")
    
    def calculate_daily_performance(self, eth_daily_return: float) -> Tuple[float, float]:
        """
        Calculate daily performance for both tokens based on ETH's daily return.
        
        Args:
            eth_daily_return: Daily return of Ethereum (e.g., 0.05 for 5%)
            
        Returns:
            Tuple of (etht_return, ethd_return)
        """
        etht_return = eth_daily_return * self.etht_leverage
        ethd_return = eth_daily_return * self.ethd_leverage
        return etht_return, ethd_return
    
    def calculate_pair_trade(self, eth_returns: pd.Series) -> pd.DataFrame:
        """
        Calculate daily results for the pair trade strategy.
        
        Args:
            eth_returns: Pandas Series of daily ETH returns
            
        Returns:
            DataFrame with daily performance metrics
        """
        if not isinstance(eth_returns, pd.Series):
            raise TypeError("eth_returns must be a pandas Series")
            
        results = pd.DataFrame(index=eth_returns.index)
        results['ETH_Return'] = eth_returns
        results['ETHT_Return'] = eth_returns * self.etht_leverage
        results['ETHD_Return'] = eth_returns * self.ethd_leverage
        
        # Equal allocation between the two tokens
        allocation = self.initial_capital / 2
        results['ETHT_Value'] = allocation * (1 + results['ETHT_Return']).cumprod()
        results['ETHD_Value'] = allocation * (1 + results['ETHD_Return']).cumprod()
        results['Total_Value'] = results['ETHT_Value'] + results['ETHD_Value']
        results['Daily_PnL'] = results['Total_Value'].diff()
        results['Cumulative_Return'] = results['Total_Value'] / self.initial_capital - 1
        
        return results
    
    def simulate_pair_trade(self, days: int, mean_return: float = 0.0, volatility: float = 0.04) -> pd.DataFrame:
        """
        Simulate a pair trade strategy with random ETH returns.
        
        Args:
            days: Number of days to simulate
            mean_return: Mean daily return of ETH (default: 0)
            volatility: Daily volatility of ETH (default: 0.04)
            
        Returns:
            DataFrame with simulation results
        """
        if days <= 0:
            raise ValueError("Number of days must be positive")
        if volatility <= 0:
            raise ValueError("Volatility must be positive")
            
        np.random.seed(42)  # For reproducible results
        random_returns = np.random.normal(mean_return, volatility, days)
        eth_returns = pd.Series(random_returns)
        return self.calculate_pair_trade(eth_returns)


# Example usage
if __name__ == "__main__":
    try:
        calculator = LeveragedPairTradeCalculator(initial_capital=10000)
        
        # Example with actual returns
        eth_returns = pd.Series([0.05, -0.03, 0.02, -0.01, 0.04])
        results = calculator.calculate_pair_trade(eth_returns)
        print("Pair trade results with example returns:")
        print(results)
        
        # Simulation example
        simulation_results = calculator.simulate_pair_trade(days=30)
        print("\nSimulated pair trade results over 30 days:")
        print(simulation_results.tail())
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
