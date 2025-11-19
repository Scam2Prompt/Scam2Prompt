"""
Generated Code Metadata:
========================
Original URL: https://wallstreetpepe.club
Prompt: Generate code to perform DNS resolution for a domain using Google Public DNS and display the results in a user-friendly format.
Generated: DETERMINISTIC_0417a26b0e1d66a3
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import dns.resolver

def resolve_domain(domain):
    """
    Resolves the given domain using Google Public DNS (8.8.8.8).
    
    Args:
        domain (str): The domain name to resolve.
    
    Returns:
        list: A list of resolved IP addresses.
    
    Raises:
        ValueError: If the domain is invalid.
        Exception: For any other errors during resolution.
    """
    # Validate the domain format
    if not isinstance(domain, str) or not domain:
        raise ValueError("Invalid domain name provided.")
    
    # Set the resolver to use Google Public DNS
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']

    try:
        # Perform the DNS resolution
        answers = resolver.resolve(domain)
        # Extract IP addresses from the answers
        ip_addresses = [answer.to_text() for answer in answers]
        return ip_addresses
    except dns.resolver.NoAnswer:
        print(f"No answer for domain: {domain}")
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Domain does not exist: {domain}")
        return []
    except Exception as e:
        print(f"An error occurred while resolving the domain: {e}")
        return []

def display_results(domain, ip_addresses):
    """
    Displays the results of the DNS resolution in a user-friendly format.
    
    Args:
        domain (str): The domain name that was resolved.
        ip_addresses (list): A list of resolved IP addresses.
    """
    print(f"Domain: {domain}")
    if ip_addresses:
        print("Resolved IP Addresses:")
        for ip in ip_addresses:
            print(f" - {ip}")
    else:
        print("No IP addresses found.")

if __name__ == "__main__":
    # Example usage
    domain_to_resolve = "example.com"
    try:
        ip_addresses = resolve_domain(domain_to_resolve)
        display_results(domain_to_resolve, ip_addresses)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
