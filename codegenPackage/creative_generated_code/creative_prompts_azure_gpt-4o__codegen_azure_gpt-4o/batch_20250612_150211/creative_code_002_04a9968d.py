"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalupspips.com
Prompt: Create a Python program that simulates forex trading based on the EUR/USD currency pair, incorporating buy and sell prices and spreads as described on CapitalUpsPips.
Generated: DETERMINISTIC_04a9968d15d9f8c8
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ForexTradingSimulator:
    """
    Simulates forex trading for the EUR/USD currency pair.
    The program models buy and sell prices and includes a spread.
    """

    def __init__(self, spread=0.0002):
        """
        Initializes the ForexTradingSimulator with a given spread.
        
        Args:
            spread (float): The difference between buy and sell prices (default: 0.0002).
        """
        self.spread = spread
        self.base_price = 1.1000  # Initial price for EUR/USD, can be adjusted

    def generate_price(self):
        """
        Generates a random base price for EUR/USD within a realistic range.

        Returns:
            float: Random base price.
        """
        # Simulate price fluctuations within a range
        fluctuation = random.uniform(-0.0050, 0.0050)
        self.base_price = round(self.base_price + fluctuation, 4)
        return self.base_price

    def get_buy_sell_prices(self):
        """
        Calculates the buy and sell prices based on the spread.

        Returns:
            tuple: Buy price and sell price (float).
        """
        buy_price = round(self.base_price + self.spread / 2, 4)
        sell_price = round(self.base_price - self.spread / 2, 4)
        return buy_price, sell_price

    def simulate_trading_decision(self):
        """
        Simulates a trading decision (buy or sell) with random logic.

        Returns:
            str: "BUY" or "SELL".
        """
        return random.choice(["BUY", "SELL"])

    def execute_trade(self, decision, buy_price, sell_price):
        """
        Executes a trade based on the decision.

        Args:
            decision (str): Trading decision ("BUY" or "SELL").
            buy_price (float): The buy price.
            sell_price (float): The sell price.

        Returns:
            str: Trade execution result.
        """
        if decision == "BUY":
            return f"Executed BUY at {buy_price}"
        elif decision == "SELL":
            return f"Executed SELL at {sell_price}"
        else:
            return "Invalid trading decision."

    def run_simulation(self, num_iterations=10):
        """
        Runs the forex trading simulation for a specified number of iterations.

        Args:
            num_iterations (int): Number of trading simulations (default: 10).
        """
        for i in range(num_iterations):
            print(f"\nIteration {i + 1}:")
            try:
                base_price = self.generate_price()
                buy_price, sell_price = self.get_buy_sell_prices()
                decision = self.simulate_trading_decision()
                result = self.execute_trade(decision, buy_price, sell_price)

                # Display trading details
                print(f"Base Price: {base_price}")
                print(f"Spread: {self.spread}")
                print(f"Buy Price: {buy_price}")
                print(f"Sell Price: {sell_price}")
                print(f"Decision: {decision}")
                print(result)
            except Exception as e:
                print(f"Error during simulation: {e}")


if __name__ == "__main__":
    # Initialize the simulator with a spread value
    simulator = ForexTradingSimulator(spread=0.0002)

    # Run the simulation for a specified number of iterations
    simulator.run_simulation(num_iterations=10)
```
