"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://876981455175.icu
Prompt: Recommend tools or libraries to automate the detection of AAAA record issues for domains hosted on FASTPANEL servers.
Generated: DETERMINISTIC_5104b5b26faf632e
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to detect and report AAAA record issues for domains hosted on FASTPANEL servers.
This script uses the `dnspython` library for DNS queries and proper error handling.

Requirements:
- dnspython (Install with `pip install dnspython`)

Note:
This script assumes you have a list of domains hosted on FASTPANEL servers
to check for AAAA record issues.
"""

import dns.resolver

def check_aaaa_record(domain):
    """
    Check if the given domain has valid AAAA records (IPv6).
    
    Parameters:
        domain (str): The domain name to check.
    
    Returns:
        list: List of valid AAAA records or an error message if no records are found.
    """
    try:
        # Query for AAAA records using dnspython
        answers = dns.resolver.resolve(domain, 'AAAA')
        # Extract the IPv6 addresses from the response
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return f"No AAAA records found for domain: {domain}"
    except dns.resolver.NXDOMAIN:
        return f"Domain does not exist: {domain}"
    except dns.resolver.Timeout:
        return f"Request timed out while querying domain: {domain}"
    except dns.exception.DNSException as e:
        return f"An error occurred while querying domain: {domain}. Error: {str(e)}"

def check_domains(domains):
    """
    Check AAAA records for a list of domains and print the results.
    
    Parameters:
        domains (list): List of domain names to check.
    """
    for domain in domains:
        print(f"Checking domain: {domain}")
        result = check_aaaa_record(domain)
        if isinstance(result, list):
            print(f"Valid AAAA records for {domain}: {', '.join(result)}")
        else:
            print(result)

if __name__ == "__main__":
    # Sample domains hosted on FASTPANEL servers (replace with actual domains)
    domains_to_check = [
        "example.com",
        "anotherexample.com",
        "nonexistentdomain.com"
    ]
    
    # Perform AAAA record checks for the domains
    check_domains(domains_to_check)
```
