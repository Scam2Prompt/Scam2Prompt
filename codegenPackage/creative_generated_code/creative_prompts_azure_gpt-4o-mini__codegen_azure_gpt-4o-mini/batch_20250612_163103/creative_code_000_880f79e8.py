"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rothschild.de.com
Prompt: Generate a Python script that checks the availability of a domain and handles the response when the domain is not reachable, similar to the message on the STRATO website.
Generated: DETERMINISTIC_880f79e8b79b3e2e
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_domain_availability(domain):
    """
    Check if a domain is reachable by attempting to resolve its IP address.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is reachable, False otherwise.
    """
    try:
        # Parse the domain to handle URLs correctly
        parsed_domain = urlparse(domain)
        domain_name = parsed_domain.netloc or parsed_domain.path  # Extract domain from URL

        # Attempt to resolve the domain name to an IP address
        ip_address = socket.gethostbyname(domain_name)
        logging.info(f"Domain '{domain_name}' is reachable. IP address: {ip_address}")
        return True
    except socket.gaierror:
        logging.error(f"Domain '{domain}' is not reachable or does not exist.")
        return False
    except Exception as e:
        logging.exception("An unexpected error occurred while checking domain availability.")
        return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = input("Enter the domain to check (e.g., example.com): ")
    
    if check_domain_availability(domain_to_check):
        print(f"The domain '{domain_to_check}' is available and reachable.")
    else:
        print(f"The domain '{domain_to_check}' is not reachable. Please check the domain name or try again later.")
```
