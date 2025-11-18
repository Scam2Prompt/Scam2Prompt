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
import socket
import ssl

def verify_tls_cipher(host: str, port: int, expected_cipher: str) -> bool:
    """
    Verify that the TLS cipher used in the connection matches the expected cipher.

    Args:
        host (str): The hostname of the server to connect to.
        port (int): The port number of the server to connect to.
        expected_cipher (str): The expected TLS cipher suite.

    Returns:
        bool: True if the cipher matches, False otherwise.

    Raises:
        ValueError: If the expected cipher is not provided.
        socket.error: If there is a problem with the socket connection.
        ssl.SSLError: If there is a problem with the SSL connection.
    """
    if not expected_cipher:
        raise ValueError("Expected cipher must be provided.")

    try:
        # Create a socket and wrap it with SSL
        with socket.create_connection((host, port)) as sock:
            context = ssl.create_default_context()
            with context.wrap_socket(sock, server_hostname=host) as ssl_socket:
                # Retrieve the negotiated cipher suite
                negotiated_cipher = ssl_socket.cipher()[0]
                print(f"Negotiated Cipher: {negotiated_cipher}")

                # Compare the negotiated cipher with the expected cipher
                return negotiated_cipher == expected_cipher

    except socket.error as e:
        print(f"Socket error: {e}")
        return False
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    HOST = "example.com"  # Replace with the target host
    PORT = 443             # Replace with the target port
    EXPECTED_CIPHER = "AEAD-AES256-GCM-SHA384"

    # Verify the TLS cipher
    is_cipher_valid = verify_tls_cipher(HOST, PORT, EXPECTED_CIPHER)
    if is_cipher_valid:
        print("The TLS cipher is valid.")
    else:
        print("The TLS cipher does not match the expected value.")
```

Make sure to replace `example.com` and `443` with the target host and port as needed.
