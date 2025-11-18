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

def check_domain_availability(domain_name):
    """
    Checks the availability of a domain using the `whois` library.
    
    Parameters:
        domain_name (str): The domain name to check (e.g., "example.com").
        
    Returns:
        str: A message indicating if the domain is available or already registered.
    """
    try:
        # Perform the whois query
        domain_info = whois.whois(domain_name)
        
        # Check if the domain has a 'domain_name' field indicating registration
        if domain_info.get('domain_name'):
            return f"The domain '{domain_name}' is already registered."
        else:
            return f"The domain '{domain_name}' appears to be available."
    except Exception as e:
        # Handle errors gracefully (e.g., invalid domain names or connection issues)
        return f"Error checking the domain '{domain_name}': {str(e)}"

def check_domains_from_list(domain_list):
    """
    Checks the availability of a list of domains.
    
    Parameters:
        domain_list (list): A list of domain names to check.
        
    Returns:
        dict: A dictionary with domain names as keys and availability messages as values.
    """
    results = {}
    for domain in domain_list:
        results[domain] = check_domain_availability(domain)
    return results

if __name__ == "__main__":
    # Domain list to check (including "optimism.rs")
    domain_list = [
        "optimism.rs",
        "example.com",
        "nonexistentdomain.xyz"
    ]
    
    # Check domain availability
    domain_availability = check_domains_from_list(domain_list)
    
    # Print results
    print("Domain Availability Results:")
    for domain, status in domain_availability.items():
        print(f"{domain}: {status}")
```
