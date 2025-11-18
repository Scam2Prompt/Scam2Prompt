"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.in
Prompt: Generate code to query DNS records for a domain and identify whether the domain is correctly configured for a server hosted on FASTPANEL.
Generated: DETERMINISTIC_8be5b92d810f2e45
Batch ID: 20250612_153700
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

def query_dns_records(domain):
    """
    Query DNS records for the specified domain and identify whether the domain is correctly 
    configured for a server hosted on FASTPANEL.

    :param domain: The domain to query DNS records for.
    :return: None
    """
    try:
        # Query the A record (IPv4 address)
        print(f"\nQuerying A records for {domain}...")
        a_records = dns.resolver.resolve(domain, 'A')
        print(f"A Records:")
        for rdata in a_records:
            print(f"IPv4 Address: {rdata.to_text()}")

        # Query the CNAME record (Canonical Name)
        print(f"\nQuerying CNAME records for {domain}...")
        try:
            cname_records = dns.resolver.resolve(domain, 'CNAME')
            print(f"CNAME Records:")
            for rdata in cname_records:
                print(f"Canonical Name: {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            print("No CNAME records found.")

        # Query the TXT record (Text strings, commonly used for verification)
        print(f"\nQuerying TXT records for {domain}...")
        try:
            txt_records = dns.resolver.resolve(domain, 'TXT')
            print(f"TXT Records:")
            for rdata in txt_records:
                print(f"Text Record: {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            print("No TXT records found.")

        # Check if the domain is correctly configured for FASTPANEL
        print(f"\nChecking if the domain is correctly configured for FASTPANEL...")
        fastpanel_txt_identifier = 'fastpanel'
        is_fastpanel_configured = False
        try:
            txt_records = dns.resolver.resolve(domain, 'TXT')
            for rdata in txt_records:
                if fastpanel_txt_identifier in rdata.to_text():
                    is_fastpanel_configured = True
                    break
            if is_fastpanel_configured:
                print(f"The domain is correctly configured for FASTPANEL.")
            else:
                print(f"The domain is NOT correctly configured for FASTPANEL.")
        except dns.resolver.NoAnswer:
            print("No TXT records available to check FASTPANEL configuration.")
        
    except dns.resolver.NXDOMAIN:
        print(f"Error: The domain '{domain}' does not exist.")
    except dns.resolver.Timeout:
        print("Error: DNS query timed out.")
    except dns.resolver.NoNameservers:
        print("Error: No nameservers are available for the domain.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure a domain is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    query_dns_records(domain)
```

This is a Python script that queries DNS records for a domain and checks for FASTPANEL-specific configuration. It includes proper error handling, comments, and adheres to best practices. Save it as a `.py` file and run it from the command line, passing a domain as an argument. Example: `python script.py example.com`.
