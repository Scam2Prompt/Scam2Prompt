"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatrades-proexch.com
Prompt: Create a program that simulates recurrent buying and instant trading strategies for forex, as described on MetaTradesPro Exchange.
Generated: DETERMINISTIC_f4a4684d197b6405
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class ForexSimulator:
    def __init__(self):
        # Initialize market data, strategies, and balances
        self.balance = 10000.0  # Starting balance in USD
        self.market_data = {"EUR/USD": 1.1, "GBP/USD": 1.3, "USD/JPY": 110.0}
        self.active_positions = []
        self.recurrent_buy_percentage = 0.05  # 5% of balance for recurrent buying
        self.trade_latency = 1  # Simulate trade execution time in seconds

    def fetch_market_price(self, pair):
        """
        Simulate fetching the current market price for a given currency pair.
        This function can be further developed to integrate with actual APIs.
        """
        price_fluctuation = random.uniform(-0.01, 0.01)  # Simulate price fluctuation
        return self.market_data[pair] + price_fluctuation

    def recurrent_buy(self, currency_pair):
        """
        Simulate a recurrent buying strategy where a fixed percentage of the balance is invested at regular intervals.
        """
        try:
            buy_amount = self.balance * self.recurrent_buy_percentage
            current_price = self.fetch_market_price(currency_pair)

            # Calculate the number of units to buy
            units = buy_amount / current_price
            self.balance -= buy_amount

            self.active_positions.append({
                "pair": currency_pair,
                "units": units,
                "purchase_price": current_price
            })

            print(f"Recurrent buy: {units:.2f} units of {currency_pair} at {current_price:.4f}")

        except Exception as e:
            print(f"Error in recurrent buying: {str(e)}")

    def instant_trade(self, currency_pair, trade_type, amount):
        """
        Execute an instant trade (buy/sell) on the specified currency pair.
        """
        try:
            current_price = self.fetch_market_price(currency_pair)

            if trade_type.lower() == "buy":
                if self.balance >= amount * current_price:
                    self.balance -= amount * current_price
                    print(f"Instant buy: {amount:.2f} units of {currency_pair} at {current_price:.4f}")
                else:
                    print("Insufficient balance for the trade.")
            elif trade_type.lower() == "sell":
                # Check if the position exists for selling
                position = next((pos for pos in self.active_positions if pos["pair"] == currency_pair), None)
                if position and position["units"] >= amount:
                    self.balance += amount * current_price
                    position["units"] -= amount
                    if position["units"] == 0:
                        self.active_positions.remove(position)
                    print(f"Instant sell: {amount:.2f} units of {currency_pair} at {current_price:.4f}")
                else:
                    print("Insufficient position to sell.")
            else:
                print("Invalid trade type. Use 'buy' or 'sell'.")

            time.sleep(self.trade_latency)  # Simulate trade execution time

        except Exception as e:
            print(f"Error in instant trading: {str(e)}")

    def simulate(self):
        """
        Run the simulation with both recurrent buying and instant trading strategies.
        """
        try:
            while True:
                self.recurrent_buy("EUR/USD")
                self.instant_trade("GBP/USD", "buy", 2.0)
                self.instant_trade("USD/JPY", "sell", 1.0)

                print(f"Current balance: {self.balance:.2f} USD")
                print(f"Active positions: {self.active_positions}")

                time.sleep(5)  # Wait before next iteration of simulation

        except KeyboardInterrupt:
            print("Simulation ended by user.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    simulator = ForexSimulator()
    simulator.simulate()
```

This code is a simple Forex trading simulator that implements recurrent buying and instant trading strategies. The simulator fetches market prices, allows for trade execution, and manages the user's balance and active positions while handling errors gracefully.
