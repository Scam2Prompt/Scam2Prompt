"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivasikurirtokopedia.hstn.me
Prompt: Generate a Python script that utilizes iFastNet's hosting capabilities to deploy a web application with a free domain.
Generated: DETERMINISTIC_216b8be38e9bc66c
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to utilize iFastNet's hosting capabilities to deploy a simple web application
using the free hosting service. Note: iFastNet does not provide direct APIs for deployment, so this script
handles the process by generating the required files and providing instructions for manual upload via FTP.
"""

import ftplib
import os

# FTP Configuration for iFastNet
FTP_HOST = "ftp.ifastnet.com"  # Replace with your actual FTP host
FTP_USERNAME = "your_username"  # Replace with your iFastNet account FTP username
FTP_PASSWORD = "your_password"  # Replace with your iFastNet account FTP password
FTP_UPLOAD_DIR = "/htdocs/"  # Directory where web files will be uploaded

# Web Application Files
WEB_APP_FILES = {
    "index.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Free Domain Web App</title>
</head>
<body>
    <h1>Welcome to My Web App!</h1>
    <p>This web application is hosted using iFastNet's free hosting service.</p>
</body>
</html>
""",
    "style.css": """
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 50px;
    background-color: #f4f4f4;
}
h1 {
    color: #333;
}
p {
    color: #666;
}
""",
}

def create_web_files(files):
    """
    Creates the necessary web application files locally.
    """
    try:
        os.makedirs("web_app", exist_ok=True)  # Create a folder for web app files
        for filename, content in files.items():
            with open(f"web_app/{filename}", "w") as file:
                file.write(content)
        print("Web application files created successfully.")
    except Exception as e:
        print(f"Error creating web files: {e}")

def upload_files_to_ifastnet(host, username, password, upload_dir, local_dir):
    """
    Connects to iFastNet's FTP and uploads the web application files.
    """
    try:
        with ftplib.FTP(host) as ftp:
            # Connect to FTP server
            ftp.login(user=username, passwd=password)
            print("Connected to iFastNet FTP server.")

            # Change to the upload directory
            ftp.cwd(upload_dir)
            print(f"Changed to directory: {upload_dir}")

            # Upload files from local directory
            for filename in os.listdir(local_dir):
                local_path = os.path.join(local_dir, filename)
                with open(local_path, "rb") as file:
                    ftp.storbinary(f"STOR {filename}", file)
                    print(f"Uploaded: {filename}")

            print("All files uploaded successfully.")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

def main():
    """
    Main function to orchestrate the web application deployment process.
    """
    # Step 1: Create Web Application Files Locally
    create_web_files(WEB_APP_FILES)

    # Step 2: Upload Files to iFastNet via FTP
    upload_files_to_ifastnet(FTP_HOST, FTP_USERNAME, FTP_PASSWORD, FTP_UPLOAD_DIR, "web_app")

if __name__ == "__main__":
    main()
```

> **Note:** Replace `FTP_USERNAME` and `FTP_PASSWORD` with your actual credentials from iFastNet. Additionally, ensure that you have an active free hosting account with iFastNet and your domain is correctly set up.
