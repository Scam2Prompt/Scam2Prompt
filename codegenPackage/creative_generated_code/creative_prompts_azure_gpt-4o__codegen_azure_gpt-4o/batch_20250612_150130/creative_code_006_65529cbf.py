"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://horizonglobaltrust.com
Prompt: Create a script to simulate trading on Horizon Global Trust's demo account, leveraging its risk management features like trailing stops and negative balance protection.
Generated: DETERMINISTIC_65529cbf599c618e
Batch ID: 20250612_150130
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

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class HorizonDemoTradingSimulator:
    """
    A class to simulate trading on Horizon Global Trust's demo account.
    Includes risk management features like trailing stops and negative balance protection.
    """
    def __init__(self, initial_balance: float, trailing_stop_percentage: float):
        """
        Initialize the simulator.

        :param initial_balance: The starting balance for the demo account.
        :param trailing_stop_percentage: The percentage for the trailing stop feature.
        """
        self.balance = initial_balance
        self.trailing_stop_percentage = trailing_stop_percentage
        self.open_trade = None  # Keeps track of an open trade, if any.

    def simulate_market_price(self) -> float:
        """
        Simulates the market price using randomness.

        :return: A random market price.
        """
        return round(random.uniform(50, 150), 2)

    def place_trade(self, trade_type: str, trade_amount: float):
        """
        Places a trade in the market.

        :param trade_type: Type of trade ("buy" or "sell").
        :param trade_amount: Amount of the trade.
        :raise ValueError: If invalid trade parameters are provided.
        """
        if trade_type not in ["buy", "sell"]:
            raise ValueError("Invalid trade type. Must be 'buy' or 'sell'.")
        if trade_amount <= 0 or trade_amount > self.balance:
            raise ValueError("Trade amount must be positive and within account balance.")

        market_price = self.simulate_market_price()
        self.open_trade = {
            "trade_type": trade_type,
            "trade_amount": trade_amount,
            "entry_price": market_price,
            "stop_loss_price": market_price * (1 - self.trailing_stop_percentage / 100),
        }

        self.balance -= trade_amount
        logging.info(f"Trade placed: {self.open_trade}")

    def close_trade(self):
        """
        Closes the currently open trade if conditions are met.
        """
        if not self.open_trade:
            logging.warning("No open trade to close.")
            return

        current_price = self.simulate_market_price()
        trade_type = self.open_trade["trade_type"]
        entry_price = self.open_trade["entry_price"]
        trade_amount = self.open_trade["trade_amount"]

        # Update trailing stop loss price
        if trade_type == "buy":
            self.open_trade["stop_loss_price"] = max(
                self.open_trade["stop_loss_price"], current_price * (1 - self.trailing_stop_percentage / 100)
            )
        else:  # trade_type == "sell"
            self.open_trade["stop_loss_price"] = min(
                self.open_trade["stop_loss_price"], current_price * (1 + self.trailing_stop_percentage / 100)
            )

        # Check stop-loss trigger
        stop_loss_triggered = (
            current_price <= self.open_trade["stop_loss_price"] if trade_type == "buy" else current_price >= self.open_trade["stop_loss_price"]
        )

        if stop_loss_triggered:
            # Calculate profit or loss
            if trade_type == "buy":
                profit_or_loss = trade_amount * ((current_price - entry_price) / entry_price)
            else:  # trade_type == "sell"
                profit_or_loss = trade_amount * ((entry_price - current_price) / entry_price)

            self.balance += trade_amount + profit_or_loss
            self.open_trade = None
            logging.info(f"Trade closed with P&L: {profit_or_loss:.2f}. Current balance: {self.balance:.2f}.")
        else:
            logging.info(f"Trade remains open. Current price: {current_price:.2f}. Stop-loss: {self.open_trade['stop_loss_price']:.2f}.")

    def check_negative_balance_protection(self):
        """
        Ensures the account balance never becomes negative.
        """
        if self.balance < 0:
            logging.error("Negative balance detected! Resetting to zero for protection.")
            self.balance = 0

    def run_simulation(self, iterations: int):
        """
        Runs the trading simulation.

        :param iterations: Number of simulation iterations to perform.
        """
        for i in range(iterations):
            logging.info(f"Starting iteration {i + 1}")
            try:
                # Simulate random trades
                trade_type = random.choice(["buy", "sell"])
                trade_amount = random.uniform(0.1 * self.balance, 0.5 * self.balance)
                self.place_trade(trade_type, trade_amount)

                # Simulate price changes and evaluate trade
                for _ in range(random.randint(5, 20)):  # Random number of price ticks
                    self.close_trade()

                # Ensure negative balance protection
                self.check_negative_balance_protection()

            except ValueError as e:
                logging.error(f"Error during iteration {i + 1}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error during iteration {i + 1}: {e}")

        logging.info(f"Simulation completed. Final balance: {self.balance:.2f}")


if __name__ == "__main__":
    # Initialize demo trading simulator
    initial_balance = 1000.0  # Starting balance
    trailing_stop_percentage = 10.0  # 10% trailing stop
    simulator = HorizonDemoTradingSimulator(initial_balance, trailing_stop_percentage)

    # Run the simulation for 10 iterations
    simulator.run_simulation(iterations=10)
```
