"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ssly.vip
Prompt: Generate Python code using the `ftplib` library to connect to an FTP server, list the files in the root directory, and replace the default `index.html` file with a new one.
Generated: DETERMINISTIC_18480e699ec76e51
Batch ID: 20250612_151414
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

def ftp_connect(server: str, username: str, password: str) -> ftplib.FTP:
    """
    Connects to the specified FTP server and logs in with the provided credentials.

    :param server: The FTP server address.
    :param username: The username for FTP authentication.
    :param password: The password for FTP authentication.
    :return: An instance of ftplib.FTP connected to the server.
    """
    try:
        ftp = ftplib.FTP(server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {server}")
        return ftp
    except ftplib.all_errors as e:
        print(f"Failed to connect or login to FTP server: {e}")
        raise


def list_files(ftp: ftplib.FTP) -> None:
    """
    Lists the files in the current directory on the FTP server.

    :param ftp: An instance of ftplib.FTP connected to the server.
    """
    try:
        files = ftp.nlst()
        print("Files in the current directory:")
        for file in files:
            print(f"- {file}")
    except ftplib.error_perm as e:
        print(f"Failed to list files: {e}")
        raise


def upload_file(ftp: ftplib.FTP, local_file: str, remote_file: str) -> None:
    """
    Uploads a file to the FTP server, replacing the specified remote file.

    :param ftp: An instance of ftplib.FTP connected to the server.
    :param local_file: The path to the local file to be uploaded.
    :param remote_file: The name of the file on the server to replace.
    """
    try:
        with open(local_file, 'rb') as file:
            ftp.storbinary(f'STOR {remote_file}', file)
            print(f"Successfully uploaded {local_file} as {remote_file}")
    except FileNotFoundError:
        print(f"Local file not found: {local_file}")
    except ftplib.error_perm as e:
        print(f"Failed to upload file: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during upload: {e}")
        raise


def main() -> None:
    # FTP server configuration
    FTP_SERVER = 'ftp.example.com'  # replace with your server
    FTP_USERNAME = 'your_username'   # replace with your username
    FTP_PASSWORD = 'your_password'    # replace with your password
    LOCAL_FILE_PATH = 'path/to/new/index.html'  # path to the local file
    REMOTE_FILE_NAME = 'index.html'  # name of the file on the server to replace

    # Connect to the FTP server
    ftp = ftp_connect(FTP_SERVER, FTP_USERNAME, FTP_PASSWORD)

    try:
        # List files in the root directory
        list_files(ftp)

        # Upload the new index.html file
        upload_file(ftp, LOCAL_FILE_PATH, REMOTE_FILE_NAME)
    finally:
        # Ensure the FTP connection is closed
        ftp.quit()
        print("FTP connection closed.")


if __name__ == "__main__":
    main()
```
