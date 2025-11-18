"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectprotocol.42web.io
Prompt: Create a Python script for SSL certificate validation and explain how to use it on a hosting platform that offers free and simple SSL, as described by iFastNet.
Generated: DETERMINISTIC_23dbcc21721dfa7c
Batch ID: 20250612_145238
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

def validate_ssl_certificate(hostname: str, port: int = 443):
    """
    Validates the SSL certificate of a given hostname.

    Args:
        hostname (str): The domain name to validate the SSL certificate for.
        port (int, optional): The port to connect to (default is 443).

    Returns:
        dict: A dictionary containing SSL certificate details and validation status.
    """
    try:
        # Connect to the server and get the SSL certificate
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Retrieve the certificate
                cert = ssock.getpeercert()

        # Parse certificate details
        issued_to = cert.get("subject", [])
        issued_by = cert.get("issuer", [])
        valid_from = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z")
        valid_to = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        current_time = datetime.utcnow()

        # Check if the certificate is currently valid
        is_valid = valid_from <= current_time <= valid_to

        # Format the output
        return {
            "hostname": hostname,
            "issued_to": issued_to,
            "issued_by": issued_by,
            "valid_from": valid_from,
            "valid_to": valid_to,
            "is_valid": is_valid
        }

    except ssl.CertificateError as e:
        return {"error": f"SSL Certificate error: {e}"}
    except socket.timeout:
        return {"error": "Connection timed out"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
if __name__ == "__main__":
    # Replace 'yourdomain.com' with the actual domain name to validate its SSL certificate
    domain = "yourdomain.com"
    result = validate_ssl_certificate(domain)

    if "error" in result:
        print(f"Error validating SSL certificate for {domain}: {result['error']}")
    else:
        print(f"SSL certificate details for {domain}:")
        print(f"  Issued To: {result['issued_to']}")
        print(f"  Issued By: {result['issued_by']}")
        print(f"  Valid From: {result['valid_from']}")
        print(f"  Valid To: {result['valid_to']}")
        print(f"  Is Valid: {'Yes' if result['is_valid'] else 'No'}")
```

This Python script validates the SSL certificate for a given hostname. It checks the certificate's validity dates and provides details about the issuer and subject. Proper error handling is included for cases like certificate errors, timeout issues, or unexpected exceptions.
