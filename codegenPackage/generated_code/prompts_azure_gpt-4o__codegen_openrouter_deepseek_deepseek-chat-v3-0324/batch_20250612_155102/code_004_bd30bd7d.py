"""
Generated Code Metadata:
========================
Original URL: https://ethergas.biz
Prompt: Create a script to query and validate domain settings (e.g., DNS records, SSL certificates) for websites hosted on FASTPANEL, ensuring compatibility with both IPv4 and IPv6.
Generated: DETERMINISTIC_bd30bd7df6447366
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import dns.resolver
import socket
import ssl
import OpenSSL
import argparse
from datetime import datetime
import sys
from typing import List, Dict, Tuple, Optional

def resolve_dns(domain: str, record_type: str) -> List[str]:
    """
    Resolve DNS records for a given domain and record type.
    
    Args:
        domain: Domain name to query
        record_type: Type of DNS record (A, AAAA, MX, etc.)
    
    Returns:
        List of resolved records
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(r) for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return []
    except dns.resolver.NoNameservers:
        raise Exception(f"No nameservers found for {domain}")
    except Exception as e:
        raise Exception(f"DNS resolution failed for {domain}: {str(e)}")

def check_ipv4_ipv6(domain: str) -> Dict[str, List[str]]:
    """
    Check IPv4 and IPv6 resolution for a domain.
    
    Args:
        domain: Domain name to check
    
    Returns:
        Dictionary with 'ipv4' and 'ipv6' keys containing resolved addresses
    """
    result = {'ipv4': [], 'ipv6': []}
    
    # Check IPv4
    try:
        result['ipv4'] = resolve_dns(domain, 'A')
    except Exception as e:
        print(f"IPv4 check failed: {str(e)}", file=sys.stderr)
    
    # Check IPv6
    try:
        result['ipv6'] = resolve_dns(domain, 'AAAA')
    except Exception as e:
        print(f"IPv6 check failed: {str(e)}", file=sys.stderr)
    
    return result

def get_ssl_certificate(domain: str, port: int = 443) -> Dict:
    """
    Retrieve SSL certificate information for a domain.
    
    Args:
        domain: Domain name to check
        port: Port to connect to (default: 443)
    
    Returns:
        Dictionary with certificate details
    """
    result = {
        'valid': False,
        'issuer': None,
        'subject': None,
        'expires': None,
        'days_remaining': None,
        'errors': []
    }
    
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert(binary_form=True)
                x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert)
                
                # Parse certificate details
                result['issuer'] = dict(x509.get_issuer().get_components())
                result['subject'] = dict(x509.get_subject().get_components())
                
                # Check expiration
                expires = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
                result['expires'] = expires.isoformat()
                
                days_remaining = (expires - datetime.now()).days
                result['days_remaining'] = days_remaining
                result['valid'] = days_remaining > 0
                
                if days_remaining <= 0:
                    result['errors'].append("Certificate has expired")
                elif days_remaining <= 30:
                    result['errors'].append(f"Certificate expires in {days_remaining} days")
    
    except ssl.SSLError as e:
        result['errors'].append(f"SSL error: {str(e)}")
    except socket.gaierror:
        result['errors'].append("Could not resolve domain")
    except Exception as e:
        result['errors'].append(f"Unexpected error: {str(e)}")
    
    return result

def check_mx_records(domain: str) -> List[str]:
    """
    Check MX records for a domain.
    
    Args:
        domain: Domain name to check
    
    Returns:
        List of MX records
    """
    try:
        return resolve_dns(domain, 'MX')
    except Exception as e:
        print(f"MX record check failed: {str(e)}", file=sys.stderr)
        return []

def check_nameservers(domain: str) -> List[str]:
    """
    Check nameservers for a domain.
    
    Args:
        domain: Domain name to check
    
    Returns:
        List of nameservers
    """
    try:
        return resolve_dns(domain, 'NS')
    except Exception as e:
        print(f"Nameserver check failed: {str(e)}", file=sys.stderr)
        return []

def validate_domain(domain: str) -> Dict:
    """
    Validate all domain settings.
    
    Args:
        domain: Domain name to validate
    
    Returns:
        Dictionary with validation results
    """
    result = {
        'domain': domain,
        'ipv4': [],
        'ipv6': [],
        'ssl': {},
        'mx': [],
        'nameservers': [],
        'errors': []
    }
    
    # Check DNS resolution
    ip_info = check_ipv4_ipv6(domain)
    result['ipv4'] = ip_info['ipv4']
    result['ipv6'] = ip_info['ipv6']
    
    if not result['ipv4'] and not result['ipv6']:
        result['errors'].append("Domain does not resolve to any IP address")
    
    # Check SSL certificate
    result['ssl'] = get_ssl_certificate(domain)
    if not result['ssl']['valid']:
        result['errors'].extend(result['ssl']['errors'])
    
    # Check MX records
    result['mx'] = check_mx_records(domain)
    
    # Check nameservers
    result['nameservers'] = check_nameservers(domain)
    
    return result

def format_results(results: Dict) -> str:
    """
    Format validation results for display.
    
    Args:
        results: Validation results dictionary
    
    Returns:
        Formatted string with results
    """
    output = []
    output.append(f"=== Domain Validation Report for {results['domain']} ===")
    
    # IP Addresses
    output.append("\nIP Addresses:")
    output.append(f"IPv4: {', '.join(results['ipv4']) if results['ipv4'] else 'None'}")
    output.append(f"IPv6: {', '.join(results['ipv6']) if results['ipv6'] else 'None'}")
    
    # SSL Certificate
    output.append("\nSSL Certificate:")
    if results['ssl']['valid']:
        output.append(f"Valid until: {results['ssl']['expires']} ({results['ssl']['days_remaining']} days remaining)")
        output.append(f"Issuer: {results['ssl']['issuer']}")
    else:
        output.append("Invalid or missing certificate")
        for error in results['ssl']['errors']:
            output.append(f"  - {error}")
    
    # MX Records
    output.append("\nMX Records:")
    if results['mx']:
        for mx in results['mx']:
            output.append(f"  - {mx}")
    else:
        output.append("No MX records found")
    
    # Nameservers
    output.append("\nNameservers:")
    if results['nameservers']:
        for ns in results['nameservers']:
            output.append(f"  - {ns}")
    else:
        output.append("No nameservers found")
    
    # Errors
    if results['errors']:
        output.append("\nValidation Errors:")
        for error in results['errors']:
            output.append(f"  - {error}")
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description='Validate domain settings for websites hosted on FASTPANEL')
    parser.add_argument('domains', nargs='+', help='Domain names to validate')
    parser.add_argument('--output', '-o', help='Output file to save results')
    
    args = parser.parse_args()
    
    all_results = []
    for domain in args.domains:
        try:
            results = validate_domain(domain)
            all_results.append(results)
            print(format_results(results))
            print("\n" + "="*50 + "\n")
        except Exception as e:
            print(f"Error validating {domain}: {str(e)}", file=sys.stderr)
    
    if args.output:
        try:
            with open(args.output, 'w') as f:
                for result in all_results:
                    f.write(format_results(result))
                    f.write("\n" + "="*50 + "\n")
        except IOError as e:
            print(f"Error writing to output file: {str(e)}", file=sys.stderr)

if __name__ == '__main__':
    main()
```
