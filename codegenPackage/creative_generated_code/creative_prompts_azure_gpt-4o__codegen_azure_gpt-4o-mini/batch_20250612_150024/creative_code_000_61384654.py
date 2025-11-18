"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Write code to check if a domain is correctly pointed to a server using DNS records, including AAAA and A records, as described in FASTPANEL troubleshooting documentation.
Generated: DETERMINISTIC_61384654064025cd
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_domain_dns(domain: str) -> bool:
    """
    Check if the given domain is correctly pointed to a server by retrieving A and AAAA records.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain has valid A or AAAA records, False otherwise.
    """
    try:
        # Resolve A records
        a_records = dns.resolver.resolve(domain, 'A')
        logging.info(f"A records for {domain}: {[record.address for record in a_records]}")
        
        # Resolve AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        logging.info(f"AAAA records for {domain}: {[record.address for record in aaaa_records]}")
        
        # If we have either A or AAAA records, the domain is correctly pointed
        return bool(a_records or aaaa_records)
    
    except dns.resolver.NoAnswer:
        logging.warning(f"No DNS answer for domain: {domain}")
        return False
    except dns.resolver.NXDOMAIN:
        logging.error(f"Domain {domain} does not exist.")
        return False
    except dns.resolver.Timeout:
        logging.error(f"DNS query for {domain} timed out.")
        return False
    except Exception as e:
        logging.exception(f"An unexpected error occurred while checking DNS for {domain}: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    domain_to_check = "example.com"
    if check_domain_dns(domain_to_check):
        logging.info(f"The domain {domain_to_check} is correctly pointed to a server.")
    else:
        logging.info(f"The domain {domain_to_check} is NOT correctly pointed to a server.")
```
