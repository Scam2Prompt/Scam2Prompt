"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x1111.icu
Prompt: Create a diagnostic tool to identify issues with AAAA records and IPv4 compatibility for domains hosted on FASTPANEL.
Generated: DETERMINISTIC_4b30fefaa81f52ef
Batch ID: 20250612_154207
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

def check_aaaa_records(domain):
    """
    Check for AAAA (IPv6) records of a domain.
    :param domain: The domain to check
    :return: List of AAAA records if they exist, otherwise an empty list
    """
    try:
        # Resolve AAAA records using DNS resolver
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        return [record.to_text() for record in aaaa_records]
    except dns.resolver.NoAnswer:
        return []  # No AAAA records found
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain '{domain}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"Failed to resolve AAAA records for '{domain}': {str(e)}")


def check_ipv4_compatibility(domain):
    """
    Check for IPv4 compatibility of a domain.
    :param domain: The domain to check
    :return: IPv4 address if compatible, otherwise None
    """
    try:
        # Attempt to resolve IPv4 address using socket library
        ipv4_address = socket.gethostbyname(domain)
        return ipv4_address
    except socket.gaierror:
        return None  # No IPv4 compatibility


def diagnostic_tool(domain):
    """
    Perform diagnostic checks on a domain for AAAA records and IPv4 compatibility.
    :param domain: The domain to check
    :return: Dictionary with diagnostic results
    """
    results = {
        "domain": domain,
        "aaaa_records": [],
        "ipv4_compatible": False,
        "ipv4_address": None
    }
    
    try:
        # Check for AAAA records
        results["aaaa_records"] = check_aaaa_records(domain)
        
        # Check for IPv4 compatibility
        ipv4_address = check_ipv4_compatibility(domain)
        results["ipv4_compatible"] = ipv4_address is not None
        results["ipv4_address"] = ipv4_address

    except ValueError as ve:
        results["error"] = str(ve)
    except RuntimeError as re:
        results["error"] = str(re)
    except Exception as e:
        results["error"] = f"An unexpected error occurred: {str(e)}"
    
    return results


if __name__ == "__main__":
    # Example usage
    print("FASTPANEL Domain Diagnostic Tool")
    domain = input("Enter the domain to diagnose: ").strip()
    
    if not domain:
        print("Error: No domain provided.")
    else:
        results = diagnostic_tool(domain)
        print("\nDiagnostic Results:")
        print(f"Domain: {results['domain']}")
        print(f"AAAA Records: {results['aaaa_records'] if results['aaaa_records'] else 'None found'}")
        print(f"IPv4 Compatible: {results['ipv4_compatible']}")
        if results["ipv4_compatible"]:
            print(f"IPv4 Address: {results['ipv4_address']}")
        if "error" in results:
            print(f"Error: {results['error']}")
```
