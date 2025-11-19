"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Explain how to implement a secure communication system between two parties, like QRubi's connection between the finder and the owner of a lost object.
Generated: DETERMINISTIC_8deffe6026e8f11d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import ssl
import threading
import json

# Constants for server configuration
HOST = 'localhost'  # Server hostname or IP address
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Function to handle client connections
def handle_client(connection, address):
    """Handles communication with a connected client."""
    print(f"Connection from {address} has been established.")
    try:
        while True:
            # Receive data from the client
            data = connection.recv(1024)
            if not data:
                break  # Exit loop if no data is received
            
            # Decode and process the received data
            message = json.loads(data.decode('utf-8'))
            print(f"Received message: {message}")

            # Here you can implement your logic to handle the message
            response = {"status": "success", "message": "Data received"}
            connection.sendall(json.dumps(response).encode('utf-8'))
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        connection.close()
        print(f"Connection from {address} has been closed.")

# Function to start the secure server
def start_secure_server():
    """Starts a secure server to handle incoming connections."""
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL
    secure_socket = ssl.wrap_socket(server_socket,
                                     keyfile="server-key.pem",
                                     certfile="server-cert.pem",
                                     server_side=True)

    # Bind the socket to the address and port
    secure_socket.bind((HOST, PORT))
    secure_socket.listen(5)  # Allow up to 5 pending connections
    print(f"Secure server is listening on {HOST}:{PORT}")

    try:
        while True:
            # Accept a new client connection
            client_connection, client_address = secure_socket.accept()
            # Handle the client in a new thread
            threading.Thread(target=handle_client, args=(client_connection, client_address)).start()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        secure_socket.close()

if __name__ == "__main__":
    start_secure_server()
```

### Notes:
- Ensure you have the necessary SSL certificate (`server-cert.pem`) and key (`server-key.pem`) files in the same directory as this script.
- This code implements a basic secure server that can handle multiple clients using threading.
- The communication is done in JSON format for easy data exchange.
- Proper error handling is included to manage exceptions during client handling and server operation.
