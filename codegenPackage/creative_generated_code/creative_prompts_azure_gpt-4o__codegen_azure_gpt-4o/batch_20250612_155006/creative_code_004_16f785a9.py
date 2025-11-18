"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.network
Prompt: Write a script to query DNS records for a domain and identify potential misconfigurations, including missing A or AAAA records.
Generated: DETERMINISTIC_16f785a9877c565d
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver

def query_dns_records(domain):
    """
    Queries DNS records for a domain and identifies potential misconfigurations.

    Args:
        domain (str): The domain name to query.

    Returns:
        dict: A dictionary containing the status of A and AAAA records and any misconfigurations.
    """
    results = {
        "domain": domain,
        "A_records": [],
        "AAAA_records": [],
        "misconfigurations": []
    }

    try:
        # Query A records
        a_records = dns.resolver.resolve(domain, 'A')
        results["A_records"] = [r.address for r in a_records]
    except dns.resolver.NoAnswer:
        results["misconfigurations"].append("Missing A records.")
    except dns.resolver.NXDOMAIN:
        results["misconfigurations"].append("Domain does not exist.")
        return results
    except Exception as e:
        results["misconfigurations"].append(f"Error querying A records: {str(e)}")

    try:
        # Query AAAA records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        results["AAAA_records"] = [r.address for r in aaaa_records]
    except dns.resolver.NoAnswer:
        results["misconfigurations"].append("Missing AAAA records.")
    except dns.resolver.NXDOMAIN:
        results["misconfigurations"].append("Domain does not exist.")
        return results
    except Exception as e:
        results["misconfigurations"].append(f"Error querying AAAA records: {str(e)}")

    return results


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: python query_dns.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    result = query_dns_records(domain)

    # Output results
    print(f"Results for domain: {result['domain']}")
    print(f"A records: {result['A_records']}")
    print(f"AAAA records: {result['AAAA_records']}")
    if result["misconfigurations"]:
        print(f"Potential misconfigurations: {', '.join(result['misconfigurations'])}")
    else:
        print("No misconfigurations detected.")
```
