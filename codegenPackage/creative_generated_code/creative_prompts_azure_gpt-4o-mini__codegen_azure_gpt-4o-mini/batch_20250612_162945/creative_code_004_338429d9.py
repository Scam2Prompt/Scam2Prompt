"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: How can I verify if my domain is correctly pointed to my server using DNS records?
Generated: DETERMINISTIC_338429d9cf16137a
Batch ID: 20250612_162945
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
import sys

def check_dns_record(domain, record_type):
    """Check if the specified DNS record for the given domain exists and matches the server's IP."""
    try:
        # Resolve the DNS record
        answers = dns.resolver.resolve(domain, record_type)
        return answers
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No DNS record found for {domain} of type {record_type}.")
        return None
    except Exception as e:
        print(f"An error occurred while resolving DNS records: {e}")
        return None

def verify_domain(domain, expected_ip):
    """Verify if the domain is pointing to the expected server IP."""
    # Check A record
    a_records = check_dns_record(domain, 'A')
    if a_records:
        for record in a_records:
            if record.to_text() == expected_ip:
                print(f"Domain {domain} is correctly pointing to {expected_ip}.")
                return True
            else:
                print(f"Domain {domain} is pointing to {record.to_text()}, expected {expected_ip}.")
                return False
    
    # Check AAAA record for IPv6
    aaaa_records = check_dns_record(domain, 'AAAA')
    if aaaa_records:
        for record in aaaa_records:
            if record.to_text() == expected_ip:
                print(f"Domain {domain} is correctly pointing to {expected_ip} (IPv6).")
                return True
            else:
                print(f"Domain {domain} is pointing to {record.to_text()} (IPv6), expected {expected_ip}.")
                return False
    
    print(f"Domain {domain} has no valid A or AAAA records.")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_dns.py <domain> <expected_ip>")
        sys.exit(1)

    domain_input = sys.argv[1]
    expected_ip_input = sys.argv[2]

    # Verify the domain
    verify_domain(domain_input, expected_ip_input)
```

Make sure to install the required library using:
```bash
pip install dnspython
```

To run the script, use the following command:
```bash
python check_dns.py <domain> <expected_ip>
```
