"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tyrioncapital.com
Prompt: Write Python code to interact with the MetaTrader5 API and execute trades using the account types and leverage options provided by Tyrion Capital. Include functionality to calculate profitability based on spreads and leverage.
Generated: DETERMINISTIC_222bcb8094f9b10b
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetaTrader5Client:
    def __init__(self, account, password, server):
        """
        Initialize the MetaTrader5 client.

        :param account: Trader's account number
        :param password: Account password
        :param server: Server name
        """
        self.account = account
        self.password = password
        self.server = server
        self.connected = False

    def connect(self):
        """Connect to the MetaTrader5 server."""
        if not mt5.initialize():
            logging.error("Initialization failed: {}".format(mt5.last_error()))
            return False
        
        if not mt5.login(self.account, self.password, self.server):
            logging.error("Login failed: {}".format(mt5.last_error()))
            return False
        
        self.connected = True
        logging.info("Connected to MetaTrader5 successfully.")
        return True

    def disconnect(self):
        """Disconnect from the MetaTrader5 server."""
        if self.connected:
            mt5.shutdown()
            self.connected = False
            logging.info("Disconnected from MetaTrader5.")

    def execute_trade(self, symbol, lot_size, order_type):
        """
        Execute a trade on the MetaTrader5 platform.

        :param symbol: Trading symbol (e.g., "EURUSD")
        :param lot_size: Size of the trade in lots
        :param order_type: Type of order (0 for buy, 1 for sell)
        :return: True if trade was successful, False otherwise
        """
        if not self.connected:
            logging.error("Not connected to MetaTrader5. Cannot execute trade.")
            return False

        price = mt5.symbol_info_tick(symbol).ask if order_type == 0 else mt5.symbol_info_tick(symbol).bid

        trade_request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot_size,
            "type": order_type,
            "price": price,
            "sl": 0,
            "tp": 0,
            "deviation": 10,
            "magic": 0,
            "comment": "Trade executed via MetaTrader5Client",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC
        }

        result = mt5.order_send(trade_request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logging.error("Trade failed: {}".format(result.retcode))
            return False
        
        logging.info("Trade executed: {}".format(result))
        return True
    
    def calculate_profitability(self, entry_price, exit_price, lot_size, spread, leverage):
        """
        Calculate profitability based on entry and exit prices, lot size, spread, and leverage.

        :param entry_price: Price at which the trade was entered
        :param exit_price: Price at which the trade was exited
        :param lot_size: Size of the trade in lots
        :param spread: Spread in pips
        :param leverage: Leverage ratio
        :return: Profitability in account currency
        """
        # Calculate profit in pips
        profit_pips = (exit_price - entry_price) * (10 ** 5) - spread  # Assuming 5 decimal places for forex pairs
        profit = profit_pips * lot_size * leverage  # Calculate profit in account currency
        
        return profit

# Example usage
if __name__ == "__main__":
    account_number = 123456
    account_password = "your_password"
    server_name = "MetaQuotes-Demo"

    client = MetaTrader5Client(account_number, account_password, server_name)

    if client.connect():
        symbol = "EURUSD"
        lot_size = 0.1
        order_type = 0  # 0 for buy, 1 for sell

        if client.execute_trade(symbol, lot_size, order_type):
            # Example values for calculating profitability
            entry = 1.1000  # Sample entry price
            exit = 1.1050   # Sample exit price
            spread = 1      # Sample spread in pips
            leverage = 100  # Sample leverage

            profit = client.calculate_profitability(entry, exit, lot_size, spread, leverage)
            logging.info("Calculated Profit: {:.2f}".format(profit))
        
        client.disconnect()
```
