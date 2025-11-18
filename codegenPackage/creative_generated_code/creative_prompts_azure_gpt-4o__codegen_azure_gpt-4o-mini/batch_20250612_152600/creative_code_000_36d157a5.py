"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism.rs
Prompt: Write a script in Python using the `whois` library to check the availability of the domain "optimism.rs" and other domains listed on the website.
Generated: DETERMINISTIC_36d157a5dc31d5da
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import whois
import logging

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_domain_availability(domain):
    """
    Check the availability of a domain.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is available, False otherwise.
    """
    try:
        # Use the whois library to retrieve domain information
        domain_info = whois.whois(domain)

        # If the domain_info object is empty, the domain is available
        if domain_info is None or not domain_info.domain_name:
            logging.info(f'The domain "{domain}" is available.')
            return True
        else:
            logging.info(f'The domain "{domain}" is NOT available.')
            return False

    except Exception as e:
        logging.error(f'An error occurred while checking the domain "{domain}": {e}')
        return False

def main():
    # List of domains to check
    domains_to_check = [
        "optimism.rs",
        "example.com",
        "testdomain123.org",
        "nonexistentdomain.xyz"
    ]

    logging.info("Checking domain availability...")
    
    # Check each domain for availability
    for domain in domains_to_check:
        is_available = check_domain_availability(domain)
        print(f'Domain: {domain}, Available: {is_available}')

if __name__ == "__main__":
    main()
```
