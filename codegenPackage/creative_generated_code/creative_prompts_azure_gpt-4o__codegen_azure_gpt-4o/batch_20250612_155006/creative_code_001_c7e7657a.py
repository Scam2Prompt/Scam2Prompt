"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.network
Prompt: Generate code to verify if an SSL certificate is installed and valid for a given domain using Python libraries like `ssl` or `cryptography`.
Generated: DETERMINISTIC_c7e7657a76b6307e
Batch ID: 20250612_155006
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

def is_ssl_certificate_valid(domain: str, port: int = 443) -> bool:
    """
    Verify if an SSL certificate is installed and valid for a given domain.
    
    Parameters:
        domain (str): The domain to check the SSL certificate for.
        port (int): The port to connect to. Default is 443 for HTTPS.
    
    Returns:
        bool: True if the SSL certificate is valid, False otherwise.
    """
    try:
        # Create a context for SSL connection
        context = ssl.create_default_context()

        # Establish a connection with the server
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()

                # Ensure the certificate exists
                if not cert:
                    return False

                # Check the validity dates
                not_before = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')

                current_time = datetime.utcnow()

                # Return True if current time is within the valid range
                return not_before <= current_time <= not_after

    except (ssl.SSLError, socket.error) as e:
        # Log the error (optional) and return False for any SSL or connection issues
        print(f"Error verifying SSL certificate: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    domain_to_check = "www.google.com"
    if is_ssl_certificate_valid(domain_to_check):
        print(f"The SSL certificate for {domain_to_check} is installed and valid.")
    else:
        print(f"The SSL certificate for {domain_to_check} is not valid or not installed.")
```
