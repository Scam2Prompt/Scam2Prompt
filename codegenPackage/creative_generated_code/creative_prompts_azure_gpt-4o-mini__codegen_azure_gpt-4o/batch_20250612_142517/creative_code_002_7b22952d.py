"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realogs.space
Prompt: Write a code snippet for a simple chat application that allows users to share thoughts and ideas without the distraction of financial discussions.
Generated: DETERMINISTIC_7b22952df55050f4
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

# Server constants
HOST = '127.0.0.1'  # localhost
PORT = 12345        # Port for the chat application

# List of forbidden words (e.g., financial discussions)
FORBIDDEN_WORDS = ['money', 'finance', 'dollar', 'pay']

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"[INFO] Connection established with {client_address}")
    
    try:
        client_socket.send("Welcome to the chat! Please avoid discussing financial topics.\n".encode('utf-8'))
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            
            if not message:  # Handle client disconnect
                print(f"[INFO] {client_address} disconnected.")
                break
            
            # Check for forbidden words
            if any(word in message.lower() for word in FORBIDDEN_WORDS):
                client_socket.send("Message contains forbidden words. Please follow the rules.\n".encode('utf-8'))
                continue
            
            # Broadcast the message to the chat
            broadcast_message(f"{client_address}: {message}", client_socket)
    except Exception as e:
        print(f"[ERROR] Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

# Function to broadcast messages to all connected clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:  # Do not send the message back to the sender
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"[ERROR] Failed to send message to a client: {e}")
                clients.remove(client)

# Main server function
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[INFO] Server started on {HOST}:{PORT}")
    
    try:
        while True:
            # Accept incoming client connections
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            
            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("[INFO] Server shutting down...")
    except Exception as e:
        print(f"[ERROR] Server error: {e}")
    finally:
        server_socket.close()

# Global list of connected clients
clients = []

if __name__ == '__main__':
    start_server()
```
