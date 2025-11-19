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
import tempfile

def connect_to_ftp(host, username, password):
    """
    Connect to an FTP server and return the FTP connection object.
    
    Args:
        host (str): FTP server hostname or IP address.
        username (str): FTP username.
        password (str): FTP password.
    
    Returns:
        ftplib.FTP: FTP connection object.
    
    Raises:
        ftplib.all_errors: If connection or login fails.
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(username, password)
        return ftp
    except ftplib.all_errors as e:
        raise ftplib.error_perm(f"Failed to connect to FTP server: {e}")

def download_file(ftp, remote_path, local_path):
    """
    Download a file from the FTP server.
    
    Args:
        ftp (ftplib.FTP): FTP connection object.
        remote_path (str): Path to the file on the FTP server.
        local_path (str): Local path to save the downloaded file.
    
    Raises:
        ftplib.error_perm: If download fails.
    """
    try:
        with open(local_path, 'wb') as local_file:
            ftp.retrbinary(f'RETR {remote_path}', local_file.write)
    except ftplib.all_errors as e:
        raise ftplib.error_perm(f"Failed to download file: {e}")

def upload_file(ftp, local_path, remote_path):
    """
    Upload a file to the FTP server.
    
    Args:
        ftp (ftplib.FTP): FTP connection object.
        local_path (str): Local path of the file to upload.
        remote_path (str): Path to save the file on the FTP server.
    
    Raises:
        ftplib.error_perm: If upload fails.
    """
    try:
        with open(local_path, 'rb') as local_file:
            ftp.storbinary(f'STOR {remote_path}', local_file)
    except ftplib.all_errors as e:
        raise ftplib.error_perm(f"Failed to upload file: {e}")

def update_html_content(file_path, new_content):
    """
    Update the content of an HTML file.
    
    Args:
        file_path (str): Path to the HTML file.
        new_content (str): New content to write to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
    except IOError as e:
        raise IOError(f"Failed to update file content: {e}")

def main():
    # FTP server configuration
    FTP_HOST = 'ftp.example.com'
    FTP_USER = 'username'
    FTP_PASS = 'password'
    REMOTE_FILE = 'index.html'
    
    try:
        # Step 1: Connect to FTP server
        ftp = connect_to_ftp(FTP_HOST, FTP_USER, FTP_PASS)
        print("Connected to FTP server successfully.")
        
        # Step 2: Create a temporary local file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
            temp_path = temp_file.name
        
        # Step 3: Download the remote file
        download_file(ftp, REMOTE_FILE, temp_path)
        print(f"Downloaded {REMOTE_FILE} to {temp_path}")
        
        # Step 4: Update the file content
        new_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Updated Page</title>
        </head>
        <body>
            <h1>This page has been updated programmatically!</h1>
        </body>
        </html>
        """
        update_html_content(temp_path, new_content)
        print("Updated file content.")
        
        # Step 5: Upload the updated file back to the server
        upload_file(ftp, temp_path, REMOTE_FILE)
        print(f"Uploaded updated {REMOTE_FILE} to server.")
        
        # Step 6: Clean up
        os.unlink(temp_path)
        ftp.quit()
        print("Operation completed successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        if 'ftp' in locals():
            ftp.quit()
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.unlink(temp_path)

if __name__ == "__main__":
    main()
```
