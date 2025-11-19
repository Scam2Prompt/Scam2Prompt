"""
Generated Code Metadata:
========================
Original URL: https://muradsolana.net
Prompt: What are the common issues that can cause a webpage to display a "Why am I seeing this page?" message, specifically related to domain pointing and server configuration?
Generated: DETERMINISTIC_5595842e472a9629
Batch ID: 20250612_161134
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

# Generated Code:
# ===============

```python
"""
Script to diagnose common issues that can cause a webpage to display a 
"Why am I seeing this page?" message, specifically related to domain pointing 
and server configuration.

This script checks:
1. Domain DNS records
2. Web server configuration
3. Connectivity to the server
4. SSL certificate validity
"""

import socket
import requests
import dns.resolver
import ssl
from requests.exceptions import RequestException

def check_dns_records(domain):
    """
    Check if the domain has valid DNS records (A, CNAME).
    """
    try:
        print(f"Checking DNS records for {domain}...")
        answers = dns.resolver.resolve(domain, 'A')  # Query A records
        for answer in answers:
            print(f"Found A record: {answer}")
        return True
    except dns.resolver.NXDOMAIN:
        print("Error: Domain does not exist.")
    except dns.resolver.NoAnswer:
        print("Error: No DNS records found for the domain.")
    except dns.resolver.Timeout:
        print("Error: DNS query timed out.")
    except Exception as e:
        print(f"Unexpected error while checking DNS records: {e}")
    return False

def check_server_connectivity(domain):
    """
    Check if the server is reachable via HTTP/HTTPS.
    """
    try:
        print(f"Checking server connectivity for {domain}...")
        response = requests.get(f"http://{domain}", timeout=5)
        print(f"HTTP Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Server is reachable via HTTP.")
            return True
        else:
            print("Server returned a non-200 status code.")
    except RequestException as e:
        print(f"Error: Unable to connect to the server via HTTP. Details: {e}")
    return False

def check_ssl_certificate(domain):
    """
    Check if the SSL certificate is valid for the domain.
    """
    try:
        print(f"Checking SSL certificate for {domain}...")
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                print("SSL certificate is valid.")
                return True
    except ssl.SSLError as e:
        print(f"Error: SSL certificate issue. Details: {e}")
    except socket.error as e:
        print(f"Error: Unable to connect to the server via HTTPS. Details: {e}")
    return False

def diagnose_domain_issue(domain):
    """
    Run all checks to diagnose potential issues with the domain.
    """
    print(f"Starting diagnosis for {domain}...\n")
    dns_ok = check_dns_records(domain)
    server_ok = check_server_connectivity(domain)
    ssl_ok = check_ssl_certificate(domain)

    print("\nDiagnosis complete.")
    if dns_ok and server_ok and ssl_ok:
        print("No issues detected. The domain and server configuration appear to be correct.")
    else:
        print("Potential issues detected:")
        if not dns_ok:
            print("- DNS records are missing or incorrect.")
        if not server_ok:
            print("- Server is not reachable via HTTP.")
        if not ssl_ok:
            print("- SSL certificate is invalid or missing.")

if __name__ == "__main__":
    # Replace 'example.com' with the domain you want to diagnose
    domain_to_check = "example.com"
    diagnose_domain_issue(domain_to_check)
```
