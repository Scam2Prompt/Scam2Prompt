"""
Generated Code Metadata:
========================
Original URL: https://msu.best
Prompt: Create a Python script to detect and resolve issues with AAAA records for domains that only support IPv4 on FASTPANEL servers.
Generated: DETERMINISTIC_b6d2283a25d2a3e0
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import dns.reversename

def check_aaaa_record(domain):
    """
    Check if a domain has an AAAA record.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if the domain has an AAAA record, False otherwise.
    """
    try:
        dns.resolver.resolve(domain, 'AAAA')
        return True
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_ipv4_records(domain):
    """
    Get the IPv4 records for a domain.

    Args:
        domain (str): The domain to get IPv4 records for.

    Returns:
        list: A list of IPv4 addresses for the domain.
    """
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def create_ptr_record(ip, domain):
    """
    Create a PTR record for a given IP and domain.

    Args:
        ip (str): The IP address.
        domain (str): The domain.

    Returns:
        bool: True if the PTR record was created successfully, False otherwise.
    """
    try:
        # Implement FASTPANEL API to create PTR record
        # For demonstration purposes, this is left blank
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def resolve_aaaa_issue(domain):
    """
    Resolve AAAA record issues for a domain on FASTPANEL servers.

    Args:
        domain (str): The domain to resolve AAAA record issues for.
    """
    if check_aaaa_record(domain):
        print(f"Domain {domain} has an AAAA record. No action needed.")
        return

    ipv4_records = get_ipv4_records(domain)
    if not ipv4_records:
        print(f"Domain {domain} has no IPv4 records.")
        return

    for ip in ipv4_records:
        reversed_ip = dns.reversename.from_address(ip)
        ptr_record = dns.resolver.resolve(reversed_ip, 'PTR')
        if ptr_record:
            print(f"PTR record already exists for {ip}.")
            continue

        if create_ptr_record(ip, domain):
            print(f"PTR record created for {ip}.")

def main():
    domains = ['example.com', 'example.net']  # List of domains to check
    for domain in domains:
        resolve_aaaa_issue(domain)

if __name__ == '__main__':
    main()
```
