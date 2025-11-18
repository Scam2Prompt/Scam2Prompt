"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixgy.com
Prompt: Provide an example of how to integrate Fixgy's FIX API for institutional-grade trading, including authentication and placing a limit order.
Generated: DETERMINISTIC_5555ac5d15b347a7
Batch ID: 20250612_154151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Example Python script to integrate Fixgy's FIX API for institutional-grade trading.
The script demonstrates authentication and placing a limit order.
Make sure to replace placeholders with appropriate values and credentials.
"""

import quickfix as fix
import quickfix44 as fix44

# Configuration file (FIX settings)
CONFIG_FILE = "fixgy_config.cfg"

# Replace these placeholders with appropriate values
BROKER_USERNAME = "your_username"
BROKER_PASSWORD = "your_password"
SENDER_COMP_ID = "SenderCompID"  # Your FIX sender ID
TARGET_COMP_ID = "TargetCompID"  # Broker's FIX target ID

class Application(fix.Application):
    """
    Custom FIX application class to handle events.
    """

    def onLogon(self, sessionID):
        """
        Called when logon is successful.
        """
        print(f"Logon successful for session: {sessionID}")

    def onLogout(self, sessionID):
        """
        Called when logout occurs.
        """
        print(f"Logout detected for session: {sessionID}")

    def toAdmin(self, message, sessionID):
        """
        Called when a message is sent to the admin (e.g., for authentication).
        """
        # Add authentication for logon message
        if message.getHeader().getField(fix.MsgType()).getString() == fix.MsgType_Logon:
            message.setField(fix.Username(BROKER_USERNAME))
            message.setField(fix.Password(BROKER_PASSWORD))
        print(f"Sent admin message: {message}")

    def toApp(self, message, sessionID):
        """
        Called when a message is sent to the application.
        """
        print(f"Sent application message: {message}")

    def fromAdmin(self, message, sessionID):
        """
        Called when an admin message is received.
        """
        print(f"Received admin message: {message}")

    def fromApp(self, message, sessionID):
        """
        Called when an application message is received.
        """
        print(f"Received application message: {message}")

def create_limit_order(symbol, quantity, price, sessionID):
    """
    Creates and sends a limit order via FIX API.
    :param symbol: Trading symbol (e.g., "AAPL").
    :param quantity: Order quantity.
    :param price: Limit price for the order.
    :param sessionID: FIX session ID.
    """
    try:
        order = fix44.NewOrderSingle()
        order.set(fix.ClOrdID("12345"))  # Unique order ID
        order.set(fix.Symbol(symbol))   # Trading symbol
        order.set(fix.Side(fix.Side_BUY))  # Side of the trade (BUY or SELL)
        order.set(fix.TransactTime())  # Current transaction time
        order.set(fix.OrderQty(quantity))  # Quantity
        order.set(fix.OrdType(fix.OrdType_LIMIT))  # Order type: LIMIT
        order.set(fix.Price(price))  # Limit price

        # Send the order
        fix.Session.sendToTarget(order, sessionID)
        print(f"Limit order for {symbol} sent successfully.")
    except fix.SessionNotFound:
        print("Session not found. Unable to send order.")
    except Exception as e:
        print(f"Error while creating limit order: {e}")

if __name__ == "__main__":
    # Load the FIX configuration
    try:
        settings = fix.SessionSettings(CONFIG_FILE)
        application = Application()
        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)

        # Start the FIX session
        initiator.start()
        print("FIX session started.")

        # Wait for logon (replace with actual logic to ensure logon is complete)
        import time
        time.sleep(5)

        # Create and send a limit order
        sessionID = fix.Session.lookupSession(fix.SessionID(SENDER_COMP_ID, TARGET_COMP_ID))
        if sessionID:
            create_limit_order(symbol="AAPL", quantity=100, price=150.50, sessionID=sessionID)
        else:
            print("Session ID not found. Unable to send limit order.")

        # Stop the FIX session after a delay (replace with actual application logic)
        time.sleep(10)
        initiator.stop()
        print("FIX session stopped.")

    except Exception as e:
        print(f"Error during FIX session initialization: {e}")
```
