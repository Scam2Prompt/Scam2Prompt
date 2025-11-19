"""
Generated Code Metadata:
========================
Original URL: https://claim-puffer.com
Prompt: Write a script to list all domains on a FASTPANEL server and check their SSL certificate status.
Generated: DETERMINISTIC_a2c94b6ee573b7fe
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import os
import subprocess
import ssl
import socket
import datetime
from OpenSSL import crypto
from typing import List, Dict, Optional, Tuple

def get_fastpanel_domains() -> List[str]:
    """
    Retrieve all domains configured in FASTPANEL.
    """
    try:
        # Assuming FASTPANEL stores domains in /etc/nginx/conf.d/
        domains = []
        conf_dir = "/etc/nginx/conf.d/"
        if not os.path.exists(conf_dir):
            raise FileNotFoundError(f"Directory {conf_dir} not found")
        
        for filename in os.listdir(conf_dir):
            if filename.endswith(".conf"):
                with open(os.path.join(conf_dir, filename), 'r') as f:
                    for line in f:
                        if "server_name" in line:
                            # Extract domain names from server_name directive
                            parts = line.split("server_name")[1].split(";")[0].strip()
                            domains.extend([d.strip() for d in parts.split() if d.strip() != "_"])
        return list(set(domains))  # Remove duplicates
    except Exception as e:
        print(f"Error retrieving domains: {e}")
        return []

def check_ssl_certificate(domain: str, port: int = 443) -> Optional[Dict]:
    """
    Check SSL certificate for a given domain.
    Returns dictionary with certificate info or None if error occurs.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                cert_der = ssock.getpeercert(binary_form=True)
                x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_der)
                
                not_before = datetime.datetime.strptime(x509.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
                not_after = datetime.datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
                days_left = (not_after - datetime.datetime.now()).days
                
                return {
                    'domain': domain,
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'subject': dict(x[0] for x in cert['subject']),
                    'valid_from': not_before,
                    'valid_to': not_after,
                    'days_left': days_left,
                    'is_valid': days_left > 0,
                    'serial_number': x509.get_serial_number(),
                    'version': x509.get_version() + 1
                }
    except Exception as e:
        print(f"Error checking SSL for {domain}: {e}")
        return None

def print_certificate_info(cert_info: Dict) -> None:
    """
    Print formatted certificate information.
    """
    if not cert_info:
        print("No certificate information available")
        return
    
    print(f"\nDomain: {cert_info['domain']}")
    print(f"Issuer: {cert_info['issuer'].get('organizationName', 'Unknown')}")
    print(f"Subject: {cert_info['subject'].get('commonName', 'Unknown')}")
    print(f"Valid From: {cert_info['valid_from']}")
    print(f"Valid To: {cert_info['valid_to']}")
    print(f"Days Left: {cert_info['days_left']}")
    print(f"Status: {'VALID' if cert_info['is_valid'] else 'EXPIRED'}")
    print(f"Serial Number: {cert_info['serial_number']}")
    print(f"Version: {cert_info['version']}")

def main():
    print("Fetching domains from FASTPANEL...")
    domains = get_fastpanel_domains()
    
    if not domains:
        print("No domains found or error occurred while fetching domains.")
        return
    
    print(f"\nFound {len(domains)} domains:")
    for domain in sorted(domains):
        print(f"- {domain}")
    
    print("\nChecking SSL certificates...")
    results = []
    for domain in domains:
        cert_info = check_ssl_certificate(domain)
        if cert_info:
            results.append(cert_info)
    
    print("\nSSL Certificate Status Summary:")
    for cert in sorted(results, key=lambda x: x['days_left']):
        print_certificate_info(cert)

if __name__ == "__main__":
    main()
```
