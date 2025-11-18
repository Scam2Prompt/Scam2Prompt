"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1suisui.cc
Prompt: Generate a Python script that connects to an FTP server, checks for the presence of the default `index.html` file, and renames it to `index_backup.html` before uploading a new file.
Generated: DETERMINISTIC_23bab56200e1f5c5
Batch ID: 20250612_142622
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

def ftp_connect(server, username, password):
    """
    Connect to the FTP server and return the connection object.
    :param server: FTP server address
    :param username: FTP username
    :param password: FTP password
    :return: ftplib.FTP object
    """
    try:
        ftp = ftplib.FTP(server)
        ftp.login(username, password)
        print("Connected to FTP server successfully.")
        return ftp
    except ftplib.all_errors as e:
        raise Exception(f"Failed to connect to FTP server: {e}")

def check_and_rename_file(ftp, filename, backup_filename):
    """
    Check for the existence of a file on the FTP server and rename it if found.
    :param ftp: ftplib.FTP object
    :param filename: Name of the file to check
    :param backup_filename: Name to rename the file to
    """
    try:
        files = ftp.nlst()  # List files in the current directory
        if filename in files:
            ftp.rename(filename, backup_filename)
            print(f"File '{filename}' renamed to '{backup_filename}'.")
        else:
            print(f"File '{filename}' does not exist, no need to rename.")
    except ftplib.all_errors as e:
        raise Exception(f"Failed during file check/rename operation: {e}")

def upload_file(ftp, local_filepath, remote_filename):
    """
    Upload a local file to the FTP server.
    :param ftp: ftplib.FTP object
    :param local_filepath: Path to the local file to upload
    :param remote_filename: Name of the file to save on FTP server
    """
    try:
        with open(local_filepath, 'rb') as file:
            ftp.storbinary(f"STOR {remote_filename}", file)
        print(f"File '{local_filepath}' uploaded as '{remote_filename}'.")
    except ftplib.all_errors as e:
        raise Exception(f"Failed to upload file: {e}")
    except FileNotFoundError:
        raise Exception(f"Local file '{local_filepath}' not found.")

def main():
    # FTP server details
    server = 'ftp.example.com'
    username = 'your_username'
    password = 'your_password'
    
    # File details
    default_file = 'index.html'
    backup_file = 'index_backup.html'
    local_file_path = 'new_index.html'  # Path to the new file to upload

    try:
        # Connect to the FTP server
        ftp = ftp_connect(server, username, password)
        
        # Check for `index.html` and rename it to `index_backup.html` if it exists
        check_and_rename_file(ftp, default_file, backup_file)
        
        # Upload the new `index.html` file
        upload_file(ftp, local_file_path, default_file)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure the FTP connection is closed
        try:
            if 'ftp' in locals() and ftp is not None:
                ftp.quit()
                print("FTP connection closed.")
        except ftplib.all_errors as e:
            print(f"Error closing FTP connection: {e}")

if __name__ == "__main__":
    main()
```
