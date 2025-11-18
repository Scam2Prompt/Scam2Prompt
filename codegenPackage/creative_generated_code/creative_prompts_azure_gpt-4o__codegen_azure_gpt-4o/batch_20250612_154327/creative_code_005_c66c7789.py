"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercexhange.epizy.com
Prompt: Develop a Python script to test the SSL certificate setup on a hosting platform that provides free and simple SSL, as described on iFastNet.
Generated: DETERMINISTIC_c66c77896ab4398d
Batch ID: 20250612_154327
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

def check_ssl_certificate(domain):
    """
    Check the SSL certificate of the given domain.

    Parameters:
    domain (str): The domain to check the SSL certificate for.

    Returns:
    dict: A dictionary containing SSL certificate information and validity.
    """
    try:
        # Connect to the server and retrieve the SSL certificate
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
        
        # Parse certificate details
        issuer = dict(x[0] for x in cert.get('issuer'))
        subject = dict(x[0] for x in cert.get('subject'))
        valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
        valid_to = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        validity = valid_to > datetime.utcnow()

        # Return SSL certificate information
        return {
            "issuer": issuer,
            "subject": subject,
            "valid_from": valid_from,
            "valid_to": valid_to,
            "is_valid": validity
        }
    except ssl.SSLError as e:
        return {"error": f"SSL error occurred: {str(e)}"}
    except socket.error as e:
        return {"error": f"Socket error occurred: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

if __name__ == "__main__":
    # Prompt the user for a domain to check
    domain = input("Enter the domain to check SSL certificate (e.g., example.com): ").strip()

    if not domain:
        print("Error: Domain name cannot be empty.")
    else:
        # Check SSL certificate and display the results
        result = check_ssl_certificate(domain)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("SSL Certificate Details:")
            print(f"Issuer: {result['issuer']}")
            print(f"Subject: {result['subject']}")
            print(f"Valid From: {result['valid_from']}")
            print(f"Valid To: {result['valid_to']}")
            print(f"Is Certificate Valid: {'Yes' if result['is_valid'] else 'No'}")
```
