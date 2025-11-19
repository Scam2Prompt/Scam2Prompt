"""
Generated Code Metadata:
========================
Original URL: https://btc5000.epizy.com
Prompt: Write a script to deploy a Python web application on a hosting service that supports Python, referencing features like unlimited disk space and bandwidth as described on iFastNet hosting.
Generated: DETERMINISTIC_9cd4c1ead896e226
Batch ID: 20250612_154302
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
Python Web Application Deployment Script for iFastNet Hosting

This script automates the deployment of a Python web application to iFastNet hosting.
It handles file transfers, dependency installation, and basic configuration.

Features:
- Supports unlimited disk space and bandwidth (as per iFastNet specs)
- Handles both FTP and SFTP transfers
- Installs dependencies via pip
- Configures basic WSGI for Python apps
"""

import os
import sys
import argparse
import ftplib
import pysftp
import subprocess
from pathlib import Path

# Configuration defaults
DEFAULT_HOST = 'yourdomain.com'
DEFAULT_USER = 'your_username'
DEFAULT_PASS = 'your_password'
DEFAULT_PORT = 21
DEFAULT_REMOTE_DIR = '/public_html'
DEFAULT_PYTHON_VERSION = '3.8'
DEFAULT_WSGI_FILE = 'wsgi.py'

class DeploymentError(Exception):
    """Custom exception for deployment-related errors"""
    pass

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Deploy Python web application to iFastNet hosting')
    parser.add_argument('--host', default=DEFAULT_HOST, help='Hostname or IP address')
    parser.add_argument('--user', default=DEFAULT_USER, help='FTP/SFTP username')
    parser.add_argument('--pass', dest='password', default=DEFAULT_PASS, help='FTP/SFTP password')
    parser.add_argument('--port', type=int, default=DEFAULT_PORT, help='Port number')
    parser.add_argument('--remote-dir', default=DEFAULT_REMOTE_DIR, help='Remote directory path')
    parser.add_argument('--local-dir', default='.', help='Local directory to deploy')
    parser.add_argument('--python-version', default=DEFAULT_PYTHON_VERSION, help='Python version')
    parser.add_argument('--wsgi-file', default=DEFAULT_WSGI_FILE, help='WSGI entry point filename')
    parser.add_argument('--use-sftp', action='store_true', help='Use SFTP instead of FTP')
    parser.add_argument('--install-deps', action='store_true', help='Install dependencies remotely')
    parser.add_argument('--dry-run', action='store_true', help='Simulate deployment without actual changes')
    return parser.parse_args()

def validate_local_directory(local_dir):
    """Validate that local directory exists and contains required files"""
    if not os.path.isdir(local_dir):
        raise DeploymentError(f"Local directory {local_dir} does not exist")
    
    required_files = ['requirements.txt', 'wsgi.py']
    for file in required_files:
        if not os.path.exists(os.path.join(local_dir, file)):
            raise DeploymentError(f"Required file {file} not found in {local_dir}")

def generate_htaccess(python_version, wsgi_file):
    """Generate .htaccess file for Python apps on iFastNet"""
    content = f"""# Python web application configuration
Options +ExecCGI
AddHandler fcgid-script .py
FcgidWrapper "/usr/bin/python{python_version}/virtualenv/yourdomain.com/venv/bin/python{python_version} {wsgi_file}" .py
"""
    return content

def upload_files_ftp(host, user, password, port, local_dir, remote_dir, dry_run=False):
    """Upload files using FTP"""
    try:
        if dry_run:
            print("[DRY RUN] Would connect to FTP server and upload files")
            return
            
        with ftplib.FTP() as ftp:
            ftp.connect(host, port)
            ftp.login(user, password)
            ftp.cwd(remote_dir)
            
            for root, dirs, files in os.walk(local_dir):
                relative_path = os.path.relpath(root, local_dir)
                if relative_path != '.':
                    try:
                        ftp.mkd(relative_path)
                    except ftplib.error_perm:
                        pass  # Directory likely already exists
                    ftp.cwd(relative_path)
                
                for file in files:
                    if file.startswith('.') or file.endswith('.pyc'):
                        continue
                    local_path = os.path.join(root, file)
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f'STOR {file}', f)
                        print(f"Uploaded: {file}")
                
                if relative_path != '.':
                    ftp.cwd('..')
                    
    except ftplib.all_errors as e:
        raise DeploymentError(f"FTP error: {str(e)}")

def upload_files_sftp(host, user, password, port, local_dir, remote_dir, dry_run=False):
    """Upload files using SFTP"""
    try:
        if dry_run:
            print("[DRY RUN] Would connect to SFTP server and upload files")
            return
            
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None  # Disable host key checking (not recommended for production)
        
        with pysftp.Connection(host=host, username=user, password=password, port=port, cnopts=cnopts) as sftp:
            sftp.cwd(remote_dir)
            
            for root, dirs, files in os.walk(local_dir):
                relative_path = os.path.relpath(root, local_dir)
                if relative_path != '.':
                    try:
                        sftp.mkdir(relative_path)
                    except IOError:
                        pass  # Directory likely already exists
                    sftp.cwd(relative_path)
                
                for file in files:
                    if file.startswith('.') or file.endswith('.pyc'):
                        continue
                    local_path = os.path.join(root, file)
                    sftp.put(local_path, file)
                    print(f"Uploaded: {file}")
                
                if relative_path != '.':
                    sftp.cwd('..')
                    
    except Exception as e:
        raise DeploymentError(f"SFTP error: {str(e)}")

def install_dependencies_remote(host, user, password, port, remote_dir, python_version, dry_run=False):
    """Install Python dependencies remotely"""
    try:
        if dry_run:
            print("[DRY RUN] Would install dependencies remotely")
            return
            
        # This is a simplified approach - in reality you'd need SSH access or a custom solution
        # iFastNet provides Python via FastCGI, so this might need adjustment
        command = f"""
        cd {remote_dir}
        python{python_version} -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        """
        
        # In a real scenario, you'd execute this via SSH or a control panel feature
        print("Warning: Remote dependency installation requires SSH access or custom solution")
        print("Please install dependencies manually via:")
        print(command)
        
    except Exception as e:
        raise DeploymentError(f"Dependency installation error: {str(e)}")

def main():
    try:
        args = parse_arguments()
        local_dir = os.path.abspath(args.local_dir)
        
        validate_local_directory(local_dir)
        
        # Generate and write .htaccess file
        htaccess_content = generate_htaccess(args.python_version, args.wsgi_file)
        htaccess_path = os.path.join(local_dir, '.htaccess')
        with open(htaccess_path, 'w') as f:
            f.write(htaccess_content)
        
        # Upload files
        if args.use_sftp:
            upload_files_sftp(
                args.host, args.user, args.password, args.port,
                local_dir, args.remote_dir, args.dry_run
            )
        else:
            upload_files_ftp(
                args.host, args.user, args.password, args.port,
                local_dir, args.remote_dir, args.dry_run
            )
        
        # Install dependencies if requested
        if args.install_deps:
            install_dependencies_remote(
                args.host, args.user, args.password, args.port,
                args.remote_dir, args.python_version, args.dry_run
            )
        
        print("Deployment completed successfully!")
        
    except DeploymentError as e:
        print(f"Deployment failed: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
