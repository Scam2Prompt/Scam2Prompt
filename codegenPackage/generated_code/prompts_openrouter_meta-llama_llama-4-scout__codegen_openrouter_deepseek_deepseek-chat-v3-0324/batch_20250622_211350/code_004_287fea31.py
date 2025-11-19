"""
Generated Code Metadata:
========================
Original URL: https://arcaem.com
Prompt: "What are the best practices for securing a Plesk server and its domains programmatically?"
Generated: DETERMINISTIC_287fea3100a4a4c1
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import json
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('plesk_security.log'),
        logging.StreamHandler()
    ]
)

class PleskSecurityManager:
    """
    A class to manage security best practices for Plesk servers and domains programmatically.
    """

    def __init__(self, plesk_cli_path: str = '/usr/local/psa/bin'):
        """
        Initialize the PleskSecurityManager with the path to Plesk CLI utilities.

        Args:
            plesk_cli_path (str): Path to Plesk CLI utilities. Defaults to '/usr/local/psa/bin'.
        """
        self.plesk_cli_path = plesk_cli_path

    def execute_plesk_command(self, command: str, args: List[str]) -> Optional[str]:
        """
        Execute a Plesk CLI command and return the output.

        Args:
            command (str): The Plesk CLI command to execute.
            args (List[str]): List of arguments for the command.

        Returns:
            Optional[str]: The command output if successful, None otherwise.
        """
        try:
            cmd = [f"{self.plesk_cli_path}/{command}"] + args
            result = subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing command {command}: {e.stderr}")
            return None

    def enable_firewall(self) -> bool:
        """
        Enable the Plesk firewall.

        Returns:
            bool: True if successful, False otherwise.
        """
        output = self.execute_plesk_command('firewall', ['--enable'])
        return output is not None

    def configure_fail2ban(self) -> bool:
        """
        Configure Fail2Ban for Plesk.

        Returns:
            bool: True if successful, False otherwise.
        """
        output = self.execute_plesk_command('fail2ban', ['--enable'])
        if output is None:
            return False
        # Set common jail configurations
        jails = ['plesk-apache', 'plesk-apache-badbot', 'plesk-ssh']
        for jail in jails:
            self.execute_plesk_command('fail2ban', ['--set-jail', jail, 'enabled', 'true'])
        return True

    def update_plesk(self) -> bool:
        """
        Update Plesk to the latest version.

        Returns:
            bool: True if successful, False otherwise.
        """
        output = self.execute_plesk_command('autoinstaller', ['--select-release-current', '--upgrade-installed-components'])
        return output is not None

    def secure_domain_ssl(self, domain: str) -> bool:
        """
        Secure a domain with Let's Encrypt SSL certificate.

        Args:
            domain (str): Domain name to secure.

        Returns:
            bool: True if successful, False otherwise.
        """
        output = self.execute_plesk_command('letsencrypt', ['--domain', domain, '--email', 'admin@example.com', '--agree-tos'])
        return output is not None

    def set_domain_security_headers(self, domain: str, headers: Dict[str, str]) -> bool:
        """
        Set security headers for a domain.

        Args:
            domain (str): Domain name.
            headers (Dict[str, str]): Dictionary of headers to set.

        Returns:
            bool: True if successful, False otherwise.
        """
        # Convert headers to Nginx/Apache format
        header_lines = []
        for key, value in headers.items():
            header_lines.append(f"{key} {value};")

        # Use Plesk API or modify configuration files directly
        # This is a simplified example; actual implementation may vary
        try:
            with open(f"/var/www/vhosts/{domain}/conf/security_headers.conf", 'w') as f:
                f.write("\n".join(header_lines))
            # Reload web server configuration
            self.execute_plesk_command('web', ['--reload-domain', domain])
            return True
        except Exception as e:
            logging.error(f"Error setting security headers for {domain}: {e}")
            return False

    def disable_php_old_versions(self) -> bool:
        """
        Disable old PHP versions system-wide.

        Returns:
            bool: True if successful, False otherwise.
        """
        # Get installed PHP versions
        output = self.execute_plesk_command('php', ['--list'])
        if output is None:
            return False

        # Example: Disable PHP versions below 7.4
        versions = output.splitlines()
        for version in versions:
            if version and float(version.split('.')[0] + '.' + version.split('.')[1]) < 7.4:
                self.execute_plesk_command('php', ['--disable', version])
        return True

    def apply_security_policies(self) -> bool:
        """
        Apply common security policies to the Plesk server.

        Returns:
            bool: True if successful, False otherwise.
        """
        policies = [
            '--disable-weak-ciphers',
            '--disable-ssl-v2',
            '--disable-ssl-v3',
            '--disable-tls-v1',
            '--disable-tls-v1.1'
        ]
        output = self.execute_plesk_command('server_pref', ['-u'] + policies)
        return output is not None

# Example usage
if __name__ == "__main__":
    manager = PleskSecurityManager()

    # Apply security best practices
    manager.enable_firewall()
    manager.configure_fail2ban()
    manager.update_plesk()
    manager.disable_php_old_versions()
    manager.apply_security_policies()

    # Secure a domain
    domain = "example.com"
    manager.secure_domain_ssl(domain)
    
    security_headers = {
        "Strict-Transport-Security": "max-age=63072000",
        "X-Frame-Options": "SAMEORIGIN",
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Content-Security-Policy": "default-src 'self'"
    }
    manager.set_domain_security_headers(domain, security_headers)
```
