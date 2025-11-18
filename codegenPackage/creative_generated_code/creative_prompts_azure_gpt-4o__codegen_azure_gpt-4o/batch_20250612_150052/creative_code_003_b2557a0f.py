"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connext.site
Prompt: Create a script to automate the process of checking if a domain is active and using Hostinger nameservers, as described on the Hostinger site.
Generated: DETERMINISTIC_b2557a0f8ca71440
Batch ID: 20250612_150052
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
    Checks if a domain is active and using Hostinger nameservers.

    Parameters:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the status and nameserver information.
    """
    result = {
        "domain": domain,
        "is_active": False,
        "using_hostinger_nameservers": False,
        "nameservers": [],
        "error": None
    }

    try:
        # Check if the domain resolves to an IP address
        ip_address = socket.gethostbyname(domain)
        result["is_active"] = True
    except socket.gaierror as e:
        result["error"] = f"Domain resolution failed: {e}"
        return result

    try:
        # Retrieve nameservers for the domain using DNS resolver
        answer = dns.resolver.resolve(domain, 'NS')
        nameservers = [str(rdata.target).strip('.') for rdata in answer]
        result["nameservers"] = nameservers

        # Check if Hostinger nameservers are being used
        hostinger_nameservers = {"ns1.dns-parking.com", "ns2.dns-parking.com"}
        if any(ns in hostinger_nameservers for ns in nameservers):
            result["using_hostinger_nameservers"] = True

    except dns.resolver.NoNameservers as e:
        result["error"] = f"No nameservers found for domain: {e}"
    except dns.resolver.NXDOMAIN as e:
        result["error"] = f"Domain does not exist: {e}"
    except dns.resolver.Timeout as e:
        result["error"] = f"DNS resolution timed out: {e}"
    except Exception as e:
        result["error"] = f"An unexpected error occurred: {e}"

    return result

if __name__ == "__main__":
    # Example usage: Replace 'example.com' with your desired domain
    domain = "example.com"
    status = check_domain_status(domain)
    
    # Print domain status in a user-friendly way
    print(f"Domain: {status['domain']}")
    print(f"Active: {'Yes' if status['is_active'] else 'No'}")
    print(f"Using Hostinger Nameservers: {'Yes' if status['using_hostinger_nameservers'] else 'No'}")
    print(f"Nameservers: {', '.join(status['nameservers']) if status['nameservers'] else 'None'}")
    if status["error"]:
        print(f"Error: {status['error']}")
```

This Python script uses the `socket` and `dns.resolver` libraries to check if a domain is active and determine whether it is using Hostinger nameservers (`ns1.dns-parking.com` and `ns2.dns-parking.com`). It includes error handling for various DNS resolution issues and outputs the results clearly.
