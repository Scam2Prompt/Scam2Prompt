"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Create a Python script that uses a library like `socket` or `dnspython` to test IPv4 and IPv6 compatibility for a given domain.
Generated: DETERMINISTIC_63cea43c5a336d3e
Batch ID: 20250612_153700
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

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ipv4(domain):
    """Check if the domain has an IPv4 address."""
    try:
        ipv4_address = socket.getaddrinfo(domain, None, socket.AF_INET)
        logging.info(f"IPv4 addresses for {domain}: {[addr[4][0] for addr in ipv4_address]}")
        return True
    except socket.gaierror as e:
        logging.error(f"Error fetching IPv4 addresses for {domain}: {e}")
        return False

def check_ipv6(domain):
    """Check if the domain has an IPv6 address."""
    try:
        ipv6_address = socket.getaddrinfo(domain, None, socket.AF_INET6)
        logging.info(f"IPv6 addresses for {domain}: {[addr[4][0] for addr in ipv6_address]}")
        return True
    except socket.gaierror as e:
        logging.error(f"Error fetching IPv6 addresses for {domain}: {e}")
        return False

def test_domain_compatibility(domain):
    """Test the IPv4 and IPv6 compatibility for the given domain."""
    logging.info(f"Testing domain: {domain}")
    ipv4_compatible = check_ipv4(domain)
    ipv6_compatible = check_ipv6(domain)

    if ipv4_compatible and ipv6_compatible:
        logging.info(f"{domain} is compatible with both IPv4 and IPv6.")
    elif ipv4_compatible:
        logging.info(f"{domain} is compatible with IPv4 only.")
    elif ipv6_compatible:
        logging.info(f"{domain} is compatible with IPv6 only.")
    else:
        logging.info(f"{domain} has no compatible addresses.")

if __name__ == "__main__":
    # Example domain; you can replace it with any valid domain to test
    domain_to_test = "example.com"
    test_domain_compatibility(domain_to_test)
```
