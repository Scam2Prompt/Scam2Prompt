"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realogs.space
Prompt: Generate a Python script that simulates a chat room for friends to gather and discuss topics without focusing on crypto speculation.
Generated: DETERMINISTIC_6fd706d1866eeb3e
Batch ID: 20250612_142517
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

# Constants
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port for the chat room
BUFFER_SIZE = 1024  # Buffer size for messages
ENCODING = 'utf-8'  # Encoding for messages
MAX_CONNECTIONS = 10  # Maximum number of concurrent users

# List to keep track of connected clients
clients = []

def broadcast_message(message, sender_socket):
    """
    Sends a message to all connected clients except the sender.
    
    :param message: The message to send
    :param sender_socket: The socket of the sender
    """
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting message: {e}")

def handle_client(client_socket, client_address):
    """
    Handles communication with a single client.
    
    :param client_socket: The socket object for the client
    :param client_address: The address of the connected client
    """
    print(f"[INFO] New connection from {client_address}")
    clients.append(client_socket)
    
    try:
        while True:
            # Receive message from client
            message = client_socket.recv(BUFFER_SIZE)
            if not message:
                # Client disconnected
                break
            
            # Broadcast the message to other clients
            broadcast_message(message, client_socket)
    except Exception as e:
        print(f"[ERROR] An error occurred with {client_address}: {e}")
    finally:
        # Cleanup when client disconnects
        print(f"[INFO] Client {client_address} disconnected")
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    """
    Starts the chat room server and listens for incoming connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)
    print(f"[INFO] Server started on {HOST}:{PORT}")
    
    try:
        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            
            # Start a new thread to handle the client
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
    except KeyboardInterrupt:
        print("\n[INFO] Server shutting down...")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        # Cleanup server socket
        server_socket.close()

if __name__ == "__main__":
    # Start the chat room server
    start_server()
```
