"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://425876928756287.icu
Prompt: Provide a Python function to identify whether a domain has an AAAA record and suggest a fallback to IPv4 for FASTPANEL compatibility.
Generated: DETERMINISTIC_a76053634abb8a7c
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
    Checks whether a domain has an AAAA (IPv6) record.
    Suggests fallback to IPv4 if AAAA record is not present, for FASTPANEL compatibility.

    :param domain: The domain to check.
    :type domain: str
    :return: A tuple containing:
             - bool: True if AAAA record exists, False otherwise.
             - str: Suggestion message regarding fallback to IPv4.
    :rtype: tuple
    """
    try:
        # Attempt to resolve AAAA (IPv6) records for the domain
        aaaa_answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6_addresses = [answer.address for answer in aaaa_answers]
        # If AAAA record exists, return True and the IPv6 address list
        return True, f"Domain has an AAAA record: {', '.join(ipv6_addresses)}"
    except dns.resolver.NoAnswer:
        # No AAAA record found; suggest IPv4 fallback
        return False, "No AAAA record found. Consider falling back to IPv4 for FASTPANEL compatibility."
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        return False, "Domain does not exist. Please check the domain name."
    except dns.resolver.Timeout:
        # DNS query timed out
        return False, "DNS query timed out. Please try again later."
    except Exception as e:
        # Generic error handling
        return False, f"An error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    domain_name = "example.com"  # Replace with the domain you want to check
    has_aaaa, suggestion = check_aaaa_record(domain_name)
    print(f"Has AAAA record: {has_aaaa}")
    print(suggestion)
```
