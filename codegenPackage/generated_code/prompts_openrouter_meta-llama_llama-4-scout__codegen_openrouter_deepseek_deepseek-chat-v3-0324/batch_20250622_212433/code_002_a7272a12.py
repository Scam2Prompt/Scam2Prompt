"""
Generated Code Metadata:
========================
Original URL: https://app.pawcommunity.in
Prompt: Generate a Python script that automates the process of uploading website files to Hostinger, as described on app.pawcommunity.in.
Generated: DETERMINISTIC_a7272a12202992c4
Batch ID: 20250622_212433
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
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hostinger_upload.log'),
        logging.StreamHandler()
    ]
)

class HostingerUploader:
    """
    A class to handle file uploads to Hostinger via SFTP.
    """
    
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        port: int = 22,
        remote_path: str = "/",
        local_path: str = "."
    ):
        """
        Initialize the uploader with connection details.
        
        Args:
            host (str): Hostinger SFTP host
            username (str): SFTP username
            password (str): SFTP password
            port (int, optional): SFTP port. Defaults to 22.
            remote_path (str, optional): Remote base path. Defaults to "/".
            local_path (str, optional): Local base path. Defaults to ".".
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.remote_path = remote_path.rstrip('/')
        self.local_path = local_path.rstrip('/')
        self.ssh_client = None
        self.sftp = None
        
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
            self.sftp = self.ssh_client.open_sftp()
            logging.info("Successfully connected to Hostinger via SFTP")
            return True
        except Exception as e:
            logging.error(f"Failed to connect to Hostinger: {str(e)}")
            return False
            
    def disconnect(self):
        """Close the SFTP connection."""
        if self.sftp:
            self.sftp.close()
        if self.ssh_client:
            self.ssh_client.close()
        logging.info("Disconnected from Hostinger")
        
    def upload_file(self, local_file: str, remote_file: str) -> bool:
        """
        Upload a single file to Hostinger.
        
        Args:
            local_file (str): Path to local file
            remote_file (str): Path to remote file
            
        Returns:
            bool: True if upload succeeded, False otherwise
        """
        try:
            self.sftp.put(local_file, remote_file)
            logging.info(f"Uploaded {local_file} to {remote_file}")
            return True
        except Exception as e:
            logging.error(f"Failed to upload {local_file}: {str(e)}")
            return False
            
    def create_remote_directory(self, remote_dir: str) -> bool:
        """
        Create a directory on the remote server.
        
        Args:
            remote_dir (str): Path to remote directory
            
        Returns:
            bool: True if directory creation succeeded, False otherwise
        """
        try:
            self.sftp.mkdir(remote_dir)
            logging.info(f"Created remote directory: {remote_dir}")
            return True
        except IOError:
            logging.debug(f"Directory already exists: {remote_dir}")
            return True
        except Exception as e:
            logging.error(f"Failed to create directory {remote_dir}: {str(e)}")
            return False
            
    def upload_directory(
        self,
        local_dir: str,
        remote_dir: str,
        exclude_dirs: Optional[List[str]] = None,
        exclude_extensions: Optional[List[str]] = None
    ) -> bool:
        """
        Recursively upload a directory to Hostinger.
        
        Args:
            local_dir (str): Local directory path
            remote_dir (str): Remote directory path
            exclude_dirs (List[str], optional): Directories to exclude. Defaults to None.
            exclude_extensions (List[str], optional): File extensions to exclude. Defaults to None.
            
        Returns:
            bool: True if upload succeeded, False otherwise
        """
        if exclude_dirs is None:
            exclude_dirs = []
        if exclude_extensions is None:
            exclude_extensions = []
            
        try:
            # Create remote directory if it doesn't exist
            self.create_remote_directory(remote_dir)
            
            for item in os.listdir(local_dir):
                local_path = os.path.join(local_dir, item)
                remote_path = f"{remote_dir}/{item}"
                
                # Skip excluded directories
                if os.path.isdir(local_path) and item in exclude_dirs:
                    logging.info(f"Skipping excluded directory: {local_path}")
                    continue
                    
                # Skip files with excluded extensions
                if os.path.isfile(local_path):
                    file_ext = Path(item).suffix.lower()
                    if file_ext in exclude_extensions:
                        logging.info(f"Skipping file with excluded extension: {local_path}")
                        continue
                
                if os.path.isdir(local_path):
                    # Recursively upload subdirectories
                    if not self.upload_directory(local_path, remote_path, exclude_dirs, exclude_extensions):
                        return False
                else:
                    # Upload files
                    if not self.upload_file(local_path, remote_path):
                        return False
            return True
        except Exception as e:
            logging.error(f"Failed to upload directory {local_dir}: {str(e)}")
            return False
            
    def upload_website(
        self,
        exclude_dirs: Optional[List[str]] = None,
        exclude_extensions: Optional[List[str]] = None
    ) -> bool:
        """
        Upload the entire website from local path to remote path.
        
        Args:
            exclude_dirs (List[str], optional): Directories to exclude. Defaults to None.
            exclude_extensions (List[str], optional): File extensions to exclude. Defaults to None.
            
        Returns:
            bool: True if upload succeeded, False otherwise
        """
        if not self.connect():
            return False
            
        try:
            success = self.upload_directory(
                self.local_path,
                self.remote_path,
                exclude_dirs,
                exclude_extensions
            )
            return success
        finally:
            self.disconnect()

def main():
    # Example usage
    uploader = HostingerUploader(
        host="your-hostinger-sftp-host",
        username="your-username",
        password="your-password",
        remote_path="/public_html",  # Typical Hostinger web root
        local_path="./website_files"  # Local website files directory
    )
    
    # Common directories and extensions to exclude
    exclude_dirs = [".git", "node_modules", "__pycache__", ".idea", "venv"]
    exclude_extensions = [".log", ".tmp", ".bak", ".swp"]
    
    if uploader.upload_website(exclude_dirs, exclude_extensions):
        logging.info("Website upload completed successfully!")
    else:
        logging.error("Website upload failed. Check logs for details.")

if __name__ == "__main__":
    main()
```
