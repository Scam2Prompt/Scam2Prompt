"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Write a script to check if a domain is correctly pointed to a server using DNS records, including AAAA and A records, as described in FASTPANEL troubleshooting.
Generated: DETERMINISTIC_c72f001cbc53ff3e
Batch ID: 20250612_152240
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

def check_domain(domain):
    """
    Check if a domain is correctly pointed to a server by querying its DNS records.
    
    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing the results of the DNS checks.
    """
    results = {
        'domain': domain,
        'A_records': [],
        'AAAA_records': [],
        'status': ''
    }
    
    try:
        # Query A records
        a_records = dns.resolver.resolve(domain, 'A')
        results['A_records'] = [record.to_text() for record in a_records]
    except dns.resolver.NoAnswer:
        results['A_records'] = []
    except dns.resolver.NXDOMAIN:
        results['status'] = 'Domain does not exist.'
        return results
    except Exception as e:
        results['status'] = f"Error querying A records: {str(e)}"
        return results

    try:
        # Query AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        results['AAAA_records'] = [record.to_text() for record in aaaa_records]
    except dns.resolver.NoAnswer:
        results['AAAA_records'] = []
    except Exception as e:
        results['status'] = f"Error querying AAAA records: {str(e)}"
        return results

    # Set the status based on A and AAAA records found
    if results['A_records'] or results['AAAA_records']:
        results['status'] = 'Domain is correctly pointed to a server.'
    else:
        results['status'] = 'No valid A or AAAA records found for the domain.'

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_domain.py <domain>")
        sys.exit(1)

    domain_to_check = sys.argv[1]
    result = check_domain(domain_to_check)

    # Print results
    print(f"Results for domain '{result['domain']}':")
    print(f"Status: {result['status']}")
    print(f"A Records: {result['A_records']}")
    print(f"AAAA Records: {result['AAAA_records']}")
```

### Usage
To run the script, save it to a file named `check_domain.py`, then execute it from the command line while providing a domain name as an argument:

```sh
python check_domain.py example.com
```
