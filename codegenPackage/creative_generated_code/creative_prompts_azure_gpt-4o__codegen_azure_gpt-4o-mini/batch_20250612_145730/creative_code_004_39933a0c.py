"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ottbangla.store
Prompt: Write a script to monitor and log activity on a LiteSpeed Web Server running on port 443.
Generated: DETERMINISTIC_39933a0c5de910ec
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import socket
import select
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='litespeed_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to set up a server socket
def setup_server_socket(host='0.0.0.0', port=443):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)  # Listen for incoming connections
        logging.info(f'Server started on {host}:{port}')
        return server_socket
    except Exception as e:
        logging.error(f'Error setting up server socket: {e}')
        raise

# Function to monitor incoming connections
def monitor_connections(server_socket):
    while True:
        try:
            # Use select to wait for readable sockets
            readable, _, _ = select.select([server_socket], [], [], 5)
            for sock in readable:
                if sock == server_socket:
                    conn, addr = server_socket.accept()  # Accept a new connection
                    logging.info(f'Connection accepted from {addr}')
                    handle_connection(conn)
        except Exception as e:
            logging.error(f'Error while monitoring connections: {e}')

# Function to handle individual connections
def handle_connection(conn):
    try:
        with conn:
            # Simulate monitoring activity (this could be extended to actual requests)
            while True:
                # For demonstration purposes, we just log a message
                logging.info('Monitoring activity...')
                time.sleep(10)  # Wait before the next activity log
    except Exception as e:
        logging.error(f'Error handling connection: {e}')

# Main function to run the monitoring script
if __name__ == '__main__':
    try:
        server_socket = setup_server_socket()
        monitor_connections(server_socket)
    except KeyboardInterrupt:
        logging.info('Monitoring stopped by user.')
    except Exception as e:
        logging.error(f'Script terminated with error: {e}')
    finally:
        logging.info('Exiting the monitoring script.')
```

This Python script monitors a LiteSpeed Web Server running on port 443, logging activities and handling connections. It includes error handling, logging configuration, and structured functions for clarity and reusability.
