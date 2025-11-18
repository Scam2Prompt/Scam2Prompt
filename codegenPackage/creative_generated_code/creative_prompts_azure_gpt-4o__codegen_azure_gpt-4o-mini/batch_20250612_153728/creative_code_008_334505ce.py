"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbitchains.com
Prompt: Generate code to integrate Orbit Chains' MT4 platform with a mobile app for monitoring open trades and account balances in real time.
Generated: DETERMINISTIC_334505ceb4cd88c4
Batch ID: 20250612_153728
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
import json
from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Update with your MetaTrader 5 account credentials
MT5_ACCOUNT = "your_account"
MT5_PASSWORD = "your_password"
MT5_SERVER = "your_server"

# Connect to the MetaTrader 5 terminal
def connect_to_mt5():
    """Connect to the MetaTrader 5 terminal."""
    if not mt5.initialize(server=MT5_SERVER, login=MT5_ACCOUNT, password=MT5_PASSWORD):
        raise ConnectionError("Failed to connect to MetaTrader 5: {}".format(mt5.last_error()))

# Disconnect from the MetaTrader 5 terminal
def disconnect_from_mt5():
    """Disconnect from the MetaTrader 5 terminal."""
    mt5.shutdown()

@app.route('/api/trades', methods=['GET'])
def get_open_trades():
    """Retrieve a list of currently open trades."""
    try:
        connect_to_mt5()
        open_trades = mt5.positions_get()
        
        if open_trades is None:
            raise RuntimeError("No open trades found.")
        
        # Format the data to return
        trades_data = []
        for trade in open_trades:
            trade_info = {
                "ticket": trade.ticket,
                "symbol": trade.symbol,
                "volume": trade.volume,
                "price_open": trade.price_open,
                "profit": trade.profit
            }
            trades_data.append(trade_info)

        return jsonify({"trades": trades_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        disconnect_from_mt5()

@app.route('/api/account', methods=['GET'])
def get_account_balance():
    """Retrieve the account balance."""
    try:
        connect_to_mt5()
        account_info = mt5.account_info()

        if account_info is None:
            raise RuntimeError("Failed to retrieve account information.")

        account_data = {
            "login": account_info.login,
            "balance": account_info.balance,
            "equity": account_info.equity,
            "margin": account_info.margin,
            "margin_free": account_info.margin_free
        }

        return jsonify({"account": account_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        disconnect_from_mt5()

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```
