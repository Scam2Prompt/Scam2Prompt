"""
Generated Code Metadata:
========================
Original URL: https://arastrum.com
Prompt: Provide code examples for uploading website files to a hosting platform, specifically Hostinger, based on the instructions from Arastrum.
Generated: DETERMINISTIC_4dab083d01a43332
Batch ID: 20250612_145933
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
from pathlib import Path
from typing import Optional, List

class HostingerUploader:
    """
    A utility class to upload website files to Hostinger hosting platform via SFTP.
    """
    
    def __init__(self, host: str, username: str, password: str, port: int = 22):
        """
        Initialize the uploader with Hostinger SFTP credentials.
        
        Args:
            host: Hostinger SFTP host address
            username: Hostinger SFTP username
            password: Hostinger SFTP password
            port: SFTP port (default: 22)
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ssh_client = None
        self.sftp_client = None
        
    def connect(self) -> bool:
        """
        Establish SFTP connection to Hostinger.
        
        Returns:
            bool: True if connection succeeded, False otherwise
        """
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(
                hostname=self.host,
                username=self.username,
                password=self.password,
                port=self.port
            )
            self.sftp_client = self.ssh_client.open_sftp()
            return True
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            return False
            
    def disconnect(self):
        """Close the SFTP connection."""
        if self.sftp_client:
            self.sftp_client.close()
        if self.ssh_client:
            self.ssh_client.close()
            
    def upload_file(self, local_path: str, remote_path: str) -> bool:
        """
        Upload a single file to Hostinger.
        
        Args:
            local_path: Path to local file
            remote_path: Destination path on Hostinger
            
        Returns:
            bool: True if upload succeeded, False otherwise
        """
        try:
            self.sftp_client.put(local_path, remote_path)
            return True
        except Exception as e:
            print(f"Failed to upload {local_path}: {str(e)}")
            return False
            
    def upload_directory(self, local_dir: str, remote_dir: str, exclude: Optional[List[str]] = None) -> bool:
        """
        Recursively upload a directory to Hostinger.
        
        Args:
            local_dir: Path to local directory
            remote_dir: Destination directory on Hostinger
            exclude: List of file patterns to exclude
            
        Returns:
            bool: True if all files uploaded successfully, False otherwise
        """
        if exclude is None:
            exclude = []
            
        try:
            # Create remote directory if it doesn't exist
            try:
                self.sftp_client.stat(remote_dir)
            except IOError:
                self.sftp_client.mkdir(remote_dir)
                
            success = True
            for item in os.listdir(local_dir):
                local_path = os.path.join(local_dir, item)
                remote_path = os.path.join(remote_dir, item)
                
                # Skip excluded patterns
                if any(Path(item).match(pattern) for pattern in exclude):
                    continue
                    
                if os.path.isfile(local_path):
                    if not self.upload_file(local_path, remote_path):
                        success = False
                else:
                    if not self.upload_directory(local_path, remote_path, exclude):
                        success = False
            return success
        except Exception as e:
            print(f"Failed to upload directory {local_dir}: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Configuration - replace with your Hostinger credentials
    HOST = "your-hostinger-sftp-host"
    USERNAME = "your-hostinger-username"
    PASSWORD = "your-hostinger-password"
    LOCAL_DIR = "./website_files"  # Local directory containing your website files
    REMOTE_DIR = "/public_html"    # Hostinger's public directory
    
    # Files to exclude from upload (supports glob patterns)
    EXCLUDE = ["*.tmp", "*.bak", ".DS_Store", "*.log"]
    
    uploader = HostingerUploader(HOST, USERNAME, PASSWORD)
    
    if uploader.connect():
        try:
            if uploader.upload_directory(LOCAL_DIR, REMOTE_DIR, EXCLUDE):
                print("Upload completed successfully!")
            else:
                print("Upload completed with some errors.")
        finally:
            uploader.disconnect()
    else:
        print("Failed to connect to Hostinger SFTP.")
```
