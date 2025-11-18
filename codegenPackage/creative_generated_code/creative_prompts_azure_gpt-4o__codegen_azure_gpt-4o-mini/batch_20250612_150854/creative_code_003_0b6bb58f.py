"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediaterevolution-360.co
Prompt: Provide code to verify if a domain's DNS records are correctly configured using the `dnspython` library.
Generated: DETERMINISTIC_0b6bb58f7bdd6681
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import dns.exception

def verify_dns_records(domain):
    """
    Verify if a domain's DNS records are correctly configured.

    Parameters:
    domain (str): The domain name to verify.

    Returns:
    dict: A dictionary containing the results of DNS record checks.
    """
    results = {
        "A": None,
        "AAAA": None,
        "MX": None,
        "NS": None,
        "CNAME": None,
        "TXT": None,
        "errors": []
    }
    
    try:
        # Check A records
        results["A"] = [str(record) for record in dns.resolver.resolve(domain, 'A')]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results["errors"].append(f"No A record found for {domain}")
    except Exception as e:
        results["errors"].append(f"Error retrieving A records: {e}")

    try:
        # Check AAAA records
        results["AAAA"] = [str(record) for record in dns.resolver.resolve(domain, 'AAAA')]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results["errors"].append(f"No AAAA record found for {domain}")
    except Exception as e:
        results["errors"].append(f"Error retrieving AAAA records: {e}")

    try:
        # Check MX records
        results["MX"] = [str(record) for record in dns.resolver.resolve(domain, 'MX')]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results["errors"].append(f"No MX record found for {domain}")
    except Exception as e:
        results["errors"].append(f"Error retrieving MX records: {e}")

    try:
        # Check NS records
        results["NS"] = [str(record) for record in dns.resolver.resolve(domain, 'NS')]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results["errors"].append(f"No NS record found for {domain}")
    except Exception as e:
        results["errors"].append(f"Error retrieving NS records: {e}")

    try:
        # Check CNAME records
        results["CNAME"] = [str(record) for record in dns.resolver.resolve(domain, 'CNAME')]
    except dns.resolver.NoAnswer:
        results["CNAME"] = None  # No CNAME record is not an error
    except Exception as e:
        results["errors"].append(f"Error retrieving CNAME records: {e}")

    try:
        # Check TXT records
        results["TXT"] = [str(record) for record in dns.resolver.resolve(domain, 'TXT')]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        results["errors"].append(f"No TXT record found for {domain}")
    except Exception as e:
        results["errors"].append(f"Error retrieving TXT records: {e}")

    return results

if __name__ == "__main__":
    # Example domain to verify
    domain = "example.com"
    dns_results = verify_dns_records(domain)
    
    print(f"DNS records for {domain}:")
    for record_type, record_values in dns_results.items():
        if record_type != "errors":
            print(f"{record_type}: {record_values}")
    
    if dns_results["errors"]:
        print("Errors:")
        for error in dns_results["errors"]:
            print(f" - {error}")
```
