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
import socket
import json
import logging
from time import sleep

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FixApiClient:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.socket = None
        self.session_id = None

    def connect(self):
        """Establish a connection to the FIX API server."""
        try:
            self.socket = socket.create_connection((self.host, self.port))
            logging.info("Connected to FIX API server at %s:%d", self.host, self.port)
            self.authenticate()
        except Exception as e:
            logging.error("Failed to connect: %s", str(e))
            raise

    def authenticate(self):
        """Authenticate the user with the FIX API using provided credentials."""
        auth_message = {
            "username": self.username,
            "password": self.password
        }
        self.send_message("AUTHENTICATE", auth_message)

    def send_message(self, message_type: str, payload: dict):
        """Send a message to the FIX API server."""
        message = {
            "type": message_type,
            "payload": payload
        }
        logging.info("Sending message: %s", message)
        self.socket.sendall(json.dumps(message).encode('utf-8'))

    def receive_message(self):
        """Receive a message from the FIX API server."""
        response = self.socket.recv(4096).decode('utf-8')
        logging.info("Received message: %s", response)
        return json.loads(response)

    def place_limit_order(self, symbol: str, quantity: int, price: float):
        """Place a limit order via the FIX API."""
        order_message = {
            "action": "NEW_ORDER",
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "order_type": "LIMIT"
        }
        self.send_message("ORDER", order_message)
        response = self.receive_message()
        return response

    def close(self):
        """Close the connection to the FIX API server."""
        if self.socket:
            self.socket.close()
            logging.info("Connection closed.")

if __name__ == "__main__":
    # Example usage
    HOST = "api.fixgy.com"
    PORT = 9876
    USERNAME = "your_username"
    PASSWORD = "your_password"

    try:
        client = FixApiClient(HOST, PORT, USERNAME, PASSWORD)
        client.connect()
        
        # Place a limit order
        symbol = "AAPL"
        quantity = 10
        price = 150.00
        order_response = client.place_limit_order(symbol, quantity, price)
        logging.info("Order response: %s", order_response)

    except Exception as e:
        logging.error("An error occurred: %s", str(e))

    finally:
        client.close()
```
