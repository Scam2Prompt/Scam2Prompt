"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: Generate a script that verifies if a domain is correctly pointed to a server.
Generated: DETERMINISTIC_f63e311e6175110a
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import sys

def check_domain(domain):
    """
    Check if the given domain is pointing to the expected IP address.

    Parameters:
    - domain (str): The domain name to check.

    Returns:
    - str: The resolved IP address of the domain.
    """
    try:
        # Resolve the domain name to an IP address
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"Error resolving domain '{domain}': {e}")
        sys.exit(1)

def main():
    """
    Main function to run the domain check.
    """
    # Example usage: replace with the domain you want to check
    domain = "example.com"

    # Check the domain and retrieve its IP address
    ip_address = check_domain(domain)

    # Print the resolved IP address
    print(f"The IP address for the domain '{domain}' is: {ip_address}")

if __name__ == "__main__":
    main()
```
