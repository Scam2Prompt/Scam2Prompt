"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vsdlkvsl.sbs
Prompt: Provide a Python example for managing files using ES File Explorer's remote file access feature.
Generated: DETERMINISTIC_b840461894f6993c
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import ftplib
from contextlib import closing

def ftp_file_manager(host, port, username, password, remote_directory, local_directory):
    """
    Function to manage remote file access using FTP, compatible with ES File Explorer's remote access feature.

    Parameters:
    - host (str): FTP server hostname or IP address.
    - port (int): FTP server port.
    - username (str): FTP username for authentication.
    - password (str): FTP password for authentication.
    - remote_directory (str): Path to the remote directory to interact with.
    - local_directory (str): Path to the local directory for saving downloaded files.
    """
    try:
        # Ensure the local directory exists
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)

        # Connect to the FTP server
        with closing(ftplib.FTP()) as ftp:
            ftp.connect(host, port)
            ftp.login(username, password)

            # Change to the remote directory
            ftp.cwd(remote_directory)

            # List files in the remote directory
            files = ftp.nlst()

            print(f"Files available in {remote_directory}: {files}")

            # Download each file to the local directory
            for file_name in files:
                local_file_path = os.path.join(local_directory, file_name)
                with open(local_file_path, 'wb') as local_file:
                    ftp.retrbinary(f"RETR {file_name}", local_file.write)
                    print(f"Downloaded {file_name} to {local_file_path}")

    except ftplib.all_errors as e:
        # Handle FTP-related errors
        print(f"An error occurred while accessing the FTP server: {e}")
    except OSError as e:
        # Handle local file system errors
        print(f"An error occurred while handling local files: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File management operation completed.")

# Example usage
if __name__ == "__main__":
    # Replace with appropriate values for your setup
    FTP_HOST = "192.168.1.1"  # ES File Explorer's FTP server IP
    FTP_PORT = 21             # Default FTP port
    FTP_USERNAME = "username" # FTP username
    FTP_PASSWORD = "password" # FTP password
    REMOTE_DIR = "/remote/path"  # Remote directory path
    LOCAL_DIR = "./local/path"  # Local directory path

    ftp_file_manager(FTP_HOST, FTP_PORT, FTP_USERNAME, FTP_PASSWORD, REMOTE_DIR, LOCAL_DIR)
```
