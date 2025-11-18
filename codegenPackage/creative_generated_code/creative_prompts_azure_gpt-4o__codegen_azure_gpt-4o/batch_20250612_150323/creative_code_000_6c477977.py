"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitriunm.cloud
Prompt: Write code to automate the migration of a website to Hostinger using FTP and provide steps for uploading files as described on the Hostinger platform.
Generated: DETERMINISTIC_6c477977e5b9d16f
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready Python code for automating the migration of a website to Hostinger via FTP:

```python
import ftplib
import os

def upload_files_to_hostinger(ftp_host, ftp_user, ftp_password, local_directory, remote_directory):
    """
    Automates the process of uploading files to Hostinger via FTP.

    Args:
        ftp_host (str): FTP server hostname (e.g., ftp.hostinger.com)
        ftp_user (str): FTP username.
        ftp_password (str): FTP password.
        local_directory (str): Path to the local directory containing website files.
        remote_directory (str): Path to the remote directory on the server.
    
    Raises:
        Exception: If any error occurs during connecting or transferring files.
    """
    try:
        # Establish connection to the FTP server
        print("Connecting to FTP server...")
        ftp = ftplib.FTP(ftp_host)
        ftp.login(ftp_user, ftp_password)
        print("Connection established successfully.")

        # Change to the desired remote directory
        ftp.cwd(remote_directory)

        # Recursively upload files and directories
        for root, dirs, files in os.walk(local_directory):
            relative_path = os.path.relpath(root, local_directory)
            remote_path = os.path.join(remote_directory, relative_path).replace("\\", "/")

            # Create remote directories if they don't exist
            try:
                ftp.cwd(remote_path)
            except ftplib.error_perm:
                print(f"Creating directory: {remote_path}")
                ftp.mkd(remote_path)
                ftp.cwd(remote_path)

            # Upload files
            for file in files:
                local_file_path = os.path.join(root, file)
                print(f"Uploading file: {local_file_path} -> {remote_path}/{file}")
                with open(local_file_path, 'rb') as file_obj:
                    ftp.storbinary(f"STOR {file}", file_obj)
        
        print("File upload completed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is properly closed
        if 'ftp' in locals():
            ftp.quit()
            print("FTP connection closed.")

# Example usage (replace with your own parameters)
if __name__ == "__main__":
    FTP_HOST = "ftp.hostinger.com"
    FTP_USER = "your_username"
    FTP_PASSWORD = "your_password"
    LOCAL_DIRECTORY = "/path/to/your/local/website/files"
    REMOTE_DIRECTORY = "/public_html"  # Change to your specific remote directory
    
    upload_files_to_hostinger(FTP_HOST, FTP_USER, FTP_PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
```

**Steps for uploading files to Hostinger using this script:**

1. Replace the placeholders in the script (`FTP_HOST`, `FTP_USER`, `FTP_PASSWORD`, `LOCAL_DIRECTORY`, and `REMOTE_DIRECTORY`) with your actual FTP credentials and paths.
2. Make sure the `ftplib` library is available (it's part of Python's standard library).
3. Save the script to a `.py` file.
4. Run the script using Python (e.g., `python your_script.py`).
5. Verify that your website files are successfully uploaded to Hostinger.
