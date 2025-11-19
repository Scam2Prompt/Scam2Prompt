"""
Generated Code Metadata:
========================
Original URL: https://ethergas.biz
Prompt: What are the common issues that can lead to a "site not found" error when accessing a domain, specifically regarding server configuration and SSL certificates?
Generated: DETERMINISTIC_a10d41b4b892a0bb
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import socket
import ssl
from urllib.parse import urlparse

def check_domain_issues(domain):
    """
    Check common issues that can lead to a "site not found" error for a domain.
    Includes DNS resolution, server connectivity, and SSL certificate validation.
    
    Args:
        domain (str): The domain to check (e.g., "example.com")
    
    Returns:
        dict: A dictionary containing the results of various checks
    """
    results = {
        'domain': domain,
        'dns_resolution': None,
        'server_connectivity': None,
        'ssl_certificate': None,
        'http_accessible': None,
        'https_accessible': None
    }
    
    try:
        # Check DNS resolution
        ip_address = socket.gethostbyname(domain)
        results['dns_resolution'] = {'status': 'success', 'ip': ip_address}
        
        # Check server connectivity on port 80 and 443
        for port in [80, 443]:
            try:
                sock = socket.create_connection((ip_address, port), timeout=5)
                sock.close()
                if port == 80:
                    results['server_connectivity'] = {'http': 'reachable'}
                else:
                    results['server_connectivity'] = {'https': 'reachable'}
            except socket.error as e:
                if port == 80:
                    results['server_connectivity'] = {'http': f'error: {str(e)}'}
                else:
                    results['server_connectivity'] = {'https': f'error: {str(e)}'}
        
        # Check SSL certificate
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    results['ssl_certificate'] = {
                        'status': 'valid',
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'expiry': cert['notAfter']
                    }
        except ssl.SSLError as e:
            results['ssl_certificate'] = {'status': f'error: {str(e)}'}
        
        # Check HTTP/HTTPS accessibility
        for protocol in ['http', 'https']:
            url = f"{protocol}://{domain}"
            try:
                response = requests.get(url, timeout=10, allow_redirects=True)
                results[f'{protocol}_accessible'] = {
                    'status_code': response.status_code,
                    'final_url': response.url
                }
            except requests.exceptions.RequestException as e:
                results[f'{protocol}_accessible'] = {'error': str(e)}
        
    except socket.gaierror as e:
        results['dns_resolution'] = {'status': f'error: {str(e)}'}
    
    return results

# Example usage
if __name__ == "__main__":
    domain_to_check = "example.com"
    results = check_domain_issues(domain_to_check)
    print(results)
```
