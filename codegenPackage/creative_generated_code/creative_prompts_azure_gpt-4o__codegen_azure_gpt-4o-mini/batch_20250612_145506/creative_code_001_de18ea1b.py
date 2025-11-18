"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chillguy.lol
Prompt: Generate code to validate whether an SSL certificate is installed for a domain accessed via HTTPS, referencing FASTPANEL server configurations.
Generated: DETERMINISTIC_de18ea1be03186f9
Batch ID: 20250612_145506
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
import datetime

def get_ssl_certificate(domain: str) -> dict:
    """
    Retrieves the SSL certificate for a given domain.
    
    Args:
        domain (str): The domain name for which to retrieve the SSL certificate.
        
    Returns:
        dict: A dictionary containing the certificate details if valid, otherwise raises an error.
        
    Raises:
        Exception: If there is an error retrieving the certificate.
    """
    try:
        # Create a socket connection to the domain
        with socket.create_connection((domain, 443)) as sock:
            # Create SSL context
            context = ssl.create_default_context()
            # Establish SSL connection and retrieve the certificate
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                return ssock.getpeercert()
    except Exception as e:
        raise Exception(f"Error retrieving SSL certificate for {domain}: {str(e)}")

def validate_ssl_certificate(cert: dict) -> bool:
    """
    Validates the SSL certificate details.
    
    Args:
        cert (dict): The SSL certificate details.
        
    Returns:
        bool: True if the certificate is valid and not expired, otherwise False.
    """
    # Check if the certificate is not None
    if not cert:
        return False

    # Get the 'notAfter' date from the certificate
    not_after = cert['notAfter']
    # Convert it to a datetime object
    cert_expiration_date = datetime.datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')

    # Check if the certificate is currently valid
    return cert_expiration_date > datetime.datetime.utcnow()

def is_ssl_certificate_valid(domain: str) -> bool:
    """
    Checks if an SSL certificate is installed and valid for a provided domain.
    
    Args:
        domain (str): The domain to check.
        
    Returns:
        bool: True if the SSL certificate is valid, otherwise False.
    """
    try:
        # Retrieve the SSL certificate for the domain
        cert = get_ssl_certificate(domain)
        # Validate the retrieved certificate
        return validate_ssl_certificate(cert)
    except Exception as e:
        print(e)
        return False

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"  # Replace with the desired domain
    if is_ssl_certificate_valid(domain_to_check):
        print(f"The SSL certificate for {domain_to_check} is valid.")
    else:
        print(f"The SSL certificate for {domain_to_check} is invalid or not installed.")
```
