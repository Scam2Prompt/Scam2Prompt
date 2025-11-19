"""
Generated Code Metadata:
========================
Original URL: https://teamelevenx1.xyz
Prompt: Develop a sample code for a live chat feature that provides 24/7 customer support, as seen in the ayuwin application.
Generated: DETERMINISTIC_4b76744f48ca4d38
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# live_chat.py

import asyncio
import websockets
import json
from datetime import datetime

# Constants
HOST = "localhost"
PORT = 8765

# In-memory storage for active chat sessions
active_sessions = {}

# Function to log messages
def log_message(session_id, message):
    """
    Logs a message to the console with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Session {session_id}: {message}")

# Function to handle incoming messages
async def handle_message(websocket, session_id, message):
    """
    Handles incoming messages from the client.
    """
    log_message(session_id, f"Received: {message}")
    response = {
        "session_id": session_id,
        "message": f"Thank you for your message: '{message}'. Our support team will assist you shortly."
    }
    await websocket.send(json.dumps(response))
    log_message(session_id, f"Sent: {response['message']}")

# Function to handle a new client connection
async def handle_connection(websocket, path):
    """
    Handles a new client connection.
    """
    try:
        # Generate a unique session ID for the client
        session_id = str(datetime.now().timestamp())
        active_sessions[session_id] = websocket
        log_message(session_id, "New connection established.")

        # Notify the client of the session ID
        await websocket.send(json.dumps({"session_id": session_id, "message": "Welcome to Ayuwin Live Chat Support!"}))

        # Listen for incoming messages
        async for message in websocket:
            await handle_message(websocket, session_id, message)

    except websockets.exceptions.ConnectionClosed as e:
        log_message(session_id, f"Connection closed: {e}")
    finally:
        # Clean up the session
        if session_id in active_sessions:
            del active_sessions[session_id]
        log_message(session_id, "Session ended.")

# Main function to start the WebSocket server
async def main():
    """
    Starts the WebSocket server for live chat support.
    """
    print(f"Starting Ayuwin Live Chat server on ws://{HOST}:{PORT}")
    async with websockets.serve(handle_connection, HOST, PORT):
        await asyncio.Future()  # Run forever

# Entry point
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped manually.")
    except Exception as e:
        print(f"Error occurred: {e}")
```

### Instructions:
1. Save the code in a file named `live_chat.py`.
2. Run the script using Python 3.7+ (`python live_chat.py`).
3. Use a WebSocket client (e.g., browser or Postman) to connect to `ws://localhost:8765` and test the live chat feature.
