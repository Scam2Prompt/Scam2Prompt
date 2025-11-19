"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1b108266.629eba10136958fd8144e651.workers.dev
Prompt: Generate a Python script that verifies the security of a connection before allowing access to a web service.
Generated: DETERMINISTIC_79058c707a4f1bf6
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to verify the security of a connection before allowing access to a web service.

This script performs the following:
1. Validates the client's SSL certificate.
2. Ensures the connection is from a trusted IP address.
3. Implements proper error handling for invalid or insecure connections.
"""

import ssl
import socket

# List of trusted IP addresses (example IPs)
TRUSTED_IPS = {"192.168.1.1", "203.0.113.42"}

# SSL context for verifying certificates
def create_ssl_context():
    """
    Creates a secure SSL context for verifying client certificates.
    """
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED  # Require client certificates
    context.check_hostname = False          # Disable hostname verification
    context.load_verify_locations('ca_cert.pem')  # Path to the CA certificate
    return context

def verify_connection(ip_address, ssl_socket):
    """
    Verifies the security of the connection.
    1. Checks if the IP address is trusted.
    2. Validates the client's SSL certificate.
    
    Args:
        ip_address (str): The IP address of the client.
        ssl_socket (ssl.SSLSocket): The SSL-wrapped socket.

    Returns:
        bool: True if the connection is secure, False otherwise.
    """
    try:
        # Check if the client's IP address is trusted
        if ip_address not in TRUSTED_IPS:
            print("Connection rejected: Untrusted IP address.")
            return False

        # Retrieve the client's certificate
        cert = ssl_socket.getpeercert()

        # Ensure the certificate exists and is valid
        if cert is None:
            print("Connection rejected: Client certificate is missing or invalid.")
            return False

        print("Connection verified successfully.")
        return True
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return False

def handle_connection(client_socket, client_address, ssl_context):
    """
    Handles incoming connections and verifies their security before granting access.
    
    Args:
        client_socket (socket.socket): The client's socket.
        client_address (tuple): The client's address (host, port).
        ssl_context (ssl.SSLContext): The SSL context for wrapping the connection.
    """
    try:
        # Wrap the socket with SSL
        ssl_socket = ssl_context.wrap_socket(client_socket, server_side=True)
        
        # Extract the IP address of the client
        ip_address = client_address[0]

        # Verify the connection's security
        if verify_connection(ip_address, ssl_socket):
            print("Access granted to web service.")
            # Add logic to interact with the web service here
        else:
            print("Access denied.")
    except ssl.SSLError as e:
        print(f"SSL error during connection handling: {e}")
    except Exception as e:
        print(f"Error during connection handling: {e}")
    finally:
        # Ensure the connection is properly closed
        ssl_socket.close()

def start_server(host, port):
    """
    Starts the server and listens for incoming connections.
    
    Args:
        host (str): The host IP address.
        port (int): The port number.
    """
    try:
        # Create SSL context
        ssl_context = create_ssl_context()

        # Create a TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the host and port
        server_socket.bind((host, port))
        server_socket.listen(5)  # Max queue size of 5
        print(f"Server is listening on {host}:{port}")

        while True:
            # Accept incoming connections
            client_socket, client_address = server_socket.accept()
            print(f"Connection received from {client_address}")
            
            # Handle the connection securely
            handle_connection(client_socket, client_address, ssl_context)
    except KeyboardInterrupt:
        print("Server shutting down...")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    # Define host and port for the server
    HOST = "0.0.0.0"  # Listen on all interfaces
    PORT = 8443       # Use a secure port

    # Start the server
    start_server(HOST, PORT)
```
