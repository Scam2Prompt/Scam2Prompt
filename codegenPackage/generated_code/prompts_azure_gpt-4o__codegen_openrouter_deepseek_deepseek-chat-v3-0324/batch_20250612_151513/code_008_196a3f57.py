"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Write code to integrate DX Link's FTP server options into a file transfer application, ensuring compatibility with their network specifications.
Generated: DETERMINISTIC_196a3f577ceb6c73
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ftplib
import os
import logging
from typing import Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DXFTPClient:
    """
    A client for interacting with DX Link's FTP server with their specific requirements.
    """
    
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        port: int = 21,
        timeout: int = 30,
        passive_mode: bool = True
    ):
        """
        Initialize the FTP client with DX Link's specifications.
        
        Args:
            host: FTP server hostname
            username: FTP username
            password: FTP password
            port: FTP port (default: 21)
            timeout: Connection timeout in seconds (default: 30)
            passive_mode: Whether to use passive mode (default: True)
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.passive_mode = passive_mode
        self.ftp = None

    def connect(self) -> bool:
        """
        Connect to the FTP server with DX Link's specifications.
        
        Returns:
            bool: True if connection succeeded, False otherwise
        """
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(self.host, self.port, self.timeout)
            self.ftp.login(self.username, self.password)
            
            # Set passive mode if specified
            if self.passive_mode:
                self.ftp.set_pasv(True)
                
            logger.info("Successfully connected to DX Link FTP server")
            return True
            
        except ftplib.all_errors as e:
            logger.error(f"Failed to connect to FTP server: {str(e)}")
            self.disconnect()
            return False

    def disconnect(self):
        """Disconnect from the FTP server if connected."""
        if self.ftp:
            try:
                self.ftp.quit()
            except:
                self.ftp.close()
            finally:
                self.ftp = None
                logger.info("Disconnected from FTP server")

    def upload_file(
        self,
        local_path: str,
        remote_path: str,
        retries: int = 3
    ) -> bool:
        """
        Upload a file to the FTP server.
        
        Args:
            local_path: Path to local file
            remote_path: Destination path on FTP server
            retries: Number of upload retries (default: 3)
            
        Returns:
            bool: True if upload succeeded, False otherwise
        """
        if not self.ftp:
            logger.error("Not connected to FTP server")
            return False

        if not os.path.exists(local_path):
            logger.error(f"Local file not found: {local_path}")
            return False

        for attempt in range(retries):
            try:
                with open(local_path, 'rb') as file:
                    self.ftp.storbinary(f'STOR {remote_path}', file)
                logger.info(f"Successfully uploaded {local_path} to {remote_path}")
                return True
            except ftplib.all_errors as e:
                logger.warning(
                    f"Upload attempt {attempt + 1} failed: {str(e)}"
                )
                if attempt < retries - 1:
                    self.reconnect()
                    
        logger.error(f"Failed to upload {local_path} after {retries} attempts")
        return False

    def download_file(
        self,
        remote_path: str,
        local_path: str,
        retries: int = 3
    ) -> bool:
        """
        Download a file from the FTP server.
        
        Args:
            remote_path: Path to remote file
            local_path: Destination path on local system
            retries: Number of download retries (default: 3)
            
        Returns:
            bool: True if download succeeded, False otherwise
        """
        if not self.ftp:
            logger.error("Not connected to FTP server")
            return False

        for attempt in range(retries):
            try:
                with open(local_path, 'wb') as file:
                    self.ftp.retrbinary(f'RETR {remote_path}', file.write)
                logger.info(f"Successfully downloaded {remote_path} to {local_path}")
                return True
            except ftplib.all_errors as e:
                logger.warning(
                    f"Download attempt {attempt + 1} failed: {str(e)}"
                )
                if attempt < retries - 1:
                    self.reconnect()
                    
        logger.error(f"Failed to download {remote_path} after {retries} attempts")
        return False

    def list_files(self, remote_path: str = '') -> Optional[List[str]]:
        """
        List files in a remote directory.
        
        Args:
            remote_path: Path to remote directory (default: root)
            
        Returns:
            Optional[List[str]]: List of filenames or None if failed
        """
        if not self.ftp:
            logger.error("Not connected to FTP server")
            return None

        try:
            files = self.ftp.nlst(remote_path)
            logger.info(f"Found {len(files)} files in {remote_path}")
            return files
        except ftplib.all_errors as e:
            logger.error(f"Failed to list files: {str(e)}")
            return None

    def reconnect(self) -> bool:
        """Reconnect to the FTP server."""
        self.disconnect()
        return self.connect()

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    # Configuration - replace with actual DX Link credentials
    config = {
        'host': 'ftp.dxlink.example.com',
        'username': 'your_username',
        'password': 'your_password',
        'port': 21,
        'timeout': 30,
        'passive_mode': True
    }

    with DXFTPClient(**config) as ftp_client:
        # Example operations
        files = ftp_client.list_files()
        if files:
            print("Files in root directory:", files)

        # Example upload
        ftp_client.upload_file('local_file.txt', 'remote_file.txt')

        # Example download
        ftp_client.download_file('remote_file.txt', 'downloaded_file.txt')
```
