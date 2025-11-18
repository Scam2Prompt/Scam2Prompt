"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Write a script to monitor and log requests to a LiteSpeed Web Server running on port 443.
Generated: DETERMINISTIC_f7efa21751706416
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import datetime
import os

# Constants
LOG_FILE = "litespeed_requests.log"  # File to store logs
SERVER_IP = "0.0.0.0"  # Listen on all available network interfaces
SERVER_PORT = 443      # Port to monitor (default HTTPS port)

def setup_logging():
    """Ensure the log file exists and is writable."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("LiteSpeed Web Server Request Log\n")
            f.write("=" * 50 + "\n")

def log_request(ip, data):
    """
    Log the request details to the log file.
    
    :param ip: IP address of the client.
    :param data: Data received from the client.
    """
    try:
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.datetime.now()} - IP: {ip} - Data: {data}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def monitor_litespeed():
    """
    Start monitoring LiteSpeed Web Server traffic on port 443.
    """
    # Create a socket for listening to incoming connections
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_IP, SERVER_PORT))
        server_socket.listen(5)  # Listen for up to 5 simultaneous connections
        print(f"Monitoring LiteSpeed Web Server traffic on port {SERVER_PORT}...")
    except Exception as e:
        print(f"Failed to set up server socket: {e}")
        return
    
    while True:
        try:
            # Accept connection from client
            client_socket, client_address = server_socket.accept()
            print(f"Connection received from {client_address}")
            
            # Read data from client
            data = client_socket.recv(1024).decode("utf-8")  # Read up to 1024 bytes
            log_request(client_address[0], data)  # Log the request
            
            # Respond to the client (optional)
            response = "HTTP/1.1 200 OK\r\n\r\nLiteSpeed Web Server Monitor Active"
            client_socket.sendall(response.encode("utf-8"))
            
            # Close connection
            client_socket.close()
        except KeyboardInterrupt:
            print("\nShutting down monitor.")
            break
        except Exception as e:
            print(f"Error handling request: {e}")

if __name__ == "__main__":
    setup_logging()
    monitor_litespeed()
```
