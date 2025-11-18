"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mortgage-foreclosure.com
Prompt: Provide a step-by-step guide for migrating a website to Hostinger, including code snippets for transferring files via FTP.
Generated: DETERMINISTIC_1e6b8c2b65df119e
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Step-by-step guide for migrating website files to Hostinger via FTP.

This Python script demonstrates how to transfer website files using FTP.
Ensure you have the `ftplib` module installed (standard in Python).
"""

import ftplib
import os

def ftp_upload(host, username, password, source_dir, target_dir):
    """
    Uploads files from a local directory to an FTP server.

    Parameters:
        host (str): The FTP server address.
        username (str): FTP username.
        password (str): FTP password.
        source_dir (str): Local directory containing website files to upload.
        target_dir (str): Target directory on the FTP server.
    """
    try:
        # Step 1: Establish connection to the FTP server
        print("Connecting to FTP server...")
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        print("Connected successfully.")

        # Step 2: Change directory on the server
        ftp.cwd(target_dir)
        print(f"Changed to target directory: {target_dir}")

        # Step 3: Upload files
        for root, dirs, files in os.walk(source_dir):  # Traverse the local directory
            for filename in files:
                local_path = os.path.join(root, filename)
                server_path = os.path.join(target_dir, filename)

                # Open the file in binary mode and upload
                print(f"Uploading {filename}...")
                with open(local_path, "rb") as file:
                    ftp.storbinary(f"STOR {server_path}", file)
                print(f"{filename} uploaded successfully.")

        print("All files uploaded successfully.")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    finally:
        # Step 4: Close FTP connection
        ftp.quit()
        print("FTP connection closed.")


if __name__ == "__main__":
    # Replace the following values with your actual credentials and paths
    FTP_HOST = "ftp.yourdomain.com"  # Hostinger FTP server address
    FTP_USER = "your_username"       # Hostinger FTP username
    FTP_PASS = "your_password"       # Hostinger FTP password
    SOURCE_DIR = "/path/to/your/local/files"  # Local directory containing website files
    TARGET_DIR = "/public_html"      # Target directory on Hostinger server

    # Call the FTP upload function
    ftp_upload(FTP_HOST, FTP_USER, FTP_PASS, SOURCE_DIR, TARGET_DIR)
```
