"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hosico-cat.fun
Prompt: Generate a script to identify and resolve mismatched AAAA records for a domain that only supports IPv4, referencing FASTPANEL's guidelines.
Generated: DETERMINISTIC_3c125d92f99bc4b7
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to identify and resolve mismatched AAAA (IPv6) DNS records for a domain
that only supports IPv4, following FASTPANEL's guidelines.

Usage:
- Ensure the `dns.resolver` module is installed: `pip install dnspython`.
- Run the script and provide the domain name as input.
"""

import dns.resolver
import dns.exception
import dns.update
import dns.query

def get_aaaa_records(domain):
    """
    Fetch the AAAA records for the given domain.

    :param domain: The domain name to query AAAA records for.
    :return: A list of AAAA records or an empty list if none exist.
    """
    try:
        resolver = dns.resolver.Resolver()
        # Query AAAA records for the domain
        answers = resolver.resolve(domain, 'AAAA')
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        # No AAAA records found
        return []
    except dns.resolver.NXDOMAIN:
        print(f"Error: Domain '{domain}' does not exist.")
        return []
    except dns.exception.DNSException as e:
        print(f"DNS query error: {e}")
        return []

def delete_aaaa_records(domain, nameserver, key_name, key):
    """
    Delete AAAA records for the given domain.

    :param domain: The domain name for which AAAA records should be removed.
    :param nameserver: The authoritative nameserver for DNS changes.
    :param key_name: TSIG key name for authentication.
    :param key: TSIG key for authentication.
    :return: True if the update succeeds, False otherwise.
    """
    try:
        # Create an update message
        update = dns.update.Update(domain, keyring=dns.tsigkeyring.from_text({key_name: key}))
        # Remove all AAAA records
        update.delete(domain, 'AAAA')
        # Send the update to the nameserver
        response = dns.query.tcp(update, nameserver)
        if response.rcode() == dns.rcode.NOERROR:
            print(f"AAAA records successfully deleted for domain '{domain}'.")
            return True
        else:
            print(f"Failed to delete AAAA records for domain '{domain}'. DNS response code: {response.rcode()}")
            return False
    except dns.exception.DNSException as e:
        print(f"Error during DNS update: {e}")
        return False

if __name__ == "__main__":
    import sys

    # Input domain name
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    # Fetch AAAA records
    print(f"Checking AAAA records for domain: {domain}")
    aaaa_records = get_aaaa_records(domain)

    if not aaaa_records:
        print("No AAAA records found. No action needed.")
    else:
        print(f"Found AAAA records: {aaaa_records}")
        print("Removing AAAA records...")

        # Configuration for DNS update (replace with your values)
        NAMESERVER = "127.0.0.1"  # Replace with the authoritative nameserver IP
        TSIG_KEY_NAME = "your-key-name"  # Replace with your TSIG key name
        TSIG_KEY = "your-tsig-key"  # Replace with your TSIG key

        # Attempt to delete AAAA records
        delete_aaaa_records(domain, NAMESERVER, TSIG_KEY_NAME, TSIG_KEY)
```
