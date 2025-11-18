"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Generate Python code to set up remote support functionality for a retail IT system, inspired by Retail Tech Solutions' "Remote Support on Demand" feature.
Generated: DETERMINISTIC_01c5d047c58592af
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import threading
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RemoteSupportServer:
    def __init__(self, host='0.0.0.0', port=5000):
        """Initialize the server with host and port."""
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        """Start the remote support server."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logging.info(f'Server started on {self.host}:{self.port}')
            self.accept_connections()
        except Exception as e:
            logging.error(f'Error starting server: {e}')
            if self.server_socket:
                self.server_socket.close()

    def accept_connections(self):
        """Accept incoming client connections."""
        while True:
            try:
                client_socket, addr = self.server_socket.accept()
                logging.info(f'Connection established with {addr}')
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
            except Exception as e:
                logging.error(f'Error accepting connections: {e}')

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    logging.info('Client disconnected')
                    break
                logging.info(f'Received message: {message}')
                response = self.process_message(message)
                client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            logging.error(f'Error handling client: {e}')
        finally:
            client_socket.close()

    def process_message(self, message):
        """Process the incoming message and respond accordingly."""
        try:
            data = json.loads(message)
            action = data.get('action')
            if action == 'request_support':
                return json.dumps({'status': 'success', 'message': 'Support session initiated.'})
            else:
                return json.dumps({'status': 'error', 'message': 'Unknown action.'})
        except json.JSONDecodeError:
            logging.error('Received invalid JSON format')
            return json.dumps({'status': 'error', 'message': 'Invalid JSON format.'})

if __name__ == "__main__":
    server = RemoteSupportServer()
    server.start()
```

Make sure to run this script in an appropriate environment where you have permissions to bind to the specified host and port.
