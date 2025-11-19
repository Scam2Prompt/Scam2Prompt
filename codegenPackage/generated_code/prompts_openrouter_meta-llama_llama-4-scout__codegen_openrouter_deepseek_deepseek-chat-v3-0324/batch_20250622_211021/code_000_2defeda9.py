"""
Generated Code Metadata:
========================
Original URL: https://connect-derive.com
Prompt: "How can I configure LiteSpeed Web Server to serve a website with a custom CGI setup?"
Generated: DETERMINISTIC_2defeda9b05cf1e4
Batch ID: 20250622_211021
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
LiteSpeed Web Server CGI Configuration Script

This script automates the configuration of LiteSpeed Web Server to serve a website
with a custom CGI setup. It handles:
- Virtual host creation
- CGI handler configuration
- Directory permissions
- Error handling for common issues
"""

import os
import subprocess
import shutil
from pathlib import Path

class LiteSpeedCGIConfigurator:
    def __init__(self, domain, document_root, cgi_path):
        """
        Initialize the configurator with website details.
        
        Args:
            domain (str): Domain name for the virtual host
            document_root (str): Path to website files
            cgi_path (str): Path to CGI scripts directory
        """
        self.domain = domain
        self.document_root = Path(document_root).resolve()
        self.cgi_path = Path(cgi_path).resolve()
        self.lsws_conf_dir = Path("/usr/local/lsws/conf/")
        self.vhost_template = f"""
virtualHost {self.domain} {{
  vhRoot                  {self.document_root}
  configFile             {self.lsws_conf_dir / f'{self.domain}.conf'}
  allowSymbolLink        1
  enableScript           1
  restrained             0
  setUIDMode             2
}}

virtualhost {self.domain} {{
  cgiHandlers + {{
    handler              lsapi
    extensions           pl,py,cgi
  }}
  scriptHandler + {{
    addHandler           {self.cgi_path}/
    suffixes            .cgi,.pl,.py
    priority            0
  }}
}}
"""

    def validate_paths(self):
        """Validate that required paths exist and are accessible."""
        if not self.document_root.exists():
            raise FileNotFoundError(f"Document root not found: {self.document_root}")
        if not self.cgi_path.exists():
            raise FileNotFoundError(f"CGI directory not found: {self.cgi_path}")
        if not self.lsws_conf_dir.exists():
            raise FileNotFoundError("LiteSpeed configuration directory not found")

    def configure_virtual_host(self):
        """Create virtual host configuration file."""
        vhost_conf = self.lsws_conf_dir / f"{self.domain}.conf"
        try:
            with open(vhost_conf, 'w') as f:
                f.write(self.vhost_template)
            print(f"Created virtual host config: {vhost_conf}")
        except IOError as e:
            raise Exception(f"Failed to write virtual host config: {e}")

    def set_permissions(self):
        """Set appropriate permissions for CGI directory."""
        try:
            os.chmod(self.cgi_path, 0o755)
            for root, dirs, files in os.walk(self.cgi_path):
                for d in dirs:
                    os.chmod(Path(root) / d, 0o755)
                for f in files:
                    os.chmod(Path(root) / f, 0o755)
            print(f"Set permissions for CGI directory: {self.cgi_path}")
        except Exception as e:
            raise Exception(f"Failed to set permissions: {e}")

    def restart_litespeed(self):
        """Gracefully restart LiteSpeed to apply changes."""
        try:
            subprocess.run(['/usr/local/lsws/bin/lswsctrl', 'restart'], check=True)
            print("LiteSpeed restarted successfully")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to restart LiteSpeed: {e}")

    def configure(self):
        """Main configuration method."""
        try:
            self.validate_paths()
            self.configure_virtual_host()
            self.set_permissions()
            self.restart_litespeed()
            print("Configuration completed successfully")
        except Exception as e:
            print(f"Error during configuration: {e}")
            raise

if __name__ == "__main__":
    # Example usage - replace with your actual values
    configurator = LiteSpeedCGIConfigurator(
        domain="example.com",
        document_root="/var/www/example.com/public_html",
        cgi_path="/var/www/example.com/cgi-bin"
    )
    configurator.configure()
```
