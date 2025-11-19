"""
Generated Code Metadata:
========================
Original URL: https://netsecurity.pages.dev
Prompt: "Write a Python script to verify TLS 1.3 cipher suites, specifically 'AEAD-AES256-GCM-SHA384', and provide a list of accepted cipher suites."
Generated: DETERMINISTIC_d279a9e659253fac
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
import socket
from typing import List, Optional

def get_accepted_cipher_suites(host: str, port: int = 443) -> Optional[List[str]]:
    """
    Retrieve the list of accepted TLS 1.3 cipher suites for a given host and port.
    
    Args:
        host: The hostname to connect to (e.g., 'example.com').
        port: The port number (default is 443 for HTTPS).
    
    Returns:
        A list of accepted cipher suites or None if the connection fails.
    """
    try:
        # Create a secure SSL context with TLS 1.3
        context = ssl.create_default_context()
        context.minimum_version = ssl.TLSVersion.TLSv1_3
        context.maximum_version = ssl.TLSVersion.TLSv1_3
        
        # Set the cipher suite to verify
        context.set_ciphers('AEAD-AES256-GCM-SHA384')
        
        # Create a socket and wrap it with SSL
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get the negotiated cipher suite
                cipher = ssock.cipher()
                if cipher:
                    # Return all shared cipher suites (Python doesn't expose all accepted ones directly)
                    # Note: This will only return the negotiated cipher suite due to Python's limitations
                    return [cipher[0]]
                return None
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        return None
    except socket.error as e:
        print(f"Socket error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None

def main():
    host = input("Enter the hostname (e.g., 'example.com'): ")
    accepted_ciphers = get_accepted_cipher_suites(host)
    
    if accepted_ciphers:
        print(f"Accepted TLS 1.3 cipher suites for {host}:")
        for cipher in accepted_ciphers:
            print(f"- {cipher}")
    else:
        print(f"Failed to retrieve cipher suites for {host}")

if __name__ == "__main__":
    main()
```
