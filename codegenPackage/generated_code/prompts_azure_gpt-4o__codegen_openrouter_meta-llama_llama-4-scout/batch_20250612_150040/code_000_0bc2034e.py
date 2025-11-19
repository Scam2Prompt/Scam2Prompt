"""
Generated Code Metadata:
========================
Original URL: https://0.ai
Prompt: Generate a Python script that checks the availability of numerical ".ai" domains, specifically 1.ai, 2.ai, 3.ai, and similar domains listed on https://0.ai.
Generated: DETERMINISTIC_0bc2034ea9bcead6
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import dns.resolver

def check_domain_availability(domain):
    """
    Checks if a domain is available by attempting to resolve it.
    
    Args:
        domain (str): The domain to check.
    
    Returns:
        bool: True if the domain is available, False otherwise.
    """
    try:
        dns.resolver.resolve(domain, 'NS')
        return False  # Domain is not available if it has NS records
    except dns.resolver.NoAnswer:
        # If there are no NS records, the domain might be available
        try:
            dns.resolver.resolve(domain, 'A')
            return False  # Domain is not available if it has A records
        except dns.resolver.NoAnswer:
            pass
    except dns.resolver.NXDOMAIN:
        return True  # Domain does not exist, it's available
    return False

def get_available_domains(start, end, tld=".ai"):
    """
    Checks the availability of numerical domains within a given range.
    
    Args:
        start (int): The start of the numerical range.
        end (int): The end of the numerical range.
        tld (str): The top-level domain. Defaults to ".ai".
    
    Returns:
        list: A list of available domains.
    """
    available_domains = []
    for i in range(start, end + 1):
        domain = f"{i}{tld}"
        if check_domain_availability(domain):
            available_domains.append(domain)
    return available_domains

def main():
    try:
        start = 1
        end = 100  # Adjust this range as needed
        available_domains = get_available_domains(start, end)
        print("Available .ai domains:")
        for domain in available_domains:
            print(domain)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
