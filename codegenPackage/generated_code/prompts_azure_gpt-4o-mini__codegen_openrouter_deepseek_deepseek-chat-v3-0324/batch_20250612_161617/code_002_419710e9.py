"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: What are the steps to set up a FastCGI application using Plesk?
Generated: DETERMINISTIC_419710e952fe4bae
Batch ID: 20250612_161617
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
FastCGI Application Setup for Plesk

This script automates the setup of a FastCGI application in Plesk.
It creates necessary directories, configuration files, and sets appropriate permissions.
"""

import os
import subprocess
import shutil
from pathlib import Path

def setup_fastcgi_app(domain_name: str, app_name: str, python_path: str) -> bool:
    """
    Set up a FastCGI application in Plesk for a given domain.
    
    Args:
        domain_name: The domain name (e.g., 'example.com')
        app_name: The application name (e.g., 'myapp')
        python_path: Path to Python interpreter (e.g., '/usr/bin/python3')
    
    Returns:
        bool: True if setup was successful, False otherwise
    """
    try:
        # Define paths
        domain_path = Path(f"/var/www/vhosts/{domain_name}")
        httpdocs_path = domain_path / "httpdocs"
        fcgi_bin_path = domain_path / "fcgi-bin"
        app_path = httpdocs_path / app_name
        fcgi_handler = fcgi_bin_path / f"{app_name}.fcgi"
        
        # Create directories if they don't exist
        fcgi_bin_path.mkdir(exist_ok=True, mode=0o755)
        app_path.mkdir(exist_ok=True, mode=0o755)
        
        # Create FastCGI handler file
        fcgi_handler_content = f"""#!/bin/sh
# FastCGI wrapper for {app_name}
export PYTHONPATH="{httpdocs_path}"
exec {python_path} -m flup.server.fcgi
"""
        with open(fcgi_handler, 'w') as f:
            f.write(fcgi_handler_content)
        
        # Set permissions
        fcgi_handler.chmod(0o755)
        
        # Create .htaccess file
        htaccess_path = app_path / ".htaccess"
        htaccess_content = f"""Options +ExecCGI
AddHandler fcgid-script .fcgi
RewriteEngine On
RewriteCond %{{REQUEST_FILENAME}} !-f
RewriteRule ^(.*)$ {fcgi_bin_path}/{app_name}.fcgi/$1 [QSA,L]
"""
        with open(htaccess_path, 'w') as f:
            f.write(htaccess_content)
        
        # Set ownership to Plesk user
        subprocess.run(['chown', '-R', f'psacln:psaserv', str(domain_path)], check=True)
        
        return True
    
    except Exception as e:
        print(f"Error setting up FastCGI application: {str(e)}")
        return False

if __name__ == "__main__":
    # Example usage
    domain = "example.com"
    app = "myapp"
    python_interpreter = "/usr/bin/python3"
    
    if setup_fastcgi_app(domain, app, python_interpreter):
        print(f"Successfully set up FastCGI application '{app}' for domain '{domain}'")
    else:
        print("Failed to set up FastCGI application")
```
