"""
Generated Code Metadata:
========================
Original URL: https://contractmergenew.com
Prompt: Write a step-by-step guide on how to migrate a website to Hostinger, including uploading website files.
Generated: DETERMINISTIC_439033ce3b43b035
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python script that automates the process of uploading website files to Hostinger using FTP. This script assumes you have the necessary credentials (FTP hostname, username, and password) and the website files ready to upload.

```python
import os
import ftplib

def upload_to_hostinger(ftp_host, ftp_user, ftp_password, local_directory, remote_directory):
    """
    Uploads website files to Hostinger using FTP.

    Args:
        ftp_host (str): The FTP hostname (e.g., ftp.yourdomain.com).
        ftp_user (str): The FTP username.
        ftp_password (str): The FTP password.
        local_directory (str): The local directory containing website files.
        remote_directory (str): The remote directory on the server to upload files to.

    Raises:
        Exception: If any error occurs during the FTP connection or file upload.
    """
    try:
        # Connect to the FTP server
        print("Connecting to FTP server...")
        ftp = ftplib.FTP(ftp_host)
        ftp.login(ftp_user, ftp_password)
        print("Connected to FTP server successfully.")

        # Change to the desired remote directory
        ftp.cwd(remote_directory)
        print(f"Changed to remote directory: {remote_directory}")

        # Upload files recursively
        for root, dirs, files in os.walk(local_directory):
            # Calculate the relative path to preserve directory structure
            relative_path = os.path.relpath(root, local_directory)
            remote_path = os.path.join(remote_directory, relative_path).replace("\\", "/")

            # Create directories on the server if they don't exist
            try:
                ftp.cwd(remote_path)
            except ftplib.error_perm:
                ftp.mkd(remote_path)
                print(f"Created remote directory: {remote_path}")
                ftp.cwd(remote_path)

            # Upload files in the current directory
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_path, file).replace("\\", "/")
                with open(local_file_path, "rb") as file_handle:
                    ftp.storbinary(f"STOR {remote_file_path}", file_handle)
                    print(f"Uploaded: {local_file_path} -> {remote_file_path}")

        print("All files uploaded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

    finally:
        # Close the FTP connection
        if 'ftp' in locals():
            ftp.quit()
            print("FTP connection closed.")

# Example usage
if __name__ == "__main__":
    # Replace these values with your actual FTP credentials and paths
    FTP_HOST = "ftp.yourdomain.com"
    FTP_USER = "your_ftp_username"
    FTP_PASSWORD = "your_ftp_password"
    LOCAL_DIRECTORY = "/path/to/your/local/website/files"
    REMOTE_DIRECTORY = "/path/to/your/remote/directory"

    try:
        upload_to_hostinger(FTP_HOST, FTP_USER, FTP_PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    except Exception as e:
        print(f"Migration failed: {e}")
```

### Notes:
- Replace the placeholders (`ftp.yourdomain.com`, `your_ftp_username`, etc.) with your actual FTP credentials and paths.
- Ensure the `LOCAL_DIRECTORY` contains all the website files you want to upload.
- This script uses the `ftplib` library, which is part of Python's standard library, so no additional dependencies are required.
- Proper error handling is included to catch and report issues during the FTP connection or file upload process.
