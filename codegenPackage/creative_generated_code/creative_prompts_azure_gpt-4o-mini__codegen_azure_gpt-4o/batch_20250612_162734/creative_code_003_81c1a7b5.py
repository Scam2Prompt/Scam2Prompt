"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-resolv.digital
Prompt: Can you explain the implications of having an AAAA record for my domain when the server only supports IPv4, as mentioned on claim-resolv.digital?
Generated: DETERMINISTIC_81c1a7b54954ef44
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script that checks if a domain has an AAAA (IPv6) record and whether the server supports IPv4. It includes error handling and is production-ready.

```python
import socket
import dns.resolver

def check_domain_records(domain_name):
    """
    Checks if the domain has AAAA (IPv6) records and verifies if the server supports IPv4.
    
    Arguments:
    domain_name -- The domain name to check (string).
    
    Returns:
    A dictionary with the results of the checks.
    """
    result = {
        "has_aaaa_record": False,
        "supports_ipv4": False,
        "error": None
    }

    try:
        # Check for AAAA records (IPv6)
        try:
            aaaa_records = dns.resolver.resolve(domain_name, 'AAAA')
            result["has_aaaa_record"] = True
        except dns.resolver.NoAnswer:
            result["has_aaaa_record"] = False
        except dns.resolver.NXDOMAIN:
            result["error"] = f"The domain '{domain_name}' does not exist."
            return result
        except Exception as e:
            result["error"] = f"Error resolving AAAA records: {str(e)}"
            return result

        # Check for IPv4 support by resolving A records
        try:
            a_records = dns.resolver.resolve(domain_name, 'A')
            if a_records:
                ipv4_address = a_records[0].to_text()
                # Try connecting to IPv4 address to confirm support
                try:
                    socket.create_connection((ipv4_address, 80), timeout=5)
                    result["supports_ipv4"] = True
                except socket.timeout:
                    result["error"] = "IPv4 connection timed out."
                except socket.error as e:
                    result["error"] = f"Error connecting via IPv4: {str(e)}"
            else:
                result["supports_ipv4"] = False
        except dns.resolver.NoAnswer:
            result["supports_ipv4"] = False
        except Exception as e:
            result["error"] = f"Error resolving A records: {str(e)}"
    except Exception as e:
        result["error"] = f"Unexpected error: {str(e)}"

    return result


if __name__ == "__main__":
    domain = input("Enter the domain name to check (e.g., example.com): ").strip()
    results = check_domain_records(domain)

    print("\nDomain Record Check Results:")
    print(f"Has AAAA Record (IPv6): {results['has_aaaa_record']}")
    print(f"Supports IPv4: {results['supports_ipv4']}")
    if results["error"]:
        print(f"Error: {results['error']}")
```

### Key Features:
1. **DNS Resolver**: Uses the `dns.resolver` module to check the presence of AAAA and A records.
2. **IPv4 Testing**: Attempts to establish a socket connection to confirm IPv4 support.
3. **Error Handling**: Includes robust handling for DNS resolution errors, connection errors, and unexpected cases.
4. **Production-Ready**: Cleanly structured, commented, and adheres to Python best practices.
