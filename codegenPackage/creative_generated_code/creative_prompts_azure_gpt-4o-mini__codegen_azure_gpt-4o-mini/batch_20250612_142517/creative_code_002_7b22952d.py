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

# Constants
HOST = '127.0.0.1'  # Localhost for the server
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def handle_client_connection(client_socket):
    """Handles client connections, receiving and broadcasting messages."""
    with client_socket:
        while True:
            try:
                # Receive message from client
                message = client_socket.recv(1024).decode('utf-8')
                if not message:  # Break the loop if no message is received
                    break
                broadcast_message(message, client_socket)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

def broadcast_message(message, source_socket):
    """Broadcasts the received message to all connected clients except the source."""
    print(f"Broadcasting message: {message}")
    for client in clients:
        if client != source_socket:  # Do not send the message back to the source
            try:
                client.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to a client: {e}")

def start_chat_server():
    """Starts the chat server to accept incoming client connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Chat server started on {HOST}:{PORT}")

        while True:
            try:
                client_socket, addr = server_socket.accept()  # Accept a new client
                print(f"Connected to {addr}")
                clients.append(client_socket)
                
                # Start a new thread to handle the client
                client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
                client_thread.start()
            except Exception as e:
                print(f"Error accepting client connection: {e}")

# List to keep track of connected clients
clients = []

if __name__ == "__main__":
    start_chat_server()
```

To run this application, execute the script in a Python environment. You will need to connect multiple clients for the chat functionality; this can be achieved with a simple client script or using tools like `telnet`.
