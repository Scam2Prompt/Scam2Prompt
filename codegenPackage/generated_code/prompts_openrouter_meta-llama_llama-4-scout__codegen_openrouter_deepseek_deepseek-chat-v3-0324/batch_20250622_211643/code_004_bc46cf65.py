"""
Generated Code Metadata:
========================
Original URL: https://mindsol.app
Prompt: Write a script to automate tasks on a LiteSpeed Web Server, such as setting up virtual hosts or managing SSL certificates, using a programming language of choice.
Generated: DETERMINISTIC_bc46cf65dc0dd638
Batch ID: 20250622_211643
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

This script automates common tasks on a LiteSpeed Web Server, such as:
- Setting up virtual hosts
- Managing SSL certificates
- Restarting services

Requirements:
- Python 3.6+
- LiteSpeed Web Server installed
- sudo/root privileges for certain operations
"""

import os
import subprocess
import shutil
import argparse
from typing import Optional, List, Dict
import json
import sys
from pathlib import Path

# Constants
LSWS_CONF_DIR = "/usr/local/lsws/conf/"
LSWS_VHOST_CONF_DIR = os.path.join(LSWS_CONF_DIR, "vhosts")
LSWS_TEMPLATE_DIR = os.path.join(LSWS_CONF_DIR, "templates")
LSWS_BIN = "/usr/local/lsws/bin/lswsctrl"
DEFAULT_VHOST_TEMPLATE = os.path.join(LSWS_TEMPLATE_DIR, "virtual_host.conf")


class LiteSpeedAutomator:
    def __init__(self):
        self._validate_environment()

    def _validate_environment(self) -> None:
        """Validate that LiteSpeed is installed and directories exist."""
        required_dirs = [LSWS_CONF_DIR, LSWS_VHOST_CONF_DIR, LSWS_TEMPLATE_DIR]
        for directory in required_dirs:
            if not os.path.isdir(directory):
                raise FileNotFoundError(
                    f"LiteSpeed directory not found: {directory}. Is LiteSpeed installed?"
                )

        if not os.path.isfile(LSWS_BIN):
            raise FileNotFoundError(
                f"LiteSpeed binary not found at {LSWS_BIN}. Is LiteSpeed installed?"
            )

    def create_vhost(
        self,
        domain: str,
        document_root: str,
        admin_email: str = "webmaster@localhost",
        template_path: Optional[str] = None,
    ) -> bool:
        """
        Create a new virtual host configuration.

        Args:
            domain: Domain name for the virtual host
            document_root: Path to the document root
            admin_email: Admin email for the server
            template_path: Custom template path (optional)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate inputs
            if not domain or not document_root:
                raise ValueError("Domain and document root are required")

            # Use default template if none provided
            template = template_path if template_path else DEFAULT_VHOST_TEMPLATE
            if not os.path.isfile(template):
                raise FileNotFoundError(f"Template file not found: {template}")

            # Create document root if it doesn't exist
            os.makedirs(document_root, exist_ok=True)

            # Read template
            with open(template, "r") as f:
                content = f.read()

            # Replace placeholders
            content = content.replace("${DOMAIN}", domain)
            content = content.replace("${DOC_ROOT}", document_root)
            content = content.replace("${ADMIN_EMAIL}", admin_email)

            # Write new vhost config
            vhost_conf_path = os.path.join(LSWS_VHOST_CONF_DIR, f"{domain}.conf")
            with open(vhost_conf_path, "w") as f:
                f.write(content)

            # Add to main configuration
            self._add_vhost_to_main_config(domain)

            return True
        except Exception as e:
            print(f"Error creating virtual host: {e}", file=sys.stderr)
            return False

    def _add_vhost_to_main_config(self, domain: str) -> None:
        """Add virtual host reference to main LiteSpeed configuration."""
        main_conf_path = os.path.join(LSWS_CONF_DIR, "httpd_config.conf")
        with open(main_conf_path, "a") as f:
            f.write(f"\nInclude {os.path.join(LSWS_VHOST_CONF_DIR, domain + '.conf')}\n")

    def install_ssl_certificate(
        self, domain: str, cert_path: str, key_path: str, chain_path: Optional[str] = None
    ) -> bool:
        """
        Install SSL certificate for a virtual host.

        Args:
            domain: Domain name for the certificate
            cert_path: Path to the certificate file
            key_path: Path to the private key file
            chain_path: Path to the chain file (optional)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate files exist
            for path in [cert_path, key_path]:
                if not os.path.isfile(path):
                    raise FileNotFoundError(f"File not found: {path}")

            if chain_path and not os.path.isfile(chain_path):
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

            # Update vhost configuration
            vhost_conf_path = os.path.join(LSWS_VHOST_CONF_DIR, f"{domain}.conf")
            if not os.path.isfile(vhost_conf_path):
                raise FileNotFoundError(f"Virtual host config not found: {domain}")

            with open(vhost_conf_path, "r") as f:
                content = f.read()

            # Add SSL configuration
            ssl_config = f"""
secureListeners {{
    listener {{
        address                  *:443
        secure                  1
        certFile                {domain_ssl_dir}/cert.pem
        keyFile                 {domain_ssl_dir}/key.pem
        {"caCertFile             " + domain_ssl_dir + "/chain.pem" if chain_path else ""}
    }}
}}
"""
            content = content.replace("</virtualHost>", f"{ssl_config}</virtualHost>")

            with open(vhost_conf_path, "w") as f:
                f.write(content)

            return True
        except Exception as e:
            print(f"Error installing SSL certificate: {e}", file=sys.stderr)
            return False

    def restart_lsws(self) -> bool:
        """Restart LiteSpeed web server."""
        try:
            result = subprocess.run([LSWS_BIN, "restart"], check=True, capture_output=True)
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            print(f"Error restarting LiteSpeed: {e.stderr.decode()}", file=sys.stderr)
            return False


def main():
    parser = argparse.ArgumentParser(description="LiteSpeed Web Server Automation Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create vhost command
    vhost_parser = subparsers.add_parser("create-vhost", help="Create a virtual host")
    vhost_parser.add_argument("--domain", required=True, help="Domain name")
    vhost_parser.add_argument("--docroot", required=True, help="Document root path")
    vhost_parser.add_argument("--email", default="webmaster@localhost", help="Admin email")
    vhost_parser.add_argument("--template", help="Custom template path")

    # SSL command
    ssl_parser = subparsers.add_parser("install-ssl", help="Install SSL certificate")
    ssl_parser.add_argument("--domain", required=True, help="Domain name")
    ssl_parser.add_argument("--cert", required=True, help="Certificate file path")
    ssl_parser.add_argument("--key", required=True, help="Private key file path")
    ssl_parser.add_argument("--chain", help="Chain file path")

    # Restart command
    subparsers.add_parser("restart", help="Restart LiteSpeed web server")

    args = parser.parse_args()
    automator = LiteSpeedAutomator()

    try:
        if args.command == "create-vhost":
            success = automator.create_vhost(
                args.domain, args.docroot, args.email, args.template
            )
            if success:
                print(f"Virtual host {args.domain} created successfully")
            else:
                sys.exit(1)

        elif args.command == "install-ssl":
            success = automator.install_ssl_certificate(
                args.domain, args.cert, args.key, args.chain
            )
            if success:
                print(f"SSL certificate installed for {args.domain}")
            else:
                sys.exit(1)

        elif args.command == "restart":
            success = automator.restart_lsws()
            if success:
                print("LiteSpeed rest
