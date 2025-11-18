"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-webnode.rf.gd
Prompt: Generate a script to check SSL certificate installation on a hosting service that provides free and simple SSL, similar to iFastNet hosting.
Generated: DETERMINISTIC_6ad81665bb6d086d
Batch ID: 20250612_154502
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
    Function to check SSL certificate installation and validity for a given domain.

    Parameters:
    domain (str): The domain name to check SSL certificate for.

    Returns:
    dict: SSL certificate details including validity and expiration date.
    """
    try:
        # Connect to the server using SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                # Get the SSL certificate
                cert = ssl_sock.getpeercert()

        # Extract SSL certificate details
        issued_to = cert.get("subject", [])
        issued_by = cert.get("issuer", [])
        valid_from = datetime.strptime(cert.get("notBefore"), "%b %d %H:%M:%S %Y %Z")
        valid_to = datetime.strptime(cert.get("notAfter"), "%b %d %H:%M:%S %Y %Z")

        return {
            "domain": domain,
            "issued_to": issued_to,
            "issued_by": issued_by,
            "valid_from": valid_from,
            "valid_to": valid_to,
            "is_valid": valid_from <= datetime.utcnow() <= valid_to
        }

    except ssl.SSLError as e:
        return {"error": f"SSL error occurred: {str(e)}", "domain": domain}
    except socket.error as e:
        return {"error": f"Socket error occurred: {str(e)}", "domain": domain}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}", "domain": domain}


def main():
    """
    Main function to check SSL certificate for a list of domains.
    """
    domains_to_check = [
        "example.com",  # Replace with domains you want to check.
        "google.com",
        "ifastnet.com"
    ]

    for domain in domains_to_check:
        print(f"Checking SSL certificate for: {domain}")
        result = check_ssl_certificate(domain)

        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Domain: {result['domain']}")
            print(f"Issued to: {result['issued_to']}")
            print(f"Issued by: {result['issued_by']}")
            print(f"Valid from: {result['valid_from']}")
            print(f"Valid to: {result['valid_to']}")
            print(f"SSL certificate is valid: {result['is_valid']}")
        print("-" * 50)


if __name__ == "__main__":
    main()
```
