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

def check_ssl_certificate(domain, port=443):
    """
    Check the SSL certificate of a given domain.
    
    Args:
        domain (str): The domain name to check.
        port (int): The port number to connect to (default is 443 for HTTPS).
    
    Returns:
        dict: A dictionary containing certificate details or an error message.
    """
    try:
        # Create a socket connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the SSL certificate
                cert = ssock.getpeercert()
                cert_details = {
                    "subject": dict(x[0] for x in cert["subject"]),
                    "issuer": dict(x[0] for x in cert["issuer"]),
                    "notBefore": cert["notBefore"],
                    "notAfter": cert["notAfter"],
                }
                # Convert notBefore and notAfter to datetime objects
                cert_details["notBefore"] = datetime.strptime(cert_details["notBefore"], '%b %d %H:%M:%S %Y GMT')
                cert_details["notAfter"] = datetime.strptime(cert_details["notAfter"], '%b %d %H:%M:%S %Y GMT')
                
                return {
                    "status": "success",
                    "certificate": cert_details
                }
    
    except ssl.SSLError as e:
        return {
            "status": "error",
            "message": f"SSL error occurred: {str(e)}"
        }
    except socket.gaierror:
        return {
            "status": "error",
            "message": "Domain name could not be resolved."
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"An unexpected error occurred: {str(e)}"
        }

if __name__ == "__main__":
    # Example usage of the check_ssl_certificate function
    domain = "example.com"  # Replace with your domain
    result = check_ssl_certificate(domain)
    
    if result["status"] == "success":
        print("SSL Certificate Details:")
        print(f"Subject: {result['certificate']['subject']}")
        print(f"Issuer: {result['certificate']['issuer']}")
        print(f"Valid From: {result['certificate']['notBefore']}")
        print(f"Valid Until: {result['certificate']['notAfter']}")
    else:
        print("Error:", result["message"])
```
