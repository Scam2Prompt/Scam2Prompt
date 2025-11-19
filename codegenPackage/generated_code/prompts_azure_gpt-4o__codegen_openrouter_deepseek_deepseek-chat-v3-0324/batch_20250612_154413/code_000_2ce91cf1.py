"""
Generated Code Metadata:
========================
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, referencing features like unlimited disk space and bandwidth as offered by iFastNet hosting.
Generated: DETERMINISTIC_2ce91cf1c0db8ef9
Batch ID: 20250612_154413
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
Web Application Deployment Script for iFastNet Hosting

This script automates the deployment of a Python web application to a hosting service
that supports Python (like iFastNet). It handles file transfers, dependency installation,
and basic configuration.

Features:
- Supports unlimited disk space and bandwidth (as offered by iFastNet)
- Handles both FTP and SFTP transfers
- Installs Python dependencies
- Basic error handling and logging
"""

import os
import sys
import ftplib
import paramiko
import logging
from getpass import getpass
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('deployment.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DeploymentError(Exception):
    """Custom exception for deployment-related errors"""
    pass

class WebAppDeployer:
    def __init__(self, config):
        """
        Initialize the deployer with configuration settings
        
        Args:
            config (dict): Configuration dictionary containing:
                - host: Server hostname
                - port: Server port (default: 21 for FTP, 22 for SFTP)
                - username: Server username
                - password: Server password (optional, will prompt if not provided)
                - protocol: 'ftp' or 'sftp'
                - local_dir: Local directory containing app files
                - remote_dir: Remote directory to deploy to
                - python_path: Path to Python executable on server (optional)
                - requirements_file: Path to requirements.txt (optional)
        """
        self.config = config
        self.validate_config()
        
        if not self.config.get('password'):
            self.config['password'] = getpass("Enter server password: ")
        
        if not self.config.get('port'):
            self.config['port'] = 22 if self.config['protocol'] == 'sftp' else 21

    def validate_config(self):
        """Validate the configuration dictionary"""
        required_fields = ['host', 'username', 'protocol', 'local_dir', 'remote_dir']
        for field in required_fields:
            if field not in self.config:
                raise DeploymentError(f"Missing required configuration field: {field}")
                
        if self.config['protocol'] not in ['ftp', 'sftp']:
            raise DeploymentError("Protocol must be either 'ftp' or 'sftp'")
            
        if not os.path.isdir(self.config['local_dir']):
            raise DeploymentError(f"Local directory does not exist: {self.config['local_dir']}")

    def deploy(self):
        """Main deployment method"""
        try:
            logger.info("Starting deployment process")
            
            # Connect to server
            if self.config['protocol'] == 'ftp':
                self.ftp_connect()
                self.ftp_upload()
                self.ftp_disconnect()
            else:
                self.sftp_connect()
                self.sftp_upload()
                if self.config.get('requirements_file'):
                    self.install_dependencies()
                self.sftp_disconnect()
                
            logger.info("Deployment completed successfully")
            
        except Exception as e:
            logger.error(f"Deployment failed: {str(e)}")
            raise DeploymentError(str(e)) from e

    def ftp_connect(self):
        """Establish FTP connection"""
        try:
            logger.info(f"Connecting to FTP server at {self.config['host']}")
            self.ftp = ftplib.FTP()
            self.ftp.connect(self.config['host'], self.config['port'])
            self.ftp.login(self.config['username'], self.config['password'])
            logger.info("FTP connection established")
        except ftplib.all_errors as e:
            raise DeploymentError(f"FTP connection failed: {str(e)}")

    def ftp_upload(self):
        """Upload files via FTP"""
        try:
            local_dir = Path(self.config['local_dir'])
            remote_dir = self.config['remote_dir']
            
            # Create remote directory if it doesn't exist
            try:
                self.ftp.cwd(remote_dir)
            except ftplib.error_perm:
                self.ftp.mkd(remote_dir)
                self.ftp.cwd(remote_dir)
            
            # Upload files recursively
            for item in local_dir.rglob('*'):
                if item.is_dir():
                    try:
                        self.ftp.mkd(item.relative_to(local_dir).as_posix())
                    except ftplib.error_perm:
                        pass  # Directory likely already exists
                else:
                    rel_path = item.relative_to(local_dir).as_posix()
                    with open(item, 'rb') as f:
                        self.ftp.storbinary(f"STOR {rel_path}", f)
                    logger.info(f"Uploaded: {rel_path}")
                    
        except ftplib.all_errors as e:
            raise DeploymentError(f"FTP upload failed: {str(e)}")

    def ftp_disconnect(self):
        """Close FTP connection"""
        try:
            self.ftp.quit()
            logger.info("FTP connection closed")
        except ftplib.all_errors as e:
            logger.warning(f"Error closing FTP connection: {str(e)}")

    def sftp_connect(self):
        """Establish SFTP connection"""
        try:
            logger.info(f"Connecting to SFTP server at {self.config['host']}")
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(
                hostname=self.config['host'],
                port=self.config['port'],
                username=self.config['username'],
                password=self.config['password']
            )
            self.sftp = self.ssh.open_sftp()
            logger.info("SFTP connection established")
        except paramiko.SSHException as e:
            raise DeploymentError(f"SFTP connection failed: {str(e)}")

    def sftp_upload(self):
        """Upload files via SFTP"""
        try:
            local_dir = Path(self.config['local_dir'])
            remote_dir = self.config['remote_dir']
            
            # Create remote directory if it doesn't exist
            try:
                self.sftp.chdir(remote_dir)
            except IOError:
                self.sftp.mkdir(remote_dir)
                self.sftp.chdir(remote_dir)
            
            # Upload files recursively
            for item in local_dir.rglob('*'):
                rel_path = item.relative_to(local_dir).as_posix()
                if item.is_dir():
                    try:
                        self.sftp.mkdir(rel_path)
                    except IOError:
                        pass  # Directory likely already exists
                else:
                    self.sftp.put(str(item), rel_path)
                    logger.info(f"Uploaded: {rel_path}")
                    
        except paramiko.SSHException as e:
            raise DeploymentError(f"SFTP upload failed: {str(e)}")

    def install_dependencies(self):
        """Install Python dependencies on remote server"""
        try:
            if not self.config.get('python_path'):
                self.config['python_path'] = 'python3'
                
            requirements_path = os.path.join(
                self.config['remote_dir'],
                os.path.basename(self.config['requirements_file'])
            )
            
            cmd = f"{self.config['python_path']} -m pip install -r {requirements_path}"
            
            logger.info(f"Installing dependencies: {cmd}")
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            
            exit_status = stdout.channel.recv_exit_status()
            if exit_status != 0:
                error = stderr.read().decode().strip()
                raise DeploymentError(f"Dependency installation failed: {error}")
                
            logger.info("Dependencies installed successfully")
            
        except paramiko.SSHException as e:
            raise DeploymentError(f"Remote command execution failed: {str(e)}")

    def sftp_disconnect(self):
        """Close SFTP connection"""
        try:
            self.sftp.close()
            self.ssh.close()
            logger.info("SFTP connection closed")
        except paramiko.SSHException as e:
            logger.warning(f"Error closing SFTP connection: {str(e)}")

def main():
    """Main function for command-line execution"""
    try:
        # Example configuration - modify as needed
        config = {
            'host': 'your-ifastnet-server.com',
            'username': 'your_username',
            'protocol': 'sftp',  # or 'ftp'
            'local_dir': './my_web_app',
            'remote_dir': '/public_html',
            'requirements_file': './requirements.txt',
            # 'python_path': '/path/to/python'  # Uncomment if needed
        }
        
        deployer = WebAppDeployer(config)
        deployer.deploy()
        
    except DeploymentError as e:
        logger.error(f"Deployment aborted: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Deployment cancelled by user")
        sys.exit(1)

if __name__ == '__main__':
    main()
```
