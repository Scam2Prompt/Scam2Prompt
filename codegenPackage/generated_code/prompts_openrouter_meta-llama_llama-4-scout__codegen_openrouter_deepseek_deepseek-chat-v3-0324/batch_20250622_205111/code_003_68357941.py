"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: How to troubleshoot a 404 error on a LiteSpeed Web Server?
Generated: DETERMINISTIC_6835794144fd913e
Batch ID: 20250622_205111
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
LiteSpeed Web Server 404 Error Troubleshooting Script

This script helps troubleshoot 404 errors on a LiteSpeed Web Server by:
1. Checking if the requested URL exists
2. Verifying file permissions
3. Checking LiteSpeed configuration
4. Looking for rewrite rule issues
5. Checking for .htaccess conflicts
"""

import os
import subprocess
import sys
from pathlib import Path

def check_url_exists(url_path):
    """Check if the requested URL path exists on the filesystem"""
    if not os.path.exists(url_path):
        print(f"Error: Path {url_path} does not exist")
        return False
    return True

def check_file_permissions(file_path):
    """Verify file has proper read permissions"""
    if not os.access(file_path, os.R_OK):
        print(f"Error: Insufficient permissions for {file_path}")
        return False
    return True

def check_litespeed_config():
    """Check LiteSpeed configuration for potential issues"""
    try:
        result = subprocess.run(
            ["/usr/local/lsws/bin/lswsctrl", "configtest"],
            capture_output=True,
            text=True
        )
        if "Configuration OK" not in result.stdout:
            print("LiteSpeed configuration issues found:")
            print(result.stdout)
            return False
    except FileNotFoundError:
        print("Error: lswsctrl command not found. Is LiteSpeed installed?")
        return False
    return True

def check_rewrite_rules(htaccess_path):
    """Check .htaccess for rewrite rule issues"""
    if not os.path.exists(htaccess_path):
        return True
        
    try:
        with open(htaccess_path, 'r') as f:
            content = f.read()
            if "RewriteRule" in content:
                print(f"Rewrite rules found in {htaccess_path}. Verify they are correct.")
                return False
    except IOError as e:
        print(f"Error reading {htaccess_path}: {str(e)}")
        return False
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: ./troubleshoot_404.py <url_path> [document_root]")
        sys.exit(1)
        
    url_path = sys.argv[1]
    doc_root = sys.argv[2] if len(sys.argv) > 2 else "/usr/local/lsws/Example/html"
    
    print(f"Troubleshooting 404 error for: {url_path}")
    
    # Construct full filesystem path
    full_path = os.path.join(doc_root, url_path.lstrip('/'))
    
    # Run checks
    checks = [
        ("URL existence", lambda: check_url_exists(full_path)),
        ("File permissions", lambda: check_file_permissions(full_path)),
        ("LiteSpeed config", check_litespeed_config),
        ("Rewrite rules", lambda: check_rewrite_rules(os.path.join(doc_root, ".htaccess"))),
    ]
    
    all_ok = True
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        if not check_func():
            all_ok = False
    
    if all_ok:
        print("\nAll basic checks passed. Consider checking:")
        print("- Virtual host configuration")
        print("- Context configuration in LiteSpeed Admin")
        print("- Server logs for more details")
    else:
        print("\nIssues found. See above for details.")

if __name__ == "__main__":
    main()
```
