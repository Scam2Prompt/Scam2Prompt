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

def connect_to_ftp(host, username, password):
    """
    Connects to the FTP server and returns the FTP object.
    
    :param host: The FTP server hostname or IP address.
    :param username: The FTP username.
    :param password: The FTP password.
    :return: An FTP object connected to the specified server.
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        return ftp
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        raise

def check_and_rename_file(ftp, filename, new_filename):
    """
    Checks for the presence of a file on the FTP server and renames it if it exists.
    
    :param ftp: The FTP connection object.
    :param filename: The name of the file to check.
    :param new_filename: The new name to which the file will be renamed.
    """
    try:
        # Attempt to retrieve the file to check its existence
        ftp.size(filename)
        # If the file exists, rename it
        ftp.rename(filename, new_filename)
        print(f"Renamed '{filename}' to '{new_filename}'.")
    except ftplib.error_perm as e:
        if str(e).startswith('550'):
            print(f"File '{filename}' does not exist; skipping rename.")
        else:
            print(f"Error checking or renaming file: {e}")
            raise

def upload_file(ftp, local_file, remote_file):
    """
    Uploads a file to the FTP server.
    
    :param ftp: The FTP connection object.
    :param local_file: The path to the local file to be uploaded.
    :param remote_file: The name of the file on the FTP server after upload.
    """
    try:
        with open(local_file, 'rb') as file:
            ftp.storbinary(f'STOR {remote_file}', file)
        print(f"Uploaded '{local_file}' to '{remote_file}'.")
    except FileNotFoundError:
        print(f"Local file '{local_file}' not found.")
    except ftplib.all_errors as e:
        print(f"Error uploading file: {e}")
        raise

def main():
    # FTP server credentials
    host = 'ftp.example.com'  # Replace with your FTP server host
    username = 'your_username'  # Replace with your FTP username
    password = 'your_password'  # Replace with your FTP password
    
    # File names
    default_file = 'index.html'
    backup_file = 'index_backup.html'
    new_file = 'new_index.html'  # Replace with your new file path

    # Connect to the FTP server
    ftp = connect_to_ftp(host, username, password)

    # Check and rename the default index.html file if it exists
    check_and_rename_file(ftp, default_file, backup_file)
    
    # Upload the new index file
    upload_file(ftp, new_file, default_file)

    # Close the FTP connection
    ftp.quit()
    print("FTP connection closed.")

if __name__ == '__main__':
    main()
```
