"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nibblesps.com
Prompt: Generate Python code to implement a WebSocket server using the Tornado framework for real-time communication.
Generated: DETERMINISTIC_d6ef969d89c3ad2d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tornado.ioloop
import tornado.web
import tornado.websocket
import json

# A list to keep track of connected clients
clients = []

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """WebSocket handler for managing connections and messages."""

    def open(self):
        """Called when a new WebSocket connection is opened."""
        print("Client connected")
        clients.append(self)

    def on_message(self, message):
        """Called when a message is received from a client."""
        print(f"Message received: {message}")
        # Broadcast the message to all connected clients
        self.broadcast_message(message)

    def on_close(self):
        """Called when the WebSocket connection is closed."""
        print("Client disconnected")
        clients.remove(self)

    @classmethod
    def broadcast_message(cls, message):
        """Sends a message to all connected clients."""
        for client in clients:
            try:
                client.write_message(message)
            except Exception as e:
                print(f"Error sending message: {e}")

def make_app():
    """Creates the Tornado application."""
    return tornado.web.Application([
        (r"/ws", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    # Set the port for the WebSocket server
    port = 8888
    app.listen(port)
    print(f"WebSocket server is running on ws://localhost:{port}/ws")
    tornado.ioloop.IOLoop.current().start()
```
