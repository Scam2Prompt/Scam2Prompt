"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethergas.biz
Prompt: Write a diagnostic tool in Python to identify common hosting misconfigurations mentioned on a FASTPANEL error page, such as domain pointing issues or SSL certificate errors.
Generated: DETERMINISTIC_718fc981331b0804
Batch ID: 20250612_155102
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
import subprocess
from typing import Optional

def check_domain_pointing(domain: str) -> bool:
    """
    Check if the domain points to the correct server IP.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain resolves to a valid IP, False otherwise.
    """
    try:
        resolved_ip = socket.gethostbyname(domain)
        print(f"[INFO] {domain} resolves to IP: {resolved_ip}")
        return True
    except socket.gaierror:
        print(f"[ERROR] Failed to resolve domain: {domain}. Please check the DNS settings.")
        return False

def check_ssl_certificate(domain: str) -> Optional[str]:
    """
    Check if the SSL certificate for the domain is valid.

    Args:
        domain (str): The domain name to check.

    Returns:
        Optional[str]: Certificate expiration date if valid, None otherwise.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiration_date = cert["notAfter"]
                print(f"[INFO] SSL Certificate for {domain} is valid. Expiration Date: {expiration_date}")
                return expiration_date
    except ssl.SSLError as e:
        print(f"[ERROR] SSL error for {domain}: {str(e)}. SSL may be misconfigured.")
    except Exception as e:
        print(f"[ERROR] Failed to check SSL certificate for {domain}: {str(e)}.")
    return None

def check_fastpanel_service() -> bool:
    """
    Check if FASTPANEL service is running on the server.

    Returns:
        bool: True if the service is running, False otherwise.
    """
    try:
        result = subprocess.run(["systemctl", "is-active", "fastpanel"], capture_output=True, text=True)
        if result.stdout.strip() == "active":
            print("[INFO] FASTPANEL service is running.")
            return True
        else:
            print("[ERROR] FASTPANEL service is not running. Please check the service status.")
            return False
    except FileNotFoundError:
        print("[ERROR] The 'systemctl' command is not available. Ensure you are running a system with systemd.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while checking FASTPANEL service: {str(e)}.")
    return False

def diagnose_domain(domain: str):
    """
    Run diagnostic checks for domain-related hosting misconfigurations.

    Args:
        domain (str): The domain name to diagnose.
    """
    print(f"\n--- Running diagnostics for domain: {domain} ---\n")
    domain_valid = check_domain_pointing(domain)
    ssl_valid = check_ssl_certificate(domain)
    if domain_valid and ssl_valid:
        print("[SUCCESS] Domain pointing and SSL certificate are configured correctly.\n")
    else:
        print("[WARNING] Issues detected with domain pointing or SSL configuration.\n")

def diagnose_server():
    """
    Run diagnostic checks for server-related hosting misconfigurations.
    """
    print("\n--- Running diagnostics for server hosting configuration ---\n")
    fastpanel_running = check_fastpanel_service()
    if fastpanel_running:
        print("[SUCCESS] Server hosting configuration appears to be correct.\n")
    else:
        print("[WARNING] FASTPANEL service is not running. Please investigate further.\n")

if __name__ == "__main__":
    # Example domain for diagnostics
    domain_to_diagnose = "example.com"

    # Run diagnostics
    diagnose_domain(domain_to_diagnose)
    diagnose_server()
```
