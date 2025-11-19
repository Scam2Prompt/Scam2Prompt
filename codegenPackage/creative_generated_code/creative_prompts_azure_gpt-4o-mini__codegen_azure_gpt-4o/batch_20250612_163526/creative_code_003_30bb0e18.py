"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bancdaviplata1.vastserve.com
Prompt: What are the steps to set up a free SSL certificate on iFastNet hosting for my domain?
Generated: DETERMINISTIC_30bb0e18eff086aa
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Unfortunately, setting up a free SSL certificate on iFastNet hosting involves configuration and settings within the hosting platform itself. It cannot be accomplished purely by code. However, I can provide a Python script that checks if your SSL certificate is active and valid for your domain once you have set it up. Here's the code for that scenario:

```python
import socket
import ssl
from datetime import datetime

def check_ssl_certificate(domain):
    """
    Function to check the validity of an SSL certificate for a given domain.
    
    Args:
        domain (str): The domain name to check the SSL certificate for.
        
    Returns:
        dict: A dictionary containing information about the SSL certificate validity.
    """
    try:
        # Connect to the server using SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate details
                cert = ssock.getpeercert()
        
        # Check the validity period
        not_before = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
        not_after = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        current_time = datetime.utcnow()
        
        certificate_validity = {
            "domain": domain,
            "valid_from": not_before,
            "valid_until": not_after,
            "is_valid": not_before <= current_time <= not_after
        }
        return certificate_validity
    
    except ssl.SSLCertVerificationError as e:
        # Handle SSL certificate verification error
        return {"error": f"SSL certificate verification failed: {e}"}
    except socket.gaierror as e:
        # Handle domain connection error
        return {"error": f"Failed to connect to domain: {e}"}
    except Exception as e:
        # Handle other exceptions
        return {"error": f"An error occurred: {e}"}

# Example usage:
if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with your domain
    result = check_ssl_certificate(domain_to_check)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"SSL Certificate details for {result['domain']}:")
        print(f"  Valid From: {result['valid_from']}")
        print(f"  Valid Until: {result['valid_until']}")
        print(f"  Is Valid: {'Yes' if result['is_valid'] else 'No'}")
```

You can use this script to verify your SSL certificate's validity once you've set it up on iFastNet hosting. Be sure to replace `"example.com"` with your actual domain name.
