"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tech-connect.cloud
Prompt: Create a script to check if a domain is active and using Hostinger nameservers, leveraging DNS query libraries in Python.
Generated: DETERMINISTIC_a38aa1c417c262b1
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import socket


def is_domain_active(domain: str) -> bool:
    """
    Checks if a given domain is active by attempting to resolve its A record.

    :param domain: The domain name to check
    :return: True if the domain resolves, False otherwise
    """
    try:
        # Attempt to resolve the domain's A record
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
        # Domain does not resolve or the query times out
        return False


def is_using_hostinger_nameservers(domain: str) -> bool:
    """
    Checks if a given domain is using Hostinger's nameservers.

    :param domain: The domain name to check
    :return: True if the domain is using Hostinger's nameservers, False otherwise
    """
    try:
        # Resolve the domain's NS (nameserver) records
        ns_records = dns.resolver.resolve(domain, 'NS')

        # Hostinger's known nameservers (this list can be updated as needed)
        hostinger_ns = {
            "ns1.dns-parking.com",
            "ns2.dns-parking.com",
        }

        # Check if any of the domain's nameservers match Hostinger's
        for ns in ns_records:
            if str(ns.target).strip(".").lower() in hostinger_ns:
                return True

        return False
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
        # Domain does not resolve or the query times out
        return False


def main():
    """
    Main function to check if a domain is active and using Hostinger's nameservers.
    Prompts the user for a domain name and outputs the result.
    """
    print("Domain Status Checker")
    print("======================")

    # Get the domain name from the user
    domain = input("Enter the domain to check (e.g., example.com): ").strip()

    # Check if the domain is active
    print("\nChecking domain status...")
    if not is_domain_active(domain):
        print(f"The domain '{domain}' is not active or cannot be resolved.")
        return

    print(f"The domain '{domain}' is active.")

    # Check if the domain is using Hostinger's nameservers
    print("\nChecking nameservers...")
    if is_using_hostinger_nameservers(domain):
        print(f"The domain '{domain}' is using Hostinger's nameservers.")
    else:
        print(f"The domain '{domain}' is NOT using Hostinger's nameservers.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user. Exiting...")
    except socket.gaierror:
        print("Network error: Unable to resolve domain. Please check your connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
