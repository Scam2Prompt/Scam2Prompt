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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """
    WebSocketHandler to handle WebSocket connections and communication.
    """

    # Store connected clients
    connected_clients = set()

    def open(self):
        """
        Called when a new WebSocket connection is opened.
        """
        self.connected_clients.add(self)
        logging.info(f"New client connected. Total connected clients: {len(self.connected_clients)}")
        self.write_message("Welcome to the WebSocket server!")

    def on_message(self, message):
        """
        Called when the WebSocket receives a new message from the client.

        :param message: The message received from the client.
        """
        logging.info(f"Message received: {message}")
        # Broadcast the received message to all connected clients
        for client in self.connected_clients:
            if client != self:  # Avoid echoing back to the sender
                client.write_message(message)

    def on_close(self):
        """
        Called when the WebSocket connection is closed.
        """
        self.connected_clients.remove(self)
        logging.info(f"Client disconnected. Total connected clients: {len(self.connected_clients)}")

    def check_origin(self, origin):
        """
        Override to enable support for cross-origin WebSocket connections.
        This is a security measure; allow only trusted origins in production.

        :param origin: The origin of the request.
        :return: True to accept the connection, False to reject it.
        """
        return True  # Allow all origins (for development purposes)


class MainHandler(tornado.web.RequestHandler):
    """
    HTTP handler for the root URL.
    """

    def get(self):
        """
        Handle GET requests to the root URL.
        """
        self.write("Welcome to the Tornado WebSocket server!")


def make_app():
    """
    Create a Tornado application with the necessary routes.

    :return: A Tornado web application instance.
    """
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WebSocketHandler),
    ])


if __name__ == "__main__":
    # Define the port to listen on
    PORT = 8888

    # Create the application
    app = make_app()

    # Start the application on the specified port
    app.listen(PORT)
    logging.info(f"WebSocket server started on ws://localhost:{PORT}/ws")

    # Start the Tornado I/O loop
    tornado.ioloop.IOLoop.current().start()
```
