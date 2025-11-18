"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x000000000000000.icu
Prompt: Create a function to detect whether a domain has an AAAA record and provide a fallback solution for IPv4-only servers in FASTPANEL.
Generated: DETERMINISTIC_6cfefe6fc06b8052
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_aaaa_record(domain):
    """
    Check if a given domain has an AAAA record (IPv6).

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if an AAAA record exists, False otherwise.
    """
    try:
        # Query the AAAA record for the specified domain
        answers = dns.resolver.resolve(domain, 'AAAA')
        # If the query returns answers, the domain has an AAAA record
        return len(answers) > 0
    except dns.resolver.NoAnswer:
        logging.warning(f"No AAAA record found for {domain}.")
        return False
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
        return False
    except Exception as e:
        logging.error(f"An error occurred while checking AAAA record for {domain}: {e}")
        return False

def fallback_to_ipv4(domain):
    """
    Fallback function to check for an A record (IPv4) if AAAA record does not exist.

    Args:
        domain (str): The domain name for fallback check.

    Returns:
        bool: True if an A record exists, False otherwise.
    """
    try:
        # Query the A record for the specified domain
        answers = dns.resolver.resolve(domain, 'A')
        return len(answers) > 0
    except dns.resolver.NoAnswer:
        logging.warning(f"No A record found for {domain}.")
        return False
    except dns.resolver.NXDOMAIN:
        logging.error(f"The domain {domain} does not exist.")
        return False
    except Exception as e:
        logging.error(f"An error occurred while checking A record for {domain}: {e}")
        return False

def main(domain):
    """
    Main function to check for AAAA record and fallback to A record if necessary.

    Args:
        domain (str): The domain name to check.
    """
    has_aaaa = check_aaaa_record(domain)
    
    if has_aaaa:
        logging.info(f"The domain {domain} has an AAAA record.")
    else:
        logging.info(f"The domain {domain} does not have an AAAA record. Checking for fallback to IPv4...")
        has_a = fallback_to_ipv4(domain)
        
        if has_a:
            logging.info(f"The domain {domain} has an A record (IPv4).")
        else:
            logging.info(f"The domain {domain} does not have an A record (IPv4) either.")

if __name__ == "__main__":
    # Example usage of the main function with a specified domain
    domain_to_check = "example.com"  # Replace with the desired domain
    main(domain_to_check)
```
