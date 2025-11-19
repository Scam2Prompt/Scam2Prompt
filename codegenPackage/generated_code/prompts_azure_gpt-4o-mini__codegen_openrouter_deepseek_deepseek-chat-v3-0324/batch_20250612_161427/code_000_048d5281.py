"""
Generated Code Metadata:
========================
Original URL: https://uniapt.space
Prompt: How can I troubleshoot a 500 Internal Server Error on an Apache server, specifically for the site uniapt.space?
Generated: DETERMINISTIC_048d528193e8dc52
Batch ID: 20250612_161427
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
Apache 500 Internal Server Error Troubleshooting Script for uniapt.space

This script helps diagnose common causes of 500 errors on Apache servers by:
1. Checking Apache error logs
2. Verifying file permissions
3. Checking .htaccess for errors
4. Testing PHP configuration (if applicable)
"""

import subprocess
import os
import sys
from datetime import datetime

# Configuration
SITE_NAME = "uniapt.space"
APACHE_LOG_DIR = "/var/log/apache2"
APACHE_SITES_DIR = "/etc/apache2/sites-enabled"
WEB_ROOT = "/var/www/html"  # Default, adjust if different
HTACCESS_FILE = os.path.join(WEB_ROOT, ".htaccess")

def run_command(cmd):
    """Execute a shell command and return output."""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def check_apache_status():
    """Check if Apache is running."""
    return run_command("systemctl is-active apache2")

def check_error_logs():
    """Search recent error logs for the site."""
    log_file = os.path.join(APACHE_LOG_DIR, f"{SITE_NAME}-error.log")
    if not os.path.exists(log_file):
        log_file = os.path.join(APACHE_LOG_DIR, "error.log")
    
    cmd = f"tail -n 50 {log_file} | grep -i '500\\|error\\|exception'"
    return run_command(cmd)

def check_file_permissions():
    """Check web root directory permissions."""
    cmd = f"ls -la {WEB_ROOT} | head -n 10"
    return run_command(cmd)

def check_htaccess():
    """Check if .htaccess exists and its contents."""
    if not os.path.exists(HTACCESS_FILE):
        return "No .htaccess file found"
    
    with open(HTACCESS_FILE, 'r') as f:
        content = f.read()
    return f".htaccess contents:\n{content}"

def check_php_errors():
    """Check for PHP errors if PHP is used."""
    test_script = os.path.join(WEB_ROOT, "phpinfo.php")
    try:
        with open(test_script, 'w') as f:
            f.write("<?php phpinfo(); ?>")
        
        permissions = run_command(f"ls -la {test_script}")
        output = run_command(f"php {test_script}")
        os.remove(test_script)
        return f"PHP Test:\n{permissions}\nOutput truncated for brevity"
    except Exception as e:
        return f"PHP check failed: {str(e)}"

def generate_report():
    """Generate troubleshooting report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"""
=== Apache 500 Error Troubleshooting Report ===
Site: {SITE_NAME}
Generated: {timestamp}

[1] Apache Status:
{check_apache_status()}

[2] Recent Error Logs:
{check_error_logs()}

[3] File Permissions (Web Root):
{check_file_permissions()}

[4] .htaccess Check:
{check_htaccess()}

[5] PHP Check:
{check_php_errors()}
"""
    return report

if __name__ == "__main__":
    print("Generating troubleshooting report...\n")
    report = generate_report()
    print(report)
    
    # Save report to file
    report_file = f"apache_troubleshoot_{SITE_NAME}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"Report saved to: {report_file}")
```
