"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: How can I host a website for free using InfinityFree on a domain like example.infy.uk?
Generated: DETERMINISTIC_76bd57bd90a91d34
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, well-documented, and production-ready code demonstrating how to upload website files to InfinityFree using FTP for hosting on your `example.infy.uk` domain. The code uses Python and the `ftplib` library to upload files:

```python
import ftplib
import os

def upload_files_to_infinityfree(ftp_host, ftp_user, ftp_password, local_directory, remote_directory):
    """
    Uploads all files from a local directory to a remote directory on InfinityFree's FTP server.

    Args:
        ftp_host (str): The FTP hostname (e.g., ftpupload.net for InfinityFree).
        ftp_user (str): The FTP username (use the one provided by InfinityFree).
        ftp_password (str): The FTP password (use the one provided by InfinityFree).
        local_directory (str): Path to the local directory containing website files.
        remote_directory (str): Path to the remote directory where files will be uploaded.

    Raises:
        Exception: If any FTP operation fails, an exception is raised with details.
    """
    try:
        # Connect to InfinityFree's FTP server
        with ftplib.FTP(ftp_host) as ftp:
            print(f"Connecting to FTP server {ftp_host}...")
            ftp.login(user=ftp_user, passwd=ftp_password)
            print("Login successful!")

            # Change to the desired directory on the server
            ftp.cwd(remote_directory)
            print(f"Changed to remote directory: {remote_directory}")

            # Walk through the local directory and upload files
            for root, _, files in os.walk(local_directory):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    
                    # Prepare the remote file path relative to the remote directory
                    relative_path = os.path.relpath(local_file_path, local_directory)
                    remote_file_path = os.path.join(remote_directory, relative_path).replace("\\", "/")

                    print(f"Uploading {local_file_path} to {remote_file_path}...")
                    
                    # Open the file in binary mode and upload using FTP
                    with open(local_file_path, 'rb') as f:
                        ftp.storbinary(f"STOR {remote_file_path}", f)

            print("All files uploaded successfully.")

    except ftplib.all_errors as e:
        raise Exception(f"FTP operation failed: {str(e)}")


if __name__ == "__main__":
    # Configuration for InfinityFree FTP access
    FTP_HOST = "ftpupload.net"  # InfinityFree FTP host (example)
    FTP_USER = "your_ftp_username"  # Replace with your actual FTP username
    FTP_PASSWORD = "your_ftp_password"  # Replace with your actual FTP password
    LOCAL_DIRECTORY = "path/to/your/local/website/files"  # Replace with the path to your website files
    REMOTE_DIRECTORY = "/htdocs"  # Default root folder for InfinityFree (usually /htdocs)

    try:
        upload_files_to_infinityfree(
            ftp_host=FTP_HOST,
            ftp_user=FTP_USER,
            ftp_password=FTP_PASSWORD,
            local_directory=LOCAL_DIRECTORY,
            remote_directory=REMOTE_DIRECTORY
        )
    except Exception as err:
        print(f"Error: {err}")
```

### Required Setup:
1. Replace `your_ftp_username` and `your_ftp_password` with the FTP credentials provided by InfinityFree.
2. Ensure your `example.infy.uk` domain points to InfinityFree’s nameservers (you can configure this in your domain registrar's settings).
3. Make sure the `LOCAL_DIRECTORY` contains the website files (e.g., HTML, CSS, JS, etc.).
4. Install Python (if not already installed) and ensure you have proper permissions to access your local directory.

### Notes:
- The code ensures reliable error handling to fail gracefully in case of issues with FTP.
- It uses Python's built-in `ftplib` library to interact with InfinityFree’s FTP server.
