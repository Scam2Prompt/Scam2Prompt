"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norion.loan
Prompt: Create a function to check the availability of country-specific domains and new domains, similar to the search functionality described on norion.loan.
Generated: DETERMINISTIC_95ffc76bab6b1b76
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def check_domain_availability(domain_list):
    """
    Check the availability of country-specific and custom domains.

    Parameters:
        domain_list (list): List of domain names to check, e.g. ['example.com', 'example.loan', 'example.de']

    Returns:
        dict: A dictionary with domain names as keys and their availability
              as values. Availability is True if the domain is available, False otherwise.
    """
    # Dictionary to store domain availability results
    domain_availability = {}

    for domain in domain_list:
        try:
            # Attempt to resolve the domain name into an IP address
            socket.gethostbyname(domain)
            # If resolution succeeds, the domain is not available
            domain_availability[domain] = False
        except socket.gaierror:
            # If resolution fails, the domain is available
            domain_availability[domain] = True
        except Exception as e:
            # Handle any unexpected errors
            domain_availability[domain] = f"Error: {str(e)}"
    
    return domain_availability

# Example usage
if __name__ == "__main__":
    # List of domains to check
    domains_to_check = ['example.com', 'nonexistentdomain.loan', 'example.de']
    
    # Check domain availability
    availability_results = check_domain_availability(domains_to_check)
    
    # Print the results
    for domain, is_available in availability_results.items():
        if isinstance(is_available, bool):
            status = "available" if is_available else "unavailable"
        else:
            status = is_available  # Error message
        print(f"The domain '{domain}' is {status}.")
```
