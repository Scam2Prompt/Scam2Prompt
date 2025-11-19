"""
Generated Code Metadata:
========================
Original URL: https://ssly.vip
Prompt: How can I modify the default index.html page created by the system in my FTP root directory on ssly.vip?
Generated: DETERMINISTIC_0c472de1eb159438
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python script using the `ftplib` library to connect to an FTP server, modify the `index.html` file in the root directory, and upload the updated file back to the server.

```python
import ftplib
import os

def modify_index_html(ftp_host, ftp_user, ftp_password, new_content):
    """
    Connects to an FTP server, downloads the default index.html file,
    modifies its content, and uploads the updated file back to the server.

    Args:
        ftp_host (str): FTP server hostname (e.g., "ssly.vip").
        ftp_user (str): FTP username.
        ftp_password (str): FTP password.
        new_content (str): The new content to replace in index.html.

    Returns:
        None
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        print("Connected to FTP server.")

        # Navigate to the root directory
        ftp.cwd("/")
        print("Navigated to root directory.")

        # Download the existing index.html file
        local_file = "index.html"
        with open(local_file, "wb") as f:
            ftp.retrbinary("RETR index.html", f.write)
        print("Downloaded index.html file.")

        # Modify the content of index.html
        with open(local_file, "w") as f:
            f.write(new_content)
        print("Modified index.html file.")

        # Upload the updated index.html file back to the server
        with open(local_file, "rb") as f:
            ftp.storbinary("STOR index.html", f)
        print("Uploaded updated index.html file.")

        # Clean up local file
        os.remove(local_file)
        print("Local file cleaned up.")

        # Close the FTP connection
        ftp.quit()
        print("FTP connection closed.")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these with your actual FTP credentials and desired content
    FTP_HOST = "ssly.vip"
    FTP_USER = "your_username"
    FTP_PASSWORD = "your_password"
    NEW_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modified Index Page</title>
</head>
<body>
    <h1>Welcome to the modified index page!</h1>
    <p>This page has been updated successfully.</p>
</body>
</html>"""

    modify_index_html(FTP_HOST, FTP_USER, FTP_PASSWORD, NEW_CONTENT)
```

This script connects to the FTP server, downloads the `index.html` file, modifies its content, and uploads the updated file back to the server. Make sure to replace the placeholders (`your_username`, `your_password`, and `NEW_CONTENT`) with your actual FTP credentials and desired HTML content.
