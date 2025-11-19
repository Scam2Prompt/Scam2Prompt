"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropro.co.nz
Prompt: How can I upload my website contents using FTP for my domain hosted on Micropro?
Generated: DETERMINISTIC_d20fbcf0d8254391
Batch ID: 20250612_160720
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

def upload_directory(ftp, path, ftp_path):
    """
    Uploads the contents of a directory to the specified FTP path.

    :param ftp: An active FTP connection object.
    :param path: The local directory to upload.
    :param ftp_path: The destination path on the FTP server.
    """
    # Change to the destination directory
    try:
        ftp.cwd(ftp_path)
    except ftplib.error_perm as e:
        print(f"Directory {ftp_path} not found. Creating it now.")
        ftp.mkd(ftp_path)
        ftp.cwd(ftp_path)

    # Iterate through the files and subdirectories in the local directory
    for item in os.listdir(path):
        local_item_path = os.path.join(path, item)
        remote_item_path = os.path.join(ftp_path, item)

        if os.path.isdir(local_item_path):
            # Recursively upload subdirectories
            upload_directory(ftp, local_item_path, remote_item_path)
        else:
            # Upload files
            try:
                with open(local_item_path, 'rb') as file:
                    ftp.storbinary(f'STOR {remote_item_path}', file)
                    print(f"Uploaded: {local_item_path} to {remote_item_path}")
            except Exception as e:
                print(f"Failed to upload {local_item_path}: {e}")

def upload_website(host, username, password, local_directory, remote_directory):
    """
    Uploads website contents to an FTP server.

    :param host: FTP server address.
    :param username: FTP login username.
    :param password: FTP login password.
    :param local_directory: Local directory containing website files.
    :param remote_directory: Remote directory where files should be uploaded.
    """
    try:
        # Establish FTP connection
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        print("Successfully logged in to the FTP server.")

        # Upload contents of the local directory
        upload_directory(ftp, local_directory, remote_directory)

        # Close the FTP connection
        ftp.quit()
        print("FTP connection closed.")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

if __name__ == "__main__":
    # User-configurable settings
    HOST = 'ftp.micropro.com'        # Replace with your FTP host
    USERNAME = 'your_username'       # Replace with your FTP username
    PASSWORD = 'your_password'       # Replace with your FTP password
    LOCAL_DIRECTORY = 'path/to/your/local/website'  # Local path to website files
    REMOTE_DIRECTORY = '/public_html'  # Remote path on the FTP server

    # Start the upload process
    upload_website(HOST, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
```

**Note:** Please replace `your_username`, `your_password`, `path/to/your/local/website`, and `ftp.micropro.com` with your actual FTP credentials and paths.
