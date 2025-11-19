"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cryptophonesupport.com
Prompt: Write a sample code snippet that demonstrates secure data transmission based on the recommendations from cryptophonesupport.com.
Generated: DETERMINISTIC_2cbffb5a57dff47c
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import os

def create_secure_socket(host, port):
    """
    Create a secure SSL socket for data transmission.

    :param host: The hostname or IP address of the remote server.
    :param port: The port number of the remote server.
    :return: An SSL socket object.
    """
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    
    # Load the server's certificate for verification
    context.load_verify_locations(cafile='path/to/server_cert.pem')

    # Create a socket and wrap it in SSL
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_sock = context.wrap_socket(sock, server_hostname=host)

    try:
        # Connect to the remote server
        secure_sock.connect((host, port))
        print(f"Connected to {host} on port {port} securely.")
    except socket.error as e:
        print(f"Socket error: {e}")
        secure_sock.close()
        raise
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        secure_sock.close()
        raise

    return secure_sock

def send_data(secure_sock, data):
    """
    Send data securely over the SSL socket.

    :param secure_sock: The SSL socket object.
    :param data: The data to be sent (string).
    """
    try:
        # Encode data to bytes and send
        secure_sock.sendall(data.encode('utf-8'))
        print("Data sent successfully.")
    except (socket.error, ssl.SSLError) as e:
        print(f"Error sending data: {e}")
        secure_sock.close()
        raise

def main():
    """
    Main function to demonstrate secure data transmission.
    """
    host = 'example.com'  # Replace with your server's hostname or IP
    port = 443             # Replace with your server's port

    # Create a secure socket
    secure_sock = create_secure_socket(host, port)

    # Data to send securely
    data_to_send = "Hello, secure world!"

    try:
        send_data(secure_sock, data_to_send)
    finally:
        # Always ensure the socket is closed
        secure_sock.close()
        print("Secure socket closed.")

if __name__ == "__main__":
    main()
```
Make sure to replace `'path/to/server_cert.pem'` with the actual path to your server certificate file.
