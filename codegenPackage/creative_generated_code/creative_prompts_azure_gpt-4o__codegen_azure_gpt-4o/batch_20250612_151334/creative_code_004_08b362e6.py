"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.vip
Prompt: Provide code to query and list all configured nameservers for a domain using Python's `dnspython` library.
Generated: DETERMINISTIC_08b362e6e7c7d8db
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def get_nameservers(domain):
    """
    Queries and retrieves all configured nameservers for a given domain.

    Args:
        domain (str): The domain name to query.

    Returns:
        list: A list of nameservers (as strings) for the domain.
    """
    try:
        # Query the domain for NS (nameserver) records using dnspython
        answer = dns.resolver.resolve(domain, 'NS')
        
        # Extract nameserver hostnames from the response
        nameservers = [ns.to_text() for ns in answer]
        return nameservers

    except dns.resolver.NXDOMAIN:
        # Handle the case where the domain does not exist
        print(f"Error: The domain '{domain}' does not exist.")
        return []

    except dns.resolver.Timeout:
        # Handle DNS query timeout issues
        print("Error: DNS query timed out.")
        return []

    except dns.resolver.NoAnswer:
        # Handle cases where no answer could be obtained
        print(f"Error: No answer was received for the domain '{domain}'.")
        return []

    except dns.exception.DNSException as e:
        # Catch-all for other DNS-related exceptions
        print(f"Error: An unexpected DNS error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    domain = "example.com"  # Replace with the domain you want to query
    nameservers = get_nameservers(domain)
    if nameservers:
        print(f"Nameservers for '{domain}':")
        for ns in nameservers:
            print(f"- {ns}")
    else:
        print("No nameservers found or an error occurred.")
```
