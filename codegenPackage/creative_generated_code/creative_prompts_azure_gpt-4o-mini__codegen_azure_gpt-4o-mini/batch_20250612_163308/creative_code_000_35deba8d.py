"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-2v.xyz
Prompt: How can I use Google Public DNS to resolve a domain name like example.com?
Generated: DETERMINISTIC_35deba8d5cb18c1a
Batch ID: 20250612_163308
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

def resolve_domain(domain_name):
    """
    Resolves the given domain name using Google Public DNS (8.8.8.8 and 8.8.4.4).
    
    Args:
        domain_name (str): The domain name to resolve.
    
    Returns:
        list: A list of IP addresses associated with the domain name.
    
    Raises:
        ValueError: If the provided domain name is invalid.
        Exception: For any other errors encountered during resolution.
    """
    # Validate the domain name
    if not isinstance(domain_name, str) or not domain_name:
        raise ValueError("Invalid domain name provided.")
    
    # Define Google Public DNS servers
    google_dns_servers = ['8.8.8.8', '8.8.4.4']
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    
    try:
        # Set the nameservers to Google Public DNS
        dns.resolver.default_resolver.nameservers = google_dns_servers
        
        # Perform the DNS query
        answers = dns.resolver.resolve(domain_name, 'A')
        
        # Extract IP addresses from the response
        ip_addresses = [answer.to_string() for answer in answers]
        return ip_addresses
    
    except dns.resolver.NoAnswer:
        raise Exception("No answer for the domain: {}".format(domain_name))
    except dns.resolver.NXDOMAIN:
        raise Exception("Domain does not exist: {}".format(domain_name))
    except Exception as e:
        raise Exception("An error occurred while resolving the domain: {}".format(e))

# Example usage
if __name__ == "__main__":
    try:
        domain = "example.com"
        ip_list = resolve_domain(domain)
        print(f"IP addresses for {domain}: {ip_list}")
    except Exception as e:
        print(f"Error: {e}")
```
