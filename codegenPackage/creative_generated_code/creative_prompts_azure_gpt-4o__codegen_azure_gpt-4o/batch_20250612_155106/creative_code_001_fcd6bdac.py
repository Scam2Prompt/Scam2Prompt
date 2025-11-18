"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: Generate a script to verify if an SSL certificate is installed for a domain using OpenSSL or a similar library, referencing FASTPANEL's HTTPS-related troubleshooting.
Generated: DETERMINISTIC_fcd6bdac6745c9d6
Batch ID: 20250612_155106
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

def check_ssl_certificate(domain, port=443):
    """
    Verifies if an SSL certificate is installed for the given domain and retrieves its details.
    
    Args:
        domain (str): The domain name to check.
        port (int): The port to check for the SSL certificate (default is 443).
    
    Returns:
        dict: A dictionary containing certificate details if installed, or error details if not.
    """
    try:
        # Establish a connection to the server using SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve the certificate
                certificate = ssock.getpeercert()
                
                if certificate:
                    # Extract certificate details
                    cert_details = {
                        "subject": dict(x[0] for x in certificate.get("subject", [])),
                        "issuer": dict(x[0] for x in certificate.get("issuer", [])),
                        "version": certificate.get("version"),
                        "serial_number": certificate.get("serialNumber"),
                        "valid_from": certificate.get("notBefore"),
                        "valid_to": certificate.get("notAfter"),
                        "is_expired": datetime.strptime(certificate["notAfter"], "%b %d %H:%M:%S %Y GMT") < datetime.utcnow()
                    }
                    return {"status": "success", "certificate": cert_details}
                else:
                    return {"status": "error", "message": "No certificate found."}

    except ssl.SSLError as e:
        # Handle SSL-related errors
        return {"status": "error", "message": f"SSL error: {e}"}
    except socket.error as e:
        # Handle socket-related errors
        return {"status": "error", "message": f"Socket error: {e}"}
    except Exception as e:
        # Handle other unexpected exceptions
        return {"status": "error", "message": f"Unexpected error: {e}"}

# Example usage
if __name__ == "__main__":
    domain = "example.com"  # Replace with the domain you want to check
    result = check_ssl_certificate(domain)
    print(result)
```
