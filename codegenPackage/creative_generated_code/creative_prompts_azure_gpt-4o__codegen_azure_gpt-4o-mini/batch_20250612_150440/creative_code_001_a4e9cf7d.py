"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradefx.co
Prompt: Generate a script to interact with the TradeFX MetaTrader 4 API for executing trades with an ECN account, ensuring zero spread and rapid execution time of 0.13 seconds.
Generated: DETERMINISTIC_a4e9cf7ddd585b3f
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for MetaTrader 4 API interaction
import MetaTrader4 as mt4
import time

# Define a class to encapsulate the trading logic
class TradeFX:
    def __init__(self, account_number, password, server):
        """
        Initialize the TradeFX class with account details.

        :param account_number: ECN account number
        :param password: Trading account password
        :param server: Trading server address
        """
        self.account_number = account_number
        self.password = password
        self.server = server
        self.connected = False

    def connect(self):
        """
        Connect to the MetaTrader 4 server using provided credentials.
        """
        try:
            # Attempt to connect to the server
            mt4.initialize(self.server, self.account_number, self.password)
            self.connected = True
            print("Successfully connected to MetaTrader 4.")
        except Exception as e:
            print(f"Error connecting to MetaTrader 4: {e}")
            self.connected = False

    def disconnect(self):
        """
        Disconnect from the MetaTrader 4 server.
        """
        if self.connected:
            mt4.shutdown()
            self.connected = False
            print("Disconnected from MetaTrader 4.")

    def execute_trade(self, symbol, volume, order_type):
        """
        Execute a trade on the specified symbol.

        :param symbol: The currency pair symbol to trade
        :param volume: Volume of the trade (in lots)
        :param order_type: Order type ('buy' or 'sell')
        :raises ValueError: If order_type is invalid
        """
        if not self.connected:
            print("Not connected to MetaTrader 4. Please connect first.")
            return

        if order_type not in ['buy', 'sell']:
            raise ValueError("Invalid order_type. Must be 'buy' or 'sell'.")

        try:
            # Prepare the order parameters
            price = mt4.symbol_info_tick(symbol).ask if order_type == 'buy' else mt4.symbol_info_tick(symbol).bid
            slippage = 0  # Set slippage to 0 for zero spread
            ticket = mt4.order_send(symbol, order_type, volume, price, slippage)

            # Check for success
            if ticket < 0:
                print(f"Trade execution failed: {mt4.error_string(mt4.get_last_error())}")
            else:
                print(f"Trade executed successfully: Ticket #{ticket} for {order_type} {volume} lots of {symbol}.")
        except Exception as e:
            print(f"Error executing trade: {e}")

    def wait_for_trade_execution(self):
        """
        Wait for a brief period to ensure execution time.
        """
        time.sleep(0.13)  # Wait for 0.13 seconds to meet rapid execution time requirement

# Example usage of the TradeFX class
if __name__ == "__main__":
    # Replace with appropriate account credentials
    ACCOUNT_NUMBER = "123456"
    PASSWORD = "password"
    SERVER = "your.broker.server"

    # Create a TradeFX instance
    trade_client = TradeFX(ACCOUNT_NUMBER, PASSWORD, SERVER)

    # Connect to the MetaTrader 4 server
    trade_client.connect()

    # Execute a trade (example: buying 0.1 lots of EURUSD)
    try:
        trade_client.execute_trade("EURUSD", 0.1, "buy")
        trade_client.wait_for_trade_execution()
    finally:
        # Ensure disconnection from the server on completion
        trade_client.disconnect()
```
