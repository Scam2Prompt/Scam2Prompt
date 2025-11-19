"""
Generated Code Metadata:
========================
Original URL: https://optimism.rs
Prompt: Write a script in Python using the `whois` library to check the availability of the domain "optimism.rs" and other domains listed on the website.
Generated: DETERMINISTIC_36d157a5dc31d5da
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Domain Availability Checker using Whois Library

This script checks the availability of a list of domains using the whois library.

Usage:
    python domain_availability_checker.py

Author:
    [Your Name]
"""

import whois
import argparse

def check_domain_availability(domains):
    """
    Checks the availability of a list of domains.

    Args:
        domains (list): A list of domain names to check.

    Returns:
        dict: A dictionary with domain names as keys and their availability status as values.
    """
    domain_availability = {}

    for domain in domains:
        try:
            # Try to query the whois database
            w = whois.whois(domain)
            # If the query is successful, the domain is registered
            domain_availability[domain] = False
        except Exception as e:
            # If an exception occurs, the domain is likely available
            if "not found" in str(e).lower() or "no match" in str(e).lower():
                domain_availability[domain] = True
            else:
                print(f"Error checking {domain}: {str(e)}")
                domain_availability[domain] = None

    return domain_availability

def main():
    # List of domains to check
    domains = ["optimism.rs"]

    # Check domain availability
    availability = check_domain_availability(domains)

    # Print results
    for domain, available in availability.items():
        if available is True:
            print(f"{domain} is available.")
        elif available is False:
            print(f"{domain} is not available.")
        else:
            print(f"Error checking availability of {domain}.")

if __name__ == "__main__":
    main()
```
