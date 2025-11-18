"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecryptex-secure.com
Prompt: Generate code to simulate CrypTEX Secure's demo account functionality, allowing users to test trading strategies with virtual funds before committing real investments.
Generated: DETERMINISTIC_e7d3bfc2c6236cc3
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemoAccount:
    """
    A class representing a CrypTEX Secure demo account for simulating virtual trading.
    Allows users to test trading strategies with virtual funds.
    """

    def __init__(self, initial_balance: float = 10000.0) -> None:
        """
        Initialize the demo account with virtual funds.
        
        :param initial_balance: The starting virtual funds for the demo account.
        """
        self.virtual_balance = initial_balance  # Virtual funds
        self.trading_history = []  # List to store simulated trades
        logging.info(f"Demo account created with initial balance: ${self.virtual_balance:.2f}")

    def place_trade(self, trade_type: str, amount: float, price: float) -> Union[Dict[str, Union[str, float]], str]:
        """
        Simulate a trade (buy or sell) using virtual funds.
        
        :param trade_type: The type of trade ('buy' or 'sell').
        :param amount: The amount of the asset to trade.
        :param price: The price per unit of the asset.
        :return: The details of the trade or an error message.
        """
        # Validate trade type
        if trade_type not in ['buy', 'sell']:
            logging.error("Invalid trade type! Use 'buy' or 'sell'.")
            return "Invalid trade type! Use 'buy' or 'sell'."

        # Calculate total trade cost
        trade_cost = amount * price

        if trade_type == 'buy':
            # Ensure sufficient virtual balance for the trade
            if trade_cost > self.virtual_balance:
                logging.error(f"Insufficient virtual funds for the trade. Current balance: ${self.virtual_balance:.2f}")
                return "Insufficient virtual funds for the trade."
            
            self.virtual_balance -= trade_cost  # Deduct trade cost from virtual balance
            logging.info(f"Buy trade executed: {amount} units at ${price:.2f} each. Remaining balance: ${self.virtual_balance:.2f}")

        elif trade_type == 'sell':
            self.virtual_balance += trade_cost  # Add trade income to virtual balance
            logging.info(f"Sell trade executed: {amount} units at ${price:.2f} each. Updated balance: ${self.virtual_balance:.2f}")

        # Record the trade
        trade_details = {
            'type': trade_type,
            'amount': amount,
            'price': price,
            'total': trade_cost
        }
        self.trading_history.append(trade_details)
        return trade_details

    def get_balance(self) -> float:
        """
        Get the current virtual balance of the demo account.
        
        :return: The current virtual balance.
        """
        logging.info(f"Current virtual balance: ${self.virtual_balance:.2f}")
        return self.virtual_balance

    def get_trading_history(self) -> list:
        """
        Get the trading history of the demo account.
        
        :return: A list of all simulated trades.
        """
        logging.info(f"Retrieved trading history. Total trades: {len(self.trading_history)}")
        return self.trading_history


if __name__ == "__main__":
    # Example usage of the DemoAccount class
    try:
        demo_account = DemoAccount(initial_balance=5000.0)  # Create a demo account with a custom initial balance
        print(demo_account.place_trade(trade_type="buy", amount=10, price=50))  # Place a buy trade
        print(demo_account.get_balance())  # Get the current balance
        print(demo_account.place_trade(trade_type="sell", amount=5, price=75))  # Place a sell trade
        print(demo_account.get_trading_history())  # Get trading history
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
