"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoinbankbreaker.com
Prompt: Generate a script to implement SSL encryption and secure login protocols for a cryptocurrency trading platform, as described in the Bitcoin bank breaker website.
Generated: DETERMINISTIC_029f853486ec5ed2
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
from hashlib import sha256
from hmac import compare_digest

# Constants
SERVER_HOST = 'localhost'
SERVER_PORT = 5000
SSL_CERT_FILE = 'server_cert.pem'
SSL_KEY_FILE = 'server_key.pem'

# Predefined user credentials (for demonstration purposes)
USER_CREDENTIALS = {
    "user1": sha256(b"password1").hexdigest(),
    "user2": sha256(b"password2").hexdigest(),
}

def create_ssl_context(cert_file, key_file):
    """
    Creates and configures an SSL context for secure connections.

    Args:
        cert_file (str): Path to the SSL certificate file.
        key_file (str): Path to the SSL key file.

    Returns:
        ssl.SSLContext: Configured SSL context.
    """
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(cert_file, key_file)
    return context

def handle_login(client_socket):
    """
    Handles secure login for a client.

    Args:
        client_socket (ssl.SSLSocket): SSL-wrapped client socket.
    """
    try:
        client_socket.sendall(b"Enter username: ")
        username = client_socket.recv(1024).decode().strip()

        client_socket.sendall(b"Enter password: ")
        password = client_socket.recv(1024).decode().strip()

        # Validate credentials
        if username in USER_CREDENTIALS:
            stored_password_hash = USER_CREDENTIALS[username]
            provided_password_hash = sha256(password.encode()).hexdigest()

            if compare_digest(stored_password_hash, provided_password_hash):
                client_socket.sendall(b"Login successful!\n")
            else:
                client_socket.sendall(b"Invalid credentials. Login failed.\n")
        else:
            client_socket.sendall(b"Invalid credentials. Login failed.\n")
    except Exception as e:
        client_socket.sendall(b"An error occurred during login.\n")
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    """
    Main function to start the SSL-enabled server.
    """
    # Create and configure SSL context
    ssl_context = create_ssl_context(SSL_CERT_FILE, SSL_KEY_FILE)

    # Create a socket and wrap it with SSL
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(5)
        print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

        with ssl_context.wrap_socket(server_socket, server_side=True) as ssl_server_socket:
            while True:
                try:
                    # Accept client connection
                    client_socket, addr = ssl_server_socket.accept()
                    print(f"Connection established with {addr}")

                    # Handle login for connected client
                    handle_login(client_socket)
                except KeyboardInterrupt:
                    print("Server shutting down...")
                    break
                except Exception as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
