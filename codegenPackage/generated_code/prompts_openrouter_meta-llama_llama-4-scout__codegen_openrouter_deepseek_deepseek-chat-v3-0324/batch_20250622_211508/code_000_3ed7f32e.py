"""
Generated Code Metadata:
========================
Original URL: https://876981455175.icu
Prompt: What are common reasons for seeing a default server page when accessing a website, and how can I troubleshoot them using FASTPANEL?
Generated: DETERMINISTIC_3ed7f32e3a447c25
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
FASTPANEL Default Server Page Troubleshooter

This script helps diagnose common reasons for seeing a default server page
when accessing a website hosted on FASTPANEL.
"""

import subprocess
import sys
import os
from typing import Optional, List, Tuple

def run_command(cmd: str) -> Tuple[bool, str]:
    """
    Execute a shell command and return (success, output) tuple.
    """
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.output.strip()

def check_nginx_status() -> bool:
    """
    Check if nginx is running properly.
    """
    success, output = run_command("systemctl is-active nginx")
    if not success or output != "active":
        print(f"❌ Nginx is not running. Status: {output}")
        return False
    print("✅ Nginx is running")
    return True

def check_domain_config(domain: str) -> bool:
    """
    Check if domain has proper configuration in FASTPANEL.
    """
    config_path = f"/etc/nginx/conf.d/{domain}.conf"
    if not os.path.exists(config_path):
        print(f"❌ Domain config not found at {config_path}")
        return False
    
    success, output = run_command(f"nginx -t -c {config_path}")
    if not success:
        print(f"❌ Nginx config test failed for {domain}: {output}")
        return False
    
    print(f"✅ Domain {domain} has valid nginx configuration")
    return True

def check_dns_resolution(domain: str) -> bool:
    """
    Verify DNS resolution for the domain.
    """
    success, output = run_command(f"dig +short {domain}")
    if not success or not output:
        print(f"❌ DNS resolution failed for {domain}")
        return False
    print(f"✅ DNS resolves for {domain}: {output}")
    return True

def check_hosts_file(domain: str) -> bool:
    """
    Check for localhost overrides in /etc/hosts.
    """
    with open("/etc/hosts", "r") as f:
        for line in f:
            if domain in line and "127.0.0.1" in line:
                print(f"⚠️  Found localhost override for {domain} in /etc/hosts")
                return False
    return True

def check_fastpanel_website(domain: str) -> bool:
    """
    Check if website exists and is enabled in FASTPANEL.
    """
    success, output = run_command("fastpanel site list")
    if not success:
        print("❌ Failed to list FASTPANEL sites")
        return False
    
    if domain not in output:
        print(f"❌ Domain {domain} not found in FASTPANEL")
        return False
    
    print(f"✅ Domain {domain} exists in FASTPANEL")
    return True

def restart_nginx() -> bool:
    """
    Restart nginx service.
    """
    success, output = run_command("systemctl restart nginx")
    if not success:
        print(f"❌ Failed to restart nginx: {output}")
        return False
    print("✅ Nginx restarted successfully")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: ./fastpanel_troubleshooter.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    print(f"\n🔍 Troubleshooting default server page for {domain}\n")
    
    checks = [
        ("Nginx Status", check_nginx_status),
        ("FASTPANEL Website", lambda: check_fastpanel_website(domain)),
        ("Domain Config", lambda: check_domain_config(domain)),
        ("DNS Resolution", lambda: check_dns_resolution(domain)),
        ("Hosts File", lambda: check_hosts_file(domain)),
    ]
    
    all_checks_passed = True
    for name, check_func in checks:
        print(f"\n=== {name} ===")
        if not check_func():
            all_checks_passed = False
    
    if not all_checks_passed:
        print("\n❌ Some checks failed. Review the output above.")
        sys.exit(1)
    
    print("\n✅ All basic checks passed. Trying to restart nginx...")
    if restart_nginx():
        print("\n🔄 Nginx restarted. Please check your website again.")
    else:
        print("\n❌ Failed to resolve the issue automatically. Please contact support.")

if __name__ == "__main__":
    main()
```
