"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: How do I troubleshoot common issues when my HTTP server displays the CentOS-WebPanel test page?
Generated: DETERMINISTIC_4e25b7df3d992fb4
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to troubleshoot common issues when an HTTP server displays the CentOS-WebPanel test page.
This script automates the checks for common server misconfigurations.
"""

import os
import subprocess
import sys

def check_apache_running():
    """
    Check if Apache HTTP Server is running.
    """
    try:
        print("Checking if Apache is running...")
        result = subprocess.run(["systemctl", "is-active", "httpd"], capture_output=True, text=True)
        if result.stdout.strip() == "active":
            print("[OK] Apache is running.")
        else:
            print("[ERROR] Apache is not running.")
            print("Start Apache using: sudo systemctl start httpd")
    except Exception as e:
        print(f"[ERROR] Failed to check Apache status: {e}")

def check_apache_configuration():
    """
    Check Apache configuration for syntax errors.
    """
    try:
        print("Checking Apache configuration...")
        result = subprocess.run(["apachectl", "configtest"], capture_output=True, text=True)
        if "Syntax OK" in result.stdout:
            print("[OK] Apache configuration syntax is valid.")
        else:
            print("[ERROR] Apache configuration syntax issues detected.")
            print(result.stdout)
    except Exception as e:
        print(f"[ERROR] Failed to check Apache configuration: {e}")

def check_document_root():
    """
    Verify if the DocumentRoot in Apache configuration is correctly set.
    """
    try:
        print("Checking DocumentRoot...")
        document_root_path = "/var/www/html"
        if os.path.exists(document_root_path):
            print(f"[OK] DocumentRoot exists at '{document_root_path}'.")
        else:
            print(f"[ERROR] DocumentRoot missing at '{document_root_path}'.")
            print("Ensure your VirtualHost configuration points to the correct directory.")
    except Exception as e:
        print(f"[ERROR] Failed to check DocumentRoot: {e}")

def check_firewall_rules():
    """
    Check if firewall rules allow HTTP traffic (port 80).
    """
    try:
        print("Checking firewall rules for HTTP traffic...")
        result = subprocess.run(["firewall-cmd", "--list-services"], capture_output=True, text=True)
        if "http" in result.stdout:
            print("[OK] Firewall allows HTTP traffic.")
        else:
            print("[ERROR] Firewall does not allow HTTP traffic.")
            print("Enable HTTP traffic using: sudo firewall-cmd --add-service=http --permanent && sudo firewall-cmd --reload")
    except Exception as e:
        print(f"[ERROR] Failed to check firewall rules: {e}")

def check_selinux_status():
    """
    Check if SELinux settings are blocking Apache access.
    """
    try:
        print("Checking SELinux status...")
        result = subprocess.run(["getenforce"], capture_output=True, text=True)
        selinux_status = result.stdout.strip()
        if selinux_status == "Enforcing":
            print("[WARNING] SELinux is enforcing. Ensure SELinux policies allow Apache access.")
        else:
            print("[OK] SELinux is not enforcing.")
    except Exception as e:
        print(f"[ERROR] Failed to check SELinux status: {e}")

def troubleshoot_http_server():
    """
    Main function to run all troubleshooting steps.
    """
    print("Starting HTTP server troubleshooting process...")
    check_apache_running()
    check_apache_configuration()
    check_document_root()
    check_firewall_rules()
    check_selinux_status()
    print("Troubleshooting completed.")

if __name__ == "__main__":
    try:
        troubleshoot_http_server()
    except KeyboardInterrupt:
        print("\n[INFO] Troubleshooting process interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        sys.exit(1)
```
