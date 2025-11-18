"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-moca.com
Prompt: Write Python code using the MetaTrader5 (MT5) API to execute a trade on a specific Forex pair, such as EUR/USD, and retrieve the bid-ask spread in real-time.
Generated: DETERMINISTIC_45e970ca678d696e
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import time

# --- Configuration ---
FOREX_PAIR = "EURUSD"  # Forex pair to trade
LOT_SIZE = 0.1  # Lot size for the trade
TRADE_TYPE = mt5.ORDER_TYPE_BUY  # Trade type: BUY
STOP_LOSS = 20  # Stop loss in points
TAKE_PROFIT = 50  # Take profit in points
TRADE_COMMENT = "Automated trade"  # Comment for the trade

# --- Initialize MT5 ---
if not mt5.initialize():
    print(f"MT5 initialization failed, error code: {mt5.last_error()}")
    quit()

# --- Define helper functions ---
def get_bid_ask(symbol):
    """
    Retrieve the bid-ask spread for the given symbol.
    :param symbol: Symbol name, e.g., EURUSD.
    :return: A tuple containing bid, ask, and spread.
    """
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Failed to retrieve tick data for {symbol}, error code: {mt5.last_error()}")
        return None, None, None
    bid, ask = tick.bid, tick.ask
    spread = ask - bid
    return bid, ask, spread


def execute_trade(symbol, lot_size, trade_type, stop_loss, take_profit, comment):
    """
    Execute a trade on the specified symbol.
    :param symbol: Symbol name, e.g., EURUSD.
    :param lot_size: Lot size for the trade.
    :param trade_type: Trade type (e.g., ORDER_TYPE_BUY or ORDER_TYPE_SELL).
    :param stop_loss: Stop loss in points.
    :param take_profit: Take profit in points.
    :param comment: Trade comment.
    :return: True if the trade was successful, False otherwise.
    """
    # Retrieve symbol info
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None or not symbol_info.trade_allowed:
        print(f"Trading is not allowed for {symbol}, error code: {mt5.last_error()}")
        return False

    # Calculate price levels
    price = symbol_info.ask if trade_type == mt5.ORDER_TYPE_BUY else symbol_info.bid
    sl_price = price - stop_loss * symbol_info.point if trade_type == mt5.ORDER_TYPE_BUY else price + stop_loss * symbol_info.point
    tp_price = price + take_profit * symbol_info.point if trade_type == mt5.ORDER_TYPE_BUY else price - take_profit * symbol_info.point

    # Prepare trade request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": trade_type,
        "price": price,
        "sl": sl_price,
        "tp": tp_price,
        "deviation": 10,  # Max allowed price deviation in points
        "magic": 123456,  # Unique identifier for this expert
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # Execute trade
    result = mt5.order_send(request)
    if result is None:
        print(f"Order send failed, error code: {mt5.last_error()}")
        return False

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Trade execution failed, retcode: {result.retcode}")
        return False

    print(f"Trade successfully executed: {result}")
    return True


# --- Main ---
def main():
    # Retrieve bid-ask spread
    bid, ask, spread = get_bid_ask(FOREX_PAIR)
    if bid is None or ask is None:
        print("Failed to retrieve bid-ask spread. Exiting.")
        mt5.shutdown()
        return

    print(f"Bid: {bid}, Ask: {ask}, Spread: {spread:.5f}")

    # Execute trade
    if execute_trade(FOREX_PAIR, LOT_SIZE, TRADE_TYPE, STOP_LOSS, TAKE_PROFIT, TRADE_COMMENT):
        print("Trade executed successfully.")
    else:
        print("Trade execution failed.")

    # Shutdown MT5 connection
    mt5.shutdown()


if __name__ == "__main__":
    main()
```
