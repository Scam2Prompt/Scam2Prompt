"""
Generated Code Metadata:
========================
Original URL: https://app.rpcapirestore.site
Prompt: Write a script to check if a domain is correctly pointed to a server and troubleshoot issues like missing SSL certificates or IPv4/IPv6 compatibility, as described on FASTPANEL troubleshooting pages.
Generated: DETERMINISTIC_d6e6149b776a30b8
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import socket
import ssl
import dns.resolver
import requests
import ipaddress
from urllib.parse import urlparse
from datetime import datetime

def check_dns(domain, expected_ip=None):
    """
    Check DNS records for the domain and verify if they point to the expected IP.
    Returns a dictionary with results for A, AAAA, and CNAME records.
    """
    results = {'A': [], 'AAAA': [], 'CNAME': None, 'errors': []}
    
    try:
        # Check A records (IPv4)
        try:
            answers = dns.resolver.resolve(domain, 'A')
            results['A'] = [str(r) for r in answers]
            if expected_ip and expected_ip not in results['A']:
                results['errors'].append(f"DNS A record does not point to expected IP {expected_ip}")
        except dns.resolver.NoAnswer:
            results['errors'].append("No A record found for domain")
        except dns.resolver.NXDOMAIN:
            results['errors'].append(f"Domain {domain} does not exist")
        except Exception as e:
            results['errors'].append(f"Error resolving A record: {str(e)}")

        # Check AAAA records (IPv6)
        try:
            answers = dns.resolver.resolve(domain, 'AAAA')
            results['AAAA'] = [str(r) for r in answers]
        except dns.resolver.NoAnswer:
            pass  # IPv6 is optional
        except Exception as e:
            results['errors'].append(f"Error resolving AAAA record: {str(e)}")

        # Check CNAME record
        try:
            answers = dns.resolver.resolve(domain, 'CNAME')
            results['CNAME'] = str(answers[0].target)
        except dns.resolver.NoAnswer:
            pass  # CNAME is optional
        except Exception as e:
            results['errors'].append(f"Error resolving CNAME record: {str(e)}")

    except Exception as e:
        results['errors'].append(f"DNS resolution failed: {str(e)}")

    return results

def check_ssl(domain):
    """
    Check SSL certificate for the domain.
    Returns a dictionary with certificate details and any errors.
    """
    results = {
        'valid': False,
        'expires': None,
        'issuer': None,
        'errors': []
    }

    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                
                # Check expiration
                expires = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                results['expires'] = expires.isoformat()
                if expires < datetime.now():
                    results['errors'].append("SSL certificate has expired")
                
                # Get issuer
                issuer = dict(x[0] for x in cert['issuer'])
                results['issuer'] = issuer.get('organizationName', 'Unknown')
                
                results['valid'] = True

    except ssl.SSLError as e:
        results['errors'].append(f"SSL error: {str(e)}")
    except socket.timeout:
        results['errors'].append("SSL check timed out")
    except Exception as e:
        results['errors'].append(f"Error checking SSL: {str(e)}")

    return results

def check_http(domain, expected_ip=None):
    """
    Check HTTP/HTTPS connectivity to the domain.
    Returns a dictionary with response details and any errors.
    """
    results = {
        'http_status': None,
        'https_status': None,
        'ip_mismatch': False,
        'errors': []
    }

    protocols = ['http', 'https']
    for proto in protocols:
        try:
            url = f"{proto}://{domain}"
            response = requests.get(url, timeout=10, allow_redirects=True)
            
            if proto == 'http':
                results['http_status'] = response.status_code
            else:
                results['https_status'] = response.status_code

            # Check if IP matches expected
            if expected_ip:
                resolved_ip = socket.gethostbyname(urlparse(url).hostname)
                if resolved_ip != expected_ip:
                    results['ip_mismatch'] = True
                    results['errors'].append(f"IP mismatch: {resolved_ip} != {expected_ip}")

        except requests.exceptions.SSLError as e:
            results['errors'].append(f"{proto.upper()} SSL error: {str(e)}")
        except requests.exceptions.ConnectionError as e:
            results['errors'].append(f"Could not connect to {proto.upper()}: {str(e)}")
        except requests.exceptions.Timeout:
            results['errors'].append(f"{proto.upper()} request timed out")
        except Exception as e:
            results['errors'].append(f"Error checking {proto.upper()}: {str(e)}")

    return results

def check_ip_compatibility(domain):
    """
    Check IPv4 and IPv6 connectivity to the domain.
    Returns a dictionary with results for each protocol.
    """
    results = {
        'ipv4': False,
        'ipv6': False,
        'errors': []
    }

    try:
        # Check IPv4
        try:
            socket.create_connection((domain, 80), timeout=5)
            results['ipv4'] = True
        except socket.timeout:
            results['errors'].append("IPv4 connection timed out")
        except Exception as e:
            results['errors'].append(f"IPv4 connection failed: {str(e)}")

        # Check IPv6
        try:
            socket.create_connection((domain, 80), timeout=5)
            results['ipv6'] = True
        except socket.timeout:
            pass  # IPv6 is optional
        except Exception as e:
            results['errors'].append(f"IPv6 connection failed: {str(e)}")

    except Exception as e:
        results['errors'].append(f"IP compatibility check failed: {str(e)}")

    return results

def troubleshoot_domain(domain, expected_ip=None):
    """
    Perform comprehensive troubleshooting for a domain.
    Returns a dictionary with all check results.
    """
    results = {
        'domain': domain,
        'expected_ip': expected_ip,
        'dns': None,
        'ssl': None,
        'http': None,
        'ip_compatibility': None,
        'summary': {
            'healthy': True,
            'errors': []
        }
    }

    # Run all checks
    results['dns'] = check_dns(domain, expected_ip)
    results['ssl'] = check_ssl(domain)
    results['http'] = check_http(domain, expected_ip)
    results['ip_compatibility'] = check_ip_compatibility(domain)

    # Aggregate errors
    for check in ['dns', 'ssl', 'http', 'ip_compatibility']:
        if results[check].get('errors'):
            results['summary']['healthy'] = False
            results['summary']['errors'].extend(results[check]['errors'])

    return results

def main():
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Domain troubleshooting tool')
    parser.add_argument('domain', help='Domain name to check')
    parser.add_argument('--expected-ip', help='Expected IP address the domain should resolve to')
    args = parser.parse_args()

    results = troubleshoot_domain(args.domain, args.expected_ip)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()
```
