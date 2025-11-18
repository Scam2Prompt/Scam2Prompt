"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain.tryethernal.com
Prompt: Provide an example of using the Ethernal API to monitor real-time updates on Ethereum network activity.
Generated: DETERMINISTIC_056bdfa7b95344d0
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import websocket
import json
import threading

# Ethernal API endpoint for WebSocket connection
ETHERNAL_WS_URL = "wss://api.ethernal.io/v1/subscriptions"

# Function to handle incoming WebSocket messages
def on_message(ws, message):
    """
    Callback function that is called when a message is received from the WebSocket.
    
    Args:
        ws (WebSocket): The WebSocket connection instance.
        message (str): The message received from the server.
    """
    try:
        # Parse the incoming message as JSON
        data = json.loads(message)
        # Log the received data
        print("Received data:", data)
    except json.JSONDecodeError:
        print("Error decoding JSON:", message)

# Function to handle WebSocket errors
def on_error(ws, error):
    """
    Callback function that is called when an error occurs on the WebSocket.
    
    Args:
        ws (WebSocket): The WebSocket connection instance.
        error (str): The error message.
    """
    print("WebSocket error:", error)

# Function to handle WebSocket closure
def on_close(ws, close_status_code, close_msg):
    """
    Callback function that is called when the WebSocket connection is closed.
    
    Args:
        ws (WebSocket): The WebSocket connection instance.
        close_status_code (int): The code indicating why the connection was closed.
        close_msg (str): The message describing the closure.
    """
    print("WebSocket closed:", close_status_code, close_msg)

# Function to handle WebSocket opening
def on_open(ws):
    """
    Callback function that is called when the WebSocket connection is opened.
    
    Args:
        ws (WebSocket): The WebSocket connection instance.
    """
    print("WebSocket connection opened.")
    # Subscribe to Ethereum network activity updates
    subscribe_message = {
        "type": "subscribe",
        "channel": "eth_newPendingTransactions"  # Example channel for pending transactions
    }
    ws.send(json.dumps(subscribe_message))

def run_websocket():
    """
    Function to run the WebSocket connection in a separate thread.
    """
    # Create a WebSocket application and set callbacks
    ws = websocket.WebSocketApp(
        ETHERNAL_WS_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    # Run the WebSocket
    ws.run_forever()

if __name__ == "__main__":
    # Start the WebSocket connection in a new thread
    websocket_thread = threading.Thread(target=run_websocket)
    websocket_thread.start()
```
