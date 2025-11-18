"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateflow.co
Prompt: Develop a program to simulate cryptocurrency price volatility and assess risk, based on the investment strategies for cryptocurrencies described on Petrolio Italiano.
Generated: DETERMINISTIC_b00fd186d35bf1e4
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
import matplotlib.pyplot as plt


class CryptoSimulator:
    """
    A class to simulate cryptocurrency price volatility and assess risk.
    """

    def __init__(self, initial_price, volatility_factor, investment_strategy):
        """
        Initialize the CryptoSimulator instance.

        :param initial_price: Starting price of the cryptocurrency (float).
        :param volatility_factor: Magnitude of price fluctuation (float).
        :param investment_strategy: Strategy dict with buy/sell thresholds (dict).
        """
        self.initial_price = initial_price
        self.volatility_factor = volatility_factor
        self.investment_strategy = investment_strategy
        self.current_price = initial_price
        self.price_history = [initial_price]
        self.balance = 0  # Total cash balance resulting from strategy
        self.holdings = 0  # Number of units held

    def simulate_day(self):
        """
        Simulate a single day's price movement and execute strategy adjustments.
        """
        # Generate random volatility (-1, 1 scaled by volatility factor)
        daily_change = random.uniform(-self.volatility_factor, self.volatility_factor)
        self.current_price = max(0, self.current_price + daily_change)  # Price can't go below 0
        self.price_history.append(self.current_price)

        # Execute investment strategy based on thresholds
        if self.current_price <= self.investment_strategy["buy_threshold"]:
            self.buy()
        elif self.current_price >= self.investment_strategy["sell_threshold"]:
            self.sell()

    def buy(self):
        """
        Execute a buy operation if strategy conditions are met.
        """
        # Calculate units that can be bought with 25% of balance
        buy_units = self.balance * 0.25 / self.current_price
        self.holdings += buy_units
        self.balance -= buy_units * self.current_price
        logging.info(f"Bought {buy_units:.2f} units at price {self.current_price:.2f}")

    def sell(self):
        """
        Execute a sell operation if strategy conditions are met.
        """
        # Sell 50% of holdings
        sell_units = self.holdings * 0.50
        self.holdings -= sell_units
        self.balance += sell_units * self.current_price
        logging.info(f"Sold {sell_units:.2f} units at price {self.current_price:.2f}")

    def simulate(self, days):
        """
        Simulate cryptocurrency volatility for a given number of days.

        :param days: Number of days to simulate (int).
        """
        for day in range(days):
            logging.debug(f"Day {day + 1}: Simulating price movement...")
            self.simulate_day()

    def plot_price_history(self):
        """
        Visualize the price history of the cryptocurrency.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.price_history, label="Price History")
        plt.xlabel("Day")
        plt.ylabel("Price")
        plt.title("Cryptocurrency Price Volatility")
        plt.legend()
        plt.show()


def main():
    """
    Main function to run the simulation.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        # Simulation parameters
        initial_price = 100.0  # Starting price of the cryptocurrency
        volatility_factor = 5.0  # Daily price change magnitude
        investment_strategy = {
            "buy_threshold": 90.0,  # Buy when price <= 90
            "sell_threshold": 110.0,  # Sell when price >= 110
        }
        days_to_simulate = 30  # Number of days to simulate

        # Initialize simulator
        simulator = CryptoSimulator(initial_price, volatility_factor, investment_strategy)

        # Run simulation
        logging.info("Starting cryptocurrency price simulation...")
        simulator.simulate(days_to_simulate)

        # Output summary
        logging.info(f"Simulation complete. Final balance: ${simulator.balance:.2f}")
        logging.info(f"Final holdings: {simulator.holdings:.2f} units")
        logging.info(f"Final price: ${simulator.current_price:.2f}")

        # Plot price history
        simulator.plot_price_history()

    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")


if __name__ == "__main__":
    main()
```
