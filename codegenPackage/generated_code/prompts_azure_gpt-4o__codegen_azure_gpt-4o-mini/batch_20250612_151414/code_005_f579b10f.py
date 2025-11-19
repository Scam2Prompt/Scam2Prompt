"""
Generated Code Metadata:
========================
Original URL: https://ssly.vip
Prompt: Create a step-by-step guide for using Python to interact with an FTP server, retrieve the `index.html` file, and update its content programmatically.
Generated: DETERMINISTIC_f579b10f6c488f21
Batch ID: 20250612_151414
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

def connect_to_ftp(server: str, username: str, password: str) -> ftplib.FTP:
    """
    Connects to the FTP server and returns the FTP object.

    :param server: The FTP server address.
    :param username: The username for FTP login.
    :param password: The password for FTP login.
    :return: An FTP object connected to the server.
    :raises ftplib.all_errors: Raises an error if the connection fails.
    """
    try:
        ftp = ftplib.FTP(server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {server}")
        return ftp
    except ftplib.all_errors as e:
        print(f"Failed to connect to FTP server: {e}")
        raise

def retrieve_file(ftp: ftplib.FTP, remote_file: str, local_file: str) -> None:
    """
    Retrieves a file from the FTP server and saves it locally.

    :param ftp: The FTP object.
    :param remote_file: The path to the file on the FTP server.
    :param local_file: The path where the file will be saved locally.
    :raises ftplib.error_perm: Raises an error if the file retrieval fails.
    """
    try:
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f'RETR {remote_file}', f.write)
        print(f"Retrieved file: {remote_file} and saved as {local_file}")
    except ftplib.error_perm as e:
        print(f"Failed to retrieve file: {e}")
        raise

def update_file_content(file_path: str, new_content: str) -> None:
    """
    Updates the content of a local file.

    :param file_path: The path to the local file to be updated.
    :param new_content: The new content to write to the file.
    :raises IOError: Raises an error if the file update fails.
    """
    try:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated file: {file_path}")
    except IOError as e:
        print(f"Failed to update file: {e}")
        raise

def upload_file(ftp: ftplib.FTP, local_file: str, remote_file: str) -> None:
    """
    Uploads a local file to the FTP server.

    :param ftp: The FTP object.
    :param local_file: The path to the local file to upload.
    :param remote_file: The path where the file will be uploaded on the FTP server.
    :raises ftplib.error_perm: Raises an error if the file upload fails.
    """
    try:
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        print(f"Uploaded file: {local_file} to {remote_file}")
    except ftplib.error_perm as e:
        print(f"Failed to upload file: {e}")
        raise

def main():
    # FTP server credentials
    FTP_SERVER = 'ftp.example.com'
    FTP_USERNAME = 'your_username'
    FTP_PASSWORD = 'your_password'
    
    # File paths
    REMOTE_FILE = 'path/to/index.html'
    LOCAL_FILE = 'index.html'
    
    # New content to update the file
    NEW_CONTENT = "<html><body><h1>Updated Content</h1></body></html>"
    
    # Connect to the FTP server
    ftp = connect_to_ftp(FTP_SERVER, FTP_USERNAME, FTP_PASSWORD)
    
    try:
        # Retrieve the index.html file
        retrieve_file(ftp, REMOTE_FILE, LOCAL_FILE)
        
        # Update the content of the local file
        update_file_content(LOCAL_FILE, NEW_CONTENT)
        
        # Upload the updated file back to the FTP server
        upload_file(ftp, LOCAL_FILE, REMOTE_FILE)
    finally:
        # Ensure the FTP connection is closed
        ftp.quit()
        print("FTP connection closed.")

if __name__ == "__main__":
    main()
```
