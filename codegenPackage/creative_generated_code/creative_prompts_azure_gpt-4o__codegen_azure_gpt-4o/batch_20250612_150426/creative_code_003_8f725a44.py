"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter.graphy.com
Prompt: Provide a Python script to create a networking feature where users can interact in exclusive chat groups, inspired by the community engagement feature on Jupiter Swap™.
Generated: DETERMINISTIC_8f725a446d6eb041
Batch ID: 20250612_150426
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
from typing import Dict, List

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# Global storage for chat groups and user connections
chat_groups: Dict[str, List[socket.socket]] = {}  # Mapping group names to list of client sockets
clients: Dict[socket.socket, str] = {}           # Mapping client sockets to group names


def handle_client(client_socket: socket.socket):
    """
    Handles communication with a connected client.
    """
    try:
        # Send welcome message to client
        client_socket.send("Welcome! Enter a group name to join or create a new group:\n".encode())
        group_name = client_socket.recv(1024).decode().strip()

        if not group_name:
            client_socket.send("Invalid group name! Disconnecting...\n".encode())
            client_socket.close()
            return

        # Add client to the specified group
        if group_name not in chat_groups:
            chat_groups[group_name] = []
        chat_groups[group_name].append(client_socket)
        clients[client_socket] = group_name

        client_socket.send(f"You have joined the group: {group_name}\n".encode())
        broadcast_message(group_name, f"A new user has joined the group: {group_name}\n", client_socket)

        # Receive and broadcast messages
        while True:
            message = client_socket.recv(1024).decode().strip()
            if message.lower() == 'exit':
                # User requested to leave the group
                client_socket.send("You have left the group.\n".encode())
                break
            if message:
                broadcast_message(group_name, message, client_socket)

    except (ConnectionResetError, ConnectionAbortedError):
        pass  # Handle client disconnection gracefully

    finally:
        # Clean up client on disconnection
        remove_client(client_socket)


def broadcast_message(group_name: str, message: str, sender_socket: socket.socket):
    """
    Sends a message to all clients in the specified group except the sender.
    """
    for client in chat_groups.get(group_name, []):
        if client != sender_socket:
            try:
                client.send(message.encode())
            except BrokenPipeError:
                # Handle cases where a client is abruptly disconnected
                remove_client(client)


def remove_client(client_socket: socket.socket):
    """
    Removes a client from the group and closes its connection.
    """
    group_name = clients.get(client_socket)
    if group_name:
        chat_groups[group_name].remove(client_socket)
        if not chat_groups[group_name]:
            del chat_groups[group_name]  # Remove group if empty
        del clients[client_socket]
    try:
        client_socket.close()
    except Exception:
        pass


def start_server():
    """
    Initializes and starts the chat server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Configure the server socket
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)  # Listen for up to 5 simultaneous connections

        print(f"Server running on {HOST}:{PORT}...")

        while True:
            # Accept a new client connection
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}")

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.daemon = True  # Ensure threads close when the main program exits
            client_thread.start()


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Error: {e}")
```
