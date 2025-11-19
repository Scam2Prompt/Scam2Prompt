"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skymavis-ron.rf.gd
Prompt: Provide an example of how to transfer an existing website to iFastNet hosting while maintaining SSL security.
Generated: DETERMINISTIC_7f09f4af0bceccd5
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Transferring a website to iFastNet hosting while maintaining SSL security involves multiple steps that cannot be achieved solely through code. It requires DNS configuration, SSL certificate installation, and file/database migration via tools like cPanel, FTP, or other hosting management utilities. 

However, I can provide you with a Python script to automate the uploading of website files via FTP and ensure that the SSL certificate files are uploaded correctly. You would need to manually configure the SSL certificate through the iFastNet hosting control panel after the upload.

```python
import ftplib
import os
import ssl

def upload_to_ifastnet(host, username, password, local_folder, remote_folder):
    """
    Uploads files from a local folder to iFastNet hosting via FTP.
    
    Args:
        host (str): FTP server hostname (e.g., ftp.ifastnet.com).
        username (str): Your FTP username.
        password (str): Your FTP password.
        local_folder (str): Path to the local folder containing website files.
        remote_folder (str): Path to the remote folder on the host server.
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP_TLS(host)
        ftp.login(user=username, passwd=password)
        ftp.prot_p()  # Use secure data connection (TLS)

        print("Connection established successfully.")

        # Ensure the remote folder exists
        try:
            ftp.cwd(remote_folder)
        except ftplib.error_perm:
            print(f"Remote folder '{remote_folder}' not found. Creating it...")
            ftp.mkd(remote_folder)
            ftp.cwd(remote_folder)

        # Upload files recursively
        for root, dirs, files in os.walk(local_folder):
            relative_path = os.path.relpath(root, local_folder)
            remote_path = os.path.join(remote_folder, relative_path).replace("\\", "/")

            # Ensure the remote path exists
            try:
                ftp.cwd(remote_path)
            except ftplib.error_perm:
                print(f"Creating remote folder '{remote_path}'...")
                ftp.mkd(remote_path)
                ftp.cwd(remote_path)

            # Upload files in the current directory
            for file in files:
                local_file = os.path.join(root, file)
                remote_file = os.path.join(remote_path, file).replace("\\", "/")
                with open(local_file, "rb") as f:
                    ftp.storbinary(f"STOR {remote_file}", f)
                print(f"Uploaded: {file} -> {remote_file}")

        print("Upload completed successfully.")

        # Close the connection
        ftp.quit()

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

if __name__ == "__main__":
    # Configuration
    FTP_HOST = "ftp.ifastnet.com"  # Replace with your FTP host
    FTP_USERNAME = "your_username"  # Replace with your FTP username
    FTP_PASSWORD = "your_password"  # Replace with your FTP password
    LOCAL_FOLDER = "/path/to/your/website/files"  # Replace with the local folder path
    REMOTE_FOLDER = "/public_html"  # Replace with the desired remote folder (e.g., /public_html)

    # Start the upload process
    upload_to_ifastnet(FTP_HOST, FTP_USERNAME, FTP_PASSWORD, LOCAL_FOLDER, REMOTE_FOLDER)
```

**Notes:**
- Replace `FTP_HOST`, `FTP_USERNAME`, `FTP_PASSWORD`, `LOCAL_FOLDER`, and `REMOTE_FOLDER` with your actual values.
- Once your website files are uploaded, go to the iFastNet control panel and install/configure your SSL certificate through their interface, as this part cannot be automated directly via FTP.
- Ensure that your SSL certificate files (`.crt`, `.key`, etc.) are included in the `LOCAL_FOLDER` if required for manual installation later.
