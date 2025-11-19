"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ssly.vip
Prompt: How can I modify the default index.html page created by the system in my FTP root directory on ssly.vip?
Generated: DETERMINISTIC_0c472de1eb159438
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's an example script for modifying the default `index.html` page in the FTP root directory using Python and the `ftplib` library. This assumes you have access to the FTP server credentials and permissions to modify files in the root directory.

```python
import ftplib
import os

def update_index_html(ftp_host, ftp_user, ftp_password, new_content):
    """
    Connects to an FTP server, modifies the index.html file in the root directory, and uploads the updated file.

    Parameters:
    ftp_host (str): FTP server hostname or IP.
    ftp_user (str): FTP username.
    ftp_password (str): FTP password.
    new_content (str): New HTML content to replace the index.html file.
    """
    try:
        # Connect to the FTP server
        with ftplib.FTP(ftp_host) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_password)
            print(f"Successfully logged in to FTP server: {ftp_host}")

            # Change to the root directory (if needed)
            ftp.cwd("/")
            print("Navigated to FTP root directory.")

            # Download the existing index.html file to local for backup (if exists)
            backup_file = "index_backup.html"
            try:
                with open(backup_file, "wb") as f:
                    ftp.retrbinary("RETR index.html", f.write)
                print(f"Existing index.html backed up as {backup_file}.")
            except ftplib.error_perm:
                print("No existing index.html found in the root directory. Continuing...")

            # Write the new content to a temporary local file
            temp_file = "index.html"
            with open(temp_file, "w") as f:
                f.write(new_content)
            print(f"New HTML content written to {temp_file}.")

            # Upload the updated index.html to the FTP server
            with open(temp_file, "rb") as f:
                ftp.storbinary("STOR index.html", f)
            print("Updated index.html successfully uploaded to the FTP server.")

            # Clean up temporary local files
            os.remove(temp_file)
            print(f"Temporary file {temp_file} deleted.")

    except ftplib.all_errors as e:
        print(f"FTP error encountered: {e}")
    except Exception as e:
        print(f"General error encountered: {e}")

# Example usage:
if __name__ == "__main__":
    # FTP server credentials
    FTP_HOST = "ftp.ssly.vip"
    FTP_USER = "your_ftp_user"
    FTP_PASSWORD = "your_ftp_password"
    
    # New HTML content for index.html
    NEW_HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to SSLY.VIP</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
    </style>
</head>
<body>
    <h1>Welcome to SSLY.VIP</h1>
    <p>This is a custom homepage served from the FTP root directory.</p>
</body>
</html>
"""

    # Call the function to update the index.html
    update_index_html(FTP_HOST, FTP_USER, FTP_PASSWORD, NEW_HTML_CONTENT)
```

Make sure to replace `your_ftp_user` and `your_ftp_password` with appropriate credentials.
