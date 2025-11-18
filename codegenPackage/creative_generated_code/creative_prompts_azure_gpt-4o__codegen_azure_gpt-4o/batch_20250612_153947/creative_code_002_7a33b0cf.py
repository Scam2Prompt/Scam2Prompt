"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Provide a Python script to automate troubleshooting for common FASTPANEL server issues, including domain pointing, SSL certificate installation, and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_7a33b0cf76eac7a1
Batch ID: 20250612_153947
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.ssllabs.com/api/v3/analyze": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.fastpanel.direct/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import socket
import requests
from typing import Tuple

# Define constants
FASTPANEL_API_URL = "https://api.fastpanel.direct/"
SSL_TEST_URL = "https://www.ssllabs.com/api/v3/analyze"

def check_domain_pointing(domain: str) -> Tuple[bool, str]:
    """
    Checks if a domain is properly pointed to the server IP.
    
    :param domain: The domain to check.
    :return: Tuple containing a boolean for success and a message.
    """
    try:
        server_ip = socket.gethostbyname(socket.gethostname())
        domain_ip = socket.gethostbyname(domain)
        if server_ip == domain_ip:
            return True, f"Domain {domain} is correctly pointed to {server_ip}."
        return False, f"Domain {domain} is pointed to {domain_ip} instead of {server_ip}."
    except socket.gaierror as e:
        return False, f"Error resolving domain {domain}: {str(e)}"

def check_ssl_certificate(domain: str) -> Tuple[bool, str]:
    """
    Checks if a domain has a valid SSL certificate installed.
    
    :param domain: The domain to check.
    :return: Tuple containing a boolean for success and a message.
    """
    try:
        response = requests.get(f"{SSL_TEST_URL}?host={domain}")
        if response.status_code == 200 and "status" in response.json():
            status = response.json()["status"]
            if status == "READY":
                return True, f"Valid SSL certificate installed for domain {domain}."
            return False, f"SSL certificate issue detected for domain {domain}: {status}."
        return False, f"Could not retrieve SSL status for domain {domain}."
    except requests.RequestException as e:
        return False, f"Error checking SSL certificate for domain {domain}: {str(e)}"

def check_ipv4_ipv6_compatibility(domain: str) -> Tuple[bool, str]:
    """
    Checks IPv4 and IPv6 compatibility for a domain.
    
    :param domain: The domain to check.
    :return: Tuple containing a boolean for success and a message.
    """
    ipv4_compatible = False
    ipv6_compatible = False
    try:
        # Check IPv4
        socket.getaddrinfo(domain, None, socket.AF_INET)
        ipv4_compatible = True
    except socket.gaierror:
        ipv4_compatible = False
    
    try:
        # Check IPv6
        socket.getaddrinfo(domain, None, socket.AF_INET6)
        ipv6_compatible = True
    except socket.gaierror:
        ipv6_compatible = False

    if ipv4_compatible and ipv6_compatible:
        return True, f"Domain {domain} is compatible with both IPv4 and IPv6."
    elif ipv4_compatible:
        return False, f"Domain {domain} is only compatible with IPv4."
    elif ipv6_compatible:
        return False, f"Domain {domain} is only compatible with IPv6."
    else:
        return False, f"Domain {domain} is not compatible with IPv4 or IPv6."

def troubleshoot_fastpanel_domain(domain: str):
    """
    Automates troubleshooting for FASTPANEL server issues related to the domain.
    
    :param domain: The domain to troubleshoot.
    """
    print("Starting troubleshooting for domain:", domain)

    # Step 1: Check domain pointing
    success, message = check_domain_pointing(domain)
    print("[Domain Pointing Check]", message)
    
    # Step 2: Check SSL certificate
    success, message = check_ssl_certificate(domain)
    print("[SSL Certificate Check]", message)
    
    # Step 3: Check IPv4/IPv6 compatibility
    success, message = check_ipv4_ipv6_compatibility(domain)
    print("[IPv4/IPv6 Compatibility Check]", message)

if __name__ == "__main__":
    try:
        domain_to_check = input("Enter the domain to troubleshoot: ").strip()
        troubleshoot_fastpanel_domain(domain_to_check)
    except Exception as e:
        print(f"Error during troubleshooting: {str(e)}")
```
