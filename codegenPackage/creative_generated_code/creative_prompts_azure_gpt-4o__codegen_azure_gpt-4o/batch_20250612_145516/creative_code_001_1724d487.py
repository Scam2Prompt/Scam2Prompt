"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-lo.com
Prompt: Generate a script to verify if an SSL certificate is installed for a domain accessed via HTTPS, referencing FASTPANEL server settings.
Generated: DETERMINISTIC_1724d487d2da1660
Batch ID: 20250612_145516
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
    Check if an SSL certificate is installed for the given domain.

    Parameters:
        domain (str): The domain to check.
        port (int): The port for HTTPS (default is 443).

    Returns:
        dict: Certificate information if SSL is installed, or error details.
    """
    try:
        # Establish a connection with SSL context
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve the certificate
                cert = ssock.getpeercert()
        
        # Parse the certificate expiration date
        not_after = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        
        # Return certificate details
        return {
            "domain": domain,
            "issuer": cert.get('issuer'),
            "valid_from": cert.get('notBefore'),
            "valid_to": cert.get('notAfter'),
            "is_valid": not_after > datetime.utcnow()
        }
    except ssl.SSLError as e:
        return {"error": f"SSL error: {e}"}
    except socket.error as e:
        return {"error": f"Socket error: {e}"}
    except Exception as e:
        return {"error": f"General error: {e}"}

if __name__ == "__main__":
    # Example domain to check (replace with your domain)
    domain_to_check = "example.com"
    
    # FASTPANEL server settings note: This script assumes standard HTTPS settings.
    print(f"Checking SSL certificate for domain: {domain_to_check}")
    
    # Result of the SSL check
    result = check_ssl_certificate(domain_to_check)
    
    # Output the result
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"SSL Certificate for {domain_to_check}:")
        print(f"Issuer: {result['issuer']}")
        print(f"Valid From: {result['valid_from']}")
        print(f"Valid To: {result['valid_to']}")
        print(f"Is Certificate Valid: {'Yes' if result['is_valid'] else 'No'}")
```
