"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Generate a code snippet that demonstrates how to query Google Public DNS for an IP address using a specific domain.
Generated: DETERMINISTIC_69bf9501b3c44b82
Batch ID: 20250612_155607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def query_google_dns(domain_name):
    """
    Queries Google Public DNS for the IP address of the given domain name.

    Args:
        domain_name (str): The domain name to be resolved.

    Returns:
        list: A list of IP addresses associated with the domain name.

    Raises:
        ValueError: If the domain name is invalid or no records are found.
        dns.exception.DNSException: If there is an issue with DNS resolution.
    """
    try:
        # Resolver setup to use Google Public DNS (8.8.8.8 and 8.8.4.4)
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        
        # Query the domain name for A (IPv4) records
        answers = resolver.resolve(domain_name, 'A')
        
        # Collect and return the IP addresses
        ip_addresses = [str(answer) for answer in answers]
        return ip_addresses

    except dns.resolver.NXDOMAIN:
        raise ValueError(f"No DNS records found for domain: {domain_name}")
    except dns.resolver.Timeout:
        raise dns.exception.DNSException("DNS query timed out.")
    except dns.resolver.NoAnswer:
        raise ValueError(f"No answer received for domain: {domain_name}")
    except dns.resolver.NoNameservers:
        raise dns.exception.DNSException("No nameservers available for resolution.")

# Example usage:
if __name__ == "__main__":
    try:
        domain = "example.com"
        ip_list = query_google_dns(domain)
        print(f"IP addresses for {domain}: {ip_list}")
    except Exception as e:
        print(f"Error: {e}")
```
