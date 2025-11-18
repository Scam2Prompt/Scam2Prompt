"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mailweb-coinbase.com
Prompt: Generate a Python script to upload website files to a hosting server using FTP, referencing Hostinger's migration process.
Generated: DETERMINISTIC_9c624c56a3331ff5
Batch ID: 20250612_151659
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
import sys

def upload_files_to_server(host, username, password, local_directory, remote_directory):
    """
    Upload website files to a hosting server using FTP.

    :param host: The FTP server address.
    :param username: The FTP username.
    :param password: The FTP password.
    :param local_directory: Local directory containing website files to upload.
    :param remote_directory: Remote directory on the server to upload files to.
    """
    try:
        # Create an FTP connection
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        print("Successfully connected to the FTP server.")

        # Change to the desired remote directory
        ftp.cwd(remote_directory)
        print(f"Switched to remote directory: {remote_directory}")

        # Walk through the local directory and upload files
        for root, dirs, files in os.walk(local_directory):
            relative_path = os.path.relpath(root, local_directory)
            remote_path = os.path.join(remote_directory, relative_path).replace('\\', '/')
            
            # Create remote directory if it doesn't exist
            try:
                ftp.mkd(remote_path)
                print(f"Created remote directory: {remote_path}")
            except ftplib.error_perm:
                # Directory might already exist, which is fine
                pass
            
            # Upload all files in the current directory
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_path, file).replace('\\', '/')
                try:
                    with open(local_file_path, 'rb') as f:
                        ftp.storbinary(f"STOR {remote_file_path}", f)
                    print(f"Uploaded: {local_file_path} to {remote_file_path}")
                except Exception as e:
                    print(f"Failed to upload {local_file_path}: {e}")

        print("File upload completed successfully.")
    
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

    finally:
        # Ensure the FTP connection is closed
        if 'ftp' in locals() and ftp:
            ftp.quit()
            print("FTP connection closed.")

if __name__ == "__main__":
    # Input required credentials and paths
    try:
        host = input("Enter FTP server address: ")
        username = input("Enter FTP username: ")
        password = input("Enter FTP password: ")
        local_directory = input("Enter the local directory path to upload: ")
        remote_directory = input("Enter the remote directory path: ")

        # Validate paths
        if not os.path.isdir(local_directory):
            print(f"Error: Local directory '{local_directory}' does not exist.")
            sys.exit(1)

        # Upload files
        upload_files_to_server(host, username, password, local_directory, remote_directory)
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
```
