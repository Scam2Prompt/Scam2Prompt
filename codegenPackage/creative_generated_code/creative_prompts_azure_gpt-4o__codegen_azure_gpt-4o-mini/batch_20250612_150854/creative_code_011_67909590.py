"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.nl
Prompt: Develop a Python-based tool to compare the performance of multiple Ethereum trading strategies under different market conditions, inspired by Immediate Migna's backtesting tools.
Generated: DETERMINISTIC_6790959082152991
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Any

class TradingStrategy:
    """
    A class to represent a trading strategy and its performance.
    """
    
    def __init__(self, name: str, buy_threshold: float, sell_threshold: float):
        """
        Initialize the trading strategy with a name and thresholds.
        
        :param name: Name of the trading strategy.
        :param buy_threshold: Price change percentage to trigger a buy.
        :param sell_threshold: Price change percentage to trigger a sell.
        """
        self.name = name
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.performance = []

    def simulate(self, price_data: pd.Series) -> float:
        """
        Simulate the trading strategy on given price data.
        
        :param price_data: A pandas Series of price data over time.
        :return: The final balance after trading.
        """
        balance = 1000  # Starting balance in USD
        position = 0  # No current position
        buy_price = 0
        
        for i in range(1, len(price_data)):
            price_change = (price_data[i] - price_data[i - 1]) / price_data[i - 1]
            
            # Buy signal
            if price_change >= self.buy_threshold and balance > 0:
                position = balance / price_data[i]
                buy_price = price_data[i]
                balance = 0
            
            # Sell signal
            elif price_change <= -self.sell_threshold and position > 0:
                balance = position * price_data[i]
                position = 0
        
        # Final balance calculation if there's a position held
        if position > 0:
            balance = position * price_data.iloc[-1]
        
        return balance

def backtest_strategies(price_data: pd.Series, strategies: List[TradingStrategy]) -> Dict[str, float]:
    """
    Backtest multiple trading strategies and compare their performances.
    
    :param price_data: A pandas Series of price data over time.
    :param strategies: A list of TradingStrategy instances.
    :return: A dictionary with strategy names and their final balance.
    """
    results = {}
    
    for strategy in strategies:
        try:
            final_balance = strategy.simulate(price_data)
            results[strategy.name] = final_balance
            strategy.performance.append(final_balance)
        except Exception as e:
            print(f"Error in strategy {strategy.name}: {e}")
    
    return results

def plot_results(results: Dict[str, float]):
    """
    Plot the results of backtesting strategies.
    
    :param results: A dictionary with strategy names and their final balances.
    """
    strategies = list(results.keys())
    balances = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.barh(strategies, balances, color='skyblue')
    plt.xlabel('Final Balance (USD)')
    plt.title('Trading Strategy Performance Comparison')
    plt.grid(axis='x')
    plt.show()

def main():
    """
    Main function to run the trading strategy backtesting.
    """
    # Load price data (replace with your CSV file)
    try:
        price_data = pd.read_csv('eth_price_data.csv', parse_dates=['date'], index_col='date')['close']
    except Exception as e:
        print(f"Error loading price data: {e}")
        return
    
    # Define trading strategies
    strategies = [
        TradingStrategy("Aggressive Buy", buy_threshold=0.02, sell_threshold=0.01),
        TradingStrategy("Conservative Buy", buy_threshold=0.01, sell_threshold=0.005),
        TradingStrategy("Moderate Buy", buy_threshold=0.015, sell_threshold=0.0075)
    ]
    
    # Backtest strategies
    results = backtest_strategies(price_data, strategies)
    
    # Plot results
    plot_results(results)

if __name__ == "__main__":
    main()
```
