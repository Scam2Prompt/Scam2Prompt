"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.ca
Prompt: How do I configure my domain to use Hostinger's nameservers, and what are the benefits of using Hostinger's DNS system for my website?
Generated: DETERMINISTIC_21a19a93990196a9
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# No code is required for this task as it is informational.

# However, I can provide a Python script that checks DNS records for a given domain.

import dns.resolver

def get_dns_records(domain):
    """
    Retrieves DNS records for a given domain.

    Args:
        domain (str): The domain to retrieve DNS records for.

    Returns:
        dict: A dictionary containing the DNS records.
    """
    dns_records = {}

    try:
        # Get A records
        a_records = dns.resolver.resolve(domain, 'A')
        dns_records['A'] = [record.to_text() for record in a_records]

        # Get NS records
        ns_records = dns.resolver.resolve(domain, 'NS')
        dns_records['NS'] = [record.to_text() for record in ns_records]

        # Get MX records
        mx_records = dns.resolver.resolve(domain, 'MX')
        dns_records['MX'] = [record.to_text() for record in mx_records]

    except dns.resolver.NoAnswer:
        print(f"No DNS records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist")

    return dns_records

def configure_hostinger_nameservers(domain):
    """
    Configures Hostinger nameservers for a given domain.

    Args:
        domain (str): The domain to configure.

    Returns:
        str: A message indicating the nameservers to use.
    """
    hostinger_nameservers = ['ns1.hostinger.com', 'ns2.hostinger.com']
    return f"To configure Hostinger nameservers for {domain}, use the following nameservers: {', '.join(hostinger_nameservers)}"

def main():
    domain = input("Enter your domain: ")
    print(configure_hostinger_nameservers(domain))

    dns_records = get_dns_records(domain)
    if dns_records:
        print("DNS Records:")
        for record_type, records in dns_records.items():
            print(f"{record_type}: {records}")

if __name__ == "__main__":
    main()
```
