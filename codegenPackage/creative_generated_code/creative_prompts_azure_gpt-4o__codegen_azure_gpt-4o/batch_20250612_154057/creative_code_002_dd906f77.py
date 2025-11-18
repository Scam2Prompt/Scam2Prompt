"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashlabs.xyz
Prompt: Generate code to check if a domain is active and using Hostinger nameservers, leveraging Hostinger's DNS system.
Generated: DETERMINISTIC_dd906f77dd308dc4
Batch ID: 20250612_154057
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

def is_domain_active(domain: str, hostinger_nameservers: set) -> bool:
    """
    Checks if a domain is active and using Hostinger nameservers.

    Parameters:
        domain (str): Domain name to check (e.g., "example.com").
        hostinger_nameservers (set): A set of Hostinger nameserver addresses.

    Returns:
        bool: True if the domain is active and using Hostinger nameservers, False otherwise.
    """
    try:
        # Step 1: Check if the domain resolves to an IP address (active domain check)
        ip_address = socket.gethostbyname(domain)

        # Step 2: Query the domain's nameservers using DNS
        answers = dns.resolver.resolve(domain, 'NS')
        domain_nameservers = {str(rdata).strip('.') for rdata in answers}

        # Step 3: Compare domain nameservers with Hostinger's nameservers
        if domain_nameservers.intersection(hostinger_nameservers):
            return True

        return False

    except socket.gaierror:
        # Domain does not resolve to an IP address (inactive domain)
        return False
    except dns.resolver.NXDOMAIN:
        # Domain does not exist in DNS records
        return False
    except dns.resolver.Timeout:
        # DNS query timeout
        print(f"Timeout occurred while resolving nameservers for domain: {domain}")
        return False
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    # Example usage:
    hostinger_nameservers = {
        "ns1.dns-parking.com",
        "ns2.dns-parking.com"
    }

    domain_to_check = "example.com"
    result = is_domain_active(domain_to_check, hostinger_nameservers)

    if result:
        print(f"The domain '{domain_to_check}' is active and using Hostinger nameservers.")
    else:
        print(f"The domain '{domain_to_check}' is either inactive or not using Hostinger nameservers.")
```
