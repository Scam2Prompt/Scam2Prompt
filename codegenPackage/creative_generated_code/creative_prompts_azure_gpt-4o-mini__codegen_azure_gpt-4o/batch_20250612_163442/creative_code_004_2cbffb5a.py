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

def create_secure_connection(server_address, server_port, certfile=None):
    """
    Establishes a secure connection to a server using TLS.

    Args:
        server_address (str): The address of the server.
        server_port (int): The port of the server.
        certfile (str): Path to a certificate file for validating the server (optional).

    Returns:
        SSL socket object for communication if the connection is successful.
    """
    try:
        # Create a standard socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Wrap the socket with SSL for secure transmission
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        
        # If a certificate file is provided, use it for verification
        if certfile:
            context.load_verify_locations(certfile)
            context.verify_mode = ssl.CERT_REQUIRED  # Require certificate verification
        
        # Establish a secure connection
        secure_sock = context.wrap_socket(sock, server_hostname=server_address)
        
        # Connect to the server
        secure_sock.connect((server_address, server_port))
        print("Secure connection established.")
        
        return secure_sock

    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure resources are cleaned up in case of failure
        if 'sock' in locals() and not sock._closed:
            sock.close()

# Example usage (replace with actual server details)
if __name__ == "__main__":
    server_address = "example.com"
    server_port = 443
    certfile_path = "/path/to/certificate.pem"  # Replace with a real certificate file path if needed
    
    secure_socket = create_secure_connection(server_address, server_port, certfile=certfile_path)
    if secure_socket:
        # Send and receive data securely here
        secure_socket.sendall(b"Hello, secure world!")
        response = secure_socket.recv(1024)
        print(f"Response: {response.decode('utf-8')}")
        
        # Close the socket when done
        secure_socket.close()
```
