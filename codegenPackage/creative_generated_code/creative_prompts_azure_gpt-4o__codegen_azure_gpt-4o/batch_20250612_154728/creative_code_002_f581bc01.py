"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomsolana.com
Prompt: Generate a script to check if a domain is active and using Hostinger nameservers, based on Hostinger's DNS system guidelines.
Generated: DETERMINISTIC_f581bc01a9e4f86c
Batch ID: 20250612_154728
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

def check_domain_hostinger_nameservers(domain):
    """
    Checks if a domain is active and using Hostinger nameservers.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary with the status of the domain and nameserver usage.
    """
    response = {
        "domain_active": False,
        "using_hostinger_nameservers": False,
        "error": None
    }

    try:
        # Step 1: Check if the domain is active by resolving its IP address
        socket.gethostbyname(domain)
        response["domain_active"] = True

        # Step 2: Query the nameservers of the domain
        resolver = dns.resolver.Resolver()
        nameservers = resolver.resolve(domain, 'NS')

        # Step 3: Validate if Hostinger nameservers are in use
        hostinger_nameservers = {"ns1.dns-parking.com.", "ns2.dns-parking.com."}
        for ns in nameservers:
            if ns.to_text() in hostinger_nameservers:
                response["using_hostinger_nameservers"] = True
                break

    except socket.gaierror:
        # Handle the case where the domain cannot be resolved
        response["error"] = f"Domain '{domain}' cannot be resolved. It may be inactive."
    except dns.resolver.NoNameservers:
        # Handle the case where no nameservers are found
        response["error"] = f"No nameservers found for domain '{domain}'."
    except Exception as e:
        # Catch other unexpected exceptions
        response["error"] = f"An error occurred: {str(e)}"

    return response

if __name__ == "__main__":
    # Example usage
    domain_to_check = input("Enter the domain to check: ").strip()
    result = check_domain_hostinger_nameservers(domain_to_check)
    print("Domain Status:")
    print(f"  Active: {result['domain_active']}")
    print(f"  Using Hostinger Nameservers: {result['using_hostinger_nameservers']}")
    if result["error"]:
        print(f"  Error: {result['error']}")
```
