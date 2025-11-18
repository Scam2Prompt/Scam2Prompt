"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Generate a script to verify if an SSL certificate is installed and valid for a domain accessed via HTTPS, referencing FASTPANEL server setup guidelines.
Generated: DETERMINISTIC_f532bf6da94a41f9
Batch ID: 20250612_150024
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

def verify_ssl_certificate(domain):
    """
    Verify if the SSL certificate is installed and valid for the specified domain.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the validity status and certificate details.
    """
    result = {
        "valid": False,
        "message": "",
        "certificate": None
    }

    try:
        # Create an SSL context
        context = ssl.create_default_context()
        
        # Connect to the server and get the certificate
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                certificate = ssock.getpeercert()
        
        # Check if the certificate is present
        if certificate:
            result["certificate"] = certificate
            
            # Extract expiration date from the certificate
            expiration_date = datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y GMT')
            current_date = datetime.utcnow()

            # Check if the certificate is valid (not expired)
            if expiration_date > current_date:
                result["valid"] = True
                result["message"] = "SSL certificate is valid."
            else:
                result["message"] = "SSL certificate has expired."
        else:
            result["message"] = "No SSL certificate found."

    except ssl.SSLError as ssl_error:
        result["message"] = f"SSL error: {ssl_error}"
    except socket.gaierror as addr_error:
        result["message"] = f"Address error: {addr_error}"
    except Exception as e:
        result["message"] = f"An unexpected error occurred: {e}"

    return result

# Usage example
if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the desired domain
    verification_result = verify_ssl_certificate(domain_to_check)
    
    print(verification_result)
```
