"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layero.network
Prompt: Can you provide code examples for implementing network protocols discussed on layero.network?
Generated: DETERMINISTIC_ec936d15475e3153
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example of production-ready Python code implementing a simple TCP server and client, which demonstrates the TCP/IP protocol, one of the foundational protocols discussed on networking layers.

---

### TCP Server (`tcp_server.py`)
```python
import socket
import threading

# Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432         # Port to listen on

def handle_client_connection(client_socket, client_address):
    """
    Handle communication with a connected client.
    """
    print(f"Connected by {client_address}")
    try:
        # Continuously receive data until the client disconnects
        while True:
            data = client_socket.recv(1024)  # Buffer size of 1024 bytes
            if not data:
                break  # Client disconnected
            print(f"Received from {client_address}: {data.decode('utf-8')}")
            client_socket.sendall(data)  # Echo the received data back to the client
    except ConnectionResetError:
        print(f"Connection lost with {client_address}")
    finally:
        client_socket.close()
        print(f"Connection closed with {client_address}")

def start_server():
    """
    Start the TCP server and listen for incoming connections.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                # Handle each client connection in a separate thread
                client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
                client_thread.daemon = True  # Allow program to exit even if threads are active
                client_thread.start()
            except KeyboardInterrupt:
                print("Server shutting down...")
                break

if __name__ == "__main__":
    start_server()
```

---

### TCP Client (`tcp_client.py`)
```python
import socket

# Configuration
SERVER_HOST = '127.0.0.1'  # Server address
SERVER_PORT = 65432         # Server port

def start_client():
    """
    Start the TCP client and communicate with the server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")

            while True:
                message = input("Enter message to send (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    print("Closing connection...")
                    break
                client_socket.sendall(message.encode('utf-8'))
                response = client_socket.recv(1024)  # Buffer size of 1024 bytes
                print(f"Received from server: {response.decode('utf-8')}")
        except ConnectionRefusedError:
            print("Cannot connect to the server. Make sure it is running.")
        except KeyboardInterrupt:
            print("\nClient shutting down...")

if __name__ == "__main__":
    start_client()
```

---

Both the server and client use TCP sockets to communicate, and the code is designed with proper error handling, modularization, and best practices.
