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

def download_file_from_ftp(server: str, port: int, username: str, password: str, remote_file_path: str, local_file_path: str):
    """
    Connects to an FTP server, downloads a file, and saves it locally.

    Parameters:
        server (str): FTP server address (e.g., MARUF ONLINE BD's FTP server).
        port (int): Port number for the FTP server (default is usually 21).
        username (str): Username for FTP login.
        password (str): Password for FTP login.
        remote_file_path (str): Path to the file on the FTP server.
        local_file_path (str): Path where the downloaded file will be saved locally.

    Returns:
        None
    """
    try:
        # Connect to the FTP server
        print(f"Connecting to FTP server: {server}:{port}")
        ftp = ftplib.FTP()
        ftp.connect(host=server, port=port, timeout=30)  # Timeout set to handle BDIX-limited connections
        ftp.login(user=username, passwd=password)
        print("Successfully connected and logged in.")

        # Ensure the remote file exists before downloading
        print(f"Checking if remote file exists: {remote_file_path}")
        file_list = ftp.nlst()  # List files in the current directory
        if os.path.basename(remote_file_path) not in file_list:
            raise FileNotFoundError(f"Remote file '{remote_file_path}' not found on the server.")

        # Download the file
        print(f"Downloading file: {remote_file_path}")
        with open(local_file_path, 'wb') as local_file:
            ftp.retrbinary(f"RETR {remote_file_path}", local_file.write)  # RETR command to retrieve the file
        print(f"File downloaded successfully to: {local_file_path}")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        # Disconnect from the server
        if 'ftp' in locals() and ftp.sock:
            print("Closing FTP connection.")
            ftp.quit()

if __name__ == "__main__":
    # Replace the following values with appropriate ones for your FTP server
    FTP_SERVER = "ftp.marufonlinebd.com"  # Example FTP server address
    FTP_PORT = 21  # Default FTP port
    FTP_USERNAME = "your_username"  # FTP username
    FTP_PASSWORD = "your_password"  # FTP password
    REMOTE_FILE_PATH = "remote/path/to/file.txt"  # Path to the file on the server
    LOCAL_FILE_PATH = "local/path/to/save/file.txt"  # Path to save the file locally

    # Ensure compatibility with BDIX-limited connections by using proper timeouts
    download_file_from_ftp(FTP_SERVER, FTP_PORT, FTP_USERNAME, FTP_PASSWORD, REMOTE_FILE_PATH, LOCAL_FILE_PATH)
```
