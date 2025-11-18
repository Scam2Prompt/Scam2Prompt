"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stormtoken.site
Prompt: Create a script to validate domain DNS settings and check for SSL certificate installation errors.
Generated: DETERMINISTIC_6758b2d72a0a6da1
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import dns.resolver

def validate_dns_settings(domain):
    """
    Validate DNS settings for the given domain.
    Checks for A and CNAME records.
    """
    try:
        print(f"Checking DNS settings for: {domain}")
        
        # Resolve A records
        a_records = dns.resolver.resolve(domain, 'A')
        print(f"A records for {domain}: {[record.to_text() for record in a_records]}")
        
        # Resolve CNAME records
        try:
            cname_records = dns.resolver.resolve(domain, 'CNAME')
            print(f"CNAME records for {domain}: {[record.to_text() for record in cname_records]}")
        except dns.resolver.NoAnswer:
            print(f"No CNAME records found for {domain}.")

    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
    except dns.resolver.Timeout:
        print(f"DNS query for {domain} timed out.")
    except dns.exception.DNSException as e:
        print(f"An error occurred while resolving DNS for {domain}: {e}")


def check_ssl_certificate(domain, port=443):
    """
    Check SSL certificate installation and validity.
    Connects to the server and retrieves SSL certificate details.
    """
    try:
        print(f"\nChecking SSL certificate for: {domain}:{port}")
        
        # Establish SSL connection
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                certificate = ssock.getpeercert()

        if certificate:
            print(f"SSL certificate found for {domain}.")
            print(f"Certificate subject: {certificate['subject']}")
            print(f"Certificate issuer: {certificate['issuer']}")
        else:
            print(f"No SSL certificate found for {domain}.")
    
    except ssl.SSLError as e:
        print(f"SSL error for {domain}: {e}")
    except socket.error as e:
        print(f"Socket error while connecting to {domain}:{port}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while checking SSL for {domain}: {e}")


# Entry point of the script
if __name__ == "__main__":
    domain = input("Enter domain to validate: ").strip()
    
    # Validate DNS settings
    validate_dns_settings(domain)
    
    # Check SSL certificate
    check_ssl_certificate(domain)
```
