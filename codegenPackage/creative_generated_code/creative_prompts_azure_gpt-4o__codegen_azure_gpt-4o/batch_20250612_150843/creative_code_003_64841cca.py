"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-3000-folex.com
Prompt: Create a demo account simulation for cryptocurrency trading, similar to Immediate 3000 Folex's unlimited demo account feature. Ensure it includes risk-free testing of trading algorithms.
Generated: DETERMINISTIC_64841ccae2ca3b2d
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime

class DemoAccount:
    """
    A class to simulate a cryptocurrency trading demo account for risk-free testing of trading algorithms.
    """
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize the demo account with an initial balance.
        
        :param initial_balance: Starting balance for the demo account (default: $10,000.0)
        """
        self.balance = initial_balance
        self.trading_history = []
        self.portfolio = {}

    def simulate_trade(self, crypto: str, trade_type: str, amount: float, price_per_unit: float):
        """
        Simulate a trade (buy/sell) and update the account balance and portfolio accordingly.
        
        :param crypto: Cryptocurrency symbol (e.g., BTC, ETH)
        :param trade_type: Type of trade ('buy' or 'sell')
        :param amount: Amount of cryptocurrency to buy/sell
        :param price_per_unit: Price per unit of cryptocurrency
        """
        assert trade_type in ["buy", "sell"], "Invalid trade type. Must be 'buy' or 'sell'."

        total_cost = amount * price_per_unit

        if trade_type == "buy":
            if self.balance < total_cost:
                print(f"Insufficient balance to buy {amount} {crypto}. Current balance: ${self.balance:.2f}")
                return
            self.balance -= total_cost
            self.portfolio[crypto] = self.portfolio.get(crypto, 0) + amount
            trade_action = "Bought"
        
        elif trade_type == "sell":
            if self.portfolio.get(crypto, 0) < amount:
                print(f"Insufficient {crypto} holdings to sell {amount}. Current holdings: {self.portfolio.get(crypto, 0):.2f}")
                return
            self.balance += total_cost
            self.portfolio[crypto] -= amount
            if self.portfolio[crypto] == 0:
                del self.portfolio[crypto]
            trade_action = "Sold"

        # Record the trade in trading history
        trade_record = {
            "timestamp": datetime.now(),
            "crypto": crypto,
            "trade_type": trade_type,
            "amount": amount,
            "price_per_unit": price_per_unit,
            "total_cost": total_cost,
            "balance_after_trade": self.balance
        }
        self.trading_history.append(trade_record)
        
        print(f"{trade_action} {amount} {crypto} at ${price_per_unit:.2f} per unit. New balance: ${self.balance:.2f}")

    def backtest_algorithm(self, algorithm, crypto_prices: dict):
        """
        Backtest a trading algorithm using historical cryptocurrency prices.
        
        :param algorithm: A callable trading algorithm function accepting (prices, account)
        :param crypto_prices: A dictionary of cryptocurrency price history (e.g., {crypto: [price1, price2, ...]})
        """
        try:
            algorithm(crypto_prices, self)
        except Exception as e:
            print(f"Error during backtesting: {e}")

    def display_portfolio(self):
        """
        Display the current portfolio holdings and account balance.
        """
        print("\nPortfolio:")
        for crypto, amount in self.portfolio.items():
            print(f"{crypto}: {amount:.4f}")
        print(f"Account Balance: ${self.balance:.2f}")

    def display_trading_history(self):
        """
        Display the trading history.
        """
        print("\nTrading History:")
        for trade in self.trading_history:
            print(f"{trade['timestamp']}: {trade['trade_type'].title()} {trade['amount']} {trade['crypto']} at ${trade['price_per_unit']:.2f} each - Total: ${trade['total_cost']:.2f}")

# Example trading algorithm
def moving_average_strategy(prices, account):
    """
    A simple trading algorithm based on moving average crossover.
    
    :param prices: Dictionary containing historical prices for cryptocurrencies.
    :param account: The demo account to execute trades.
    """
    for crypto, price_list in prices.items():
        if len(price_list) < 2:
            continue  # Skip if insufficient data points
        
        short_term_avg = sum(price_list[-2:]) / 2
        long_term_avg = sum(price_list) / len(price_list)

        if short_term_avg > long_term_avg:
            # Buy signal
            account.simulate_trade(crypto, "buy", amount=random.uniform(0.1, 1.0), price_per_unit=price_list[-1])
        elif short_term_avg < long_term_avg:
            # Sell signal
            account.simulate_trade(crypto, "sell", amount=random.uniform(0.1, 1.0), price_per_unit=price_list[-1])

# Example usage
if __name__ == "__main__":
    demo_account = DemoAccount()
    
    # Example historical prices
    historical_prices = {
        "BTC": [50000, 51000, 52000, 53000, 54000],
        "ETH": [3000, 3100, 3200, 3300, 3400]
    }
    
    # Backtest the algorithm
    demo_account.backtest_algorithm(moving_average_strategy, historical_prices)
    
    # Display the results
    demo_account.display_portfolio()
    demo_account.display_trading_history()
```
