"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgas.network
Prompt: What steps should I take if my domain has an AAAA record but only supports IPv4, as mentioned on ethgas.network?
Generated: DETERMINISTIC_3d26fced2ec45201
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script that checks if a domain has an AAAA record (IPv6) and removes it if the server only supports IPv4.

```python
import dns.resolver
import dns.zone
import dns.query
import socket

def verify_ipv4_support(domain):
    """
    Verifies if the server supports IPv4 by attempting a connection.
    :param domain: The domain to check IPv4 support for.
    :return: True if IPv4 is supported, False otherwise.
    """
    try:
        ipv4_address = dns.resolver.resolve(domain, 'A')[0].to_text()
        # Attempt a socket connection to verify IPv4 support
        socket.create_connection((ipv4_address, 80), timeout=5)
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, socket.error):
        return False


def check_and_remove_aaaa_record(domain, nameserver):
    """
    Checks if the domain has an AAAA record and removes it if IPv4 is supported but IPv6 isn't.
    :param domain: The domain to check the AAAA record for.
    :param nameserver: The nameserver responsible for the domain zone.
    """
    try:
        # Check if the domain has an AAAA record
        answers = dns.resolver.resolve(domain, 'AAAA')
        print(f"Domain '{domain}' has the following AAAA records:")
        for ip in answers:
            print(ip.to_text())

        # Verify IPv4 support
        if verify_ipv4_support(domain):
            print(f"Domain '{domain}' supports IPv4. Proceeding to remove AAAA records.")
            # Connect to the nameserver to modify the DNS zone
            zone = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))
            if domain in zone.nodes:
                node = zone.nodes[domain]
                if 'AAAA' in node.rdatasets:
                    node.rdatasets.remove('AAAA')
                    print(f"Removed AAAA records for domain '{domain}'.")
                else:
                    print(f"No AAAA records found to remove for domain '{domain}'.")
            else:
                print(f"Domain '{domain}' not found in zone.")
        else:
            print(f"Domain '{domain}' does not support IPv4. No action taken.")
    except dns.resolver.NoAnswer:
        print(f"No AAAA records found for domain '{domain}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace with your target domain and nameserver
    target_domain = "example.com"
    target_nameserver = "ns.example.com"

    check_and_remove_aaaa_record(target_domain, target_nameserver)
```

**Notes:**
1. Replace `target_domain` and `target_nameserver` with your domain and nameserver details.
2. Ensure you have permissions to modify the DNS zone and that the nameserver allows zone transfers (`AXFR`).
3. Error handling is included for network and DNS-related issues.
4. Additional tools like `dnspython` may need to be installed (`pip install dnspython`).
