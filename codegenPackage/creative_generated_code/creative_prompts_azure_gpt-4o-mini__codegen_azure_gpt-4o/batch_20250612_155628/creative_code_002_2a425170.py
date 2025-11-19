"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Can you provide code examples for checking SSL certificate installation for a domain?
Generated: DETERMINISTIC_2a425170652331f2
Batch ID: 20250612_155628
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
from datetime import datetime

def check_ssl_certificate(domain: str, port: int = 443) -> dict:
    """
    Check the SSL certificate for a given domain.

    Args:
        domain (str): The domain name to check the SSL certificate for.
        port (int): The port to connect to (default is 443).

    Returns:
        dict: A dictionary containing SSL certificate details or an error message.
    """
    try:
        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                # Get the certificate from the server
                cert = ssl_sock.getpeercert()
                
                # Extract certificate details
                certificate_details = {
                    "subject": dict(item[0] for item in cert.get("subject", [])),
                    "issuer": dict(item[0] for item in cert.get("issuer", [])),
                    "version": cert.get("version", "Unknown"),
                    "serial_number": cert.get("serialNumber", "Unknown"),
                    "valid_from": cert.get("notBefore", "Unknown"),
                    "valid_until": cert.get("notAfter", "Unknown"),
                    "is_valid": datetime.strptime(cert.get("notAfter", "9999-01-01"), "%Y-%m-%d %H:%M:%S") > datetime.now(),
                }
                return certificate_details
    except ssl.SSLError as e:
        # Handle SSL-specific errors
        return {"error": f"SSL error occurred: {e}"}
    except socket.error as e:
        # Handle socket errors
        return {"error": f"Socket error occurred: {e}"}
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
if __name__ == "__main__":
    domain = "example.com"  # Replace with your desired domain
    result = check_ssl_certificate(domain)
    print(result)
```
