"""
Generated Code Metadata:
========================
Original URL: https://safarait.com
Prompt: Generate a code snippet for setting up a VPS hosting environment using the services provided by Safara IT.
Generated: DETERMINISTIC_84e2d0912fb901b6
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import paramiko
from typing import Optional, Dict

class VPSHostingSetup:
    """
    A class to set up a VPS hosting environment using Safara IT services.
    Handles SSH connection, package installation, and basic configuration.
    """

    def __init__(self, host: str, username: str, password: str, port: int = 22):
        """
        Initialize the VPS setup with connection details.
        
        Args:
            host (str): VPS hostname or IP address
            username (str): SSH username
            password (str): SSH password
            port (int, optional): SSH port. Defaults to 22.
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ssh_client = None

    def connect(self) -> bool:
        """
        Establish SSH connection to the VPS.
        
        Returns:
            bool: True if connection succeeded, False otherwise
        """
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(
                self.host,
                port=self.port,
                username=self.username,
                password=self.password
            )
            return True
        except Exception as e:
            print(f"SSH connection failed: {str(e)}")
            return False

    def execute_command(self, command: str) -> Optional[Dict[str, str]]:
        """
        Execute a command on the remote VPS via SSH.
        
        Args:
            command (str): Command to execute
            
        Returns:
            Optional[Dict[str, str]]: Dictionary with stdout, stderr, and return code,
                                     or None if execution failed
        """
        if not self.ssh_client:
            print("SSH connection not established")
            return None

        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            return {
                'stdout': stdout.read().decode().strip(),
                'stderr': stderr.read().decode().strip(),
                'returncode': stdout.channel.recv_exit_status()
            }
        except Exception as e:
            print(f"Command execution failed: {str(e)}")
            return None

    def setup_basic_environment(self) -> bool:
        """
        Set up basic hosting environment (update packages, install common tools).
        
        Returns:
            bool: True if setup succeeded, False otherwise
        """
        commands = [
            'sudo apt-get update -y',
            'sudo apt-get upgrade -y',
            'sudo apt-get install -y nginx mysql-server php-fpm php-mysql ufw',
            'sudo ufw allow "Nginx Full"',
            'sudo ufw enable',
            'sudo systemctl enable nginx',
            'sudo systemctl start nginx'
        ]

        for cmd in commands:
            result = self.execute_command(cmd)
            if not result or result['returncode'] != 0:
                print(f"Command failed: {cmd}")
                if result:
                    print(f"Error: {result['stderr']}")
                return False
        return True

    def configure_website(self, domain: str) -> bool:
        """
        Configure a basic website with Nginx.
        
        Args:
            domain (str): Domain name to configure
            
        Returns:
            bool: True if configuration succeeded, False otherwise
        """
        nginx_config = f"""
        server {{
            listen 80;
            server_name {domain};
            root /var/www/{domain};
            index index.html index.php;

            location / {{
                try_files $uri $uri/ =404;
            }}

            location ~ \.php$ {{
                include snippets/fastcgi-php.conf;
                fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
            }}
        }}
        """

        commands = [
            f'sudo mkdir -p /var/www/{domain}',
            f'sudo chown -R $USER:$USER /var/www/{domain}',
            f'sudo chmod -R 755 /var/www/{domain}',
            f'echo "<html><body><h1>{domain} is working!</h1></body></html>" | sudo tee /var/www/{domain}/index.html',
            f'echo "{nginx_config}" | sudo tee /etc/nginx/sites-available/{domain}',
            f'sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/',
            'sudo nginx -t',
            'sudo systemctl restart nginx'
        ]

        for cmd in commands:
            result = self.execute_command(cmd)
            if not result or result['returncode'] != 0:
                print(f"Command failed: {cmd}")
                if result:
                    print(f"Error: {result['stderr']}")
                return False
        return True

    def close(self):
        """Close the SSH connection."""
        if self.ssh_client:
            self.ssh_client.close()

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Example usage
if __name__ == "__main__":
    # Replace with your actual Safara IT VPS credentials
    vps = VPSHostingSetup(
        host="your-vps-ip",
        username="root",
        password="your-password"
    )

    try:
        if vps.connect():
            print("Connected to VPS")
            if vps.setup_basic_environment():
                print("Basic environment setup complete")
                if vps.configure_website("example.com"):
                    print("Website configuration complete")
    finally:
        vps.close()
```
