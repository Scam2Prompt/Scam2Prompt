"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x000000000000000.icu
Prompt: Generate a diagnostic tool to identify common server issues (e.g., missing SSL certificates, domain misconfiguration) specifically for FASTPANEL environments.
Generated: DETERMINISTIC_6d3108d1e962b008
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import socket
import ssl


def check_ssl_certificate(domain):
    """
    Check if the domain has a valid SSL certificate.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing certificate details or errors.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return {"status": "valid", "certificate": cert}
    except ssl.SSLError as e:
        return {"status": "invalid", "error": str(e)}
    except socket.timeout:
        return {"status": "error", "error": "Connection timed out"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def check_fastpanel_services():
    """
    Check if FASTPANEL services are running properly.

    Returns:
        dict: A dictionary with service statuses.
    """
    services = ["nginx", "fastpanel", "mysql"]  # Add more services as needed
    statuses = {}
    for service in services:
        try:
            result = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
            status = result.stdout.strip()
            statuses[service] = status if status else "unknown"
        except Exception as e:
            statuses[service] = f"Error: {str(e)}"
    return statuses


def check_domain_configuration(domain):
    """
    Verify if the domain is correctly configured.

    Args:
        domain (str): The domain to check.

    Returns:
        dict: A dictionary containing domain configuration status.
    """
    try:
        ip_address = socket.gethostbyname(domain)
        return {"status": "configured", "ip_address": ip_address}
    except socket.gaierror:
        return {"status": "misconfigured", "error": "Domain not reachable"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def run_diagnostics(domains):
    """
    Run diagnostics for common server issues.

    Args:
        domains (list): List of domains to check.

    Returns:
        dict: A dictionary containing all diagnostic results.
    """
    diagnostics = {}
    diagnostics["service_statuses"] = check_fastpanel_services()
    diagnostics["domain_checks"] = {}
    diagnostics["ssl_checks"] = {}

    for domain in domains:
        diagnostics["domain_checks"][domain] = check_domain_configuration(domain)
        diagnostics["ssl_checks"][domain] = check_ssl_certificate(domain)

    return diagnostics


if __name__ == "__main__":
    # Example domains to check. Replace with actual domains used in your FASTPANEL setup.
    domains_to_check = ["example.com", "yourdomain.com"]

    try:
        results = run_diagnostics(domains_to_check)

        # Print results in a readable format
        print("FASTPANEL Diagnostics Tool Results:")
        print("\nService Statuses:")
        for service, status in results["service_statuses"].items():
            print(f"  {service}: {status}")

        print("\nDomain Checks:")
        for domain, check in results["domain_checks"].items():
            print(f"  {domain}: {check}")

        print("\nSSL Checks:")
        for domain, ssl_check in results["ssl_checks"].items():
            print(f"  {domain}: {ssl_check}")

    except Exception as e:
        print(f"An error occurred during diagnostics: {str(e)}")
```
