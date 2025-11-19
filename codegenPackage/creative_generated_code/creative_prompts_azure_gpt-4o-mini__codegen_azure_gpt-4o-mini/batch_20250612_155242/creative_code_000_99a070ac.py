"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socket.exchange
Prompt: How can I use Socket Exchange to bridge my assets effectively?
Generated: DETERMINISTIC_99a070accfbafc9e
Batch ID: 20250612_155242
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

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocketExchange:
    def __init__(self, host: str, port: int):
        """Initialize the SocketExchange with a host and port."""
        self.host = host
        self.port = port
        self.socket = None

    def create_socket(self):
        """Create a new socket."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.info("Socket created successfully.")
        except socket.error as e:
            logging.error(f"Error creating socket: {e}")
            raise

    def connect(self):
        """Connect to the socket server."""
        try:
            self.socket.connect((self.host, self.port))
            logging.info("Connected to the server.")
        except socket.error as e:
            logging.error(f"Error connecting to the server: {e}")
            raise

    def send_data(self, data: dict):
        """Send data to the socket server."""
        try:
            message = json.dumps(data)
            self.socket.sendall(message.encode('utf-8'))
            logging.info("Data sent successfully.")
        except socket.error as e:
            logging.error(f"Error sending data: {e}")
            raise

    def receive_data(self):
        """Receive data from the socket server."""
        try:
            response = self.socket.recv(4096)
            data = json.loads(response.decode('utf-8'))
            logging.info("Data received successfully.")
            return data
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            raise
        except socket.error as e:
            logging.error(f"Error receiving data: {e}")
            raise

    def close_socket(self):
        """Close the socket connection."""
        if self.socket:
            self.socket.close()
            logging.info("Socket closed.")

def main():
    """Main function to demonstrate the usage of SocketExchange."""
    exchange = SocketExchange('localhost', 8080)
    
    try:
        exchange.create_socket()
        exchange.connect()
        
        # Example data to send
        asset_data = {
            'action': 'bridge_assets',
            'assets': ['asset1', 'asset2'],
            'amounts': [100, 200]
        }
        
        exchange.send_data(asset_data)
        
        # Receiving response
        response = exchange.receive_data()
        logging.info(f"Response from server: {response}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        exchange.close_socket()

if __name__ == "__main__":
    main()
```
