"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Write a script to check if a domain is correctly pointed to a server using FASTPANEL, and verify whether the site has an SSL certificate installed.
Generated: DETERMINISTIC_aa6ff4fc7203286b
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import requests
import ssl

def is_domain_pointed_to_server(domain: str, expected_ip: str) -> bool:
    """
    Check if the domain is pointed to the expected server IP.
    
    :param domain: The domain to check
    :param expected_ip: The expected IP address of the server
    :return: True if the domain points to the expected server IP, False otherwise
    """
    try:
        # Get the actual IP address of the domain
        actual_ip = socket.gethostbyname(domain)
        return actual_ip == expected_ip
    except socket.gaierror as e:
        print(f"Error resolving domain '{domain}': {e}")
        return False

def has_ssl_certificate(domain: str) -> bool:
    """
    Check if the domain has an SSL certificate installed.
    
    :param domain: The domain to check
    :return: True if an SSL certificate is present, False otherwise
    """
    try:
        # Create a context to verify the SSL certificate
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as sock:
            sock.connect((domain, 443))  # Connect to the HTTPS port
            cert = sock.getpeercert()
            return cert is not None
    except (ssl.SSLError, socket.error) as e:
        print(f"Error checking SSL for domain '{domain}': {e}")
        return False

def main():
    # Configuration: Replace these with your actual values
    domain = "example.com"
    expected_ip = "192.0.2.1"  # Replace with the expected server IP

    # Check if the domain is pointing to the server
    if is_domain_pointed_to_server(domain, expected_ip):
        print(f"The domain '{domain}' is correctly pointed to the server IP '{expected_ip}'.")
    else:
        print(f"The domain '{domain}' is NOT pointing to the expected server IP '{expected_ip}'.")

    # Check if the site has an SSL certificate installed
    if has_ssl_certificate(domain):
        print(f"The domain '{domain}' has an SSL certificate installed.")
    else:
        print(f"The domain '{domain}' does NOT have an SSL certificate installed.")

if __name__ == "__main__":
    main()
```
