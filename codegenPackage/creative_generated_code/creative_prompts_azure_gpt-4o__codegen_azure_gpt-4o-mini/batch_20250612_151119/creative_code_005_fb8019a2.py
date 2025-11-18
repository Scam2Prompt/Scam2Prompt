"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jsmarketnow.com
Prompt: Create an algorithm to monitor and alert on price movements for commodities and stocks listed on 嘉盛外汇集团's MT5 platform.
Generated: DETERMINISTIC_fb8019a273a7a425
Batch ID: 20250612_151119
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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration for email alerts
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
ALERT_RECEIVER = "receiver_email@example.com"

# Configuration for price alerts
PRICE_THRESHOLD = 1.05  # Example threshold for price movement
CHECK_INTERVAL = 60  # Check every 60 seconds

# Initialize the MT5 connection
if not mt5.initialize():
    print("MT5 Initialization failed")
    mt5.shutdown()

def send_email_alert(stock_name, old_price, new_price):
    """Send an email alert for price movement."""
    subject = f"Price Alert for {stock_name}"
    body = f"The price of {stock_name} has moved from {old_price} to {new_price}."
    
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ALERT_RECEIVER
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Alert email sent for {stock_name}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_price(symbol):
    """Monitor the price of a given stock or commodity."""
    previous_price = None

    while True:
        # Get the latest price for the symbol
        prices = mt5.symbol_info_tick(symbol)
        
        if prices is None:
            print(f"Failed to get price for {symbol}.")
            time.sleep(CHECK_INTERVAL)
            continue

        current_price = prices.last

        # Check if we have a previous price to compare
        if previous_price is not None:
            # Check for price movement
            if abs(current_price - previous_price) / previous_price >= PRICE_THRESHOLD:
                send_email_alert(symbol, previous_price, current_price)

        previous_price = current_price
        time.sleep(CHECK_INTERVAL)

def main():
    """Main function to run the price monitoring."""
    commodities_and_stocks = ["AAPL", "GOOGL", "BTCUSD"]  # Add desired symbols here

    for symbol in commodities_and_stocks:
        monitor_price(symbol)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Price monitoring stopped.")
    finally:
        mt5.shutdown()
```
