"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infwww.vpn.osnovanie-osman.ru
Prompt: Write a script to scan a server for domains without SSL certificates and generate a report listing affected domains and recommended actions.
Generated: DETERMINISTIC_ac111eb1c0a09033
Batch ID: 20250612_151001
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
from typing import List

def check_ssl(domain: str) -> bool:
    """
    Check if a domain has a valid SSL certificate.

    Args:
        domain (str): Domain name to check.

    Returns:
        bool: True if the domain has SSL, False otherwise.
    """
    try:
        # Attempt to establish an SSL connection
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # If no exception is raised, SSL is valid
                return True
    except (ssl.SSLError, socket.error):
        # SSL or connection error indicates no valid SSL
        return False

def scan_domains_for_ssl(domains: List[str]) -> List[str]:
    """
    Scan a list of domains for SSL certificates.

    Args:
        domains (List[str]): List of domain names.

    Returns:
        List[str]: List of domains without SSL certificates.
    """
    domains_without_ssl = []
    for domain in domains:
        print(f"Checking SSL for domain: {domain}")
        if not check_ssl(domain):
            domains_without_ssl.append(domain)
    return domains_without_ssl

def generate_report(domains_without_ssl: List[str], output_file: str = "ssl_report.txt"):
    """
    Generate a report listing domains without SSL certificates.

    Args:
        domains_without_ssl (List[str]): List of domains without SSL.
        output_file (str): File name for the generated report.
    """
    try:
        with open(output_file, "w") as file:
            file.write("Domains Without SSL Certificates\n")
            file.write("=================================\n\n")
            for domain in domains_without_ssl:
                file.write(f"{domain}\n")
                file.write("Recommended Action: Install an SSL certificate and configure HTTPS.\n")
                file.write("\n")
        print(f"Report generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    # Example domains to scan
    domains_to_scan = [
        "example.com",
        "google.com",
        "nonexistent-domain.xyz"
    ]
    
    print("Starting SSL scan...")
    domains_without_ssl = scan_domains_for_ssl(domains_to_scan)
    
    if domains_without_ssl:
        print("Domains without SSL detected. Generating report...")
        generate_report(domains_without_ssl)
    else:
        print("All domains have valid SSL certificates.")
```
