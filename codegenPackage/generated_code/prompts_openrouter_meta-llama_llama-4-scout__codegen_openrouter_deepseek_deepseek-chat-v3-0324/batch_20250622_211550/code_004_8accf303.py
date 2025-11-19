"""
Generated Code Metadata:
========================
Original URL: https://dommespace.com.br
Prompt: Generate a Python script to automate tasks on a LiteSpeed Web Server, such as creating new virtual hosts or managing SSL certificates.
Generated: DETERMINISTIC_8accf303adc93baa
Batch ID: 20250622_211550
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
LiteSpeed Web Server Automation Script

This script provides functionalities to automate common tasks on a LiteSpeed Web Server,
including creating virtual hosts and managing SSL certificates.

Requirements:
- Python 3.6+
- LiteSpeed Web Server installed
- Appropriate permissions to modify LiteSpeed configuration
"""

import os
import subprocess
import argparse
import shutil
import sys
from typing import Optional, List

# Constants
LSWS_CONF_DIR = "/usr/local/lsws/conf/"
VIRTUAL_HOST_TEMPLATE = """
virtualHost {name} {{
    vhRoot                  {document_root}
    configFile             {config_file}
    allowSymbolLink         1
    enableScript            1
    restrained              1
    setUIDMode              2
}}
"""

class LiteSpeedAutomation:
    def __init__(self):
        self.check_environment()

    def check_environment(self) -> None:
        """Check if LiteSpeed is installed and user has sufficient permissions."""
        if not os.path.exists(LSWS_CONF_DIR):
            raise FileNotFoundError("LiteSpeed installation not found at default location.")

        if os.geteuid() != 0:
            raise PermissionError("This script requires root privileges to modify LiteSpeed configuration.")

    def create_virtual_host(self, name: str, document_root: str, 
                          config_file: Optional[str] = None) -> bool:
        """
        Create a new virtual host in LiteSpeed.
        
        Args:
            name: Name of the virtual host
            document_root: Path to the document root directory
            config_file: Path to the config file (optional)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create document root if it doesn't exist
            os.makedirs(document_root, exist_ok=True)
            
            # Set default config file path if not provided
            if not config_file:
                config_file = os.path.join(document_root, f"{name}.conf")
            
            # Generate virtual host configuration
            vhost_config = VIRTUAL_HOST_TEMPLATE.format(
                name=name,
                document_root=document_root,
                config_file=config_file
            )
            
            # Append to httpd_config.conf
            httpd_config_path = os.path.join(LSWS_CONF_DIR, "httpd_config.conf")
            with open(httpd_config_path, "a") as f:
                f.write(vhost_config)
            
            # Create basic config file
            with open(config_file, "w") as f:
                f.write(f"docRoot {document_root}\nindex {\n  useServer 0\n  index index.html index.php\n}")
            
            # Restart LiteSpeed to apply changes
            self.restart_litespeed()
            return True
            
        except Exception as e:
            print(f"Error creating virtual host: {str(e)}", file=sys.stderr)
            return False

    def install_ssl_certificate(self, domain: str, cert_path: str, 
                              key_path: str, chain_path: Optional[str] = None) -> bool:
        """
        Install SSL certificate for a domain.
        
        Args:
            domain: Domain name for the certificate
            cert_path: Path to the certificate file
            key_path: Path to the private key file
            chain_path: Path to the chain file (optional)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Verify files exist
            for path in [cert_path, key_path]:
                if not os.path.exists(path):
                    raise FileNotFoundError(f"File not found: {path}")
            
            if chain_path and not os.path.exists(chain_path):
                raise FileNotFoundError(f"Chain file not found: {chain_path}")
            
            # Create SSL directory if it doesn't exist
            ssl_dir = os.path.join(LSWS_CONF_DIR, "ssl")
            os.makedirs(ssl_dir, exist_ok=True)
            
            # Copy files to SSL directory
            domain_ssl_dir = os.path.join(ssl_dir, domain)
            os.makedirs(domain_ssl_dir, exist_ok=True)
            
            shutil.copy(cert_path, os.path.join(domain_ssl_dir, "cert.pem"))
            shutil.copy(key_path, os.path.join(domain_ssl_dir, "key.pem"))
            if chain_path:
                shutil.copy(chain_path, os.path.join(domain_ssl_dir, "chain.pem"))
            
            # Restart LiteSpeed to apply changes
            self.restart_litespeed()
            return True
            
        except Exception as e:
            print(f"Error installing SSL certificate: {str(e)}", file=sys.stderr)
            return False

    def restart_litespeed(self) -> bool:
        """Restart LiteSpeed server to apply configuration changes."""
        try:
            subprocess.run(["/usr/local/lsws/bin/lswsctrl", "restart"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error restarting LiteSpeed: {str(e)}", file=sys.stderr)
            return False

def main():
    parser = argparse.ArgumentParser(description="LiteSpeed Web Server Automation Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Virtual host creation subcommand
    vhost_parser = subparsers.add_parser("create-vhost", help="Create a new virtual host")
    vhost_parser.add_argument("--name", required=True, help="Name of the virtual host")
    vhost_parser.add_argument("--document-root", required=True, help="Path to document root")
    vhost_parser.add_argument("--config-file", help="Path to config file (optional)")
    
    # SSL installation subcommand
    ssl_parser = subparsers.add_parser("install-ssl", help="Install SSL certificate")
    ssl_parser.add_argument("--domain", required=True, help="Domain name for the certificate")
    ssl_parser.add_argument("--cert", required=True, help="Path to certificate file")
    ssl_parser.add_argument("--key", required=True, help="Path to private key file")
    ssl_parser.add_argument("--chain", help="Path to chain file (optional)")
    
    args = parser.parse_args()
    lsws = LiteSpeedAutomation()
    
    if args.command == "create-vhost":
        success = lsws.create_virtual_host(
            name=args.name,
            document_root=args.document_root,
            config_file=args.config_file
        )
        print("Virtual host created successfully!" if success else "Failed to create virtual host")
    
    elif args.command == "install-ssl":
        success = lsws.install_ssl_certificate(
            domain=args.domain,
            cert_path=args.cert,
            key_path=args.key,
            chain_path=args.chain
        )
        print("SSL certificate installed successfully!" if success else "Failed to install SSL certificate")

if __name__ == "__main__":
    main()
```
