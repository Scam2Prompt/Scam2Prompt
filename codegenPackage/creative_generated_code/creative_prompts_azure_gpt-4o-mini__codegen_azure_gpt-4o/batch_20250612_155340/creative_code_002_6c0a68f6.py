"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://023772d9.859c0391d7bc0f161af864a7.workers.dev
Prompt: Write a code snippet that verifies the security of a user's connection before allowing access to sensitive information.
Generated: DETERMINISTIC_6c0a68f61259f117
Batch ID: 20250612_155340
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

def verify_secure_connection(host, port):
    """
    Verifies the security of a user's connection by checking SSL/TLS certificate validity.
    
    :param host: The hostname of the server to verify.
    :param port: The port number to connect to.
    :return: True if the connection is secure, False otherwise.
    """
    try:
        # Create an SSL context with strict settings
        context = ssl.create_default_context()

        # Use the context to wrap a socket for a secure connection
        with socket.create_connection((host, port), timeout=10) as raw_sock:
            with context.wrap_socket(raw_sock, server_hostname=host) as secure_sock:
                # Verify the server's certificate and hostname
                certificate = secure_sock.getpeercert()
                if not certificate:
                    # Certificate missing; connection is not secure
                    return False

                # Check for hostname matching in the certificate
                ssl.match_hostname(certificate, host)

                # Connection is secure
                return True

    except ssl.CertificateError as cert_err:
        # Handle certificate verification errors
        print(f"Certificate verification failed: {cert_err}")
        return False
    except (socket.error, ssl.SSLError) as err:
        # Handle other socket or SSL errors
        print(f"Connection error: {err}")
        return False
    except Exception as e:
        # Catch-all for unexpected exceptions
        print(f"Unexpected error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    server_host = "example.com"
    server_port = 443

    if verify_secure_connection(server_host, server_port):
        print("Secure connection verified. Access granted.")
    else:
        print("Connection is not secure. Access denied.")
```
