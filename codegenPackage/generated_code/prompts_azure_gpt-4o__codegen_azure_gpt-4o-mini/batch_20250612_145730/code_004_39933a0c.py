"""
Generated Code Metadata:
========================
Original URL: https://ottbangla.store
Prompt: Write a script to monitor and log activity on a LiteSpeed Web Server running on port 443.
Generated: DETERMINISTIC_39933a0c5de910ec
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import socket
import select
import time

# Configure logging
logging.basicConfig(
    filename='litespeed_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 443        # LiteSpeed Web Server port

def setup_server_socket():
    """Set up the server socket to listen for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Allow up to 5 queued connections
    logging.info(f'Server listening on {HOST}:{PORT}')
    return server_socket

def log_activity(client_socket, client_address):
    """Log the activity of a connected client."""
    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        if data:
            logging.info(f'Received data from {client_address}: {data.decode("utf-8")}')
        else:
            logging.warning(f'No data received from {client_address}. Closing connection.')
    except Exception as e:
        logging.error(f'Error while receiving data from {client_address}: {e}')
    finally:
        client_socket.close()
        logging.info(f'Connection closed for {client_address}')

def main():
    """Main function to run the LiteSpeed activity monitor."""
    server_socket = setup_server_socket()
    
    try:
        while True:
            # Use select to wait for incoming connections
            readable, _, _ = select.select([server_socket], [], [], 1)
            for s in readable:
                client_socket, client_address = s.accept()
                logging.info(f'Connection established with {client_address}')
                log_activity(client_socket, client_address)
    except KeyboardInterrupt:
        logging.info('Server shutting down.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        server_socket.close()
        logging.info('Server socket closed.')

if __name__ == '__main__':
    main()
```
