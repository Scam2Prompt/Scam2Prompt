"""
Generated Code Metadata:
========================
Original URL: https://tradefx.co
Prompt: Generate a script to interact with the TradeFX MetaTrader 4 API for executing trades with an ECN account, ensuring zero spread and rapid execution time of 0.13 seconds.
Generated: DETERMINISTIC_a4e9cf7ddd585b3f
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import time
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradeFXMetaTrader:
    def __init__(self, server, username, password):
        """
        Initialize the TradeFX MetaTrader 4 API connection.

        Args:
            server (str): The MetaTrader 5 server name.
            username (str): The account username.
            password (str): The account password.
        """
        self.server = server
        self.username = username
        self.password = password

        # Establish a connection to the MetaTrader 5 server
        if not mt5.initialize():
            logging.error("Failed to initialize MetaTrader 5")
            raise Exception("Failed to initialize MetaTrader 5")

        # Authenticate with the MetaTrader 5 server
        self.account = mt5.login(self.username, password=self.password, server=self.server)
        if not self.account:
            logging.error("Failed to login to MetaTrader 5")
            mt5.shutdown()
            raise Exception("Failed to login to MetaTrader 5")

    def execute_trade(self, symbol, volume, stop_loss, take_profit):
        """
        Execute a trade with the specified parameters.

        Args:
            symbol (str): The symbol of the financial instrument.
            volume (float): The trade volume.
            stop_loss (float): The stop loss price.
            take_profit (float): The take profit price.

        Returns:
            int: The ticket number of the executed trade.
        """
        # Get the current price of the symbol
        rates = mt5.symbol_info_tick(symbol)
        if not rates:
            logging.error(f"Failed to get current price for {symbol}")
            return None

        # Prepare the trade request
        request = mt5.TradeRequest()
        request.action = mt5.TRADE_OPERATION_DEAL
        request.symbol = symbol
        request.volume = volume
        request.price = rates.bid
        request.stoploss = stop_loss
        request.takeprofit = take_profit
        request.deviation = 5  # Maximum possible deviation from the requested price

        # Send the trade request
        result = mt5.send_trade_request(request)
        if result:
            logging.info(f"Trade executed successfully. Ticket: {result.order}")
            return result.order
        else:
            logging.error(f"Failed to execute trade: {mt5.get_last_error()}")
            return None

    def close_trade(self, ticket):
        """
        Close a trade with the specified ticket number.

        Args:
            ticket (int): The ticket number of the trade to close.

        Returns:
            bool: True if the trade was closed successfully, False otherwise.
        """
        # Prepare the trade request
        request = mt5.TradeRequest()
        request.action = mt5.TRADE_OPERATION_DEAL
        request.order = ticket
        request.volume = mt5.position_get(ticket).volume

        # Send the trade request
        result = mt5.send_trade_request(request)
        if result:
            logging.info(f"Trade {ticket} closed successfully")
            return True
        else:
            logging.error(f"Failed to close trade {ticket}: {mt5.get_last_error()}")
            return False

    def shutdown(self):
        """
        Shutdown the MetaTrader 5 connection.
        """
        mt5.logout()
        mt5.shutdown()


def main():
    server = "ECN-Server"
    username = "your_username"
    password = "your_password"

    trade_fx = TradeFXMetaTrader(server, username, password)

    symbol = "EURUSD"
    volume = 0.1
    stop_loss = 1.2000
    take_profit = 1.2500

    start_time = time.time()
    ticket = trade_fx.execute_trade(symbol, volume, stop_loss, take_profit)
    end_time = time.time()

    if ticket:
        logging.info(f"Execution time: {end_time - start_time:.2f} seconds")
        assert end_time - start_time <= 0.13, "Execution time exceeded 0.13 seconds"

    trade_fx.shutdown()


if __name__ == "__main__":
    main()
```
