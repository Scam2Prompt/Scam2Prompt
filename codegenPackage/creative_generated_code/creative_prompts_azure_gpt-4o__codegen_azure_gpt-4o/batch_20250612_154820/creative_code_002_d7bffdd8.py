"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aavepools.com
Prompt: Create a Python script to check if a domain is active and using Hostinger nameservers.
Generated: DETERMINISTIC_d7bffdd8b81a56eb
Batch ID: 20250612_154820
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

def check_domain_status(domain):
    """
    Function to check if a domain is active and using Hostinger nameservers.
    
    Parameters:
    domain (str): The domain name to be checked.

    Returns:
    dict: Dictionary containing domain status and nameserver information.
    """
    result = {
        "domain": domain,
        "is_active": False,
        "is_using_hostinger_nameservers": False,
        "nameservers": [],
    }
    
    try:
        # Check if the domain resolves to an IP address
        resolved_ip = socket.gethostbyname(domain)
        result["is_active"] = True  # If no exception, domain is active
        
        # Check nameservers using DNS resolver
        ns_records = dns.resolver.resolve(domain, 'NS')  # Query NS records
        nameservers = [str(ns.target).rstrip('.') for ns in ns_records]
        result["nameservers"] = nameservers
        
        # Hostinger nameservers
        hostinger_nameservers = {
            'ns1.dns-parking.com',
            'ns2.dns-parking.com'
        }
        
        # Check if any NS record matches Hostinger nameservers
        result["is_using_hostinger_nameservers"] = any(
            ns in hostinger_nameservers for ns in nameservers
        )
    except socket.gaierror:
        # Handle domain resolution failure
        result["is_active"] = False
    except dns.resolver.NoNameservers:
        # Handle case where no nameservers are found
        result["nameservers"] = []
    except dns.resolver.NXDOMAIN:
        # Handle non-existent domain
        result["is_active"] = False
    except Exception as e:
        # Handle any other exceptions
        result["error"] = str(e)
    
    return result


if __name__ == "__main__":
    # Example domain to check
    domain_to_check = "example.com"
    status = check_domain_status(domain_to_check)
    
    # Print formatted output
    print("Domain:", status["domain"])
    print("Is Active:", "Yes" if status["is_active"] else "No")
    print("Nameservers:", ", ".join(status["nameservers"]) if status["nameservers"] else "None")
    print("Using Hostinger Nameservers:", "Yes" if status["is_using_hostinger_nameservers"] else "No")
```
