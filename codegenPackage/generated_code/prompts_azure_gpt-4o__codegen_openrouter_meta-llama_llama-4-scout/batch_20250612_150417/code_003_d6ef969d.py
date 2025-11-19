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
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

class WebSocketServer(tornado.websocket.WebSocketHandler):
    """WebSocket server handler."""

    def open(self):
        """Handle WebSocket connection open."""
        logging.info("Client connected")
        self.write_message("You are connected")

    def on_message(self, message):
        """Handle incoming message from client."""
        logging.info(f"Received message: {message}")
        self.write_message(f"Server received: {message}")

    def on_close(self):
        """Handle WebSocket connection close."""
        logging.info("Client disconnected")

    def on_error(self, status_code, reason):
        """Handle WebSocket error."""
        logging.error(f"WebSocket error: {status_code} - {reason}")


class MainHandler(tornado.web.RequestHandler):
    """Main request handler."""

    def get(self):
        """Handle GET request."""
        self.write("Welcome to the WebSocket server")


def make_app():
    """Create Tornado application."""
    return tornado.web.Application([
        (r"/websocket", WebSocketServer),
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    try:
        app = make_app()
        app.listen(8888)
        logging.info("WebSocket server listening on port 8888")
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        logging.error(f"Error starting server: {e}")
```
