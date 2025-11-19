"""
Generated Code Metadata:
========================
Original URL: https://raydium.rf.gd
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python apps, referencing features like unlimited bandwidth and modern cPanel.
Generated: DETERMINISTIC_c41db80872db0d18
Batch ID: 20250612_155028
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
Python script to deploy a web application to a hosting service with Python support.
Features include handling unlimited bandwidth and modern cPanel integration.
"""

import os
import sys
import subprocess
import shutil
import argparse
from pathlib import Path
import ftplib
import getpass
import json
from typing import Optional, Dict, Any

# Configuration constants
CONFIG_FILE = "deploy_config.json"
DEFAULT_IGNORE = [".git", "__pycache__", "venv", "env", "*.pyc", "*.pyo", "*.pyd"]
DEPLOY_LOG = "deploy.log"

class DeploymentError(Exception):
    """Custom exception for deployment-related errors."""
    pass

def load_config() -> Dict[str, Any]:
    """Load deployment configuration from JSON file."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        
        # Validate required fields
        required_fields = ['host', 'username', 'remote_dir']
        for field in required_fields:
            if field not in config:
                raise DeploymentError(f"Missing required field in config: {field}")
        
        return config
    except FileNotFoundError:
        raise DeploymentError(f"Configuration file {CONFIG_FILE} not found")
    except json.JSONDecodeError:
        raise DeploymentError(f"Invalid JSON in configuration file {CONFIG_FILE}")

def get_password() -> str:
    """Securely get FTP password from user input."""
    return getpass.getpass("Enter FTP password: ")

def create_ignore_filter(ignore_patterns: list) -> callable:
    """Create a function to filter files based on ignore patterns."""
    def ignore(path: str) -> bool:
        path = Path(path)
        for pattern in ignore_patterns:
            if pattern.startswith('*'):
                if path.name.endswith(pattern[1:]):
                    return True
            elif path.name == pattern:
                return True
        return False
    return ignore

def prepare_deployment(local_dir: str, ignore_patterns: list) -> str:
    """Prepare files for deployment by creating a temporary directory with filtered files."""
    temp_dir = os.path.join(os.path.dirname(local_dir), "deploy_temp")
    
    try:
        # Create temporary directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        
        ignore_func = create_ignore_filter(ignore_patterns)
        
        # Copy files to temporary directory, ignoring specified patterns
        for root, dirs, files in os.walk(local_dir):
            rel_path = os.path.relpath(root, local_dir)
            dest_dir = os.path.join(temp_dir, rel_path)
            
            # Skip ignored directories
            if ignore_func(rel_path):
                continue
                
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                
            for file in files:
                src_file = os.path.join(root, file)
                if not ignore_func(file):
                    shutil.copy2(src_file, os.path.join(dest_dir, file))
        
        return temp_dir
    except OSError as e:
        raise DeploymentError(f"Error preparing deployment: {str(e)}")

def deploy_via_ftp(local_dir: str, config: Dict[str, Any], password: str) -> None:
    """Deploy files to remote server via FTP."""
    try:
        with ftplib.FTP(config['host']) as ftp:
            # Login to FTP server
            ftp.login(config['username'], password)
            
            # Change to remote directory
            try:
                ftp.cwd(config['remote_dir'])
            except ftplib.error_perm:
                raise DeploymentError(f"Remote directory {config['remote_dir']} not found or inaccessible")
            
            # Upload files recursively
            for root, dirs, files in os.walk(local_dir):
                rel_path = os.path.relpath(root, local_dir)
                if rel_path == '.':
                    rel_path = ''
                
                # Create directories on remote
                for dir_name in dirs:
                    remote_dir = os.path.join(rel_path, dir_name).replace('\\', '/')
                    try:
                        ftp.mkd(remote_dir)
                    except ftplib.error_perm:
                        # Directory might already exist
                        pass
                
                # Upload files
                for file_name in files:
                    local_file = os.path.join(root, file_name)
                    remote_file = os.path.join(rel_path, file_name).replace('\\', '/')
                    
                    with open(local_file, 'rb') as f:
                        ftp.storbinary(f"STOR {remote_file}", f)
            
            # Log success
            with open(DEPLOY_LOG, 'a') as log:
                log.write(f"Successfully deployed to {config['host']}\n")
                
    except ftplib.all_errors as e:
        raise DeploymentError(f"FTP error: {str(e)}")

def cleanup(temp_dir: str) -> None:
    """Clean up temporary files."""
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
    except OSError as e:
        print(f"Warning: Could not clean up temporary directory: {str(e)}")

def main():
    """Main deployment function."""
    parser = argparse.ArgumentParser(description="Deploy web application to hosting service")
    parser.add_argument("local_dir", help="Local directory containing the application")
    parser.add_argument("--ignore", nargs='+', default=DEFAULT_IGNORE, 
                       help="File patterns to ignore during deployment")
    args = parser.parse_args()
    
    try:
        # Validate local directory
        if not os.path.isdir(args.local_dir):
            raise DeploymentError(f"Local directory {args.local_dir} does not exist")
        
        # Load configuration
        config = load_config()
        
        # Get password securely
        password = get_password()
        
        # Prepare files for deployment
        temp_dir = prepare_deployment(args.local_dir, args.ignore)
        
        # Deploy via FTP
        deploy_via_ftp(temp_dir, config, password)
        
        print("Deployment completed successfully!")
        
    except DeploymentError as e:
        print(f"Deployment failed: {str(e)}", file=sys.stderr)
        sys.exit(1)
    finally:
        # Clean up temporary files
        if 'temp_dir' in locals():
            cleanup(temp_dir)

if __name__ == "__main__":
    main()
```
