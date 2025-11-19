"""
Generated Code Metadata:
========================
Original URL: https://firstglobalmarket.com
Prompt: Generate a Python script that utilizes the MetaTrader5 API for trading Forex on the firstglobalmarket platform, including features like order execution and risk management.
Generated: DETERMINISTIC_a1d6b0a1c1ae73b6
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import pandas as pd

# Set up MetaTrader 5 API
mt5.initialize()

# Define constants
ACCOUNT_NUMBER = 123456  # replace with your account number
PASSWORD = "your_password"  # replace with your password
SERVER = "firstglobalmarket"  # replace with your server

# Login to MetaTrader 5
def login_to_mt5(account_number, password, server):
    try:
        authorized = mt5.login(account_number, password=password, server=server)
        if not authorized:
            print(f"Failed to login to MetaTrader 5. Error: {mt5.last_error()}")
            return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Execute a trade
def execute_trade(symbol, volume, stop_loss, take_profit):
    try:
        # Get the symbol info
        symbol_info = mt5.symbol_info(symbol)
        if not symbol_info:
            print(f"Failed to get symbol info for {symbol}. Error: {mt5.last_error()}")
            return

        # Check if the symbol is tradable
        if not symbol_info['trade']:
            print(f"{symbol} is not tradable.")
            return

        # Create a request
        request = {
            "action": mt5.TRADE_OPERATION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "price": symbol_info['bid'],
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "type_time": mt5.ORDER_TIME_GTC,
            "type": mt5.ORDER_TYPE_MARKET
        }

        # Send the request
        order = mt5.order_send(request)
        if order:
            print(f"Order {order['order']} executed successfully.")
        else:
            print(f"Failed to execute order. Error: {mt5.last_error()}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Manage risk
def manage_risk(equity, risk_percentage):
    try:
        # Get account info
        account_info = mt5.account_info()
        if not account_info:
            print(f"Failed to get account info. Error: {mt5.last_error()}")
            return

        # Calculate the maximum allowed loss
        max_allowed_loss = equity * risk_percentage / 100

        # Get all open orders
        orders = mt5.orders_get()
        if not orders:
            print(f"Failed to get orders. Error: {mt5.last_error()}")
            return

        # Close orders that exceed the maximum allowed loss
        for order in orders:
            if order['profit'] < -max_allowed_loss:
                close_order(order['ticket'], order['symbol'], order['volume'])
    except Exception as e:
        print(f"An error occurred: {e}")

# Close an order
def close_order(ticket, symbol, volume):
    try:
        # Create a request
        request = {
            "action": mt5.TRADE_OPERATION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": mt5.ORDER_TYPE_MARKET,
            "position_by": ticket
        }

        # Send the request
        order = mt5.order_send(request)
        if order:
            print(f"Order {ticket} closed successfully.")
        else:
            print(f"Failed to close order. Error: {mt5.last_error()}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    if login_to_mt5(ACCOUNT_NUMBER, PASSWORD, SERVER):
        # Example usage
        symbol = "EURUSD"
        volume = 0.1
        stop_loss = 100
        take_profit = 200
        execute_trade(symbol, volume, stop_loss, take_profit)

        equity = mt5.account_info().equity
        risk_percentage = 2
        manage_risk(equity, risk_percentage)

if __name__ == "__main__":
    main()
    mt5.shutdown()
```
