"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hyperliquidbridge.com
Prompt: Create a monitoring tool to track Hyperliquid Bridge metrics, including total deposits and volume bridged, in real-time.
Generated: DETERMINISTIC_297404073909653f
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready Python code for a monitoring tool to track Hyperliquid Bridge metrics, including total deposits and volume bridged in real-time. It uses Flask for the web server and WebSocket for real-time updates.

```python
from flask import Flask, jsonify
import threading
import websocket
import json

# Initialize Flask app
app = Flask(__name__)

# Global variables to store metrics
metrics = {
    "total_deposits": 0,
    "volume_bridged": 0,
}

# WebSocket URL for Hyperliquid Bridge (replace with the actual WebSocket URL)
WEBSOCKET_URL = "wss://example.hyperliquidbridge.com/metrics"

# Lock for thread-safe updates to metrics
lock = threading.Lock()

def websocket_listener():
    """
    Connect to the WebSocket server and listen for real-time updates.
    Updates are expected to be in JSON format containing 'deposit' and 'volume'.
    """
    def on_message(ws, message):
        try:
            # Parse the incoming message
            data = json.loads(message)
            deposit = data.get("deposit", 0)
            volume = data.get("volume", 0)
            
            # Update metrics safely using a lock
            with lock:
                metrics["total_deposits"] += deposit
                metrics["volume_bridged"] += volume
        except json.JSONDecodeError:
            print("Error decoding WebSocket message")
        except Exception as e:
            print(f"Error processing WebSocket message: {e}")

    def on_error(ws, error):
        print(f"WebSocket error: {error}")

    def on_close(ws, close_status_code, close_msg):
        print("WebSocket closed")

    def on_open(ws):
        print("WebSocket connection established")

    # Connect to the WebSocket server
    ws = websocket.WebSocketApp(
        WEBSOCKET_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open,
    )
    ws.run_forever()

# Start the WebSocket listener in a separate thread
threading.Thread(target=websocket_listener, daemon=True).start()

@app.route("/metrics", methods=["GET"])
def get_metrics():
    """
    Endpoint to fetch the current metrics.
    Returns a JSON response containing total deposits and volume bridged.
    """
    with lock:
        return jsonify(metrics)

if __name__ == "__main__":
    # Start the Flask app
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
1. Replace `WEBSOCKET_URL` with the actual WebSocket URL for Hyperliquid Bridge metrics.
2. Install required dependencies using `pip install flask websocket-client`.
3. To deploy in production, use `gunicorn` or another WSGI server and set up proper SSL/TLS for security.
