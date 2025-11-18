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
import dns.resolver
import sys

def check_dns_records(domain, expected_ip):
    """
    Check if the DNS A and AAAA records of a domain point to the expected IP address.

    Args:
        domain (str): The domain to check.
        expected_ip (str): The IP address to compare against.

    Returns:
        dict: Results indicating whether A and AAAA records match the expected IP.
    """
    results = {"A_record_match": False, "AAAA_record_match": False}
    
    try:
        # Check A (IPv4) records
        a_records = dns.resolver.resolve(domain, 'A')
        for record in a_records:
            if record.to_text() == expected_ip:
                results["A_record_match"] = True
        
    except dns.resolver.NoAnswer:
        print(f"No A record found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
    except Exception as e:
        print(f"Error checking A records: {e}")

    try:
        # Check AAAA (IPv6) records
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        for record in aaaa_records:
            if record.to_text() == expected_ip:
                results["AAAA_record_match"] = True
        
    except dns.resolver.NoAnswer:
        print(f"No AAAA record found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
    except Exception as e:
        print(f"Error checking AAAA records: {e}")

    return results

def main():
    """
    Main function to execute the DNS record checking script.
    """
    if len(sys.argv) != 3:
        print("Usage: python check_dns_records.py <domain> <expected_ip>")
        sys.exit(1)

    domain = sys.argv[1]
    expected_ip = sys.argv[2]

    print(f"Checking DNS records for domain: {domain}")
    print(f"Expected IP: {expected_ip}")
    
    results = check_dns_records(domain, expected_ip)

    if results["A_record_match"] or results["AAAA_record_match"]:
        print("Domain is correctly pointed to the server.")
        if results["A_record_match"]:
            print("- A record matches.")
        if results["AAAA_record_match"]:
            print("- AAAA record matches.")
    else:
        print("Domain is NOT correctly pointed to the server.")

if __name__ == "__main__":
    main()
```
