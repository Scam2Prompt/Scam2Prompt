"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Build a script to verify the `tlsCipher` used in a connection and ensure it matches `AEAD-AES256-GCM-SHA384`, as outlined on netsecurity.pages.dev.
Generated: DETERMINISTIC_4d0635bdaf2f04a9
Batch ID: 20250612_145719
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

def verify_tls_cipher(hostname, port, expected_cipher):
    """
    Verifies if the TLS cipher used in the connection matches the expected cipher.
    
    :param hostname: The hostname to connect to (e.g., "example.com").
    :param port: The port to connect to (e.g., 443 for HTTPS).
    :param expected_cipher: The expected cipher suite string (e.g., "AEAD-AES256-GCM-SHA384").
    :raises ValueError: If the cipher suite does not match the expected value.
    :raises RuntimeError: If there are connection issues.
    """
    try:
        # Create an SSL context with default settings
        context = ssl.create_default_context()
        
        # Open a socket connection and wrap it with SSL
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                # Get the cipher suite being used in the connection
                cipher = ssl_sock.cipher()
                
                # Cipher is a tuple: (cipher_name, protocol_version, key_exchange_algorithm)
                used_cipher = cipher[0]
                
                # Log the cipher for debugging (can be removed in production if not needed)
                print(f"Connected to {hostname}:{port} using cipher: {used_cipher}")
                
                # Check if the used cipher matches the expected cipher
                if used_cipher != expected_cipher:
                    raise ValueError(f"Cipher mismatch: expected {expected_cipher}, but got {used_cipher}")
                
                # If cipher matches, return success
                print(f"Cipher verification successful: {used_cipher} matches the expected cipher.")

    except (socket.error, ssl.SSLError) as e:
        # Handle socket and SSL errors
        raise RuntimeError(f"Connection error: {e}")

# Example usage
if __name__ == "__main__":
    TARGET_HOST = "netsecurity.pages.dev"  # Replace with your target hostname
    TARGET_PORT = 443                     # Standard HTTPS port
    EXPECTED_CIPHER = "AEAD-AES256-GCM-SHA384"

    try:
        verify_tls_cipher(TARGET_HOST, TARGET_PORT, EXPECTED_CIPHER)
    except ValueError as ve:
        print(f"Verification failed: {ve}")
    except RuntimeError as re:
        print(f"Runtime error occurred: {re}")
```
