"""
Generated Code Metadata:
========================
Original URL: https://vanillagift.remadet.com
Prompt: Write a script to configure a LiteSpeed Web Server to prevent directory indexing and display a custom error page instead.
Generated: DETERMINISTIC_a2bd9af35ef97209
Batch ID: 20250612_154827
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
Script to configure LiteSpeed Web Server to prevent directory indexing
and display a custom error page instead.
"""

import os
import sys
import subprocess
from pathlib import Path

# Configuration constants
LSWS_CONF_DIR = "/usr/local/lsws/conf/"
VIRTUAL_HOST_TEMPLATE = "vhosts/{host}/vhost.conf"
CUSTOM_ERROR_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>403 Forbidden</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { color: #d9534f; }
    </style>
</head>
<body>
    <h1>403 Forbidden</h1>
    <p>Directory browsing is not allowed.</p>
</body>
</html>
"""
ERROR_PAGE_PATH = "/usr/local/lsws/error/403_custom.html"

def check_root():
    """Check if script is run as root."""
    if os.geteuid() != 0:
        print("This script must be run as root.", file=sys.stderr)
        sys.exit(1)

def write_error_page():
    """Write the custom error page to disk."""
    try:
        with open(ERROR_PAGE_PATH, 'w') as f:
            f.write(CUSTOM_ERROR_PAGE)
        os.chmod(ERROR_PAGE_PATH, 0o644)
        print(f"Custom error page written to {ERROR_PAGE_PATH}")
    except IOError as e:
        print(f"Error writing custom error page: {e}", file=sys.stderr)
        sys.exit(1)

def update_vhost_config(hostname):
    """Update virtual host configuration to disable directory indexing."""
    vhost_conf = Path(LSWS_CONF_DIR) / VIRTUAL_HOST_TEMPLATE.format(host=hostname)
    
    if not vhost_conf.exists():
        print(f"Virtual host config {vhost_conf} not found.", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(vhost_conf, 'r') as f:
            config = f.read()
        
        # Add or update configuration directives
        if "autoIndex 0" not in config:
            config = config.replace("</virtualHost>", 
                                  "  autoIndex 0\n"
                                  "  errorPage 403 /error/403_custom.html\n"
                                  "</virtualHost>")
        
        with open(vhost_conf, 'w') as f:
            f.write(config)
        
        print(f"Updated {vhost_conf} to disable directory indexing")
    except IOError as e:
        print(f"Error updating virtual host config: {e}", file=sys.stderr)
        sys.exit(1)

def restart_lsws():
    """Gracefully restart LiteSpeed Web Server."""
    try:
        subprocess.run(["/usr/local/lsws/bin/lswsctrl", "restart"], check=True)
        print("LiteSpeed Web Server restarted successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting LiteSpeed: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function to execute the configuration changes."""
    check_root()
    
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <hostname>", file=sys.stderr)
        sys.exit(1)
    
    hostname = sys.argv[1]
    
    write_error_page()
    update_vhost_config(hostname)
    restart_lsws()

if __name__ == "__main__":
    main()
```
