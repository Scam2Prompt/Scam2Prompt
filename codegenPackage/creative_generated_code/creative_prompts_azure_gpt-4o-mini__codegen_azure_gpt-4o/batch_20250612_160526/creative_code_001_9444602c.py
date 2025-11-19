"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-cryptocode-pro.com
Prompt: Explain how to implement backtesting for trading strategies using the Crypto code software and provide sample code for testing a strategy against historical market data.
Generated: DETERMINISTIC_9444602c2e960e7d
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class Backtester:
    """
    A class to perform backtesting for trading strategies using historical market data.
    """
    def __init__(self, historical_data: pd.DataFrame, strategy_function):
        """
        Initialize the Backtester with historical data and a strategy function.

        :param historical_data: A Pandas DataFrame containing historical market data.
                                Must include 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'.
        :param strategy_function: A user-defined function that implements a trading strategy.
        """
        self.data = historical_data
        self.strategy_function = strategy_function
        self.results = None

    def run_backtest(self, initial_balance: float, transaction_fee: float = 0.001):
        """
        Run the backtest on the provided historical data using the specified strategy.

        :param initial_balance: The initial amount of money to start the backtest.
        :param transaction_fee: Transaction fee percentage (default: 0.1%).
        :return: A DataFrame showing backtest results including balance and trades made.
        """
        balance = initial_balance
        position = 0  # Current position in crypto (positive for holding, 0 for none)
        trade_log = []  # Log of all trades

        for i in range(len(self.data)):
            current_data = self.data.iloc[i]
            signal = self.strategy_function(current_data)  # Get strategy signal (e.g., 'buy', 'sell', 'hold')
            
            if signal == 'buy' and balance > 0:
                # Buy as much crypto as possible with current balance
                amount_to_buy = (balance * (1 - transaction_fee)) / current_data['Close']
                position += amount_to_buy
                balance = 0
                trade_log.append({'Date': current_data['Date'], 'Action': 'Buy', 'Price': current_data['Close']})
            elif signal == 'sell' and position > 0:
                # Sell all crypto holdings
                balance += position * current_data['Close'] * (1 - transaction_fee)
                position = 0
                trade_log.append({'Date': current_data['Date'], 'Action': 'Sell', 'Price': current_data['Close']})
        
        # Calculate final portfolio value
        final_balance = balance + (position * self.data.iloc[-1]['Close'])
        
        # Create results DataFrame
        self.results = pd.DataFrame(trade_log)
        self.results['Balance'] = final_balance

        return self.results

    def plot_results(self):
        """
        Plot the backtest results including trades and equity curve.

        :return: None
        """
        if self.results is None:
            raise ValueError("Backtest results are not available. Please run the backtest first.")

        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Date'], self.data['Close'], label='Market Price')
        for index, trade in self.results.iterrows():
            color = 'green' if trade['Action'] == 'Buy' else 'red'
            plt.scatter(trade['Date'], trade['Price'], color=color, label=trade['Action'], marker='o')
        
        plt.title('Backtesting Results')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()


# Example Strategy Function
def example_strategy(data):
    """
    A simple example strategy:
    - Buy if Close price is lower than Open price
    - Sell if Close price is higher than Open price
    - Hold otherwise

    :param data: A row of historical market data (Pandas Series).
    :return: 'buy', 'sell', or 'hold'
    """
    if data['Close'] < data['Open']:
        return 'buy'
    elif data['Close'] > data['Open']:
        return 'sell'
    else:
        return 'hold'


# Example Usage of Backtester
if __name__ == "__main__":
    # Load historical market data into a Pandas DataFrame
    # Replace this with actual data loading code (e.g., from CSV/API)
    historical_data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', end='2023-01-10'),
        'Open': [100, 102, 101, 105, 107, 110, 108, 112, 115, 113],
        'High': [103, 105, 104, 108, 110, 112, 111, 115, 118, 116],
        'Low': [98, 100, 99, 102, 104, 107, 106, 110, 113, 111],
        'Close': [101, 104, 102, 107, 109, 111, 110, 114, 116, 114],
        'Volume': [1000, 1200, 1100, 1500, 1300, 1400, 1200, 1600, 1700, 1500]
    })

    # Instantiate Backtester and run backtest
    backtester = Backtester(historical_data, example_strategy)
    results = backtester.run_backtest(initial_balance=1000)

    print("Trade Log:")
    print(results)

    # Plot the backtest results
    backtester.plot_results()
```
