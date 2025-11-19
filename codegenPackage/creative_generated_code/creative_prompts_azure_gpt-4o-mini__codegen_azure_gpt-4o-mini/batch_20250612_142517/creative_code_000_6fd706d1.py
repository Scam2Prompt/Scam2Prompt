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

# Constants for the server
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def handle_client_connection(client_socket, address):
    """Handles communication with a connected client."""
    print(f"[NEW CONNECTION] {address} connected.")
    
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # If message is empty, the client has disconnected
                break
            
            # Print the received message to console
            print(f"[{address}] {message}")
            
            # Broadcast the message to all connected clients
            broadcast(message, client_socket)
        
        except Exception as e:
            print(f"[ERROR] {e}")
            break
    
    # Clean up after the client disconnects
    client_socket.close()
    print(f"[DISCONNECTED] {address} disconnected.")

def broadcast(message, sender_socket):
    """Broadcasts a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"[ERROR] Failed to send message to {client}: {e}")
                client.close()
                clients.remove(client)

# List to keep track of connected clients
clients = []

def start_server():
    """Starts the chat room server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[STARTING] Chat server is starting on {HOST}:{PORT}")

    while True:
        try:
            # Accept new client connections
            client_socket, address = server_socket.accept()
            clients.append(client_socket)

            # Start a new thread for the client
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, address))
            client_thread.start()
        except KeyboardInterrupt:
            print("[SHUTTING DOWN] Chat server is shutting down.")
            break
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")

    # Clean up server resources
    for client in clients:
        client.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
```

This code creates a simple chat room server that allows multiple clients to connect and exchange messages. It handles new connections in separate threads and broadcasts messages while handling errors gracefully.
