"""
Generated Code Metadata:
========================
Original URL: https://geteasycrypto.com
Prompt: How do I troubleshoot common issues when my HTTP server displays the CentOS-WebPanel test page?
Generated: DETERMINISTIC_4e25b7df3d992fb4
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to troubleshoot common issues when an HTTP server displays the CentOS-WebPanel test page.
This script checks for common misconfigurations and provides suggestions for resolution.
"""

import os
import subprocess
import sys

def check_apache_status():
    """
    Check if Apache HTTP server is running.
    """
    try:
        result = subprocess.run(['systemctl', 'status', 'httpd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "active (running)" in result.stdout:
            print("Apache is running.")
        else:
            print("Apache is not running. Try starting it with: sudo systemctl start httpd")
    except Exception as e:
        print(f"Error checking Apache status: {e}")

def check_default_vhost():
    """
    Check if the default virtual host configuration is active.
    """
    try:
        vhost_path = "/etc/httpd/conf.d/vhost.conf"
        if os.path.exists(vhost_path):
            with open(vhost_path, 'r') as file:
                content = file.read()
                if "DocumentRoot" in content:
                    print("Default virtual host configuration found.")
                else:
                    print("Default virtual host configuration is missing DocumentRoot.")
        else:
            print(f"Virtual host configuration file not found at {vhost_path}.")
    except Exception as e:
        print(f"Error checking virtual host configuration: {e}")

def check_dns_resolution(domain):
    """
    Check if the server's domain resolves correctly.
    """
    try:
        result = subprocess.run(['ping', '-c', '1', domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Domain {domain} resolves correctly.")
        else:
            print(f"Domain {domain} does not resolve. Check your DNS settings.")
    except Exception as e:
        print(f"Error checking DNS resolution: {e}")

def check_firewall_rules():
    """
    Check if the firewall allows HTTP traffic.
    """
    try:
        result = subprocess.run(['firewall-cmd', '--list-all'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "http" in result.stdout or "80/tcp" in result.stdout:
            print("Firewall allows HTTP traffic.")
        else:
            print("Firewall does not allow HTTP traffic. Add a rule with: sudo firewall-cmd --add-service=http --permanent && sudo firewall-cmd --reload")
    except Exception as e:
        print(f"Error checking firewall rules: {e}")

def check_selinux_status():
    """
    Check if SELinux is blocking HTTP traffic.
    """
    try:
        result = subprocess.run(['sestatus'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "enabled" in result.stdout:
            print("SELinux is enabled. Ensure HTTP traffic is allowed with: sudo setsebool -P httpd_can_network_connect on")
        else:
            print("SELinux is disabled.")
    except Exception as e:
        print(f"Error checking SELinux status: {e}")

def main():
    """
    Main function to run all troubleshooting checks.
    """
    print("Starting troubleshooting for CentOS-WebPanel test page issue...\n")
    
    print("1. Checking Apache HTTP server status...")
    check_apache_status()
    
    print("\n2. Checking default virtual host configuration...")
    check_default_vhost()
    
    print("\n3. Checking DNS resolution...")
    domain = input("Enter the domain name to check DNS resolution (e.g., example.com): ")
    check_dns_resolution(domain)
    
    print("\n4. Checking firewall rules...")
    check_firewall_rules()
    
    print("\n5. Checking SELinux status...")
    check_selinux_status()
    
    print("\nTroubleshooting completed. Review the suggestions above to resolve the issue.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
