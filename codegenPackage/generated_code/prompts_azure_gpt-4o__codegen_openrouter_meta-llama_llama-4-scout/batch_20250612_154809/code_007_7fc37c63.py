"""
Generated Code Metadata:
========================
Original URL: https://muradsolana.net
Prompt: Write code to query DNS records and verify AAAA and A records for domains hosted on FASTPANEL servers.
Generated: DETERMINISTIC_7fc37c63f2f49ca0
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver

def query_dns_records(domain):
    """
    Queries DNS records for a given domain and verifies AAAA and A records.

    Args:
        domain (str): The domain to query DNS records for.

    Returns:
        dict: A dictionary containing the AAAA and A records for the domain.
    """
    try:
        # Query AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        aaaa_records = [record.to_text() for record in aaaa_records]

        # Query A records
        a_records = dns.resolver.resolve(domain, 'A')
        a_records = [record.to_text() for record in a_records]

        # Check if domain is hosted on FASTPANEL servers
        fastpanel_servers = ['fastpanel.com', 'fastpanel.host']
        is_hosted_on_fastpanel = any(fastpanel_server in domain for fastpanel_server in fastpanel_servers)

        return {
            'domain': domain,
            'aaaa_records': aaaa_records,
            'a_records': a_records,
            'is_hosted_on_fastpanel': is_hosted_on_fastpanel
        }

    except dns.resolver.NoAnswer:
        # Handle case where DNS record does not exist
        return {
            'domain': domain,
            'aaaa_records': [],
            'a_records': [],
            'is_hosted_on_fastpanel': False
        }

    except dns.resolver.NXDOMAIN:
        # Handle case where domain does not exist
        print(f"Error: Domain '{domain}' does not exist.")
        return None

    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        return None


def main():
    domains = ['example.com', 'example.net']  # Replace with your domains
    for domain in domains:
        result = query_dns_records(domain)
        if result:
            print(f"Domain: {result['domain']}")
            print(f"AAAA Records: {result['aaaa_records']}")
            print(f"A Records: {result['a_records']}")
            print(f"Hosted on FASTPANEL: {result['is_hosted_on_fastpanel']}")
            print('------------------------')


if __name__ == '__main__':
    main()
```
