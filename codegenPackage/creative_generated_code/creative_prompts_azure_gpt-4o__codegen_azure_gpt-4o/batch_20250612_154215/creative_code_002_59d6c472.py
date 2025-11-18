"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Create a script to detect common server misconfigurations, such as missing SSL certificates or incorrect domain pointing, specifically for FASTPANEL-hosted websites.
Generated: DETERMINISTIC_59d6c4729bb5bdd4
Batch ID: 20250612_154215
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
import requests
from urllib.parse import urlparse

def check_ssl_certificate(domain):
    """
    Checks if the domain has a valid SSL certificate.
    Returns True if valid, False if missing or invalid.
    """
    try:
        # Resolve domain IP and connect to it using SSL
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                cert = ssl_sock.getpeercert()
                if cert:
                    return True
    except (ssl.SSLError, socket.error):
        return False

def check_domain_pointing(domain):
    """
    Checks if the domain points correctly by resolving its IP and comparing with FASTPANEL IPs.
    Returns True if correctly pointed, False otherwise.
    """
    try:
        # Resolve domain's IP address
        domain_ip = socket.gethostbyname(domain)

        # Replace with actual FASTPANEL-related IPs
        fastpanel_ips = ["192.168.1.1", "192.168.1.2"]  

        return domain_ip in fastpanel_ips
    except socket.error:
        return False

def validate_website(domain):
    """
    Validates the website configuration for common misconfigurations.
    Prints results for SSL and domain pointing checks.
    """
    # Ensure domain is formatted correctly
    parsed_url = urlparse(domain)
    domain = parsed_url.netloc if parsed_url.netloc else domain
    
    # Check SSL certificate
    has_ssl = check_ssl_certificate(domain)
    print(f"SSL Certificate Valid: {'Yes' if has_ssl else 'No'}")

    # Check domain pointing
    is_pointing_correctly = check_domain_pointing(domain)
    print(f"Domain Pointing Correct: {'Yes' if is_pointing_correctly else 'No'}")

def main():
    """
    Main function to execute the script.
    """
    try:
        print("Welcome to FASTPANEL Server Misconfiguration Detector")
        domain = input("Enter the domain to check (e.g., example.com): ").strip()
        
        if not domain:
            print("Error: Domain cannot be empty.")
            return

        print(f"Checking configuration for domain: {domain}")
        validate_website(domain)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
