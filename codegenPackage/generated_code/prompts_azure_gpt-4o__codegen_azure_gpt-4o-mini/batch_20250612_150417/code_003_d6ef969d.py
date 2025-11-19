"""
Generated Code Metadata:
========================
Original URL: https://nibblesps.com
Prompt: Generate Python code to implement a WebSocket server using the Tornado framework for real-time communication.
Generated: DETERMINISTIC_d6ef969d89c3ad2d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# WebSocket clients storage
clients = set()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """Handles WebSocket connections and communication."""

    def open(self):
        """Called when a new WebSocket connection is opened."""
        clients.add(self)
        logging.info("WebSocket opened: %s", self.request.remote_ip)

    def on_message(self, message):
        """Called when a message is received from a client."""
        logging.info("Message received: %s", message)
        self.broadcast(message)

    def on_close(self):
        """Called when the WebSocket connection is closed."""
        clients.remove(self)
        logging.info("WebSocket closed: %s", self.request.remote_ip)

    @classmethod
    def broadcast(cls, message):
        """Sends a message to all connected clients."""
        for client in clients:
            try:
                client.write_message(message)
            except Exception as e:
                logging.error("Error sending message to client: %s", e)

def make_app():
    """Creates the Tornado application with routing."""
    return tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    # Start the Tornado server
    app = make_app()
    app.listen(8888)
    logging.info("WebSocket server started on ws://localhost:8888/websocket")
    tornado.ioloop.IOLoop.current().start()
```
