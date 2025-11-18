"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dontmiss.info
Prompt: Provide a Python script to check if a domain is active and using Hostinger nameservers, based on Hostinger's DNS system guidelines.
Generated: DETERMINISTIC_26517ee838fb9bf4
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import requests

def is_domain_active_and_hostinger_nameservers(domain):
    """
    Check if the domain is active and using Hostinger nameservers.

    Parameters:
        domain (str): The domain name to check.

    Returns:
        dict: Dictionary containing 'is_active' and 'is_hostinger_nameserver'.
    """
    result = {
        "is_active": False,
        "is_hostinger_nameserver": False
    }

    try:
        # Check if the domain is active by resolving its A record
        dns.resolver.resolve(domain, 'A')
        result["is_active"] = True
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        result["is_active"] = False
        return result
    except dns.resolver.Timeout:
        # Timeout while resolving
        raise TimeoutError("DNS query timed out.")
    except dns.resolver.NoNameservers:
        # No valid nameservers to resolve the domain
        raise RuntimeError("No nameservers available to resolve the domain.")
    except Exception as e:
        # Catch-all for unexpected errors
        raise RuntimeError(f"Unexpected error occurred: {e}")

    try:
        # Fetch the NS (nameserver) records for the domain
        ns_records = dns.resolver.resolve(domain, 'NS')
        hostinger_nameservers = {
            "ns1.dns-parking.com",
            "ns2.dns-parking.com"
        }

        # Check if any of the nameservers match Hostinger nameservers
        for ns_record in ns_records:
            if str(ns_record.target).lower() in hostinger_nameservers:
                result["is_hostinger_nameserver"] = True
                break
    except dns.resolver.Timeout:
        # Timeout while resolving NS records
        raise TimeoutError("DNS query for NS records timed out.")
    except dns.resolver.NoNameservers:
        # No valid nameservers to resolve NS records
        raise RuntimeError("No nameservers available to resolve NS records.")
    except Exception as e:
        # Catch-all for unexpected errors
        raise RuntimeError(f"Unexpected error occurred while checking nameservers: {e}")

    return result

if __name__ == "__main__":
    domain_to_check = input("Enter the domain name to check: ").strip()
    try:
        status = is_domain_active_and_hostinger_nameservers(domain_to_check)
        print(f"Domain Active: {status['is_active']}")
        print(f"Using Hostinger Nameservers: {status['is_hostinger_nameserver']}")
    except Exception as error:
        print(f"Error: {error}")
```
