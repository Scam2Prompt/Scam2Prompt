"""
Generated Code Metadata:
========================
Original URL: https://kinglol.42web.io
Prompt: Write a Python script to deploy a web application using a hosting service that supports unlimited disk space, unlimited bandwidth, and multiple versions of PHP, as described on iFastNet's hosting page.
Generated: DETERMINISTIC_3644341d1527c5dc
Batch ID: 20250612_151446
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
Deploy a web application to iFastNet hosting service.

This script automates the deployment of a web application to iFastNet hosting,
which supports unlimited disk space, unlimited bandwidth, and multiple PHP versions.

Requirements:
- Python 3.6+
- Paramiko for SFTP/SSH (pip install paramiko)
- Requests for API calls (pip install requests)
"""

import os
import sys
import argparse
import paramiko
import requests
from pathlib import Path
from getpass import getpass
from typing import Optional, Dict, List

class DeploymentError(Exception):
    """Custom exception for deployment-related errors."""
    pass

class iFastNetDeployer:
    def __init__(self, hostname: str, username: str, password: str, php_version: str = "8.1"):
        """
        Initialize the deployer with connection details.
        
        Args:
            hostname: The server hostname or IP
            username: FTP/SFTP username
            password: FTP/SFTP password
            php_version: PHP version to use (default: 8.1)
        """
        self.hostname = hostname
        self.username = username
        self.password = password
        self.php_version = php_version
        self.ssh_client = None
        self.sftp_client = None

    def connect(self) -> None:
        """Establish SFTP connection to the server."""
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(
                self.hostname,
                username=self.username,
                password=self.password
            )
            self.sftp_client = self.ssh_client.open_sftp()
        except paramiko.AuthenticationException:
            raise DeploymentError("Authentication failed, please verify your credentials")
        except paramiko.SSHException as e:
            raise DeploymentError(f"SSH connection failed: {str(e)}")
        except Exception as e:
            raise DeploymentError(f"Connection error: {str(e)}")

    def deploy(self, local_path: str, remote_path: str = "/") -> None:
        """
        Deploy application files to the server.
        
        Args:
            local_path: Local directory containing files to deploy
            remote_path: Remote directory to deploy to (default: root)
        """
        if not self.sftp_client:
            self.connect()

        local_path = Path(local_path)
        if not local_path.exists():
            raise DeploymentError(f"Local path {local_path} does not exist")

        try:
            self._create_remote_directory(remote_path)
            self._upload_files(local_path, remote_path)
            self._set_php_version()
            print("Deployment completed successfully!")
        except Exception as e:
            raise DeploymentError(f"Deployment failed: {str(e)}")
        finally:
            self.disconnect()

    def _create_remote_directory(self, remote_path: str) -> None:
        """Create remote directory structure if it doesn't exist."""
        try:
            self.sftp_client.chdir(remote_path)
        except IOError:
            try:
                self.sftp_client.mkdir(remote_path)
                self.sftp_client.chdir(remote_path)
            except Exception as e:
                raise DeploymentError(f"Failed to create remote directory: {str(e)}")

    def _upload_files(self, local_path: Path, remote_path: str) -> None:
        """Recursively upload files from local to remote."""
        for item in local_path.iterdir():
            remote_item = f"{remote_path}/{item.name}"
            
            if item.is_dir():
                self._create_remote_directory(remote_item)
                self._upload_files(item, remote_item)
            else:
                try:
                    print(f"Uploading {item} to {remote_item}")
                    self.sftp_client.put(str(item), remote_item)
                except Exception as e:
                    raise DeploymentError(f"Failed to upload {item}: {str(e)}")

    def _set_php_version(self) -> None:
        """Set PHP version via .htaccess file."""
        htaccess_content = f"""
        # Set PHP version
        AddHandler application/x-httpd-php{self.php_version} .php
        """
        
        try:
            with self.sftp_client.file(".htaccess", "w") as f:
                f.write(htaccess_content.strip())
            print(f"PHP version set to {self.php_version} via .htaccess")
        except Exception as e:
            raise DeploymentError(f"Failed to set PHP version: {str(e)}")

    def disconnect(self) -> None:
        """Close connections."""
        if self.sftp_client:
            self.sftp_client.close()
        if self.ssh_client:
            self.ssh_client.close()

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Deploy web application to iFastNet hosting")
    parser.add_argument("local_path", help="Path to local directory containing files to deploy")
    parser.add_argument("--hostname", required=True, help="Server hostname or IP")
    parser.add_argument("--username", required=True, help="FTP/SFTP username")
    parser.add_argument("--remote-path", default="/", help="Remote deployment path (default: /)")
    parser.add_argument("--php-version", default="8.1", 
                       choices=["5.6", "7.0", "7.1", "7.2", "7.3", "7.4", "8.0", "8.1", "8.2"],
                       help="PHP version to use (default: 8.1)")
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        
        # Get password securely
        password = getpass("Enter your FTP/SFTP password: ")
        
        deployer = iFastNetDeployer(
            hostname=args.hostname,
            username=args.username,
            password=password,
            php_version=args.php_version
        )
        
        deployer.deploy(
            local_path=args.local_path,
            remote_path=args.remote_path
        )
        
    except DeploymentError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDeployment cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
