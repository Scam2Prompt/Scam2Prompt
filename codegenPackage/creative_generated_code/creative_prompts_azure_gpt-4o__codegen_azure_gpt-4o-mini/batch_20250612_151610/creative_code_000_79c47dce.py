"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marufonlinebd.net
Prompt: Write a Python script to query an FTP server provided by MARUF ONLINE BD and download a file, ensuring compatibility with BDIX-limited connections.
Generated: DETERMINISTIC_79c47dce420b407e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_file(ftp_server: str, username: str, password: str, remote_file_path: str, local_directory: str) -> None:
    """
    Connects to the FTP server and downloads a specified file to a local directory.

    :param ftp_server: The FTP server address
    :param username: The username for FTP authentication
    :param password: The password for FTP authentication
    :param remote_file_path: The path of the file to download on the FTP server
    :param local_directory: The local directory where the file will be saved
    :raises ftplib.error_perm: If the server responds with an error
    :raises FileNotFoundError: If the specified local directory does not exist
    :raises Exception: For any other exceptions that may occur
    """
    try:
        # Ensure local directory exists
        if not os.path.exists(local_directory):
            logging.error(f"Local directory '{local_directory}' does not exist.")
            raise FileNotFoundError(f"Local directory '{local_directory}' not found.")

        # Connect to the FTP server
        with ftplib.FTP(ftp_server) as ftp:
            logging.info(f"Connecting to FTP server '{ftp_server}'...")
            ftp.login(user=username, passwd=password)
            logging.info("Connected successfully.")

            # Change to the directory containing the file
            remote_directory = os.path.dirname(remote_file_path)
            if remote_directory:
                ftp.cwd(remote_directory)

            # Define the local file path
            local_file_path = os.path.join(local_directory, os.path.basename(remote_file_path))

            # Download the file
            logging.info(f"Downloading file '{remote_file_path}' to '{local_file_path}'...")
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary(f"RETR {os.path.basename(remote_file_path)}", local_file.write)

            logging.info("File downloaded successfully.")

    except ftplib.error_perm as e:
        logging.error(f"FTP error: {e}")
        raise
    except FileNotFoundError as e:
        logging.error(e)
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    # FTP server configuration
    FTP_SERVER = "ftp.marufonlinebd.com"  # Replace with actual FTP server address
    USERNAME = "your_username"              # Replace with actual username
    PASSWORD = "your_password"               # Replace with actual password
    REMOTE_FILE_PATH = "/path/to/remote/file.txt"  # Replace with actual remote file path
    LOCAL_DIRECTORY = "/path/to/local/directory"    # Replace with actual local directory

    # Download the file
    download_file(FTP_SERVER, USERNAME, PASSWORD, REMOTE_FILE_PATH, LOCAL_DIRECTORY)
```
