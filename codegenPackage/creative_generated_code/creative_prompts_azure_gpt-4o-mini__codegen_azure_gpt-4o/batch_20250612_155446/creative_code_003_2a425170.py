"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chillguy.lol
Prompt: Can you provide code examples for checking SSL certificate installation for a domain?
Generated: DETERMINISTIC_2a425170652331f2
Batch ID: 20250612_155446
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
from datetime import datetime

def check_ssl_certificate(domain: str, port: int = 443) -> dict:
    """
    Check the SSL certificate installation for a given domain.

    Args:
        domain (str): The domain to check the SSL certificate for.
        port (int): The port to connect to (default is 443).

    Returns:
        dict: A dictionary containing SSL certificate details or an error message.
    """
    try:
        # Establish a connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()

                # Extract certificate details
                issued_to = cert.get("subject", [])
                issuer = cert.get("issuer", [])
                valid_from = cert.get("notBefore", "")
                valid_until = cert.get("notAfter", "")

                # Convert validity dates to datetime objects for easier handling
                valid_from_date = datetime.strptime(valid_from, "%b %d %H:%M:%S %Y %Z")
                valid_until_date = datetime.strptime(valid_until, "%b %d %H:%M:%S %Y %Z")

                # Return the certificate details
                return {
                    "status": "success",
                    "domain": domain,
                    "issued_to": issued_to,
                    "issuer": issuer,
                    "valid_from": valid_from_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "valid_until": valid_until_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "days_until_expiry": (valid_until_date - datetime.utcnow()).days
                }
    except ssl.CertificateError as e:
        # Handle certificate errors
        return {"status": "error", "message": f"Certificate error: {str(e)}"}
    except socket.timeout:
        # Handle connection timeout
        return {"status": "error", "message": "Connection to the server timed out."}
    except Exception as e:
        # Handle other exceptions
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"
    result = check_ssl_certificate(domain_to_check)
    print(result)
```
