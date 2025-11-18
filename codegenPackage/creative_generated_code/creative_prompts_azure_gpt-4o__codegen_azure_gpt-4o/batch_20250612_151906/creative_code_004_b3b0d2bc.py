"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdstarfx.com
Prompt: Write a script to simulate forex trading with a leverage of 1:500, as provided in the "STANDARD" account type on the S D STAR FX LTD platform.
Generated: DETERMINISTIC_b3b0d2bc26b1f547
Batch ID: 20250612_151906
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ForexTradingSimulator:
    """
    A simulator for Forex trading using leverage (1:500) for a STANDARD account.
    """
    def __init__(self, initial_balance: float, leverage: int = 500):
        """
        Initialize the trading simulator with an initial balance.

        :param initial_balance: Starting balance for the trading account.
        :param leverage: Leverage applied to the trades (default is 1:500).
        """
        self.initial_balance = initial_balance
        self.leverage = leverage
        self.current_balance = initial_balance

    def simulate_trade(self, lot_size: float, currency_pair: str):
        """
        Simulate a single forex trade using random price movements.

        :param lot_size: The lot size for the trade (e.g., 0.01, 1.0).
        :param currency_pair: Name of the currency pair being traded (e.g., 'EUR/USD').
        :return: A dictionary containing the trade result.
        """
        try:
            # Validate input parameters
            if lot_size <= 0:
                raise ValueError("Lot size must be greater than 0.")
            
            # Generate random price movement (-100 to +100 pips)
            price_movement = random.uniform(-100, 100)
            profit_loss = self.calculate_pnl(lot_size, price_movement)

            # Update the account balance
            self.current_balance += profit_loss

            # Log the result of the trade
            logging.info(f"Trade on {currency_pair} with lot size {lot_size}: "
                         f"Price Movement = {price_movement:.2f} pips, "
                         f"P/L = {profit_loss:.2f}, "
                         f"Balance = {self.current_balance:.2f}")

            return {
                "currency_pair": currency_pair,
                "lot_size": lot_size,
                "price_movement": price_movement,
                "profit_loss": profit_loss,
                "balance": self.current_balance
            }

        except Exception as e:
            logging.error(f"Error simulating trade: {str(e)}")
            return {"error": str(e)}

    def calculate_pnl(self, lot_size: float, price_movement: float):
        """
        Calculate profit or loss (P/L) for a trade.

        :param lot_size: The lot size for the trade.
        :param price_movement: The price movement in pips.
        :return: Calculated profit or loss in account currency.
        """
        # Calculate P/L using leverage
        pip_value = (lot_size * 10)  # Approximate value per pip per lot size
        return price_movement * pip_value * self.leverage

    def get_account_balance(self):
        """
        Get the current balance of the trading account.

        :return: Current account balance.
        """
        return self.current_balance


if __name__ == "__main__":
    # Initialize the trading simulator with a $10,000 account balance
    simulator = ForexTradingSimulator(initial_balance=10000.0)

    # Simulate a few trades
    trades = [
        simulator.simulate_trade(lot_size=1.0, currency_pair="EUR/USD"),
        simulator.simulate_trade(lot_size=0.5, currency_pair="USD/JPY"),
        simulator.simulate_trade(lot_size=2.0, currency_pair="GBP/USD"),
    ]

    # Print the results of the simulation
    for trade in trades:
        print(trade)

    # Display the final account balance
    print(f"Final Account Balance: ${simulator.get_account_balance():.2f}")
```
