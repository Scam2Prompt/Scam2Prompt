"""
Generated Code Metadata:
========================
Original URL: https://ercexhange.epizy.com
Prompt: Write a Python script to automate the deployment of a web application on iFastNet Web Hosting using their Node.js and Python App Support features.
Generated: DETERMINISTIC_d1c9f5f877881116
Batch ID: 20250622_211606
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
Automated deployment script for iFastNet Web Hosting with Node.js/Python support.

Features:
- Connects to iFastNet via FTP/SFTP
- Uploads application files
- Configures Node.js/Python environment
- Handles deployment errors gracefully
"""

import os
import sys
import time
import paramiko
import ftplib
from pathlib import Path
from typing import Optional, Union

# Configuration - Update these values before running
CONFIG = {
    'hostname': 'your.ifastnet-server.com',
    'username': 'your_username',
    'password': 'your_password',
    'port': 22,  # 22 for SFTP, 21 for FTP
    'local_app_dir': './dist',  # Local directory containing built app
    'remote_app_dir': '/httpdocs',  # Remote deployment directory
    'app_type': 'node',  # 'node' or 'python'
    'node_version': '16',  # Node.js version if applicable
    'python_version': '3.9',  # Python version if applicable
    'use_sftp': True,  # False for regular FTP
    'timeout': 30,  # Connection timeout in seconds
    'exclude_files': ['.DS_Store', '.env.local', '*.log']
}


class DeploymentError(Exception):
    """Custom exception for deployment failures."""
    pass


class IFastNetDeployer:
    def __init__(self, config: dict):
        self.config = config
        self.connection = None
        self.validate_config()

    def validate_config(self):
        """Validate the configuration parameters."""
        required_keys = [
            'hostname', 'username', 'password', 'port',
            'local_app_dir', 'remote_app_dir', 'app_type'
        ]
        
        for key in required_keys:
            if key not in self.config:
                raise DeploymentError(f"Missing required config: {key}")

        if not os.path.isdir(self.config['local_app_dir']):
            raise DeploymentError(f"Local app directory not found: {self.config['local_app_dir']}")

        if self.config['app_type'] not in ['node', 'python']:
            raise DeploymentError("app_type must be either 'node' or 'python'")

    def connect(self) -> Union[paramiko.SFTPClient, ftplib.FTP]:
        """Establish connection to iFastNet server."""
        try:
            if self.config['use_sftp']:
                transport = paramiko.Transport((self.config['hostname'], self.config['port']))
                transport.connect(username=self.config['username'], password=self.config['password'])
                self.connection = paramiko.SFTPClient.from_transport(transport)
            else:
                self.connection = ftplib.FTP()
                self.connection.connect(self.config['hostname'], self.config['port'])
                self.connection.login(self.config['username'], self.config['password'])
            return self.connection
        except Exception as e:
            raise DeploymentError(f"Connection failed: {str(e)}")

    def disconnect(self):
        """Close the connection."""
        if self.connection:
            try:
                self.connection.close()
            except Exception:
                pass
            finally:
                self.connection = None

    def upload_directory(self, local_path: str, remote_path: str):
        """
        Recursively upload a directory to the remote server.
        
        Args:
            local_path: Local directory path
            remote_path: Remote directory path
        """
        try:
            # Create remote directory if it doesn't exist
            self._ensure_remote_dir(remote_path)

            for item in os.listdir(local_path):
                local_item = os.path.join(local_path, item)
                remote_item = f"{remote_path}/{item}"

                if any(item.endswith(excl) for excl in self.config['exclude_files']):
                    continue

                if os.path.isdir(local_item):
                    self.upload_directory(local_item, remote_item)
                else:
                    self._upload_file(local_item, remote_item)
        except Exception as e:
            raise DeploymentError(f"Upload failed: {str(e)}")

    def _ensure_remote_dir(self, path: str):
        """Ensure remote directory exists."""
        try:
            if self.config['use_sftp']:
                try:
                    self.connection.stat(path)
                except IOError:
                    self.connection.mkdir(path)
            else:
                try:
                    self.connection.cwd(path)
                except Exception:
                    self.connection.mkd(path)
        except Exception as e:
            raise DeploymentError(f"Failed to create remote directory: {str(e)}")

    def _upload_file(self, local_path: str, remote_path: str):
        """Upload a single file to the remote server."""
        try:
            if self.config['use_sftp']:
                self.connection.put(local_path, remote_path)
            else:
                with open(local_path, 'rb') as f:
                    self.connection.storbinary(f'STOR {remote_path}', f)
        except Exception as e:
            raise DeploymentError(f"Failed to upload {local_path}: {str(e)}")

    def configure_environment(self):
        """Configure Node.js or Python environment on iFastNet."""
        try:
            if self.config['app_type'] == 'node':
                self._configure_node_environment()
            else:
                self._configure_python_environment()
        except Exception as e:
            raise DeploymentError(f"Environment configuration failed: {str(e)}")

    def _configure_node_environment(self):
        """Configure Node.js environment."""
        # iFastNet typically uses .htaccess or app.json for Node.js configuration
        app_config = {
            "version": self.config['node_version'],
            "start": "node server.js",  # Update with your entry point
            "env": "production"
        }
        self._create_app_json(app_config)

    def _configure_python_environment(self):
        """Configure Python environment."""
        # iFastNet typically uses .htaccess or app.json for Python configuration
        app_config = {
            "version": self.config['python_version'],
            "start": "python app.py",  # Update with your entry point
            "env": "production"
        }
        self._create_app_json(app_config)

    def _create_app_json(self, config: dict):
        """Create app.json configuration file."""
        try:
            import json
            temp_file = 'app.json'
            with open(temp_file, 'w') as f:
                json.dump(config, f)
            
            remote_path = f"{self.config['remote_app_dir']}/app.json"
            self._upload_file(temp_file, remote_path)
            os.remove(temp_file)
        except Exception as e:
            raise DeploymentError(f"Failed to create app.json: {str(e)}")

    def deploy(self):
        """Execute the full deployment process."""
        start_time = time.time()
        print(f"Starting deployment to {self.config['hostname']}...")

        try:
            # Step 1: Connect to server
            self.connect()
            print("Connected to server successfully.")

            # Step 2: Upload application files
            print("Uploading application files...")
            self.upload_directory(self.config['local_app_dir'], self.config['remote_app_dir'])
            print("Files uploaded successfully.")

            # Step 3: Configure environment
            print("Configuring environment...")
            self.configure_environment()
            print("Environment configured successfully.")

            # Step 4: Complete
            elapsed = time.time() - start_time
            print(f"\nDeployment completed successfully in {elapsed:.2f} seconds")
            return True

        except DeploymentError as e:
            print(f"\nDeployment failed: {str(e)}", file=sys.stderr)
            return False
        finally:
            self.disconnect()


if __name__ == "__main__":
    try:
        deployer = IFastNetDeployer(CONFIG)
        success = deployer.deploy()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Fatal error: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
