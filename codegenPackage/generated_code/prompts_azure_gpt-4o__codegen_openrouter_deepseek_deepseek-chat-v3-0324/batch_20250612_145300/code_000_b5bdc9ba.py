"""
Generated Code Metadata:
========================
Original URL: https://siemensgamesare.great-site.net
Prompt: Write a Python script to deploy a web application on a hosting platform that supports Python App Hosting, as described on iFastNet's web hosting service.
Generated: DETERMINISTIC_b5bdc9ba7f3e8bd4
Batch ID: 20250612_145300
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
Python script to deploy a web application on a hosting platform that supports Python App Hosting.
This script assumes the hosting platform is similar to iFastNet's web hosting service.
"""

import os
import shutil
import ftplib
import argparse
import sys
from pathlib import Path

class DeploymentError(Exception):
    """Custom exception for deployment-related errors."""
    pass

def validate_directory(directory):
    """Validate that the directory exists and contains necessary files."""
    required_files = ['app.py', 'requirements.txt']
    directory = Path(directory)
    
    if not directory.exists():
        raise DeploymentError(f"Directory {directory} does not exist")
    
    for file in required_files:
        if not (directory / file).exists():
            raise DeploymentError(f"Required file {file} not found in {directory}")
    
    return directory

def install_dependencies(directory):
    """Install Python dependencies from requirements.txt."""
    requirements_file = directory / 'requirements.txt'
    if not requirements_file.exists():
        print("No requirements.txt found. Skipping dependency installation.")
        return
    
    print("Installing dependencies...")
    exit_code = os.system(f"pip install -r {requirements_file}")
    if exit_code != 0:
        raise DeploymentError("Failed to install dependencies")

def create_deployment_package(source_dir, output_dir):
    """Create a deployment package by copying necessary files."""
    print("Creating deployment package...")
    try:
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)
        
        # Copy all files except those in exclude list
        exclude = ['__pycache__', '.git', '.env', '*.pyc']
        for item in source_dir.iterdir():
            if any(item.match(pattern) for pattern in exclude):
                continue
            if item.is_dir():
                shutil.copytree(item, output_dir / item.name)
            else:
                shutil.copy2(item, output_dir / item.name)
        
        return output_dir
    except Exception as e:
        raise DeploymentError(f"Failed to create deployment package: {str(e)}")

def deploy_via_ftp(local_dir, host, username, password, remote_dir='/'):
    """Deploy files to remote server via FTP."""
    print(f"Connecting to {host}...")
    try:
        with ftplib.FTP(host, username, password) as ftp:
            print("Connected successfully")
            
            # Change to remote directory
            try:
                ftp.cwd(remote_dir)
            except ftplib.error_perm:
                print(f"Remote directory {remote_dir} doesn't exist, creating...")
                ftp.mkd(remote_dir)
                ftp.cwd(remote_dir)
            
            # Upload files recursively
            for root, dirs, files in os.walk(local_dir):
                relative_path = os.path.relpath(root, local_dir)
                if relative_path == '.':
                    relative_path = ''
                
                # Create directories first
                for dirname in dirs:
                    remote_path = os.path.join(relative_path, dirname)
                    try:
                        ftp.mkd(remote_path)
                    except ftplib.error_perm:
                        pass  # Directory might already exist
                
                # Upload files
                for filename in files:
                    local_path = os.path.join(root, filename)
                    remote_path = os.path.join(relative_path, filename)
                    
                    with open(local_path, 'rb') as f:
                        print(f"Uploading {remote_path}...")
                        ftp.storbinary(f"STOR {remote_path}", f)
            
            print("Deployment completed successfully")
    except ftplib.all_errors as e:
        raise DeploymentError(f"FTP error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Deploy Python web application')
    parser.add_argument('source_dir', help='Source directory containing the application')
    parser.add_argument('--host', required=True, help='FTP host address')
    parser.add_argument('--username', required=True, help='FTP username')
    parser.add_argument('--password', required=True, help='FTP password')
    parser.add_argument('--remote-dir', default='/', help='Remote directory to deploy to')
    parser.add_argument('--build-dir', default='./build', help='Local build directory')
    
    args = parser.parse_args()
    
    try:
        # Validate and prepare source directory
        source_dir = validate_directory(args.source_dir)
        
        # Install dependencies
        install_dependencies(source_dir)
        
        # Create deployment package
        build_dir = Path(args.build_dir)
        deploy_dir = create_deployment_package(source_dir, build_dir)
        
        # Deploy via FTP
        deploy_via_ftp(
            deploy_dir,
            args.host,
            args.username,
            args.password,
            args.remote_dir
        )
        
        print("Deployment completed successfully!")
        return 0
    except DeploymentError as e:
        print(f"Deployment failed: {str(e)}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
```
