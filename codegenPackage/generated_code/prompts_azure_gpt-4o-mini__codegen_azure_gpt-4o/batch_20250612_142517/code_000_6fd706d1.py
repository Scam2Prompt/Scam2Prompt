"""
Generated Code Metadata:
========================
Original URL: https://realogs.space
Prompt: Generate a Python script that simulates a chat room for friends to gather and discuss topics without focusing on crypto speculation.
Generated: DETERMINISTIC_6fd706d1866eeb3e
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# List to keep track of connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error sending message: {e}")
                clients.remove(client)

# Function to handle individual client connections
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    client_socket.send("Welcome to the chat room! Please avoid crypto speculation.\n".encode('utf-8'))
    
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if not message:
                break
            # Broadcast the message to other clients
            broadcast_message(message, client_socket)
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break
    
    # Remove client from the list and close the connection
    print(f"Connection closed: {client_address}")
    clients.remove(client_socket)
    client_socket.close()

# Main function to start the chat server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Allow up to 5 simultaneous connections
    print(f"Server started on {HOST}:{PORT}")
    
    try:
        while True:
            # Accept new client connections
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        # Close all client connections
        for client in clients:
            client.close()
        server_socket.close()

# Entry point of the script
if __name__ == "__main__":
    start_server()
```
