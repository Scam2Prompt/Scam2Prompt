"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infvpn.osnovanie-osman.ru
Prompt: Describe how to configure a server to support both IPv4 and IPv6 for a domain that is experiencing connectivity issues.
Generated: DETERMINISTIC_823dc2f822329f3a
Batch ID: 20250612_135940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Python script using the `socket` module to configure a server to support both IPv4 and IPv6:

```python
import socket
import threading

# Define configuration constants
HOST_IPV4 = "0.0.0.0"  # Bind to all IPv4 addresses
HOST_IPV6 = "::"       # Bind to all IPv6 addresses
PORT = 8080            # Port to listen on

def handle_client(connection, address):
    """
    Handles client connections.
    
    Args:
        connection (socket.socket): The client socket object.
        address (tuple): The client's address (IP, port).
    """
    try:
        print(f"Connection established with {address}")
        # Receive data from the client
        data = connection.recv(1024)
        if data:
            print(f"Received data: {data.decode('utf-8')}")
            # Respond to the client
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
            connection.sendall(response.encode('utf-8'))
        else:
            print(f"No data received from {address}")
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        # Close the connection
        connection.close()
        print(f"Connection closed for {address}")

def start_server():
    """
    Starts a server that supports both IPv4 and IPv6.
    """
    try:
        # Create an IPv4 server socket
        ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ipv4_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ipv4_socket.bind((HOST_IPV4, PORT))
        ipv4_socket.listen(5)
        print(f"IPv4 server listening on {HOST_IPV4}:{PORT}")

        # Create an IPv6 server socket
        ipv6_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        ipv6_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ipv6_socket.bind((HOST_IPV6, PORT))
        ipv6_socket.listen(5)
        print(f"IPv6 server listening on [{HOST_IPV6}]:{PORT}")

        # Handle connections concurrently using threads
        def accept_connections(server_socket, protocol):
            while True:
                try:
                    client_socket, client_address = server_socket.accept()
                    print(f"New connection on {protocol} from {client_address}")
                    # Start a new thread to handle the client
                    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                    client_thread.start()
                except Exception as e:
                    print(f"Error accepting connection on {protocol}: {e}")

        # Start threads for IPv4 and IPv6 servers
        ipv4_thread = threading.Thread(target=accept_connections, args=(ipv4_socket, "IPv4"))
        ipv6_thread = threading.Thread(target=accept_connections, args=(ipv6_socket, "IPv6"))
        ipv4_thread.start()
        ipv6_thread.start()

        # Wait for threads to finish (they won't unless the server is stopped)
        ipv4_thread.join()
        ipv6_thread.join()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        ipv4_socket.close()
        ipv6_socket.close()
        print("Server sockets closed.")

if __name__ == "__main__":
    start_server()
```

This code creates a server that listens on both IPv4 and IPv6 addresses using two separate sockets. It also handles client connections in separate threads, ensuring concurrent handling for multiple clients. Error handling is implemented to catch and log exceptions that may occur during socket operations or client communication.
