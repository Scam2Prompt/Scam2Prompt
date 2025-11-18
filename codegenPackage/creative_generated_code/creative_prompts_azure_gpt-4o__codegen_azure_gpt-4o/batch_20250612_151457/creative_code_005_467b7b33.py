"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinapp.rf.gd
Prompt: Generate a Python script to test SSL functionality on a hosting service that offers free and simple SSL certificates, as mentioned on iFastNet.
Generated: DETERMINISTIC_467b7b338b9c37ee
Batch ID: 20250612_151457
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


def test_ssl(hostname, port=443):
    """
    Test SSL functionality for a given hostname and port.
    
    :param hostname: The hostname (e.g., www.example.com) to test SSL functionality on.
    :param port: The port to connect to (default is 443 for HTTPS).
    :return: None
    """
    try:
        # Create an SSL context with default settings
        context = ssl.create_default_context()
        
        # Establish a connection to the server
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                # Get SSL certificate information
                cert = ssl_sock.getpeercert()
                
                # Extract and display relevant SSL certificate details
                print(f"Successfully connected to {hostname}:{port} using SSL.")
                print(f"Certificate issued to: {cert.get('subject')}")
                print(f"Certificate issued by: {cert.get('issuer')}")
                print(f"Certificate valid from: {cert.get('notBefore')}")
                print(f"Certificate valid until: {cert.get('notAfter')}")
                
    except ssl.SSLError as e:
        # Handle SSL-specific errors
        print(f"SSL error occurred: {e}")
    except socket.timeout:
        # Handle timeout errors
        print(f"Connection to {hostname}:{port} timed out.")
    except socket.error as e:
        # Handle socket-related errors
        print(f"Socket error occurred: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Hostname to test SSL functionality on
    hostname_to_test = "ifastnet.com"  # Replace with a different hostname if needed
    
    print(f"Testing SSL functionality for {hostname_to_test}...")
    test_ssl(hostname_to_test)
```
