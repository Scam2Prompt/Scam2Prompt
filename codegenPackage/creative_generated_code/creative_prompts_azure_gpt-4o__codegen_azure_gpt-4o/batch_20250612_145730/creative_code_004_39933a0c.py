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
import os
import logging
import socket
from datetime import datetime

# Configure logging
LOG_FILENAME = "litespeed_activity.log"
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Constants for monitoring
LITESPEED_PORT = 443
BUFFER_SIZE = 1024
MONITOR_HOST = '0.0.0.0'  # Listen on all available interfaces

def start_monitoring():
    """
    Start monitoring LiteSpeed Web Server activity on port 443
    and log all connections and activities.
    """
    # Create a socket to monitor traffic
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((MONITOR_HOST, LITESPEED_PORT))
        server_socket.listen(5)  # Allow up to 5 simultaneous connections
        logging.info("Started monitoring LiteSpeed Web Server on port %d", LITESPEED_PORT)
    except Exception as e:
        logging.error("Failed to initialize monitoring: %s", str(e))
        return

    try:
        while True:
            # Wait for a client connection
            client_socket, client_address = server_socket.accept()
            logging.info("Connection established from %s", client_address)

            try:
                # Log incoming data from the client
                data = client_socket.recv(BUFFER_SIZE)
                if data:
                    logging.info("Data received from %s: %s", client_address, data.decode('utf-8', errors='replace'))

                # Respond to the client (optional: can be removed if unnecessary)
                client_socket.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n")
            except Exception as e:
                logging.error("Error handling client %s: %s", client_address, str(e))
            finally:
                # Close the client connection
                client_socket.close()
                logging.info("Connection closed with %s", client_address)
    except KeyboardInterrupt:
        # Allow graceful shutdown on keyboard interrupt
        logging.info("Shutting down monitoring due to KeyboardInterrupt")
    except Exception as e:
        logging.error("Unexpected error: %s", str(e))
    finally:
        # Ensure the server socket is properly closed
        server_socket.close()
        logging.info("Server socket closed. Monitoring stopped.")

if __name__ == "__main__":
    # Check for root privileges since port 443 requires it
    if os.geteuid() != 0:
        print("This script must be run as root to monitor port 443.")
    else:
        start_monitoring()
```
