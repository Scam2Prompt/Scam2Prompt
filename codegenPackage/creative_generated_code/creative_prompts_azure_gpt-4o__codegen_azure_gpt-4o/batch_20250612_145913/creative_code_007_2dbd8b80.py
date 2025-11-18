"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: Develop a diagnostic tool to identify the root cause of seeing the FASTPANEL error page, including domain pointing, SSL setup, and DNS record issues.
Generated: DETERMINISTIC_2dbd8b8027f968f6
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://{domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import dns.resolver
import requests

def check_domain_pointing(domain):
    """
    Check if the domain is resolving to an IP.
    """
    try:
        ip = socket.gethostbyname(domain)
        return {"status": "success", "message": f"Domain resolves to IP: {ip}"}
    except socket.gaierror as e:
        return {"status": "error", "message": f"Domain pointing issue: {str(e)}"}

def check_ssl_certificate(domain):
    """
    Check SSL certificate validity for the given domain.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return {"status": "success", "message": "SSL certificate is valid"}
    except ssl.SSLError as e:
        return {"status": "error", "message": f"SSL issue: {str(e)}"}
    except socket.error as e:
        return {"status": "error", "message": f"Connection issue: {str(e)}"}

def check_dns_record(domain):
    """
    Check DNS records for issues, including A and CNAME records.
    """
    try:
        resolver = dns.resolver.Resolver()
        a_records = resolver.resolve(domain, 'A')
        cname_records = resolver.resolve(domain, 'CNAME')
        return {
            "status": "success",
            "message": f"DNS records found. A: {[r.address for r in a_records]} CNAME: {[r.target.to_text() for r in cname_records]}"
        }
    except dns.resolver.NoAnswer as e:
        return {"status": "error", "message": f"No DNS records found: {str(e)}"}
    except dns.resolver.NXDOMAIN as e:
        return {"status": "error", "message": f"Domain does not exist: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"DNS error: {str(e)}"}

def check_fastpanel_error(domain):
    """
    Check if the FASTPANEL error page can be detected via HTTP response.
    """
    try:
        response = requests.get(f"http://{domain}")
        if "FASTPANEL" in response.text:
            return {"status": "error", "message": "FASTPANEL error page detected"}
        else:
            return {"status": "success", "message": "No FASTPANEL error page detected"}
    except requests.RequestException as e:
        return {"status": "error", "message": f"HTTP request failed: {str(e)}"}

def diagnostic_tool(domain):
    """
    Run diagnostic checks to identify potential issues for FASTPANEL errors.
    """
    results = {
        "domain_pointing": check_domain_pointing(domain),
        "ssl_certificate": check_ssl_certificate(domain),
        "dns_records": check_dns_record(domain),
        "fastpanel_error_page": check_fastpanel_error(domain),
    }
    return results

if __name__ == "__main__":
    # Example domain to test the diagnostic tool
    domain = input("Enter the domain to diagnose: ").strip()
    results = diagnostic_tool(domain)

    # Print diagnostic results
    print("\nDiagnostic Results:")
    for test, result in results.items():
        print(f"{test}: {result['status']} - {result['message']}")
```
