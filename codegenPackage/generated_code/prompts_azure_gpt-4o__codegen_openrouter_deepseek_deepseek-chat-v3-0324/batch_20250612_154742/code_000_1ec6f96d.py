"""
Generated Code Metadata:
========================
Original URL: https://datmaui.liveblog365.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python and provides unlimited bandwidth, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_1ec6f96d8fa1efb5
Batch ID: 20250612_154742
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
Deploy a Python web application to iFastNet hosting platform.

This script automates the deployment process by:
1. Compressing the application files
2. Uploading via FTP
3. Restarting the application if needed

Requirements:
- Python 3.6+
- `ftplib` (standard library)
- `os`, `sys`, `shutil`, `tempfile` (standard libraries)
"""

import os
import sys
import ftplib
import shutil
import tempfile
from pathlib import Path

# Configuration - Update these values
CONFIG = {
    'ftp_host': 'your-ftp-host.ifastnet.com',
    'ftp_user': 'your_username',
    'ftp_pass': 'your_password',
    'remote_dir': '/httpdocs',  # Typically /httpdocs or /public_html
    'app_dir': 'my_app',  # Local directory containing your app
    'exclude_dirs': ['__pycache__', 'venv', '.git'],
    'exclude_files': ['.env', '*.pyc']
}

def validate_config():
    """Validate configuration and required directories."""
    if not os.path.isdir(CONFIG['app_dir']):
        raise FileNotFoundError(f"Application directory {CONFIG['app_dir']} not found")
    
    if not all(isinstance(v, str) for v in CONFIG.values()):
        raise ValueError("All config values must be strings")

def create_temp_archive():
    """Create a temporary zip archive of the application files."""
    temp_dir = tempfile.mkdtemp()
    archive_path = os.path.join(temp_dir, 'app_deploy.zip')
    
    def should_exclude(path):
        path = Path(path)
        if any(part in CONFIG['exclude_dirs'] for part in path.parts):
            return True
        if any(path.match(pattern) for pattern in CONFIG['exclude_files']):
            return True
        return False
    
    with shutil.ZipFile(archive_path, 'w', shutil.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(CONFIG['app_dir']):
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
            for file in files:
                file_path = os.path.join(root, file)
                if not should_exclude(file_path):
                    arcname = os.path.relpath(file_path, CONFIG['app_dir'])
                    zipf.write(file_path, arcname)
    
    return archive_path, temp_dir

def upload_via_ftp(archive_path):
    """Upload the archive to the hosting server via FTP."""
    try:
        with ftplib.FTP(CONFIG['ftp_host'], CONFIG['ftp_user'], CONFIG['ftp_pass']) as ftp:
            ftp.cwd(CONFIG['remote_dir'])
            
            with open(archive_path, 'rb') as f:
                ftp.storbinary(f'STOR {os.path.basename(archive_path)}', f)
            
            # Check if unzip command is available (common on iFastNet)
            try:
                ftp.sendcmd('SITE UNZIP')
                ftp.sendcmd(f'SITE UNZIP {os.path.basename(archive_path)}')
                ftp.delete(os.path.basename(archive_path))
            except ftplib.error_perm:
                print("Warning: Automatic unzip not available. Please extract manually.")
            
            print("Upload completed successfully.")
    except ftplib.all_errors as e:
        raise RuntimeError(f"FTP error: {str(e)}")

def cleanup(temp_dir, archive_path):
    """Clean up temporary files and directories."""
    try:
        if os.path.exists(archive_path):
            os.remove(archive_path)
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
    except OSError as e:
        print(f"Warning: Cleanup failed - {str(e)}")

def main():
    try:
        validate_config()
        archive_path, temp_dir = create_temp_archive()
        upload_via_ftp(archive_path)
    except Exception as e:
        print(f"Deployment failed: {str(e)}", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'archive_path' in locals() and 'temp_dir' in locals():
            cleanup(temp_dir, archive_path)

if __name__ == '__main__':
    main()
```
