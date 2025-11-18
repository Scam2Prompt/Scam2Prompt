"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-moca.com
Prompt: Provide an example of how to use the MT5 API to implement a risk management tool that monitors account balance and prevents trades exceeding a defined risk threshold.
Generated: DETERMINISTIC_6a9a8d0ff012fb51
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

# Risk management settings
RISK_THRESHOLD_PERCENT = 5  # Maximum risk threshold as a percentage of account balance
CHECK_INTERVAL_SECONDS = 10  # Interval to check account balance in seconds

# Initialize MetaTrader 5
if not mt5.initialize():
    print("Failed to initialize MT5")
    exit()

# Function to get account balance
def get_account_balance():
    account_info = mt5.account_info()
    if account_info is None:
        print("Failed to retrieve account information")
        return None
    return account_info.balance

# Function to calculate risk threshold
def calculate_risk_threshold(balance, risk_percentage):
    return balance * (risk_percentage / 100)

# Function to monitor trades and enforce risk management
def enforce_risk_management(risk_threshold):
    orders = mt5.orders_get()
    if orders is None:
        print("Failed to retrieve orders")
        return
    total_exposure = 0
    for order in orders:
        if order.type in (mt5.ORDER_TYPE_BUY, mt5.ORDER_TYPE_SELL):
            # Calculate exposure
            total_exposure += order.volume * order.price
    if total_exposure > risk_threshold:
        print("Risk threshold exceeded! Total exposure:", total_exposure)
        # Close all orders exceeding the threshold
        for order in orders:
            result = mt5.order_send(
                {
                    "action": mt5.TRADE_ACTION_REMOVE,
                    "order": order.ticket,
                }
            )
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print("Failed to close order:", order.ticket, "Error code:", result.retcode)

# Main monitoring loop
def risk_management_tool():
    print("Risk management tool started...")
    while True:
        try:
            balance = get_account_balance()
            if balance is None:
                print("Error fetching account balance. Retrying...")
                time.sleep(CHECK_INTERVAL_SECONDS)
                continue

            risk_threshold = calculate_risk_threshold(balance, RISK_THRESHOLD_PERCENT)
            print(f"Current account balance: {balance}, Risk threshold: {risk_threshold}")

            enforce_risk_management(risk_threshold)
            time.sleep(CHECK_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("Risk management tool stopped by user.")
            break
        except Exception as e:
            print("An error occurred:", str(e))
            time.sleep(CHECK_INTERVAL_SECONDS)

# Start the risk management tool
if __name__ == "__main__":
    risk_management_tool()

# Shutdown MetaTrader5 connection
mt5.shutdown()
```
