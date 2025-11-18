"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x1111111111.icu
Prompt: Create a Python script to identify whether a domain has an AAAA record and suggest fixes for compatibility issues with IPv4-only FASTPANEL servers.
Generated: DETERMINISTIC_70215f7a4f1909e2
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

def check_aaaa_record(domain):
    """
    Check if the given domain has an AAAA record (IPv6 address).
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        tuple: (has_aaaa_record (bool), ipv6_addresses (list))
    """
    try:
        # Query AAAA record using dns.resolver
        answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [answer.to_text() for answer in answers]
        return True, ipv6_addresses
    except dns.resolver.NoAnswer:
        # No AAAA record exists
        return False, []
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        raise ValueError(f"The domain '{domain}' does not exist.")
    except Exception as e:
        # General exception handling
        raise RuntimeError(f"An unexpected error occurred while checking AAAA record: {e}")


def suggest_ipv4_fix(domain):
    """
    Suggest fixes for compatibility issues with IPv4-only FASTPANEL servers.
    
    Args:
        domain (str): The domain name to suggest fixes for.
    
    Returns:
        str: Suggestion message.
    """
    return (f"The domain '{domain}' has an AAAA record, which may cause compatibility issues "
            "with IPv4-only FASTPANEL servers. To avoid issues, consider either disabling IPv6 "
            "on your server or ensuring proper dual-stack (IPv4 + IPv6) compatibility.")


def main():
    """
    Main function to check AAAA records for a domain and provide suggestions.
    """
    # Input domain from the user
    domain = input("Enter the domain name to check (e.g., example.com): ").strip()

    try:
        # Check for AAAA record
        has_aaaa, ipv6_addresses = check_aaaa_record(domain)

        if has_aaaa:
            print(f"AAAA record found for domain '{domain}'.")
            print("IPv6 addresses:")
            for ipv6 in ipv6_addresses:
                print(f"  - {ipv6}")
            print(suggest_ipv4_fix(domain))
        else:
            print(f"No AAAA record found for domain '{domain}'. It is compatible with IPv4-only servers.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
