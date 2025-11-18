"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoin.rf.gd
Prompt: Generate a Python script to test SSL certificate installation on a hosting platform that supports Python apps and offers free SSL, as mentioned on iFastNet hosting.
Generated: DETERMINISTIC_45a6cd44445f1e68
Batch ID: 20250612_154827
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


def check_ssl_certificate(host, port=443):
    """
    Check the SSL certificate of a given host.

    Args:
        host (str): The hostname to check.
        port (int): The port to use for the connection. Default is 443.

    Returns:
        dict: A dictionary containing certificate details and validation status.
    """
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssl_sock:
                # Get certificate details
                cert = ssl_sock.getpeercert()

                # Extract expiration date
                not_after = cert.get("notAfter")
                expiration_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")

                # Check if the certificate is expired
                is_valid = expiration_date > datetime.utcnow()

                return {
                    "host": host,
                    "port": port,
                    "expiration_date": expiration_date,
                    "is_valid": is_valid,
                    "issuer": dict(cert.get("issuer")),
                }
    except ssl.SSLError as e:
        return {"error": f"SSL error: {e}"}
    except socket.error as e:
        return {"error": f"Socket error: {e}"}


def main():
    """
    Main function to test SSL certificate installation.
    """
    # Host to check (replace 'yourdomain.com' with your actual domain)
    host = "yourdomain.com"

    print(f"Checking SSL certificate for {host}...")
    result = check_ssl_certificate(host)

    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Host: {result['host']}")
        print(f"Port: {result['port']}")
        print(f"Certificate Expiration Date: {result['expiration_date']}")
        print(f"Is Certificate Valid: {'Yes' if result['is_valid'] else 'No'}")
        print(f"Issuer: {result['issuer']}")


if __name__ == "__main__":
    main()
```
