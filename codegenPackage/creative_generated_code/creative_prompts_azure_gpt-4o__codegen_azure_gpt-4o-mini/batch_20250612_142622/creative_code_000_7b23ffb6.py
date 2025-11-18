"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1suisui.cc
Prompt: Write Python code to connect to an FTP server, retrieve the `index.html` file from the root directory, and replace its content with a custom HTML template.
Generated: DETERMINISTIC_7b23ffb683a0cfd1
Batch ID: 20250612_142622
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

# Define the FTP server credentials and the file to retrieve
FTP_SERVER = 'ftp.example.com'  # Replace with your FTP server address
USERNAME = 'your_username'       # Replace with your FTP username
PASSWORD = 'your_password'       # Replace with your FTP password
FILE_NAME = 'index.html'
LOCAL_FILE_PATH = os.path.join(os.getcwd(), FILE_NAME)

# Define the custom HTML template content
CUSTOM_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Custom Page</title>
</head>
<body>
    <h1>Welcome to My Custom Page</h1>
    <p>This is a custom HTML template.</p>
</body>
</html>
"""

def connect_to_ftp():
    """Establish a connection to the FTP server."""
    try:
        ftp = ftplib.FTP(FTP_SERVER)
        ftp.login(user=USERNAME, passwd=PASSWORD)
        return ftp
    except ftplib.all_errors as e:
        print(f"Failed to connect to FTP server: {e}")
        return None

def retrieve_file(ftp, filename):
    """Retrieve a file from the FTP server."""
    try:
        with open(LOCAL_FILE_PATH, 'wb') as local_file:
            ftp.retrbinary(f'RETR {filename}', local_file.write)
        print(f"Successfully retrieved {filename} to {LOCAL_FILE_PATH}")
    except ftplib.error_perm as e:
        print(f"Failed to retrieve file: {e}")

def replace_file_content(ftp, filename, content):
    """Replace the content of a file on the FTP server."""
    try:
        # Store the new content in a temporary file
        with open(LOCAL_FILE_PATH, 'w') as temp_file:
            temp_file.write(content)
        
        # Upload the new file content
        with open(LOCAL_FILE_PATH, 'rb') as temp_file:
            ftp.storbinary(f'STOR {filename}', temp_file)
        print(f"Successfully replaced the content of {filename} on FTP server.")
    except ftplib.error_perm as e:
        print(f"Failed to replace file content: {e}")

def main():
    """Main function to execute the FTP operations."""
    ftp = connect_to_ftp()
    if ftp:
        retrieve_file(ftp, FILE_NAME)
        replace_file_content(ftp, FILE_NAME, CUSTOM_HTML_TEMPLATE)
        ftp.quit()

if __name__ == "__main__":
    main()
```
