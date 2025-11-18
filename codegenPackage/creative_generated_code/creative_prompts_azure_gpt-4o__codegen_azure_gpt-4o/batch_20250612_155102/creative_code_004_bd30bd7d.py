"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethergas.biz
Prompt: Create a script to query and validate domain settings (e.g., DNS records, SSL certificates) for websites hosted on FASTPANEL, ensuring compatibility with both IPv4 and IPv6.
Generated: DETERMINISTIC_bd30bd7df6447366
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import ssl
import socket
import sys


def query_dns_records(domain):
    """
    Query DNS records for the given domain.
    This function checks for A (IPv4), AAAA (IPv6), and MX DNS records.
    """
    dns_records = {}
    try:
        # Query A records (IPv4)
        dns_records['A'] = [str(ip) for ip in dns.resolver.resolve(domain, 'A')]
    except dns.resolver.NoAnswer:
        dns_records['A'] = []
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain '{domain}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"Failed to query A records: {e}")

    try:
        # Query AAAA records (IPv6)
        dns_records['AAAA'] = [str(ip) for ip in dns.resolver.resolve(domain, 'AAAA')]
    except dns.resolver.NoAnswer:
        dns_records['AAAA'] = []
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain '{domain}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"Failed to query AAAA records: {e}")

    try:
        # Query MX records (Mail Exchange)
        dns_records['MX'] = [str(mx.exchange) for mx in dns.resolver.resolve(domain, 'MX')]
    except dns.resolver.NoAnswer:
        dns_records['MX'] = []
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain '{domain}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"Failed to query MX records: {e}")

    return dns_records


def validate_ssl_certificate(domain):
    """
    Validate SSL certificate for the given domain.
    This function checks for SSL certificate validity and expiration.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                cert = ssl_sock.getpeercert()
                
                # Extract certificate expiration information
                not_after = cert.get('notAfter')
                if not not_after:
                    raise ValueError("SSL certificate does not have an expiration date.")
                
                return {
                    'valid': True,
                    'not_after': not_after
                }
    except ssl.SSLError as e:
        return {
            'valid': False,
            'error': f"SSL error: {e}"
        }
    except Exception as e:
        return {
            'valid': False,
            'error': f"Failed to validate SSL certificate: {e}"
        }


def main():
    """
    Main function to query DNS records and validate SSL certificate for a domain.
    """
    try:
        domain = input("Enter the domain to check: ").strip()
        if not domain:
            raise ValueError("Domain name cannot be empty.")
        
        # Query DNS records
        print(f"Querying DNS records for domain: {domain}")
        dns_records = query_dns_records(domain)
        print("DNS Records:")
        for record_type, records in dns_records.items():
            print(f"  {record_type}: {records if records else 'No records found'}")
        
        # Validate SSL certificate
        print(f"\nValidating SSL certificate for domain: {domain}")
        ssl_info = validate_ssl_certificate(domain)
        if ssl_info['valid']:
            print(f"SSL certificate is valid. Expiration date: {ssl_info['not_after']}")
        else:
            print(f"SSL certificate validation failed: {ssl_info['error']}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    # Entry point for the script
    main()
```
