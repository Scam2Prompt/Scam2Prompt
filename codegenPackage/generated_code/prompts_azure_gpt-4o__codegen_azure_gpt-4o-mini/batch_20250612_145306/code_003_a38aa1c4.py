"""
Generated Code Metadata:
========================
Original URL: https://tech-connect.cloud
Prompt: Create a script to check if a domain is active and using Hostinger nameservers, leveraging DNS query libraries in Python.
Generated: DETERMINISTIC_a38aa1c417c262b1
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.exception
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_domain_active(domain):
    """
    Check if a domain is active by querying its DNS records.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is active, False otherwise.
    """
    try:
        # Attempt to resolve the domain's A record
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        logging.warning(f"Domain {domain} does not have an active A record.")
        return False
    except dns.exception.DNSException as e:
        logging.error(f"DNS query failed for {domain}: {e}")
        return False

def is_using_hostinger_nameservers(domain):
    """
    Check if the domain is using Hostinger nameservers.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is using Hostinger nameservers, False otherwise.
    """
    hostinger_nameservers = [
        'ns1.dns-parking.com',
        'ns2.dns-parking.com',
        'ns1.hostinger.com',
        'ns2.hostinger.com',
        'ns3.hostinger.com',
        'ns4.hostinger.com'
    ]

    try:
        # Query the NS records for the domain
        ns_records = dns.resolver.resolve(domain, 'NS')
        ns_list = [str(ns).lower() for ns in ns_records]

        # Check if any of the nameservers match Hostinger's
        for ns in ns_list:
            if ns in hostinger_nameservers:
                return True
        return False
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        logging.warning(f"No NS records found for {domain}.")
        return False
    except dns.exception.DNSException as e:
        logging.error(f"DNS query failed for {domain}: {e}")
        return False

def check_domain(domain):
    """
    Check if a domain is active and using Hostinger nameservers.

    Args:
        domain (str): The domain name to check.

    Returns:
        None
    """
    if is_domain_active(domain):
        logging.info(f"Domain {domain} is active.")
        if is_using_hostinger_nameservers(domain):
            logging.info(f"Domain {domain} is using Hostinger nameservers.")
        else:
            logging.info(f"Domain {domain} is not using Hostinger nameservers.")
    else:
        logging.info(f"Domain {domain} is not active.")

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"  # Replace with the domain you want to check
    check_domain(domain_to_check)
```
