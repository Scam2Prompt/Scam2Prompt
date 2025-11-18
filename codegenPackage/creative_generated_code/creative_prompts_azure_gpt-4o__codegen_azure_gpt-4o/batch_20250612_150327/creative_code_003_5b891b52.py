"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-de.com
Prompt: Generate a Python script to upload website files to Hostinger, ensuring compatibility with the hosting platform's requirements as described on the webpage.
Generated: DETERMINISTIC_5b891b52950aead8
Batch ID: 20250612_150327
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
from ftplib import FTP, error_perm

def upload_to_hostinger(host, username, password, local_directory, remote_directory):
    """
    Uploads website files from a local directory to Hostinger's FTP server.

    Parameters:
        host (str): FTP server host (e.g., ftp.example.com).
        username (str): FTP username.
        password (str): FTP password.
        local_directory (str): Path to the local directory containing the files to upload.
        remote_directory (str): Path to the remote directory where files will be uploaded.

    Returns:
        None
    """
    try:
        # Connect to the FTP server
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        print("Connected to FTP server.")

        # Change to the remote directory
        ftp.cwd(remote_directory)
        print(f"Changed to remote directory: {remote_directory}")

        # Helper function to upload files recursively
        def upload_directory(local_dir, remote_dir):
            # List all files and directories in the local directory
            for item in os.listdir(local_dir):
                local_path = os.path.join(local_dir, item)
                remote_path = f"{remote_dir}/{item}"

                # Check if the item is a file or directory
                if os.path.isfile(local_path):
                    # Upload the file
                    with open(local_path, 'rb') as file:
                        ftp.storbinary(f"STOR {remote_path}", file)
                        print(f"Uploaded file: {remote_path}")
                elif os.path.isdir(local_path):
                    # Ensure the remote directory exists
                    try:
                        ftp.mkd(remote_path)
                        print(f"Created remote directory: {remote_path}")
                    except error_perm as e:
                        if "550" in str(e):
                            print(f"Directory already exists: {remote_path}")
                        else:
                            raise

                    # Recursively upload directory contents
                    upload_directory(local_path, remote_path)

        # Begin uploading the local directory
        upload_directory(local_directory, remote_directory)

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    finally:
        # Ensure the connection is closed
        if ftp:
            ftp.quit()
            print("Disconnected from FTP server.")


# Example usage:
if __name__ == "__main__":
    host = "ftp.hostinger.com"  # Replace with your FTP server address
    username = "your_username"  # Replace with your FTP username
    password = "your_password"  # Replace with your FTP password
    local_directory = "/path/to/local/website/files"  # Replace with your local directory path
    remote_directory = "/path/to/remote/directory"  # Replace with your remote directory path

    upload_to_hostinger(host, username, password, local_directory, remote_directory)
```

Note: Replace placeholders in the `host`, `username`, `password`, `local_directory`, and `remote_directory` variables with actual values for your Hostinger account and setup.
