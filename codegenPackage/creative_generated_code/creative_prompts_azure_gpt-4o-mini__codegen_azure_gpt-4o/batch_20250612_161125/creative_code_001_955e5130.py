"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherveum.org
Prompt: How can I troubleshoot SSL certificate issues for my website hosted on a server?
Generated: DETERMINISTIC_955e513093405bc4
Batch ID: 20250612_161125
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

def check_ssl_certificate(hostname, port=443):
    """
    Checks the SSL certificate details of a given hostname.
    
    Args:
        hostname (str): The domain name of the website.
        port (int): The port number to connect to (default is 443 for HTTPS).

    Returns:
        dict: A dictionary containing SSL certificate details or an error message.
    """
    try:
        # Establish a socket connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Retrieve the server's SSL certificate
                certificate = ssock.getpeercert()

                # Extract relevant information from the certificate
                cert_info = {
                    "subject": dict(x[0] for x in certificate.get("subject", [])),
                    "issuer": dict(x[0] for x in certificate.get("issuer", [])),
                    "version": certificate.get("version"),
                    "serial_number": certificate.get("serialNumber"),
                    "valid_from": certificate.get("notBefore"),
                    "valid_to": certificate.get("notAfter")
                }

                # Parse validity dates
                valid_from = datetime.strptime(cert_info["valid_from"], "%b %d %H:%M:%S %Y %Z")
                valid_to = datetime.strptime(cert_info["valid_to"], "%b %d %H:%M:%S %Y %Z")
                cert_info["valid_from"] = valid_from
                cert_info["valid_to"] = valid_to

                # Check if certificate is expired
                if valid_to < datetime.utcnow():
                    cert_info["status"] = "expired"
                    cert_info["days_to_expiry"] = 0
                else:
                    cert_info["status"] = "valid"
                    cert_info["days_to_expiry"] = (valid_to - datetime.utcnow()).days

                return cert_info

    except ssl.SSLError as e:
        return {"error": f"SSL error occurred: {e}"}
    except socket.error as e:
        return {"error": f"Socket error occurred: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


if __name__ == "__main__":
    # Replace 'example.com' with the hostname you want to check
    hostname_to_check = "example.com"
    ssl_details = check_ssl_certificate(hostname_to_check)

    if "error" in ssl_details:
        print(f"Error: {ssl_details['error']}")
    else:
        print("SSL Certificate Details:")
        print(f"Subject: {ssl_details['subject']}")
        print(f"Issuer: {ssl_details['issuer']}")
        print(f"Version: {ssl_details['version']}")
        print(f"Serial Number: {ssl_details['serial_number']}")
        print(f"Valid From: {ssl_details['valid_from']}")
        print(f"Valid To: {ssl_details['valid_to']}")
        print(f"Status: {ssl_details['status']}")
        print(f"Days to Expiry: {ssl_details['days_to_expiry']}")
```
