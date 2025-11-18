"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mailweb-coinbase.com
Prompt: Generate a Python script to upload website files to a hosting server using FTP, referencing Hostinger's migration process.
Generated: DETERMINISTIC_9c624c56a3331ff5
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from ftplib import FTP, error_perm
from pathlib import Path

def upload_files_to_ftp(server: str, username: str, password: str, local_directory: str, remote_directory: str):
    """
    Uploads files from a local directory to a remote FTP server.

    :param server: The FTP server address.
    :param username: The FTP username.
    :param password: The FTP password.
    :param local_directory: The path to the local directory containing files to upload.
    :param remote_directory: The path to the remote directory on the FTP server.
    """
    try:
        # Connect to the FTP server
        with FTP(server) as ftp:
            ftp.login(user=username, passwd=password)  # Login to the server
            ftp.cwd(remote_directory)  # Change to the remote directory
            
            # Traverse local directory
            for root, dirs, files in os.walk(local_directory):
                for filename in files:
                    local_file_path = Path(root) / filename
                    remote_file_path = Path(remote_directory) / filename
                    
                    # Upload the file
                    with open(local_file_path, 'rb') as file:
                        try:
                            ftp.storbinary(f'STOR {remote_file_path}', file)
                            print(f'Successfully uploaded {local_file_path} to {remote_file_path}')
                        except error_perm as e:
                            print(f'Permission error while uploading {local_file_path}: {e}')
                        except Exception as e:
                            print(f'Failed to upload {local_file_path}: {e}')

    except Exception as e:
        print(f'Failed to connect to FTP server: {e}')

if __name__ == '__main__':
    # Define FTP server details
    FTP_SERVER = 'ftp.yourserver.com'
    FTP_USERNAME = 'your_username'
    FTP_PASSWORD = 'your_password'
    LOCAL_DIRECTORY = 'path/to/local/files'  # Change this to your local files directory
    REMOTE_DIRECTORY = '/path/to/remote/directory'  # Change this to your desired remote directory

    # Upload files
    upload_files_to_ftp(FTP_SERVER, FTP_USERNAME, FTP_PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
```
