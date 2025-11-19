"""
Generated Code Metadata:
========================
Original URL: https://ftx68.com
Prompt: Write a troubleshooting guide for a web server that fails to find a site, including steps to check domain binding and configuration files.
Generated: DETERMINISTIC_95fedc3839e2ead9
Batch ID: 20250622_211826
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
Web Server Troubleshooting Guide
This script provides a step-by-step guide to troubleshoot web server issues
where a site fails to load due to configuration or domain binding problems.
"""

import os
import subprocess
import sys
from typing import List, Optional

def check_domain_binding(domain: str) -> bool:
    """
    Check if the domain is properly bound to the server's IP address.
    
    Args:
        domain: The domain name to check
        
    Returns:
        bool: True if domain resolves to server IP, False otherwise
    """
    try:
        # Get server's public IP
        server_ip = subprocess.check_output(['curl', '-s', 'ifconfig.me']).decode().strip()
        
        # Get domain's IP
        domain_ip = subprocess.check_output(['dig', '+short', domain]).decode().strip()
        
        return domain_ip == server_ip
    except subprocess.CalledProcessError as e:
        print(f"Error checking domain binding: {e}")
        return False

def check_config_files(web_server: str, config_path: str) -> List[str]:
    """
    Check web server configuration files for errors.
    
    Args:
        web_server: Type of web server (nginx/apache)
        config_path: Path to configuration file
        
    Returns:
        List[str]: List of errors found in config files
    """
    errors = []
    try:
        if web_server.lower() == 'nginx':
            result = subprocess.run(['nginx', '-t', '-c', config_path], 
                                  capture_output=True, text=True)
        elif web_server.lower() == 'apache':
            result = subprocess.run(['apachectl', 'configtest'], 
                                  capture_output=True, text=True)
        else:
            return ["Unsupported web server type"]
            
        if result.returncode != 0:
            errors = result.stderr.splitlines()
            
    except subprocess.CalledProcessError as e:
        errors.append(f"Error checking config: {e}")
        
    return errors

def check_virtual_host(web_server: str, domain: str) -> bool:
    """
    Check if virtual host configuration exists for the domain.
    
    Args:
        web_server: Type of web server (nginx/apache)
        domain: Domain name to check
        
    Returns:
        bool: True if virtual host exists, False otherwise
    """
    try:
        if web_server.lower() == 'nginx':
            config_path = '/etc/nginx/sites-enabled/'
            cmd = ['grep', '-r', domain, config_path]
        elif web_server.lower() == 'apache':
            config_path = '/etc/apache2/sites-enabled/'
            cmd = ['grep', '-r', domain, config_path]
        else:
            return False
            
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
        
    except subprocess.CalledProcessError as e:
        print(f"Error checking virtual host: {e}")
        return False

def check_file_permissions(doc_root: str) -> List[str]:
    """
    Check document root permissions and ownership.
    
    Args:
        doc_root: Path to document root
        
    Returns:
        List[str]: List of permission issues found
    """
    issues = []
    try:
        # Check if directory exists
        if not os.path.exists(doc_root):
            issues.append(f"Document root {doc_root} does not exist")
            return issues
            
        # Check read permissions
        if not os.access(doc_root, os.R_OK):
            issues.append(f"Read permission denied for {doc_root}")
            
        # Check execute permissions (for directory traversal)
        if not os.access(doc_root, os.X_OK):
            issues.append(f"Execute permission denied for {doc_root}")
            
        # Check web server user access
        stat_info = os.stat(doc_root)
        web_user = 'www-data'  # Common web server user
        try:
            pwd = subprocess.check_output(['getent', 'passwd', web_user]).decode()
            web_uid = int(pwd.split(':')[2])
            if stat_info.st_uid != web_uid and not os.access(doc_root, os.R_OK | os.X_OK, effective_ids=True):
                issues.append(f"Web server user {web_user} cannot access {doc_root}")
        except subprocess.CalledProcessError:
            issues.append(f"Web server user {web_user} not found")
            
    except Exception as e:
        issues.append(f"Error checking permissions: {e}")
        
    return issues

def troubleshoot_site(domain: str, web_server: str, config_path: str, doc_root: str) -> None:
    """
    Run complete troubleshooting steps for a website.
    
    Args:
        domain: Domain name to troubleshoot
        web_server: Type of web server (nginx/apache)
        config_path: Path to main configuration file
        doc_root: Document root path for the site
    """
    print(f"\n=== Troubleshooting website: {domain} ===\n")
    
    # 1. Check domain binding
    print("1. Checking domain binding...")
    if check_domain_binding(domain):
        print("✓ Domain correctly points to this server")
    else:
        print("✗ Domain does not point to this server. Check DNS settings.")
    
    # 2. Check virtual host configuration
    print("\n2. Checking virtual host configuration...")
    if check_virtual_host(web_server, domain):
        print("✓ Virtual host configuration found")
    else:
        print(f"✗ No virtual host configuration found for {domain}")
    
    # 3. Check configuration files
    print("\n3. Checking configuration files...")
    config_errors = check_config_files(web_server, config_path)
    if not config_errors:
        print("✓ Configuration files are valid")
    else:
        print("✗ Configuration errors found:")
        for error in config_errors:
            print(f"  - {error}")
    
    # 4. Check document root permissions
    print("\n4. Checking document root permissions...")
    permission_issues = check_file_permissions(doc_root)
    if not permission_issues:
        print("✓ Document root permissions are correct")
    else:
        print("✗ Permission issues found:")
        for issue in permission_issues:
            print(f"  - {issue}")
    
    print("\n=== Troubleshooting complete ===\n")

def main() -> None:
    """Main function to run the troubleshooting guide."""
    if len(sys.argv) != 5:
        print("Usage: ./troubleshoot_web.py <domain> <web_server> <config_path> <doc_root>")
        print("Example: ./troubleshoot_web.py example.com nginx /etc/nginx/nginx.conf /var/www/html")
        sys.exit(1)
        
    domain = sys.argv[1]
    web_server = sys.argv[2]
    config_path = sys.argv[3]
    doc_root = sys.argv[4]
    
    troubleshoot_site(domain, web_server, config_path, doc_root)

if __name__ == "__main__":
    main()
```
